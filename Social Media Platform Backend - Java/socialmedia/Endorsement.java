package socialmedia;



public class Endorsement extends Post {

    /**
     * Creates a new Endorsement with the given handle, message and fatheLink.
     * @param handle The user's handle.
     * @param message The user's message.
     * @param fatherLink ID of original post.
     */

    public Endorsement(String handle, String message, int fatherLink) {
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
