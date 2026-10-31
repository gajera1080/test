const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());
app.use(express.static(__dirname + "/public"));
app.use(express.static(__dirname + "/../dependency"));

// 1. Connect to MongoDB
mongoose.connect("mongodb://127.0.0.1:27017/eventDB")
  .then(() => console.log("Connected to MongoDB (eventDB)"))
  .catch(err => console.error("MongoDB Connection Error:", err.message));

// 2. Event model: Event(eventId, title, venue, date, fees, organizerName)
const required = type => ({ type, required: true });

const Event = mongoose.model("Event", new mongoose.Schema({
  eventId: { ...required(String), unique: true },
  title: { ...required(String), minlength: 3 },
  venue: required(String),
  date: required(String),
  fees: { ...required(Number), min: 0 },
  organizerName: required(String)
}));

// 3. Helper: wrap a route so any error becomes { error } with the given status
const handle = (errorCode, fn) => async (req, res) => {
  try { await fn(req, res); }
  catch (err) { res.status(errorCode).json({ error: err.message }); }
};

const notFound = res => res.status(404).json({ error: "Event not found" });

// 4. CRUD routes
app.get("/api/events", handle(500, async (req, res) => {
  res.json(await Event.find());
}));

app.post("/api/events", handle(400, async (req, res) => {
  res.status(201).json(await Event.create(req.body));
}));

app.put("/api/events/:eventId", handle(400, async (req, res) => {
  const updated = await Event.findOneAndUpdate(
    { eventId: req.params.eventId }, req.body, { new: true, runValidators: true });
  updated ? res.json(updated) : notFound(res);
}));

app.delete("/api/events/:eventId", handle(500, async (req, res) => {
  const { deletedCount } = await Event.deleteOne({ eventId: req.params.eventId });
  deletedCount ? res.json({ message: "Event cancelled successfully" }) : notFound(res);
}));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Event Management System (with Validation) running at http://localhost:${PORT}`));
