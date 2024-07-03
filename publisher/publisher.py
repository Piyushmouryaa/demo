from nameko.rpc import rpc

class PublisherService:
    name = "publisher_service"

    @rpc
    def publish_message(self, message):
        print(f"Publishing message: {message}")
        return message
