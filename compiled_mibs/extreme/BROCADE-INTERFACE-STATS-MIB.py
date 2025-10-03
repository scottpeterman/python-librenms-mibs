# SNMP MIB module (BROCADE-INTERFACE-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-INTERFACE-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:11 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

brocadeInterfaceStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11)
)
if mibBuilder.loadTexts:
    brocadeInterfaceStatsMIB.setRevisions(
        ("2018-05-29 12:00",
         "2016-09-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsiIfStatsNotifications_ObjectIdentity = ObjectIdentity
bcsiIfStatsNotifications = _BcsiIfStatsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 0)
)
_BcsiIfStatsObjects_ObjectIdentity = ObjectIdentity
bcsiIfStatsObjects = _BcsiIfStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1)
)
_BcsiIfStatsTable_Object = MibTable
bcsiIfStatsTable = _BcsiIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    bcsiIfStatsTable.setStatus("current")
_BcsiIfStatsEntry_Object = MibTableRow
bcsiIfStatsEntry = _BcsiIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1)
)
bcsiIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bcsiIfStatsEntry.setStatus("current")
_BcsiIfStatsInBitsPerSec_Type = CounterBasedGauge64
_BcsiIfStatsInBitsPerSec_Object = MibTableColumn
bcsiIfStatsInBitsPerSec = _BcsiIfStatsInBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 1),
    _BcsiIfStatsInBitsPerSec_Type()
)
bcsiIfStatsInBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsInBitsPerSec.setStatus("current")
_BcsiIfStatsOutBitsPerSec_Type = CounterBasedGauge64
_BcsiIfStatsOutBitsPerSec_Object = MibTableColumn
bcsiIfStatsOutBitsPerSec = _BcsiIfStatsOutBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 2),
    _BcsiIfStatsOutBitsPerSec_Type()
)
bcsiIfStatsOutBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsOutBitsPerSec.setStatus("current")
_BcsiIfStatsInPktsPerSec_Type = Gauge32
_BcsiIfStatsInPktsPerSec_Object = MibTableColumn
bcsiIfStatsInPktsPerSec = _BcsiIfStatsInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 3),
    _BcsiIfStatsInPktsPerSec_Type()
)
bcsiIfStatsInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsInPktsPerSec.setStatus("current")
_BcsiIfStatsOutPktsPerSec_Type = Gauge32
_BcsiIfStatsOutPktsPerSec_Object = MibTableColumn
bcsiIfStatsOutPktsPerSec = _BcsiIfStatsOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 4),
    _BcsiIfStatsOutPktsPerSec_Type()
)
bcsiIfStatsOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsOutPktsPerSec.setStatus("current")
_BcsiIfStatsInUtilization_Type = Unsigned32
_BcsiIfStatsInUtilization_Object = MibTableColumn
bcsiIfStatsInUtilization = _BcsiIfStatsInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 5),
    _BcsiIfStatsInUtilization_Type()
)
bcsiIfStatsInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsInUtilization.setStatus("current")
_BcsiIfStatsOutUtilization_Type = Unsigned32
_BcsiIfStatsOutUtilization_Object = MibTableColumn
bcsiIfStatsOutUtilization = _BcsiIfStatsOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 6),
    _BcsiIfStatsOutUtilization_Type()
)
bcsiIfStatsOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsOutUtilization.setStatus("current")
_BcsiIfStatsInJumboFrames_Type = Counter64
_BcsiIfStatsInJumboFrames_Object = MibTableColumn
bcsiIfStatsInJumboFrames = _BcsiIfStatsInJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 1, 1, 7),
    _BcsiIfStatsInJumboFrames_Type()
)
bcsiIfStatsInJumboFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfStatsInJumboFrames.setStatus("current")
_BcsiIfWatermarkTable_Object = MibTable
bcsiIfWatermarkTable = _BcsiIfWatermarkTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    bcsiIfWatermarkTable.setStatus("current")
_BcsiIfWatermarkEntry_Object = MibTableRow
bcsiIfWatermarkEntry = _BcsiIfWatermarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1)
)
bcsiIfWatermarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkWindowType"),
    (0, "BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkTrafficDirection"),
    (0, "BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkType"),
)
if mibBuilder.loadTexts:
    bcsiIfWatermarkEntry.setStatus("current")


class _BcsiIfWatermarkWindowType_Type(Integer32):
    """Custom type bcsiIfWatermarkWindowType based on Integer32"""
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
        *(("bcsiIfWatermarkCurrent1Hr", 1),
          ("bcsiIfWatermarkLast1Hr", 2),
          ("bcsiIfWatermarkCurrent24Hr", 3),
          ("bcsiIfWatermarkLast24Hr", 4))
    )


_BcsiIfWatermarkWindowType_Type.__name__ = "Integer32"
_BcsiIfWatermarkWindowType_Object = MibTableColumn
bcsiIfWatermarkWindowType = _BcsiIfWatermarkWindowType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 1),
    _BcsiIfWatermarkWindowType_Type()
)
bcsiIfWatermarkWindowType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiIfWatermarkWindowType.setStatus("current")


class _BcsiIfWatermarkTrafficDirection_Type(Integer32):
    """Custom type bcsiIfWatermarkTrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcsiIfWatermarkTrafficDirIn", 1),
          ("bcsiIfWatermarkTrafficDirOut", 2))
    )


_BcsiIfWatermarkTrafficDirection_Type.__name__ = "Integer32"
_BcsiIfWatermarkTrafficDirection_Object = MibTableColumn
bcsiIfWatermarkTrafficDirection = _BcsiIfWatermarkTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 2),
    _BcsiIfWatermarkTrafficDirection_Type()
)
bcsiIfWatermarkTrafficDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiIfWatermarkTrafficDirection.setStatus("current")


class _BcsiIfWatermarkType_Type(Integer32):
    """Custom type bcsiIfWatermarkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcsiIfWatermarkTypeLow", 1),
          ("bcsiIfWatermarkTypeHigh", 2))
    )


_BcsiIfWatermarkType_Type.__name__ = "Integer32"
_BcsiIfWatermarkType_Object = MibTableColumn
bcsiIfWatermarkType = _BcsiIfWatermarkType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 3),
    _BcsiIfWatermarkType_Type()
)
bcsiIfWatermarkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiIfWatermarkType.setStatus("current")
_BcsiIfWatermarkBitRate_Type = CounterBasedGauge64
_BcsiIfWatermarkBitRate_Object = MibTableColumn
bcsiIfWatermarkBitRate = _BcsiIfWatermarkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 4),
    _BcsiIfWatermarkBitRate_Type()
)
bcsiIfWatermarkBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfWatermarkBitRate.setStatus("current")
if mibBuilder.loadTexts:
    bcsiIfWatermarkBitRate.setUnits("BitsPerSec")
_BcsiIfWatermarkPktRate_Type = Gauge32
_BcsiIfWatermarkPktRate_Object = MibTableColumn
bcsiIfWatermarkPktRate = _BcsiIfWatermarkPktRate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 5),
    _BcsiIfWatermarkPktRate_Type()
)
bcsiIfWatermarkPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfWatermarkPktRate.setStatus("current")
if mibBuilder.loadTexts:
    bcsiIfWatermarkPktRate.setUnits("PktsPerSec")
_BcsiIfWatermarkUpdateTime_Type = DateAndTime
_BcsiIfWatermarkUpdateTime_Object = MibTableColumn
bcsiIfWatermarkUpdateTime = _BcsiIfWatermarkUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 6),
    _BcsiIfWatermarkUpdateTime_Type()
)
bcsiIfWatermarkUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfWatermarkUpdateTime.setStatus("current")
_BcsiIfWatermarkWindowStartTime_Type = DateAndTime
_BcsiIfWatermarkWindowStartTime_Object = MibTableColumn
bcsiIfWatermarkWindowStartTime = _BcsiIfWatermarkWindowStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 1, 2, 1, 7),
    _BcsiIfWatermarkWindowStartTime_Type()
)
bcsiIfWatermarkWindowStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiIfWatermarkWindowStartTime.setStatus("current")
_BcsiIfStatsConformance_ObjectIdentity = ObjectIdentity
bcsiIfStatsConformance = _BcsiIfStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 2)
)
_BcsiIfStatsCompliances_ObjectIdentity = ObjectIdentity
bcsiIfStatsCompliances = _BcsiIfStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 2, 1)
)
_BcsiIfStatsGroups_ObjectIdentity = ObjectIdentity
bcsiIfStatsGroups = _BcsiIfStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 2, 2)
)

# Managed Objects groups

bcsiIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 2, 2, 1)
)
bcsiIfStatsGroup.setObjects(
      *(("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsInBitsPerSec"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsOutBitsPerSec"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsInPktsPerSec"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsOutPktsPerSec"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsInUtilization"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsOutUtilization"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsInJumboFrames"))
)
if mibBuilder.loadTexts:
    bcsiIfStatsGroup.setStatus("current")

bcsiIfWatermarkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 2, 2, 2)
)
bcsiIfWatermarkGroup.setObjects(
      *(("BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkBitRate"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkPktRate"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkUpdateTime"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkWindowStartTime"))
)
if mibBuilder.loadTexts:
    bcsiIfWatermarkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bcsiIfStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 11, 2, 1, 1)
)
bcsiIfStatsCompliance.setObjects(
      *(("BROCADE-INTERFACE-STATS-MIB", "bcsiIfStatsGroup"),
        ("BROCADE-INTERFACE-STATS-MIB", "bcsiIfWatermarkGroup"))
)
if mibBuilder.loadTexts:
    bcsiIfStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-INTERFACE-STATS-MIB",
    **{"brocadeInterfaceStatsMIB": brocadeInterfaceStatsMIB,
       "bcsiIfStatsNotifications": bcsiIfStatsNotifications,
       "bcsiIfStatsObjects": bcsiIfStatsObjects,
       "bcsiIfStatsTable": bcsiIfStatsTable,
       "bcsiIfStatsEntry": bcsiIfStatsEntry,
       "bcsiIfStatsInBitsPerSec": bcsiIfStatsInBitsPerSec,
       "bcsiIfStatsOutBitsPerSec": bcsiIfStatsOutBitsPerSec,
       "bcsiIfStatsInPktsPerSec": bcsiIfStatsInPktsPerSec,
       "bcsiIfStatsOutPktsPerSec": bcsiIfStatsOutPktsPerSec,
       "bcsiIfStatsInUtilization": bcsiIfStatsInUtilization,
       "bcsiIfStatsOutUtilization": bcsiIfStatsOutUtilization,
       "bcsiIfStatsInJumboFrames": bcsiIfStatsInJumboFrames,
       "bcsiIfWatermarkTable": bcsiIfWatermarkTable,
       "bcsiIfWatermarkEntry": bcsiIfWatermarkEntry,
       "bcsiIfWatermarkWindowType": bcsiIfWatermarkWindowType,
       "bcsiIfWatermarkTrafficDirection": bcsiIfWatermarkTrafficDirection,
       "bcsiIfWatermarkType": bcsiIfWatermarkType,
       "bcsiIfWatermarkBitRate": bcsiIfWatermarkBitRate,
       "bcsiIfWatermarkPktRate": bcsiIfWatermarkPktRate,
       "bcsiIfWatermarkUpdateTime": bcsiIfWatermarkUpdateTime,
       "bcsiIfWatermarkWindowStartTime": bcsiIfWatermarkWindowStartTime,
       "bcsiIfStatsConformance": bcsiIfStatsConformance,
       "bcsiIfStatsCompliances": bcsiIfStatsCompliances,
       "bcsiIfStatsCompliance": bcsiIfStatsCompliance,
       "bcsiIfStatsGroups": bcsiIfStatsGroups,
       "bcsiIfStatsGroup": bcsiIfStatsGroup,
       "bcsiIfWatermarkGroup": bcsiIfWatermarkGroup}
)
