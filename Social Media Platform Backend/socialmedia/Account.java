package socialmedia;
import java.util.UUID;

/** 
 * This class represemts Account in the platform.
 */

public class Account {
    // Handle (username) of an account.
    private String handle;  
    // Automatically generated user id (sequential number).
    private int userid;     
    // Description of an account.
    private String description; 
    // Number of times account's posts have been endorsed.
    private int numberOfAccountEndorsements; 
    // Number of times account's posts have been commented.
    private int numberOfAccountComments;
    //Number of account's posts.
    private int numberOfAccountPosts;


    /**
     * Creates a new account with the given handle.
     * @param handle The user's handle
     */
    public Account(String handle) {
        this.handle = handle;
        this.userid = generateUserid();
    }

   /**
     * Generates user ID.
     * @return The User ID
     */
    private int generateUserid() {
        UUID uuid = UUID.randomUUID();
        long uuidlong = uuid.getMostSignificantBits() & Long.MAX_VALUE;
        int userid = (int) (uuidlong % Integer.MAX_VALUE);
        return userid;
    }

    /**
     * Return Account's handle(username).
     * @return handle (username)
     */
    public String getHandle() {
        return handle;
    }

    /**
     * Return Account's user ID.
     * @return the User ID
     */
    public int getUserid() {
        return userid;
    }

    /**
     * Return Account's description.
     * @return String description of account.
     */
    public String getDescription() {
        return description;
    }

    /**
     * Set description of the Account.
     * @param String description to set.
     */
    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * Change handle of the Account.
     * @param String new handle.
     */
    public void changeHandle(String new_handle) {
        this.handle = new_handle;
    } 

    /**
     * Get number of Account's posts.
     * @return Number of Posts.
     */
    public int getNumberOfPosts() {
        return numberOfAccountPosts;
    }

    /**
     * //Adds 1 to a number of Account's posts.
     */
    public void addNumberOfPosts() {
        numberOfAccountPosts++;
    }
    
    /**
     * // Adds 1 number of endorsements to Account based on case that Account's post has been endorsed.
     */
    public void addNumberOfAccountEndorsements() {
        this.numberOfAccountEndorsements += 1;
    }

    /**
     * // Get number of times Account's posts have been endorsed.
     * @return Number of Endorsements.
     */
    public int getNumberOfAccountEndorsements() {
        return numberOfAccountEndorsements;
    }
    
     /**
     * // Adds 1 number of comments if Account's posts are commented.
     */
    public void addNumberOfAccountComments() {
        this.numberOfAccountComments += 1;
    }

    /**
     * // Get number of comments.
     * @return Number of Comments
     */
    public int getNumberOfAccountComments() {
        return numberOfAccountComments;
    }
    /**
     * // Creates a StringBuilder with account information: ID, handle, Post Count, EndorseCount.
     * @return StringBuilder with information.
     */
    public StringBuilder showAccount(StringBuilder builder) {
        return builder.append("ID: ").append(getUserid()).append("\n")
                .append("Handle: ").append(getHandle()).append("\n")
                .append("Description: ").append(getDescription()).append("\n")
                .append("Post Count: ").append(getNumberOfPosts()).append("\n")
                .append("Endorse Count: ").append(getNumberOfAccountEndorsements()).append("\n");
    }

}



