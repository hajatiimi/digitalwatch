# digitalwatch

Goal of this third assignment for the Distributed Systems course was
to specify a state model for the system behavior of a Digital Watch
that is inspired by the 1981 Texas Instruments LCD Alarm
Chronograph. The state model was to be specified in the format
accepted by the Statechart Virtual Machine (SVM) tool, a fully
functional interpreter for UML statecharts.

We created the state model using the format suitable for SVM and
tested the model in practice with the Tk GUI bindings provided in the
assignment. The assignment's behavioral requirements for the digital
watch describe seven different requirements. Out of the requirements,
we have implemented the following:

 * Req 1: Time value is updated every second.

 * Req 2: Pressing the top right button turns on the background light.

 * Req 3: Pressing the top left button alternates between the chrono
   and the time display modes.

 * Req 4: When in chrono display mode, the elapsed time is displayed MM:SS:FF.

 * Req 5: When in time display mode, the watch will go into time
   editing mode when the bottom right button is held pressed for at
   least 1.5 seconds.

 * Req 6: When in time display mode, the alarm can be displayed and
   toggled between on or off by pressing the bottom left button.

 * Req 7: When in (either time or alarm) editing mode, briefly
   pressing the bottom left button will increase the current
   selection.

Thus all of the seven requirements were implemented.

We also created a simple finite state machine (FSM) diagram that shows
the different state machines used in the implementation of the digital
watch, and the supported transitionst that "make the digital watch
work". The diagram can be generated in PDF and PNG by running "make"
(assuming Graphviz is installed).

Deliverables:

 * [State model for SVM](digitalwatch.des)
 * [Diagram of states as PDF](digitalwatch.pdf)
