/*-------------------------------------------------------------------------
 *
 *	  SHIFT_JIS_2004 <--> UTF8
 *
 * Portions Copyright (c) 1996-2021, PostgreSQL Global Development Group
 * Portions Copyright (c) 1994, Regents of the University of California
 *
 * IDENTIFICATION
 *	  src/backend/utils/mb/conversion_procs/utf8_and_sjis2004/utf8_and_sjis2004.c
 *
 *-------------------------------------------------------------------------
 */

#include "postgres.h"
#include "fmgr.h"
#include "mb/pg_wchar.h"
#include "../../Unicode/shift_jis_2004_to_utf8.map"
#include "../../Unicode/utf8_to_shift_jis_2004.map"

PG_MODULE_MAGIC;

PG_FUNCTION_INFO_V1(shift_jis_2004_to_utf8);
PG_FUNCTION_INFO_V1(utf8_to_shift_jis_2004);

/* ----------
 * conv_proc(
 *		INTEGER,	-- source encoding id
 *		INTEGER,	-- destination encoding id
 *		CSTRING,	-- source string (null terminated C string)
 *		CSTRING,	-- destination string (null terminated C string)
 *		INTEGER,	-- source string length
 *		BOOL		-- if true, don't throw an error if conversion fails
 * ) returns INTEGER;
 *
 * Returns the number of bytes successfully converted.
 * ----------
 */
Datum
shift_jis_2004_to_utf8(PG_FUNCTION_ARGS)
{
	unsigned char *src = (unsigned char *) PG_GETARG_CSTRING(2);
	unsigned char *dest = (unsigned char *) PG_GETARG_CSTRING(3);
	int			len = PG_GETARG_INT32(4);
	bool		noError = PG_GETARG_BOOL(5);
	int			converted;

	CHECK_ENCODING_CONVERSION_ARGS(PG_SHIFT_JIS_2004, PG_UTF8);

	converted = LocalToUtf(src, len, dest,
						   &shift_jis_2004_to_unicode_tree,
						   LUmapSHIFT_JIS_2004_combined, lengthof(LUmapSHIFT_JIS_2004_combined),
						   NULL,
						   PG_SHIFT_JIS_2004,
						   noError);

	PG_RETURN_INT32(converted);
}

Datum
utf8_to_shift_jis_2004(PG_FUNCTION_ARGS)
{
	unsigned char *src = (unsigned char *) PG_GETARG_CSTRING(2);
	unsigned char *dest = (unsigned char *) PG_GETARG_CSTRING(3);
	int			len = PG_GETARG_INT32(4);
	bool		noError = PG_GETARG_BOOL(5);
	int			converted;

	CHECK_ENCODING_CONVERSION_ARGS(PG_UTF8, PG_SHIFT_JIS_2004);

	converted = UtfToLocal(src, len, dest,
						   &shift_jis_2004_from_unicode_tree,
						   ULmapSHIFT_JIS_2004_combined, lengthof(ULmapSHIFT_JIS_2004_combined),
						   NULL,
						   PG_SHIFT_JIS_2004,
						   noError);

	PG_RETURN_INT32(converted);
}
