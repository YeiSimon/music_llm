package services

import (
    "context"

    "backend/dal"
    "backend/models"

    "go.mongodb.org/mongo-driver/bson/primitive"
)

type UserService struct {
    dal *dal.UserDAL
}

func NewUserService(dal *dal.UserDAL) *UserService {
    return &UserService{dal: dal}
}

func (s *UserService) CreateUser(ctx context.Context, user *models.User) error {
    return s.dal.CreateUser(ctx, user)
}

func (s *UserService) GetUserByID(ctx context.Context, id primitive.ObjectID) (*models.User, error) {
    return s.dal.GetUserByID(ctx, id)
}