CREATE TABLE "events" (
  "id" TEXT NOT NULL PRIMARY KEY,
  "title" TEXT NOT NULL,
  "details" TEXT,
  "slug" TEXT NOT NULL,
  "maximumAttendees" INTEGER
);

CREATE TABLE "attendees" (
  "id" TEXT NOT NULL PRIMARY KEY
  "name" TEXT NOT NULL,
  "email" TEXT NOT NULL,
  "eventId" TEXT NOT NULL,
  "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "attendeesEventId" FOREIGN KEY ("eventId") REFERENCES 
  "events" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "checkIns" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
  "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
  "attendeeId" TEXT NOT NULL
  CONSTRAINT "checkInsAttendeeId" FOREIGN KEY ("attendeeId") REFERENCES 
  "attendees" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE UNIQUE INDEX "eventsSlugKey" ON "events"("slug");
CREATE UNIQUE INDEX "attendeesEventIdEmail" ON "attendees"("eventId", "email");
CREATE UNIQUE INDEX "checkInsAttendeeId" ON "checkIns"("attendeeId");