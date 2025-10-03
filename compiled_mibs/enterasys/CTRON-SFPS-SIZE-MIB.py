# SNMP MIB module (CTRON-SFPS-SIZE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-SFPS-SIZE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:38 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(sfpsSizeService,
 sfpsSizeServiceAPI) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsSizeService",
    "sfpsSizeServiceAPI")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsSizeServiceTable_Object = MibTable
sfpsSizeServiceTable = _SfpsSizeServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsSizeServiceTable.setStatus("mandatory")
_SfpsSizeServiceEntry_Object = MibTableRow
sfpsSizeServiceEntry = _SfpsSizeServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1)
)
sfpsSizeServiceEntry.setIndexNames(
    (0, "CTRON-SFPS-SIZE-MIB", "sfpsSizeServiceName"),
)
if mibBuilder.loadTexts:
    sfpsSizeServiceEntry.setStatus("mandatory")
_SfpsSizeServiceName_Type = DisplayString
_SfpsSizeServiceName_Object = MibTableColumn
sfpsSizeServiceName = _SfpsSizeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 1),
    _SfpsSizeServiceName_Type()
)
sfpsSizeServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceName.setStatus("mandatory")
_SfpsSizeServiceId_Type = Integer32
_SfpsSizeServiceId_Object = MibTableColumn
sfpsSizeServiceId = _SfpsSizeServiceId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 2),
    _SfpsSizeServiceId_Type()
)
sfpsSizeServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceId.setStatus("mandatory")
_SfpsSizeServiceElemSize_Type = Integer32
_SfpsSizeServiceElemSize_Object = MibTableColumn
sfpsSizeServiceElemSize = _SfpsSizeServiceElemSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 3),
    _SfpsSizeServiceElemSize_Type()
)
sfpsSizeServiceElemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceElemSize.setStatus("mandatory")
_SfpsSizeServiceDesired_Type = Integer32
_SfpsSizeServiceDesired_Object = MibTableColumn
sfpsSizeServiceDesired = _SfpsSizeServiceDesired_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 4),
    _SfpsSizeServiceDesired_Type()
)
sfpsSizeServiceDesired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceDesired.setStatus("mandatory")
_SfpsSizeServiceGranted_Type = Integer32
_SfpsSizeServiceGranted_Object = MibTableColumn
sfpsSizeServiceGranted = _SfpsSizeServiceGranted_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 5),
    _SfpsSizeServiceGranted_Type()
)
sfpsSizeServiceGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceGranted.setStatus("mandatory")
_SfpsSizeServiceIncrement_Type = Integer32
_SfpsSizeServiceIncrement_Object = MibTableColumn
sfpsSizeServiceIncrement = _SfpsSizeServiceIncrement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 6),
    _SfpsSizeServiceIncrement_Type()
)
sfpsSizeServiceIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceIncrement.setStatus("mandatory")
_SfpsSizeServiceTotalBytes_Type = Integer32
_SfpsSizeServiceTotalBytes_Object = MibTableColumn
sfpsSizeServiceTotalBytes = _SfpsSizeServiceTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 7),
    _SfpsSizeServiceTotalBytes_Type()
)
sfpsSizeServiceTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceTotalBytes.setStatus("mandatory")
_SfpsSizeServiceNbrCalls_Type = Integer32
_SfpsSizeServiceNbrCalls_Object = MibTableColumn
sfpsSizeServiceNbrCalls = _SfpsSizeServiceNbrCalls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 8),
    _SfpsSizeServiceNbrCalls_Type()
)
sfpsSizeServiceNbrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceNbrCalls.setStatus("mandatory")


class _SfpsSizeServiceRtnStatus_Type(Integer32):
    """Custom type sfpsSizeServiceRtnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("nvramOk", 2),
          ("unknown", 3),
          ("notAllowed", 4),
          ("nonApiOk", 5))
    )


_SfpsSizeServiceRtnStatus_Type.__name__ = "Integer32"
_SfpsSizeServiceRtnStatus_Object = MibTableColumn
sfpsSizeServiceRtnStatus = _SfpsSizeServiceRtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 9),
    _SfpsSizeServiceRtnStatus_Type()
)
sfpsSizeServiceRtnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceRtnStatus.setStatus("mandatory")


class _SfpsSizeServiceHowGranted_Type(Integer32):
    """Custom type sfpsSizeServiceHowGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("elements", 1),
          ("memory", 2),
          ("other", 3),
          ("notAllowed", 4))
    )


_SfpsSizeServiceHowGranted_Type.__name__ = "Integer32"
_SfpsSizeServiceHowGranted_Object = MibTableColumn
sfpsSizeServiceHowGranted = _SfpsSizeServiceHowGranted_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 10),
    _SfpsSizeServiceHowGranted_Type()
)
sfpsSizeServiceHowGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceHowGranted.setStatus("mandatory")


class _SfpsSizeServiceAPIVerb_Type(Integer32):
    """Custom type sfpsSizeServiceAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("next", 2),
          ("prev", 3),
          ("set", 4),
          ("clear", 5),
          ("clearAll", 6))
    )


_SfpsSizeServiceAPIVerb_Type.__name__ = "Integer32"
_SfpsSizeServiceAPIVerb_Object = MibScalar
sfpsSizeServiceAPIVerb = _SfpsSizeServiceAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 1),
    _SfpsSizeServiceAPIVerb_Type()
)
sfpsSizeServiceAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPIVerb.setStatus("mandatory")
_SfpsSizeServiceAPIName_Type = DisplayString
_SfpsSizeServiceAPIName_Object = MibScalar
sfpsSizeServiceAPIName = _SfpsSizeServiceAPIName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 2),
    _SfpsSizeServiceAPIName_Type()
)
sfpsSizeServiceAPIName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPIName.setStatus("mandatory")
_SfpsSizeServiceAPIId_Type = Integer32
_SfpsSizeServiceAPIId_Object = MibScalar
sfpsSizeServiceAPIId = _SfpsSizeServiceAPIId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 3),
    _SfpsSizeServiceAPIId_Type()
)
sfpsSizeServiceAPIId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPIId.setStatus("mandatory")
_SfpsSizeServiceAPIGrant_Type = DisplayString
_SfpsSizeServiceAPIGrant_Object = MibScalar
sfpsSizeServiceAPIGrant = _SfpsSizeServiceAPIGrant_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 4),
    _SfpsSizeServiceAPIGrant_Type()
)
sfpsSizeServiceAPIGrant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPIGrant.setStatus("mandatory")
_SfpsSizeServiceAPIIncrement_Type = Integer32
_SfpsSizeServiceAPIIncrement_Object = MibScalar
sfpsSizeServiceAPIIncrement = _SfpsSizeServiceAPIIncrement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 5),
    _SfpsSizeServiceAPIIncrement_Type()
)
sfpsSizeServiceAPIIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPIIncrement.setStatus("mandatory")
_SfpsSizeServiceAPINumberSet_Type = Integer32
_SfpsSizeServiceAPINumberSet_Object = MibScalar
sfpsSizeServiceAPINumberSet = _SfpsSizeServiceAPINumberSet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 6),
    _SfpsSizeServiceAPINumberSet_Type()
)
sfpsSizeServiceAPINumberSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPINumberSet.setStatus("mandatory")
_SfpsSizeServiceAPIVersion_Type = Integer32
_SfpsSizeServiceAPIVersion_Object = MibScalar
sfpsSizeServiceAPIVersion = _SfpsSizeServiceAPIVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 7),
    _SfpsSizeServiceAPIVersion_Type()
)
sfpsSizeServiceAPIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSizeServiceAPIVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-SIZE-MIB",
    **{"sfpsSizeServiceTable": sfpsSizeServiceTable,
       "sfpsSizeServiceEntry": sfpsSizeServiceEntry,
       "sfpsSizeServiceName": sfpsSizeServiceName,
       "sfpsSizeServiceId": sfpsSizeServiceId,
       "sfpsSizeServiceElemSize": sfpsSizeServiceElemSize,
       "sfpsSizeServiceDesired": sfpsSizeServiceDesired,
       "sfpsSizeServiceGranted": sfpsSizeServiceGranted,
       "sfpsSizeServiceIncrement": sfpsSizeServiceIncrement,
       "sfpsSizeServiceTotalBytes": sfpsSizeServiceTotalBytes,
       "sfpsSizeServiceNbrCalls": sfpsSizeServiceNbrCalls,
       "sfpsSizeServiceRtnStatus": sfpsSizeServiceRtnStatus,
       "sfpsSizeServiceHowGranted": sfpsSizeServiceHowGranted,
       "sfpsSizeServiceAPIVerb": sfpsSizeServiceAPIVerb,
       "sfpsSizeServiceAPIName": sfpsSizeServiceAPIName,
       "sfpsSizeServiceAPIId": sfpsSizeServiceAPIId,
       "sfpsSizeServiceAPIGrant": sfpsSizeServiceAPIGrant,
       "sfpsSizeServiceAPIIncrement": sfpsSizeServiceAPIIncrement,
       "sfpsSizeServiceAPINumberSet": sfpsSizeServiceAPINumberSet,
       "sfpsSizeServiceAPIVersion": sfpsSizeServiceAPIVersion}
)
