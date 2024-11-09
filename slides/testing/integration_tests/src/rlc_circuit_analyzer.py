class RLCCircuitAnalyzer:
    def __init__(self, resistance, capacitance, initial_voltage=5.0):
        """
        Initializes the RC Circuit Analyzer.

        Parameters:
        - resistance (float): Resistance in ohms (Ω).
        - capacitance (float): Capacitance in farads (F).
        - initial_voltage (float): Initial voltage across the capacitor (default is 5.0V).
        """
        self.R = resistance
        self.C = capacitance
        self.initial_voltage = initial_voltage
        self.time_constant = self.R * self.C

    def get_time_constant(self):
        """Calculates and returns the time constant τ (tau) of the RC circuit."""
        return self.time_constant

    def voltage_at_time(self, time):
        """
        Calculates the voltage across the capacitor at a given time during charging.

        Parameters:
        - time (float): Time in seconds.

        Returns:
        - voltage (float): Voltage across the capacitor at the specified time.
        """
        return self.initial_voltage * (1 - np.exp(-time / self.time_constant))

    def simulate_charging(self, duration, steps=100):
        """
        Simulates and prints the capacitor charging process over a specified duration.

        Parameters:
        - duration (float): Total simulation time in seconds.
        - steps (int): Number of time steps for the simulation (default is 100).
        """
        times = np.linspace(0, duration, steps)
        voltages = [self.voltage_at_time(t) for t in times]

        # Print results in a table-like format
        print("Time (s)\tVoltage (V)")
        for t, v in zip(times, voltages):
            print(f"{t:.2f}\t\t{v:.2f}")