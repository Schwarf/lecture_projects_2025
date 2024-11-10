from rlc_circuit_analyzer import RLCCircuitAnalyzer

# Example usage:
if __name__ == "__main__":
    # Example circuit values
    R = 100  # Resistance in ohms
    L = 1e-3  # Inductance in henries
    C = 10e-9  # Capacitance in farads

    analyzer = RLCCircuitAnalyzer(R, L, C)
    resonance_frequencies = analyzer.analyze_resonance()

    if resonance_frequencies is None:
        print("No real resonant frequency found.")
    elif isinstance(resonance_frequencies, tuple):
        print(f"Resonant Frequencies (ω): {resonance_frequencies[0]:.2e} rad/s, {resonance_frequencies[1]:.2e} rad/s")
    else:
        print(f"Resonant Frequency (ω): {resonance_frequencies:.2e} rad/s")
