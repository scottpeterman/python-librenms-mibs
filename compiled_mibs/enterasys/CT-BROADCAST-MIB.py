# SNMP MIB module (CT-BROADCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CT-BROADCAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:06 2025
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

(ctBroadcast,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctBroadcast")

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

_CtBroadcastCtl_ObjectIdentity = ObjectIdentity
ctBroadcastCtl = _CtBroadcastCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1)
)
_CtBroadcastCtlTable_Object = MibTable
ctBroadcastCtlTable = _CtBroadcastCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    ctBroadcastCtlTable.setStatus("mandatory")
_CtBroadcastCtlEntry_Object = MibTableRow
ctBroadcastCtlEntry = _CtBroadcastCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1)
)
ctBroadcastCtlEntry.setIndexNames(
    (0, "CT-BROADCAST-MIB", "ctBroadcastCtlSlotID"),
    (0, "CT-BROADCAST-MIB", "ctBroadcastCtlInterface"),
)
if mibBuilder.loadTexts:
    ctBroadcastCtlEntry.setStatus("mandatory")
_CtBroadcastCtlSlotID_Type = Integer32
_CtBroadcastCtlSlotID_Object = MibTableColumn
ctBroadcastCtlSlotID = _CtBroadcastCtlSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 1),
    _CtBroadcastCtlSlotID_Type()
)
ctBroadcastCtlSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBroadcastCtlSlotID.setStatus("mandatory")
_CtBroadcastCtlInterface_Type = Integer32
_CtBroadcastCtlInterface_Object = MibTableColumn
ctBroadcastCtlInterface = _CtBroadcastCtlInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 2),
    _CtBroadcastCtlInterface_Type()
)
ctBroadcastCtlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBroadcastCtlInterface.setStatus("mandatory")
_CtBroadcastTotalBroadcastFrames_Type = Counter32
_CtBroadcastTotalBroadcastFrames_Object = MibTableColumn
ctBroadcastTotalBroadcastFrames = _CtBroadcastTotalBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 3),
    _CtBroadcastTotalBroadcastFrames_Type()
)
ctBroadcastTotalBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBroadcastTotalBroadcastFrames.setStatus("mandatory")
_CtBroadcastPeakBroadcastRate_Type = Integer32
_CtBroadcastPeakBroadcastRate_Object = MibTableColumn
ctBroadcastPeakBroadcastRate = _CtBroadcastPeakBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 4),
    _CtBroadcastPeakBroadcastRate_Type()
)
ctBroadcastPeakBroadcastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBroadcastPeakBroadcastRate.setStatus("mandatory")
_CtBroadcastPeakBroadcastRateTime_Type = TimeTicks
_CtBroadcastPeakBroadcastRateTime_Object = MibTableColumn
ctBroadcastPeakBroadcastRateTime = _CtBroadcastPeakBroadcastRateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 5),
    _CtBroadcastPeakBroadcastRateTime_Type()
)
ctBroadcastPeakBroadcastRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBroadcastPeakBroadcastRateTime.setStatus("mandatory")


class _CtBroadcastPeakBroadcastClear_Type(Integer32):
    """Custom type ctBroadcastPeakBroadcastClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noClear", 2))
    )


_CtBroadcastPeakBroadcastClear_Type.__name__ = "Integer32"
_CtBroadcastPeakBroadcastClear_Object = MibTableColumn
ctBroadcastPeakBroadcastClear = _CtBroadcastPeakBroadcastClear_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 6),
    _CtBroadcastPeakBroadcastClear_Type()
)
ctBroadcastPeakBroadcastClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBroadcastPeakBroadcastClear.setStatus("mandatory")


class _CtBroadcastDesiredBroadcastThreshold_Type(Integer32):
    """Custom type ctBroadcastDesiredBroadcastThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtBroadcastDesiredBroadcastThreshold_Type.__name__ = "Integer32"
_CtBroadcastDesiredBroadcastThreshold_Object = MibTableColumn
ctBroadcastDesiredBroadcastThreshold = _CtBroadcastDesiredBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 7),
    _CtBroadcastDesiredBroadcastThreshold_Type()
)
ctBroadcastDesiredBroadcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBroadcastDesiredBroadcastThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-BROADCAST-MIB",
    **{"ctBroadcastCtl": ctBroadcastCtl,
       "ctBroadcastCtlTable": ctBroadcastCtlTable,
       "ctBroadcastCtlEntry": ctBroadcastCtlEntry,
       "ctBroadcastCtlSlotID": ctBroadcastCtlSlotID,
       "ctBroadcastCtlInterface": ctBroadcastCtlInterface,
       "ctBroadcastTotalBroadcastFrames": ctBroadcastTotalBroadcastFrames,
       "ctBroadcastPeakBroadcastRate": ctBroadcastPeakBroadcastRate,
       "ctBroadcastPeakBroadcastRateTime": ctBroadcastPeakBroadcastRateTime,
       "ctBroadcastPeakBroadcastClear": ctBroadcastPeakBroadcastClear,
       "ctBroadcastDesiredBroadcastThreshold": ctBroadcastDesiredBroadcastThreshold}
)
