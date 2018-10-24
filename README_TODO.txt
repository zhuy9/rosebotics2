Do the following, in the order listed, to complete this exercise:

1. Get a robot.  Power it on.  Set up your computer to Deploy and Map to it.
     - File ~ Settings ~ Build, Execution, Deployment ~ Deployment
     - Set the IP address per what the brick shows and Test SFTP Connection.
     - In Mappings tab, set the Deployment Path on EV3 Server to:
             /home/robot/csse120

2. Tools ~ Start SSH session.  Wipe out previous stuff on the brick by:
      cd
      rm -rf csse120

   Recall that   cd   means Change Directory and   rm  means Remove.

3. Right-click on the rosebotics2 folder and select
      Deployment ~ Upload to ... EV3
   Watch for the message confirming that 8 files were uploaded.

4. Back in your SSH session (tab), run m0.py by:
      ls
      cd csse120
      ls
      cd src
      python m0.py

5


