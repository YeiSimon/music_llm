package routers

import (
    "backend/controllers"

    "github.com/gin-gonic/gin"
)

func SetupRouter(userController *controllers.UserController, conversationController *controllers.ConversationController, messageController *controllers.MessageController) *gin.Engine {
    r := gin.Default()

    r.POST("/users", userController.CreateUser)
    r.GET("/users/:id", userController.GetUser)

    r.POST("/conversations", conversationController.CreateConversation)
    r.GET("/conversations/:id", conversationController.GetConversation)

    r.POST("/messages", messageController.CreateMessage)
    r.GET("/messages/:id", messageController.GetMessage)

    return r
}