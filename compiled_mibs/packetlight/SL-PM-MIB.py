# SNMP MIB module (SL-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:59 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(XpdrServiceType,) = mibBuilder.importSymbols(
    "SL-XPDR-MIB",
    "XpdrServiceType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slPmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlPmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("native", 1)
    )



class SlPmL2Type(TextualConvention, Integer32):
    status = "current"
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
        *(("rxPackets", 1),
          ("txPackets", 2),
          ("rxBytes", 3),
          ("txBytes", 4),
          ("rxCrc", 5),
          ("txCrc", 6))
    )



class SlPmDirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("near", 1),
          ("far", 2))
    )



class SlPmIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 1),
          ("day", 2))
    )



# MIB Managed Objects in the order of their OIDs

_SlPmIntervals_ObjectIdentity = ObjectIdentity
slPmIntervals = _SlPmIntervals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1)
)
_SlPmIntervalTable_Object = MibTable
slPmIntervalTable = _SlPmIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1)
)
if mibBuilder.loadTexts:
    slPmIntervalTable.setStatus("current")
_SlPmIntervalEntry_Object = MibTableRow
slPmIntervalEntry = _SlPmIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1)
)
slPmIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-PM-MIB", "slPmType"),
    (0, "SL-PM-MIB", "slPmDirectionType"),
    (0, "SL-PM-MIB", "slPmIntervalType"),
    (0, "SL-PM-MIB", "slPmIntervalNumber"),
)
if mibBuilder.loadTexts:
    slPmIntervalEntry.setStatus("current")
_SlPmType_Type = SlPmType
_SlPmType_Object = MibTableColumn
slPmType = _SlPmType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 1),
    _SlPmType_Type()
)
slPmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmType.setStatus("current")
_SlPmDirectionType_Type = SlPmDirectionType
_SlPmDirectionType_Object = MibTableColumn
slPmDirectionType = _SlPmDirectionType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 2),
    _SlPmDirectionType_Type()
)
slPmDirectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmDirectionType.setStatus("current")
_SlPmIntervalType_Type = SlPmIntervalType
_SlPmIntervalType_Object = MibTableColumn
slPmIntervalType = _SlPmIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 3),
    _SlPmIntervalType_Type()
)
slPmIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmIntervalType.setStatus("current")


class _SlPmIntervalNumber_Type(Integer32):
    """Custom type slPmIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_SlPmIntervalNumber_Type.__name__ = "Integer32"
_SlPmIntervalNumber_Object = MibTableColumn
slPmIntervalNumber = _SlPmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 4),
    _SlPmIntervalNumber_Type()
)
slPmIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmIntervalNumber.setStatus("current")
_SlPmIntervalCVs_Type = PerfIntervalCount
_SlPmIntervalCVs_Object = MibTableColumn
slPmIntervalCVs = _SlPmIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 5),
    _SlPmIntervalCVs_Type()
)
slPmIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalCVs.setStatus("current")
_SlPmIntervalESs_Type = PerfIntervalCount
_SlPmIntervalESs_Object = MibTableColumn
slPmIntervalESs = _SlPmIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 6),
    _SlPmIntervalESs_Type()
)
slPmIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalESs.setStatus("current")
_SlPmIntervalSESs_Type = PerfIntervalCount
_SlPmIntervalSESs_Object = MibTableColumn
slPmIntervalSESs = _SlPmIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 7),
    _SlPmIntervalSESs_Type()
)
slPmIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalSESs.setStatus("current")
_SlPmIntervalSEFSs_Type = PerfIntervalCount
_SlPmIntervalSEFSs_Object = MibTableColumn
slPmIntervalSEFSs = _SlPmIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 8),
    _SlPmIntervalSEFSs_Type()
)
slPmIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalSEFSs.setStatus("current")
_SlPmIntervalUASs_Type = PerfIntervalCount
_SlPmIntervalUASs_Object = MibTableColumn
slPmIntervalUASs = _SlPmIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 9),
    _SlPmIntervalUASs_Type()
)
slPmIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalUASs.setStatus("current")
_SlPmIntervalValidData_Type = TruthValue
_SlPmIntervalValidData_Object = MibTableColumn
slPmIntervalValidData = _SlPmIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 10),
    _SlPmIntervalValidData_Type()
)
slPmIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalValidData.setStatus("current")
_SlPmIntervalTcaFlag_Type = TruthValue
_SlPmIntervalTcaFlag_Object = MibTableColumn
slPmIntervalTcaFlag = _SlPmIntervalTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 11),
    _SlPmIntervalTcaFlag_Type()
)
slPmIntervalTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalTcaFlag.setStatus("current")
_SlPmIntervalReset_Type = Integer32
_SlPmIntervalReset_Object = MibTableColumn
slPmIntervalReset = _SlPmIntervalReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 12),
    _SlPmIntervalReset_Type()
)
slPmIntervalReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slPmIntervalReset.setStatus("current")
_SlPmIntervalStartTime_Type = DateAndTime
_SlPmIntervalStartTime_Object = MibTableColumn
slPmIntervalStartTime = _SlPmIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 13),
    _SlPmIntervalStartTime_Type()
)
slPmIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmIntervalStartTime.setStatus("current")
_SlPmServiceType_Type = XpdrServiceType
_SlPmServiceType_Object = MibTableColumn
slPmServiceType = _SlPmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 14),
    _SlPmServiceType_Type()
)
slPmServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmServiceType.setStatus("current")
_SlPmL2Intervals_ObjectIdentity = ObjectIdentity
slPmL2Intervals = _SlPmL2Intervals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2)
)
_SlPmL2Table_Object = MibTable
slPmL2Table = _SlPmL2Table_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1)
)
if mibBuilder.loadTexts:
    slPmL2Table.setStatus("current")
_SlPmL2Entry_Object = MibTableRow
slPmL2Entry = _SlPmL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1)
)
slPmL2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SL-PM-MIB", "slPmL2CounterType"),
    (0, "SL-PM-MIB", "slPmL2IntervalType"),
    (0, "SL-PM-MIB", "slPmL2IntervalNumber"),
)
if mibBuilder.loadTexts:
    slPmL2Entry.setStatus("current")
_SlPmL2CounterType_Type = SlPmL2Type
_SlPmL2CounterType_Object = MibTableColumn
slPmL2CounterType = _SlPmL2CounterType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 1),
    _SlPmL2CounterType_Type()
)
slPmL2CounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmL2CounterType.setStatus("current")
_SlPmL2IntervalType_Type = SlPmIntervalType
_SlPmL2IntervalType_Object = MibTableColumn
slPmL2IntervalType = _SlPmL2IntervalType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 2),
    _SlPmL2IntervalType_Type()
)
slPmL2IntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmL2IntervalType.setStatus("current")


class _SlPmL2IntervalNumber_Type(Integer32):
    """Custom type slPmL2IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_SlPmL2IntervalNumber_Type.__name__ = "Integer32"
_SlPmL2IntervalNumber_Object = MibTableColumn
slPmL2IntervalNumber = _SlPmL2IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 3),
    _SlPmL2IntervalNumber_Type()
)
slPmL2IntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slPmL2IntervalNumber.setStatus("current")
_SlPmL2Count_Type = Counter64
_SlPmL2Count_Object = MibTableColumn
slPmL2Count = _SlPmL2Count_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 4),
    _SlPmL2Count_Type()
)
slPmL2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmL2Count.setStatus("current")
_SlPmL2ValidData_Type = TruthValue
_SlPmL2ValidData_Object = MibTableColumn
slPmL2ValidData = _SlPmL2ValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 5),
    _SlPmL2ValidData_Type()
)
slPmL2ValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmL2ValidData.setStatus("current")
_SlPmL2Reset_Type = Integer32
_SlPmL2Reset_Object = MibTableColumn
slPmL2Reset = _SlPmL2Reset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 6),
    _SlPmL2Reset_Type()
)
slPmL2Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slPmL2Reset.setStatus("current")
_SlPmL2StartTime_Type = DateAndTime
_SlPmL2StartTime_Object = MibTableColumn
slPmL2StartTime = _SlPmL2StartTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 7),
    _SlPmL2StartTime_Type()
)
slPmL2StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmL2StartTime.setStatus("current")
_SlPmL2ServiceType_Type = XpdrServiceType
_SlPmL2ServiceType_Object = MibTableColumn
slPmL2ServiceType = _SlPmL2ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 8),
    _SlPmL2ServiceType_Type()
)
slPmL2ServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPmL2ServiceType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-PM-MIB",
    **{"SlPmType": SlPmType,
       "SlPmL2Type": SlPmL2Type,
       "SlPmDirectionType": SlPmDirectionType,
       "SlPmIntervalType": SlPmIntervalType,
       "slPmMib": slPmMib,
       "slPmIntervals": slPmIntervals,
       "slPmIntervalTable": slPmIntervalTable,
       "slPmIntervalEntry": slPmIntervalEntry,
       "slPmType": slPmType,
       "slPmDirectionType": slPmDirectionType,
       "slPmIntervalType": slPmIntervalType,
       "slPmIntervalNumber": slPmIntervalNumber,
       "slPmIntervalCVs": slPmIntervalCVs,
       "slPmIntervalESs": slPmIntervalESs,
       "slPmIntervalSESs": slPmIntervalSESs,
       "slPmIntervalSEFSs": slPmIntervalSEFSs,
       "slPmIntervalUASs": slPmIntervalUASs,
       "slPmIntervalValidData": slPmIntervalValidData,
       "slPmIntervalTcaFlag": slPmIntervalTcaFlag,
       "slPmIntervalReset": slPmIntervalReset,
       "slPmIntervalStartTime": slPmIntervalStartTime,
       "slPmServiceType": slPmServiceType,
       "slPmL2Intervals": slPmL2Intervals,
       "slPmL2Table": slPmL2Table,
       "slPmL2Entry": slPmL2Entry,
       "slPmL2CounterType": slPmL2CounterType,
       "slPmL2IntervalType": slPmL2IntervalType,
       "slPmL2IntervalNumber": slPmL2IntervalNumber,
       "slPmL2Count": slPmL2Count,
       "slPmL2ValidData": slPmL2ValidData,
       "slPmL2Reset": slPmL2Reset,
       "slPmL2StartTime": slPmL2StartTime,
       "slPmL2ServiceType": slPmL2ServiceType}
)
