# Concussion-Diagnostics

Purpose: intake data from sensor hardware and use given information about participant to diagnose if they have been concussed, as well as store all of the metric data from this session.

constants.py - stores all constants and values for algorithm (regularly check for numerical values and labels to move here)

Participant.py - a class to hold data fields for the participant, intended to be generic

Athlete.py - extends Participant on assumption that participant is playing a sport, which can improve accuracy of diagnosis

Diagnostic.py - where all functions that diagnose concussion belong

main.py - ***currently*** holds a system loop that can be used to generate dummy values for testing Diagnostic
