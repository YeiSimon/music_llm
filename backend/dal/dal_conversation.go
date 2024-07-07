package dal

import (
    "context"
    "time"

    "backend/models"

    "go.mongodb.org/mongo-driver/bson"
    "go.mongodb.org/mongo-driver/bson/primitive"
    "go.mongodb.org/mongo-driver/mongo"
)

type ConversationDAL struct {
    collection *mongo.Collection
}

func NewConversationDAL(client *mongo.Client, dbName, collName string) *ConversationDAL {
    return &ConversationDAL{
        collection: client.Database(dbName).Collection(collName),
    }
}

func (dal *ConversationDAL) CreateConversation(ctx context.Context, conversation *models.Conversation) error {
    conversation.ID = primitive.NewObjectID()
    conversation.StartTime = time.Now()
    _, err := dal.collection.InsertOne(ctx, conversation)
    return err
}

func (dal *ConversationDAL) GetConversationByID(ctx context.Context, id primitive.ObjectID) (*models.Conversation, error) {
    var conversation models.Conversation
    err := dal.collection.FindOne(ctx, bson.M{"_id": id}).Decode(&conversation)
    return &conversation, err
}
