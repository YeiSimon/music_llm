package models

import (
    "time"

    "go.mongodb.org/mongo-driver/bson/primitive"
)

type User struct {
    ID        primitive.ObjectID `bson:"_id,omitempty" json:"id,omitempty"`
    GoogleID  string             `bson:"googleId" json:"googleId"`
    Email     string             `bson:"email" json:"email"`
    Name      string             `bson:"name" json:"name"`
    AvatarURL string             `bson:"avatarUrl" json:"avatarUrl"`
    CreatedAt time.Time          `bson:"createdAt" json:"createdAt"`
    LastLogin time.Time          `bson:"lastLogin" json:"lastLogin"`
}