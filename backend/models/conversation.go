package models

import (
    "time"

    "go.mongodb.org/mongo-driver/bson/primitive"
)

type Conversation struct {
    ID        primitive.ObjectID `bson:"_id,omitempty" json:"id,omitempty"`
    UserID    primitive.ObjectID `bson:"userId" json:"userId"`
    StartTime time.Time          `bson:"startTime" json:"startTime"`
    EndTime   time.Time          `bson:"endTime" json:"endTime"`
    Status    string             `bson:"status" json:"status"`
}