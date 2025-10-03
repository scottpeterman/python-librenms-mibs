# SNMP MIB module (NMS-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pbn\NMS-PROCESS-MIB.mib
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:34 2025
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "NMS-TC",
    "EntPhysicalIndexOrZero")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

nmsProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109)
)
if mibBuilder.loadTexts:
    nmsProcessMIB.setRevisions(
        ("2003-10-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsProcessMIBObjects_ObjectIdentity = ObjectIdentity
nmsProcessMIBObjects = _NmsProcessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1)
)
_NmspmCPU_ObjectIdentity = ObjectIdentity
nmspmCPU = _NmspmCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1)
)
_NmspmCPUTotalTable_Object = MibTable
nmspmCPUTotalTable = _NmspmCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nmspmCPUTotalTable.setStatus("current")
_NmspmCPUTotalEntry_Object = MibTableRow
nmspmCPUTotalEntry = _NmspmCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1)
)
nmspmCPUTotalEntry.setIndexNames(
    (0, "NMS-PROCESS-MIB", "nmspmCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    nmspmCPUTotalEntry.setStatus("current")


class _NmspmCPUTotalIndex_Type(Unsigned32):
    """Custom type nmspmCPUTotalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NmspmCPUTotalIndex_Type.__name__ = "Unsigned32"
_NmspmCPUTotalIndex_Object = MibTableColumn
nmspmCPUTotalIndex = _NmspmCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 1),
    _NmspmCPUTotalIndex_Type()
)
nmspmCPUTotalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmspmCPUTotalIndex.setStatus("current")
_NmspmCPUTotalPhysicalIndex_Type = EntPhysicalIndexOrZero
_NmspmCPUTotalPhysicalIndex_Object = MibTableColumn
nmspmCPUTotalPhysicalIndex = _NmspmCPUTotalPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 2),
    _NmspmCPUTotalPhysicalIndex_Type()
)
nmspmCPUTotalPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmCPUTotalPhysicalIndex.setStatus("current")


class _NmspmCPUTotal5sec_Type(Gauge32):
    """Custom type nmspmCPUTotal5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmspmCPUTotal5sec_Type.__name__ = "Gauge32"
_NmspmCPUTotal5sec_Object = MibTableColumn
nmspmCPUTotal5sec = _NmspmCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 3),
    _NmspmCPUTotal5sec_Type()
)
nmspmCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmCPUTotal5sec.setStatus("current")
if mibBuilder.loadTexts:
    nmspmCPUTotal5sec.setUnits("percent")


class _NmspmCPUTotal1min_Type(Gauge32):
    """Custom type nmspmCPUTotal1min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmspmCPUTotal1min_Type.__name__ = "Gauge32"
_NmspmCPUTotal1min_Object = MibTableColumn
nmspmCPUTotal1min = _NmspmCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 4),
    _NmspmCPUTotal1min_Type()
)
nmspmCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmCPUTotal1min.setStatus("current")
if mibBuilder.loadTexts:
    nmspmCPUTotal1min.setUnits("percent")


class _NmspmCPUTotal5min_Type(Gauge32):
    """Custom type nmspmCPUTotal5min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmspmCPUTotal5min_Type.__name__ = "Gauge32"
_NmspmCPUTotal5min_Object = MibTableColumn
nmspmCPUTotal5min = _NmspmCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 1, 1, 5),
    _NmspmCPUTotal5min_Type()
)
nmspmCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmCPUTotal5min.setStatus("current")
if mibBuilder.loadTexts:
    nmspmCPUTotal5min.setUnits("percent")


class _NmspmCPUMaxUtilization_Type(Gauge32):
    """Custom type nmspmCPUMaxUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NmspmCPUMaxUtilization_Type.__name__ = "Gauge32"
_NmspmCPUMaxUtilization_Object = MibScalar
nmspmCPUMaxUtilization = _NmspmCPUMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 2),
    _NmspmCPUMaxUtilization_Type()
)
nmspmCPUMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmCPUMaxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    nmspmCPUMaxUtilization.setUnits("percent")


class _NmspmCPUClearMaxUtilization_Type(Integer32):
    """Custom type nmspmCPUClearMaxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_NmspmCPUClearMaxUtilization_Type.__name__ = "Integer32"
_NmspmCPUClearMaxUtilization_Object = MibScalar
nmspmCPUClearMaxUtilization = _NmspmCPUClearMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 1, 3),
    _NmspmCPUClearMaxUtilization_Type()
)
nmspmCPUClearMaxUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmspmCPUClearMaxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    nmspmCPUClearMaxUtilization.setUnits("percent")
_NmspmProcess_ObjectIdentity = ObjectIdentity
nmspmProcess = _NmspmProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2)
)
_NmspmProcessTable_Object = MibTable
nmspmProcessTable = _NmspmProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nmspmProcessTable.setStatus("current")
_NmspmProcessEntry_Object = MibTableRow
nmspmProcessEntry = _NmspmProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1)
)
nmspmProcessEntry.setIndexNames(
    (0, "NMS-PROCESS-MIB", "nmspmCPUTotalIndex"),
    (0, "NMS-PROCESS-MIB", "nmspmProcessPID"),
)
if mibBuilder.loadTexts:
    nmspmProcessEntry.setStatus("current")
_NmspmProcessPID_Type = Unsigned32
_NmspmProcessPID_Object = MibTableColumn
nmspmProcessPID = _NmspmProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 1),
    _NmspmProcessPID_Type()
)
nmspmProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmProcessPID.setStatus("current")


class _NmspmProcessName_Type(DisplayString):
    """Custom type nmspmProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NmspmProcessName_Type.__name__ = "DisplayString"
_NmspmProcessName_Object = MibTableColumn
nmspmProcessName = _NmspmProcessName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 2),
    _NmspmProcessName_Type()
)
nmspmProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmProcessName.setStatus("current")


class _NmspmProcessPriority_Type(Integer32):
    """Custom type nmspmProcessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              55,
              60,
              128,
              180,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("veryhigh", 55),
          ("high", 60),
          ("normal", 128),
          ("low", 180),
          ("verylow", 255))
    )


_NmspmProcessPriority_Type.__name__ = "Integer32"
_NmspmProcessPriority_Object = MibTableColumn
nmspmProcessPriority = _NmspmProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 3),
    _NmspmProcessPriority_Type()
)
nmspmProcessPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmspmProcessPriority.setStatus("current")
_NmspmProcessTimeCreated_Type = TimeStamp
_NmspmProcessTimeCreated_Object = MibTableColumn
nmspmProcessTimeCreated = _NmspmProcessTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 1, 2, 1, 1, 4),
    _NmspmProcessTimeCreated_Type()
)
nmspmProcessTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmspmProcessTimeCreated.setStatus("current")
_NmsProcessMIBNotifPrefix_ObjectIdentity = ObjectIdentity
nmsProcessMIBNotifPrefix = _NmsProcessMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 2)
)
_NmsProcessMIBNotifs_ObjectIdentity = ObjectIdentity
nmsProcessMIBNotifs = _NmsProcessMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 2, 0)
)
_NmsProcessMIBConformance_ObjectIdentity = ObjectIdentity
nmsProcessMIBConformance = _NmsProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3)
)
_NmspmCompliances_ObjectIdentity = ObjectIdentity
nmspmCompliances = _NmspmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 1)
)
_NmspmGroups_ObjectIdentity = ObjectIdentity
nmspmGroups = _NmspmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2)
)

# Managed Objects groups

nmspmCPUTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2, 1)
)
nmspmCPUTotalGroup.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmCPUTotalPhysicalIndex"),
        ("NMS-PROCESS-MIB", "nmspmCPUTotal5sec"),
        ("NMS-PROCESS-MIB", "nmspmCPUTotal1min"),
        ("NMS-PROCESS-MIB", "nmspmCPUTotal5min"))
)
if mibBuilder.loadTexts:
    nmspmCPUTotalGroup.setStatus("deprecated")

nmspmProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2, 2)
)
nmspmProcessGroup.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmProcessPID"),
        ("NMS-PROCESS-MIB", "nmspmProcessName"),
        ("NMS-PROCESS-MIB", "nmspmProcessuSecs"),
        ("NMS-PROCESS-MIB", "nmspmProcessTimeCreated"))
)
if mibBuilder.loadTexts:
    nmspmProcessGroup.setStatus("deprecated")

nmspmProcessExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2, 3)
)
nmspmProcessExtGroup.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmProcExtMemAllocated"),
        ("NMS-PROCESS-MIB", "nmspmProcExtMemFreed"),
        ("NMS-PROCESS-MIB", "nmspmProcExtInvoked"),
        ("NMS-PROCESS-MIB", "nmspmProcExtRuntime"),
        ("NMS-PROCESS-MIB", "nmspmProcExtUtil5Sec"),
        ("NMS-PROCESS-MIB", "nmspmProcExtUtil1Min"),
        ("NMS-PROCESS-MIB", "nmspmProcExtUtil5Min"),
        ("NMS-PROCESS-MIB", "nmspmProcExtPriority"))
)
if mibBuilder.loadTexts:
    nmspmProcessExtGroup.setStatus("deprecated")

nmspmCPUTotalGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2, 4)
)
nmspmCPUTotalGroupRev.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmCPUTotalPhysicalIndex"),
        ("NMS-PROCESS-MIB", "nmspmCPUTotal5secRev"),
        ("NMS-PROCESS-MIB", "nmspmCPUTotal1minRev"),
        ("NMS-PROCESS-MIB", "nmspmCPUTotal5minRev"))
)
if mibBuilder.loadTexts:
    nmspmCPUTotalGroupRev.setStatus("current")

nmspmProcessExtGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2, 5)
)
nmspmProcessExtGroupRev.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmProcExtMemAllocatedRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtMemFreedRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtInvokedRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtRuntimeRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtUtil5SecRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtUtil1MinRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtUtil5MinRev"),
        ("NMS-PROCESS-MIB", "nmspmProcExtPriorityRev"))
)
if mibBuilder.loadTexts:
    nmspmProcessExtGroupRev.setStatus("current")

nmspmProcessGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 2, 6)
)
nmspmProcessGroupRev.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmProcessPID"),
        ("NMS-PROCESS-MIB", "nmspmProcessName"),
        ("NMS-PROCESS-MIB", "nmspmProcessAverageUSecs"),
        ("NMS-PROCESS-MIB", "nmspmProcessTimeCreated"))
)
if mibBuilder.loadTexts:
    nmspmProcessGroupRev.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nmsProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 1, 1)
)
nmsProcessMIBCompliance.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmCPUTotalGroup"),
        ("NMS-PROCESS-MIB", "nmspmProcessGroup"),
        ("NMS-PROCESS-MIB", "nmspmProcessExtGroup"))
)
if mibBuilder.loadTexts:
    nmsProcessMIBCompliance.setStatus(
        "deprecated"
    )

nmsProcessMIBComplianceRev = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 109, 3, 1, 2)
)
nmsProcessMIBComplianceRev.setObjects(
      *(("NMS-PROCESS-MIB", "nmspmCPUTotalGroupRev"),
        ("NMS-PROCESS-MIB", "nmspmProcessGroupRev"),
        ("NMS-PROCESS-MIB", "nmspmProcessExtGroupRev"))
)
if mibBuilder.loadTexts:
    nmsProcessMIBComplianceRev.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-PROCESS-MIB",
    **{"nmsProcessMIB": nmsProcessMIB,
       "nmsProcessMIBObjects": nmsProcessMIBObjects,
       "nmspmCPU": nmspmCPU,
       "nmspmCPUTotalTable": nmspmCPUTotalTable,
       "nmspmCPUTotalEntry": nmspmCPUTotalEntry,
       "nmspmCPUTotalIndex": nmspmCPUTotalIndex,
       "nmspmCPUTotalPhysicalIndex": nmspmCPUTotalPhysicalIndex,
       "nmspmCPUTotal5sec": nmspmCPUTotal5sec,
       "nmspmCPUTotal1min": nmspmCPUTotal1min,
       "nmspmCPUTotal5min": nmspmCPUTotal5min,
       "nmspmCPUMaxUtilization": nmspmCPUMaxUtilization,
       "nmspmCPUClearMaxUtilization": nmspmCPUClearMaxUtilization,
       "nmspmProcess": nmspmProcess,
       "nmspmProcessTable": nmspmProcessTable,
       "nmspmProcessEntry": nmspmProcessEntry,
       "nmspmProcessPID": nmspmProcessPID,
       "nmspmProcessName": nmspmProcessName,
       "nmspmProcessPriority": nmspmProcessPriority,
       "nmspmProcessTimeCreated": nmspmProcessTimeCreated,
       "nmsProcessMIBNotifPrefix": nmsProcessMIBNotifPrefix,
       "nmsProcessMIBNotifs": nmsProcessMIBNotifs,
       "nmsProcessMIBConformance": nmsProcessMIBConformance,
       "nmspmCompliances": nmspmCompliances,
       "nmsProcessMIBCompliance": nmsProcessMIBCompliance,
       "nmsProcessMIBComplianceRev": nmsProcessMIBComplianceRev,
       "nmspmGroups": nmspmGroups,
       "nmspmCPUTotalGroup": nmspmCPUTotalGroup,
       "nmspmProcessGroup": nmspmProcessGroup,
       "nmspmProcessExtGroup": nmspmProcessExtGroup,
       "nmspmCPUTotalGroupRev": nmspmCPUTotalGroupRev,
       "nmspmProcessExtGroupRev": nmspmProcessExtGroupRev,
       "nmspmProcessGroupRev": nmspmProcessGroupRev}
)
