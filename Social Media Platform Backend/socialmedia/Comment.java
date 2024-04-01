package socialmedia;

/**
 * This class represents Comment class as child class of Post in the platform.
 * It stores information that post need to have to work on the platform.
 */

public class Comment extends Post {

    /**
     * Creates a new Comment with the given handle, message and fatheLink.
     * @param handle The user's handle.
     * @param message The user's message.
     * @param fatherLink ID of original post.
     */
    public Comment(String handle, String message, int fatherLink) {
        super(handle, message);
        this.fatherLink = fatherLink;
    }

    /**
     * Get a posts's fatherlink if there is one.
     * @return father link (original post id)
     */

    public int getFatherLink() {
        return fatherLink;
    }

}