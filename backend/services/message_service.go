package services

import (
    "context"

    "backend/dal"
    "backend/models"

    "go.mongodb.org/mongo-driver/bson/primitive"
)

type MessageService struct {
    dal *dal.MessageDAL
}

func NewMessageService(dal *dal.MessageDAL) *MessageService {
    return &MessageService{dal: dal}
}

func (s *MessageService) CreateMessage(ctx context.Context, message *models.Message) error {
    return s.dal.CreateMessage(ctx, message)
}

func (s *MessageService) GetMessageByID(ctx context.Context, id primitive.ObjectID) (*models.Message, error) {
    return s.dal.GetMessageByID(ctx, id)
}
