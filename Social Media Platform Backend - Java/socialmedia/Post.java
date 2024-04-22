package socialmedia;

/**
 * This class represents a post in the platform.
 * It stores information that post need to have to work on the platform.
 */

public class Post {
    // Post's unique ID
    private int postid;

    // Post's message.
    private String message;

    // Post's creator.
    //private Account account;

    // Handle of the post creator.
    private String handle;

    // True if post is original | False if post is endorsement/comment.
    private boolean original;

    // True if post is a comment | False if post is original post/enodresement. 
    private boolean comment;

    // Number of times post has been endorsed.
    private int numberOfEndorsements;

    // Number of times post has been commented.
    private int numberOfComments;

    // Assigns fatherLink (ID of original post) if post is endorsement/comment.
    public int fatherLink;

    // Counts number of posts created in the platform and assigns a chronological ID to the posts respectively.
    private static int postIdCounter = 1;

    private String endorsingHandle;



    /**
     * Creates a new post with the given handle and message.
     * @param handle The user's handle and message.
     * @param message The user's message.
     */
    public Post(String handle, String message) {
        this.handle = handle;
        this.message = message;
        this.postid = generatePostId(); // this is to generate a unique ID 
        this.original = true;
        
    }

    /**
     * Get endorsing handle
     * @return Endorsing handle
     */
    public String getEndorsingHandle() {
        return endorsingHandle;
    }

    /**
     * This generate an id for the post
     * @return Post ID (postIdCounter)
     */
    public static synchronized int generatePostId() {
        return postIdCounter++;  
    }
    
    /**
     * Get a posts's fatherlink if there is one.
     * @return father link (original post id)
     */
    public int getFatherLink() {
        return fatherLink;
    }
   
    /**
     * Get post's message.
     * @return Post's message.
     */
    public String getMessage() {
        return message;
    }
    /**
     * Get post's handle (username).
     * @return Post's handle (username).
     */
    public String getHandle(){
        return handle;
    }

    /**
     * Get post's ID.
     * @return Post's ID.
     */
    public int getPostid() {
        return postid;
    }

    /**
     * Set message for a post.
     * @param a message
     */
    public void setMessage(String message) {
        this.message = message;
    }
    
    /**
     * Get original (Check if post is original)
     * @return True(Original)/False(Not original).
     */
    public boolean getOriginal() {
        return original;
    }

    /**
     * Get original of a comment (Check if post is a comment)
     * @return True(Post is a comment)/False(Post is not a comment).
     */
    public boolean getCommentOriginal() {
        return comment;
    }

    /**
     * Change a state of post original (Make it original)
     */
    public void changeOriginalToTrue() {
        this.original = true;
        fatherLink = 0;
    }
    
    /**
     * Make a post NOT original (endorsement or comment)
     * @param Post ID of original post that has been commented or endorsed.
     */
    public void changeOriginalToFalse(int postId) {
        this.original = false;
        fatherLink = postId;
    }

    /**
     * Change post to a comment.
     * @param Post ID of original post that has been commented.
     */
    public void changeCommentToTrue(int postId) {
        this.comment = true;
        fatherLink = postId;
    }

    /**
     * Change comment to a post
     */
    public void changeCommentToFalse() {
        this.comment = false;
        fatherLink = 0;
    }

    /**
     * Get number of times post has been endorsed
     * @return number of endorsements.
     */
    public int getNumberOfEndorsements() {
        return numberOfEndorsements;
    }

    /**
     * Method to return the number of comments associated with a post.
     * @param Number of comments.
     */
    public int getNumberOfComments() {
        return numberOfComments;
    }
    
    /**
     * Method to add a new endorsement and update the number of endorsements.
     * @return Number of endorsements.
     */
    public int addNumberOfEndorsements() {
        numberOfEndorsements += 1;
        return numberOfEndorsements;
    }

    /**
     * Method to add a new comment and update the number of comments.
     * @return Number of comments.
     */
    public int addNumberOfComments() {
        numberOfComments +=1;
        return numberOfComments;
    }
    

}    

