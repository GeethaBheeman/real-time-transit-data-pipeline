package com.mongodb.quickstart;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

public class ReadCDC {

    public static void main(String[] args) {
        String mongoUri = System.getProperty(
            "mongodb.uri",
            "mongodb://localhost:27017"
        );

        try (MongoClient mongoClient =
                 MongoClients.create(mongoUri)) {

            MongoDatabase database =
                mongoClient.getDatabase("myDatabase");

            MongoCollection<Document> collection =
                database.getCollection("myCollection");

            Document cdcDocument = collection
                .find(new Document("recordId", "CDC"))
                .first();

            if (cdcDocument == null) {
                System.out.println("CDC Record not found");
            } else {
                System.out.println(
                    "CDC Record: " + cdcDocument.toJson()
                );
            }
        }
    }
}