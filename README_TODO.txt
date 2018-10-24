Do the following, in the order listed, to complete this exercise:

1. Get a robot.  Power it on.  Put it on its block.

2. Set up your computer to Deploy and Map to your robot's Brick.
     - File ~ Settings ~ Build, Execution, Deployment ~ Deployment
     - Set the IP address per what the Brick shows and Test SFTP Connection.
     - In Mappings tab, set the Deployment Path on EV3 Server to:
             /home/robot/csse120

3. Tools ~ Start SSH session.  Wipe out previous stuff on the Brick by:
      cd
      rm -rf csse120

   Recall that   cd   means Change Directory and   rm  means Remove.

4. Right-click on the rosebotics2 folder and select
      Deployment ~ Upload to ... EV3
   Watch for the message confirming that 8 files were uploaded.

5. Back in your SSH session (tab), run m0.py by:
      ls
      cd csse120
      ls
      cd src
      python m0.py

   Recall that   ls   means to LIST the contents of the directory.
   Do it only so that you know what files are where.

   When you run, your robot should move its wheels in various ways.

5. Read m0's run_test_drive_system.  Note that:
     - It constructs a Snatch3rRobot.
     - Snatch3rRobot's have a drive_sytem.
     - Its  drive_system  has a left_wheel and right_wheel,
         and each of the wheels can get or reset its "position" (degrees spun).
     - Its  drive_system  can start and stop moving.

6. Examine the code in rosebotics.py for each of the above.
     Make sure you understand that code.

7. Uncomment the next item in  main  of m0.py and then repeat
     Steps 4 to 6, but this time for the Snatch3rRobot's  touch_sensor.
     Discuss with your instructor the use of INHERITANCE.

8. Uncomment the next item in  main  of m0.py and then repeat
     Steps 4 to 6, but this time for the Snatch3rRobot's  color_sensor.
     Discuss with your instructor the use of INHERITANCE.

9. In rosebotics, there are three sets of TODO's, in :
     -- DriveSystem
     -- TouchSensor
     -- ColorSensor
   Each team member should do one of the three sets.
   Make sure that you understand what SELF is in each of these classes.



