# SNMP MIB module (ERICSSON-ROUTER-CPU-METER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-CPU-METER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:27 2025
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

(eriRouterMgmt,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterMgmt")

(EriRouterPercentage,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-TC",
    "EriRouterPercentage")

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

eriRouterCpuMeterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6)
)
if mibBuilder.loadTexts:
    eriRouterCpuMeterMIB.setRevisions(
        ("2015-01-14 18:00",
         "2011-12-13 18:00",
         "2011-01-19 18:00",
         "2002-12-16 00:00",
         "2002-06-26 00:00",
         "2002-05-29 00:00",
         "1999-06-16 23:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percentage(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_EriRouterCpuMeterMIBObjects_ObjectIdentity = ObjectIdentity
eriRouterCpuMeterMIBObjects = _EriRouterCpuMeterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1)
)
_EriRouterCpuMeterFiveSecondAvg_Type = EriRouterPercentage
_EriRouterCpuMeterFiveSecondAvg_Object = MibScalar
eriRouterCpuMeterFiveSecondAvg = _EriRouterCpuMeterFiveSecondAvg_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1, 1),
    _EriRouterCpuMeterFiveSecondAvg_Type()
)
eriRouterCpuMeterFiveSecondAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuMeterFiveSecondAvg.setStatus("current")
_EriRouterCpuMeterOneMinuteAvg_Type = EriRouterPercentage
_EriRouterCpuMeterOneMinuteAvg_Object = MibScalar
eriRouterCpuMeterOneMinuteAvg = _EriRouterCpuMeterOneMinuteAvg_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1, 2),
    _EriRouterCpuMeterOneMinuteAvg_Type()
)
eriRouterCpuMeterOneMinuteAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuMeterOneMinuteAvg.setStatus("current")
_EriRouterCpuMeterFiveMinuteAvg_Type = EriRouterPercentage
_EriRouterCpuMeterFiveMinuteAvg_Object = MibScalar
eriRouterCpuMeterFiveMinuteAvg = _EriRouterCpuMeterFiveMinuteAvg_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1, 3),
    _EriRouterCpuMeterFiveMinuteAvg_Type()
)
eriRouterCpuMeterFiveMinuteAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuMeterFiveMinuteAvg.setStatus("current")
_EriRouterCpuMeterFiveSecondPeak_Type = EriRouterPercentage
_EriRouterCpuMeterFiveSecondPeak_Object = MibScalar
eriRouterCpuMeterFiveSecondPeak = _EriRouterCpuMeterFiveSecondPeak_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1, 4),
    _EriRouterCpuMeterFiveSecondPeak_Type()
)
eriRouterCpuMeterFiveSecondPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuMeterFiveSecondPeak.setStatus("current")
_EriRouterCpuMeterOneMinutePeak_Type = EriRouterPercentage
_EriRouterCpuMeterOneMinutePeak_Object = MibScalar
eriRouterCpuMeterOneMinutePeak = _EriRouterCpuMeterOneMinutePeak_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1, 5),
    _EriRouterCpuMeterOneMinutePeak_Type()
)
eriRouterCpuMeterOneMinutePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuMeterOneMinutePeak.setStatus("current")
_EriRouterCpuMeterFiveMinutePeak_Type = EriRouterPercentage
_EriRouterCpuMeterFiveMinutePeak_Object = MibScalar
eriRouterCpuMeterFiveMinutePeak = _EriRouterCpuMeterFiveMinutePeak_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 1, 6),
    _EriRouterCpuMeterFiveMinutePeak_Type()
)
eriRouterCpuMeterFiveMinutePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuMeterFiveMinutePeak.setStatus("current")
_EriRouterCpuMeterMIBConformance_ObjectIdentity = ObjectIdentity
eriRouterCpuMeterMIBConformance = _EriRouterCpuMeterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2)
)
_EriRouterCpuMeterMIBGroups_ObjectIdentity = ObjectIdentity
eriRouterCpuMeterMIBGroups = _EriRouterCpuMeterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 1)
)
_EriRouterCpuMeterMIBCompliances_ObjectIdentity = ObjectIdentity
eriRouterCpuMeterMIBCompliances = _EriRouterCpuMeterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 2)
)
_EriRouterCpuProcGroups_ObjectIdentity = ObjectIdentity
eriRouterCpuProcGroups = _EriRouterCpuProcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 3)
)
_EriRouterCpuProcMIBObjects_ObjectIdentity = ObjectIdentity
eriRouterCpuProcMIBObjects = _EriRouterCpuProcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3)
)
_EriRouterCpuProcTable_Object = MibTable
eriRouterCpuProcTable = _EriRouterCpuProcTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    eriRouterCpuProcTable.setStatus("current")
_EriRouterCpuProcEntry_Object = MibTableRow
eriRouterCpuProcEntry = _EriRouterCpuProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1)
)
eriRouterCpuProcEntry.setIndexNames(
    (1, "ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcName"),
)
if mibBuilder.loadTexts:
    eriRouterCpuProcEntry.setStatus("current")


class _EriRouterCpuProcName_Type(DisplayString):
    """Custom type eriRouterCpuProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 114),
    )


_EriRouterCpuProcName_Type.__name__ = "DisplayString"
_EriRouterCpuProcName_Object = MibTableColumn
eriRouterCpuProcName = _EriRouterCpuProcName_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 1),
    _EriRouterCpuProcName_Type()
)
eriRouterCpuProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProcName.setStatus("current")


class _EriRouterCpuProcPriority_Type(Unsigned32):
    """Custom type eriRouterCpuProcPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EriRouterCpuProcPriority_Type.__name__ = "Unsigned32"
_EriRouterCpuProcPriority_Object = MibTableColumn
eriRouterCpuProcPriority = _EriRouterCpuProcPriority_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 2),
    _EriRouterCpuProcPriority_Type()
)
eriRouterCpuProcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProcPriority.setStatus("current")
_EriRouterCpuProcTime_Type = Counter32
_EriRouterCpuProcTime_Object = MibTableColumn
eriRouterCpuProcTime = _EriRouterCpuProcTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 3),
    _EriRouterCpuProcTime_Type()
)
eriRouterCpuProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProcTime.setStatus("current")
_EriRouterCpuProcCalls_Type = Counter32
_EriRouterCpuProcCalls_Object = MibTableColumn
eriRouterCpuProcCalls = _EriRouterCpuProcCalls_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 4),
    _EriRouterCpuProcCalls_Type()
)
eriRouterCpuProcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProcCalls.setStatus("current")
_EriRouterCpuProc5Sec_Type = EriRouterPercentage
_EriRouterCpuProc5Sec_Object = MibTableColumn
eriRouterCpuProc5Sec = _EriRouterCpuProc5Sec_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 5),
    _EriRouterCpuProc5Sec_Type()
)
eriRouterCpuProc5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProc5Sec.setStatus("current")
_EriRouterCpuProc1Min_Type = EriRouterPercentage
_EriRouterCpuProc1Min_Object = MibTableColumn
eriRouterCpuProc1Min = _EriRouterCpuProc1Min_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 6),
    _EriRouterCpuProc1Min_Type()
)
eriRouterCpuProc1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProc1Min.setStatus("current")
_EriRouterCpuProc5Min_Type = EriRouterPercentage
_EriRouterCpuProc5Min_Object = MibTableColumn
eriRouterCpuProc5Min = _EriRouterCpuProc5Min_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 7),
    _EriRouterCpuProc5Min_Type()
)
eriRouterCpuProc5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProc5Min.setStatus("current")
_EriRouterCpuProcLongest_Type = Gauge32
_EriRouterCpuProcLongest_Object = MibTableColumn
eriRouterCpuProcLongest = _EriRouterCpuProcLongest_Object(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 3, 1, 1, 8),
    _EriRouterCpuProcLongest_Type()
)
eriRouterCpuProcLongest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriRouterCpuProcLongest.setStatus("current")

# Managed Objects groups

eriRouterCpuMeterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 1, 1)
)
eriRouterCpuMeterStatsGroup.setObjects(
      *(("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterFiveSecondAvg"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterOneMinuteAvg"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterFiveMinuteAvg"))
)
if mibBuilder.loadTexts:
    eriRouterCpuMeterStatsGroup.setStatus("deprecated")

eriRouterCpuMeterStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 1, 2)
)
eriRouterCpuMeterStatsGroup2.setObjects(
      *(("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterFiveSecondAvg"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterOneMinuteAvg"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterFiveMinuteAvg"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterFiveSecondPeak"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterOneMinutePeak"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterFiveMinutePeak"))
)
if mibBuilder.loadTexts:
    eriRouterCpuMeterStatsGroup2.setStatus("current")

eriRouterCpuProcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 3, 1)
)
eriRouterCpuProcGroup.setObjects(
      *(("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcName"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcPriority"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcTime"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcCalls"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProc5Sec"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProc1Min"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProc5Min"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcLongest"))
)
if mibBuilder.loadTexts:
    eriRouterCpuProcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

eriRouterCpuMeterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 2, 1)
)
eriRouterCpuMeterMIBCompliance.setObjects(
    ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterStatsGroup")
)
if mibBuilder.loadTexts:
    eriRouterCpuMeterMIBCompliance.setStatus(
        "deprecated"
    )

eriRouterCpuMeterMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 2, 2)
)
eriRouterCpuMeterMIBCompliance1.setObjects(
      *(("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterStatsGroup"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcGroup"))
)
if mibBuilder.loadTexts:
    eriRouterCpuMeterMIBCompliance1.setStatus(
        "deprecated"
    )

eriRouterCpuMeterMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 218, 2, 6, 2, 2, 3)
)
eriRouterCpuMeterMIBCompliance2.setObjects(
      *(("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuMeterStatsGroup2"),
        ("ERICSSON-ROUTER-CPU-METER-MIB", "eriRouterCpuProcGroup"))
)
if mibBuilder.loadTexts:
    eriRouterCpuMeterMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-CPU-METER-MIB",
    **{"Percentage": Percentage,
       "eriRouterCpuMeterMIB": eriRouterCpuMeterMIB,
       "eriRouterCpuMeterMIBObjects": eriRouterCpuMeterMIBObjects,
       "eriRouterCpuMeterFiveSecondAvg": eriRouterCpuMeterFiveSecondAvg,
       "eriRouterCpuMeterOneMinuteAvg": eriRouterCpuMeterOneMinuteAvg,
       "eriRouterCpuMeterFiveMinuteAvg": eriRouterCpuMeterFiveMinuteAvg,
       "eriRouterCpuMeterFiveSecondPeak": eriRouterCpuMeterFiveSecondPeak,
       "eriRouterCpuMeterOneMinutePeak": eriRouterCpuMeterOneMinutePeak,
       "eriRouterCpuMeterFiveMinutePeak": eriRouterCpuMeterFiveMinutePeak,
       "eriRouterCpuMeterMIBConformance": eriRouterCpuMeterMIBConformance,
       "eriRouterCpuMeterMIBGroups": eriRouterCpuMeterMIBGroups,
       "eriRouterCpuMeterStatsGroup": eriRouterCpuMeterStatsGroup,
       "eriRouterCpuMeterStatsGroup2": eriRouterCpuMeterStatsGroup2,
       "eriRouterCpuMeterMIBCompliances": eriRouterCpuMeterMIBCompliances,
       "eriRouterCpuMeterMIBCompliance": eriRouterCpuMeterMIBCompliance,
       "eriRouterCpuMeterMIBCompliance1": eriRouterCpuMeterMIBCompliance1,
       "eriRouterCpuMeterMIBCompliance2": eriRouterCpuMeterMIBCompliance2,
       "eriRouterCpuProcGroups": eriRouterCpuProcGroups,
       "eriRouterCpuProcGroup": eriRouterCpuProcGroup,
       "eriRouterCpuProcMIBObjects": eriRouterCpuProcMIBObjects,
       "eriRouterCpuProcTable": eriRouterCpuProcTable,
       "eriRouterCpuProcEntry": eriRouterCpuProcEntry,
       "eriRouterCpuProcName": eriRouterCpuProcName,
       "eriRouterCpuProcPriority": eriRouterCpuProcPriority,
       "eriRouterCpuProcTime": eriRouterCpuProcTime,
       "eriRouterCpuProcCalls": eriRouterCpuProcCalls,
       "eriRouterCpuProc5Sec": eriRouterCpuProc5Sec,
       "eriRouterCpuProc1Min": eriRouterCpuProc1Min,
       "eriRouterCpuProc5Min": eriRouterCpuProc5Min,
       "eriRouterCpuProcLongest": eriRouterCpuProcLongest}
)
