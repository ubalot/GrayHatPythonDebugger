import my_debugger

debugger = my_debugger.debugger()


""" Test 1
In this test you don't see the actual program because it is launched in debug mode.
"""
# debugger.load("C:\\WINDOWS\\system32\\calc.exe")


""" Test 2
In this test you have to enter the pid of the process you want to debug, then it is
unresponsive due to the debugging mode that has been activated by this program.
"""
pid = raw_input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))


""" Test 3
This test is an add to "Test2".
"""
list = debugger.enumerate_threads()

# For each thread in the list we want to grab the value of each of the registers
for thread in list:
    thread_context = debugger.get_thread_context(thread)
    
    # Now let's output the contents of some of the registers
    print "[*] Dumping registers for thread ID: 0x%08x" % thread
    print "[**] EIP: 0x%08x" % thread_context.Eip
    print "[**] ESP: 0x%08x" % thread_context.Esp
    print "[**] EBP: 0x%08x" % thread_context.Ebp
    print "[**] EAX: 0x%08x" % thread_context.Eax
    print "[**] EBX: 0x%08x" % thread_context.Ebx
    print "[**] ECX: 0x%08x" % thread_context.Ecx
    print "[**] EDX: 0x%08x" % thread_context.Edx
    print "[*] END DUMP"


debugger.detach()