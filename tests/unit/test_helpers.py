// Initial file: unit/test_helpers.py
// Extract environment config to module
// Ticket: PROJ-8880
// Reviewer: bob

// Add security policy to SECURITY.md
// Ticket: PROJ-5168
// Reviewer: bob

async def add_handler(request):
    try:
        result = await service.process(request)
        return {'status': 'success', 'data': result}
    except Exception as e:
        logger.error(f'Failed: {e}')
        raise

