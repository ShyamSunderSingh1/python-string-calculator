class StringCalculator:
    def __init__(self):
        # Default delimiter
        self._default_delimiter = ','

    def add(self, numbers: str) -> int:
        """
        Sums numbers in a string, allowing an optional custom delimiter.
        If negative values are encountered, a ValueError is raised.
        """
        # Return 0 for an empty string
        if not numbers:
            return 0

        # Determine the delimiter and the part of the string that holds the actual numbers
        delimiter, number_section = self._determine_delimiter(numbers)
        
        # Convert newlines to the chosen delimiter
        normalized_section = number_section.replace('\n', delimiter)
        
        # Split the string into integers
        values = self._extract_integers(normalized_section, delimiter)
        
        # Validate negative values
        self._check_for_negatives(values)
        
        # Return the total
        return sum(values)

    def _determine_delimiter(self, text: str) -> (str, str):
        """
        Identifies the delimiter if the string starts with '//';
        otherwise returns the default delimiter and the original text.
        """
        if text.startswith('//'):
            # Everything after '//' up to the first newline is the custom delimiter
            delimiter_part, remainder = text.split('\n', 1)
            return delimiter_part[2:], remainder
        # If there's no special directive, use the default delimiter
        return self._default_delimiter, text

    def _extract_integers(self, text: str, delimiter: str) -> list:
        """
        Splits the text by the delimiter, strips whitespace, 
        and converts each non-empty entry into an integer.
        """
        tokens = text.split(delimiter)
        return [int(token.strip()) for token in tokens if token.strip()]

    def _check_for_negatives(self, numbers: list) -> None:
        """
        Raises ValueError if any numbers in the list are negative.
        """
        negative_values = [num for num in numbers if num < 0]
        if negative_values:
            negatives_str = ', '.join(map(str, negative_values))
            raise ValueError(f"Negative numbers not allowed: {negatives_str}")
