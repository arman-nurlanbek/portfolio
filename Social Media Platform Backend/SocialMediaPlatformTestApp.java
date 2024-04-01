import socialmedia.AccountIDNotRecognisedException;
import socialmedia.HandleNotRecognisedException;
import socialmedia.IllegalHandleException;
import socialmedia.InvalidHandleException;
import socialmedia.InvalidPostException;
import socialmedia.SocialMedia;
import socialmedia.MiniSocialMediaPlatform;
import socialmedia.NotActionablePostException;
import socialmedia.PostIDNotRecognisedException;

/**
 * A short program to illustrate an app testing some minimal functionality of a
 * concrete implementation of the SocialMediaPlatform interface -- note you will
 * want to increase these checks, and run it on your SocialMedia class (not the
 * BadSocialMedia class).
 *
 * 
 * @author Diogo Pacheco
 * @version 1.0
 */
public class SocialMediaPlatformTestApp {

	/**
	 * Test method.
	 * 
	 * @param args not used
	 */
	public static void main(String[] args) throws IllegalHandleException, InvalidHandleException, HandleNotRecognisedException, InvalidPostException, AccountIDNotRecognisedException, PostIDNotRecognisedException, NotActionablePostException{
		System.out.println("The system compiled and started the execution...");

		MiniSocialMediaPlatform socialMedia = new SocialMedia();
		
		
            // Test creating accounts
            int userFirst = socialMedia.createAccount("Arman");
            int userSecond = socialMedia.createAccount("Nurlanbek");

            
            // Test creating posts
            int postId1 = socialMedia.createPost("Arman", "Hello");
            int postId2 = socialMedia.createPost("Nurlanbek", "Hello");
            


            // Test endorsing posts
            int endorsementId1 = socialMedia.endorsePost("Arman", postId1);
            int endorsementId2 = socialMedia.endorsePost("Nurlanbek", postId2); 

            // Test commenting on posts
            int commentId1 = socialMedia.commentPost("Nurlanbek", postId1, "Comment");


	}

}
