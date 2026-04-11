$(document).ready(function() {
    
    // Simulate running the multi-class classification
    $('#run-analysis-btn').on('click', function() {
        const selectedRegion = $('#region-select option:selected').text();
        const regionCode = $('#region-select').val();
        
        // Visual feedback
        const originalText = $(this).text();
        $(this).text('Processing Imagery...').css('opacity', '0.7');
        
        // Simulate network request/model inference delay
        setTimeout(() => {
            // Restore button
            $(this).text(originalText).css('opacity', '1');
            
            // Update dummy metrics based on region
            if(regionCode === 'zaf') {
                $('#urban-metric').text('2,847 km²').hide().fadeIn();
                $('#veg-metric').text('1,523 hectares').hide().fadeIn();
            } else {
                $('#urban-metric').text('5,120 km²').hide().fadeIn();
                $('#veg-metric').text('840 hectares').hide().fadeIn();
            }
            
            alert(`Classification complete for satellite imagery in ${selectedRegion}. Model data loaded.`);
        }, 1500);
    });
});
