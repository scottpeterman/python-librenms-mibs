# SNMP MIB module (FS-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\FS-PROCESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:52 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36)
)
if mibBuilder.loadTexts:
    fsProcessMIB.setRevisions(
        ("2003-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_FsCPUMIBObjects_ObjectIdentity = ObjectIdentity
fsCPUMIBObjects = _FsCPUMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1)
)
_FsCpuGeneralMibsGroup_ObjectIdentity = ObjectIdentity
fsCpuGeneralMibsGroup = _FsCpuGeneralMibsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1)
)
_FsCPUUtilization5Sec_Type = Percent
_FsCPUUtilization5Sec_Object = MibScalar
fsCPUUtilization5Sec = _FsCPUUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 1),
    _FsCPUUtilization5Sec_Type()
)
fsCPUUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUUtilization5Sec.setStatus("current")
_FsCPUUtilization1Min_Type = Percent
_FsCPUUtilization1Min_Object = MibScalar
fsCPUUtilization1Min = _FsCPUUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 2),
    _FsCPUUtilization1Min_Type()
)
fsCPUUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUUtilization1Min.setStatus("current")
_FsCPUUtilization5Min_Type = Percent
_FsCPUUtilization5Min_Object = MibScalar
fsCPUUtilization5Min = _FsCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 3),
    _FsCPUUtilization5Min_Type()
)
fsCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUUtilization5Min.setStatus("current")
_FsCPUUtilizationWarning_Type = Percent
_FsCPUUtilizationWarning_Object = MibScalar
fsCPUUtilizationWarning = _FsCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 4),
    _FsCPUUtilizationWarning_Type()
)
fsCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCPUUtilizationWarning.setStatus("current")
_FsCPUUtilizationCritical_Type = Percent
_FsCPUUtilizationCritical_Object = MibScalar
fsCPUUtilizationCritical = _FsCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 5),
    _FsCPUUtilizationCritical_Type()
)
fsCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCPUUtilizationCritical.setStatus("current")
_FsCPUMaxUtilization5Sec_Type = Percent
_FsCPUMaxUtilization5Sec_Object = MibScalar
fsCPUMaxUtilization5Sec = _FsCPUMaxUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 6),
    _FsCPUMaxUtilization5Sec_Type()
)
fsCPUMaxUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUMaxUtilization5Sec.setStatus("current")
_FsCPUMaxUtilization1Min_Type = Percent
_FsCPUMaxUtilization1Min_Object = MibScalar
fsCPUMaxUtilization1Min = _FsCPUMaxUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 7),
    _FsCPUMaxUtilization1Min_Type()
)
fsCPUMaxUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUMaxUtilization1Min.setStatus("current")
_FsCPUMaxUtilization5Min_Type = Percent
_FsCPUMaxUtilization5Min_Object = MibScalar
fsCPUMaxUtilization5Min = _FsCPUMaxUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 8),
    _FsCPUMaxUtilization5Min_Type()
)
fsCPUMaxUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUMaxUtilization5Min.setStatus("current")
_FsCPUUtilizationCollectSwitch_Type = Integer32
_FsCPUUtilizationCollectSwitch_Object = MibScalar
fsCPUUtilizationCollectSwitch = _FsCPUUtilizationCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 9),
    _FsCPUUtilizationCollectSwitch_Type()
)
fsCPUUtilizationCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCPUUtilizationCollectSwitch.setStatus("current")
_FsCPUUtilizationCurrent_Type = Percent
_FsCPUUtilizationCurrent_Object = MibScalar
fsCPUUtilizationCurrent = _FsCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 1, 10),
    _FsCPUUtilizationCurrent_Type()
)
fsCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCPUUtilizationCurrent.setStatus("current")
_FsNodeCPUTotalTable_Object = MibTable
fsNodeCPUTotalTable = _FsNodeCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    fsNodeCPUTotalTable.setStatus("current")
_FsNodeCPUTotalEntry_Object = MibTableRow
fsNodeCPUTotalEntry = _FsNodeCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1)
)
fsNodeCPUTotalEntry.setIndexNames(
    (0, "FS-PROCESS-MIB", "fsNodeCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    fsNodeCPUTotalEntry.setStatus("current")
_FsNodeCPUTotalIndex_Type = Integer32
_FsNodeCPUTotalIndex_Object = MibTableColumn
fsNodeCPUTotalIndex = _FsNodeCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 1),
    _FsNodeCPUTotalIndex_Type()
)
fsNodeCPUTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeCPUTotalIndex.setStatus("current")
_FsNodeCPUTotalName_Type = DisplayString
_FsNodeCPUTotalName_Object = MibTableColumn
fsNodeCPUTotalName = _FsNodeCPUTotalName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 2),
    _FsNodeCPUTotalName_Type()
)
fsNodeCPUTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeCPUTotalName.setStatus("current")
_FsNodeCPUTotal5sec_Type = Percent
_FsNodeCPUTotal5sec_Object = MibTableColumn
fsNodeCPUTotal5sec = _FsNodeCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 3),
    _FsNodeCPUTotal5sec_Type()
)
fsNodeCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeCPUTotal5sec.setStatus("current")
_FsNodeCPUTotal1min_Type = Percent
_FsNodeCPUTotal1min_Object = MibTableColumn
fsNodeCPUTotal1min = _FsNodeCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 4),
    _FsNodeCPUTotal1min_Type()
)
fsNodeCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeCPUTotal1min.setStatus("current")
_FsNodeCPUTotal5min_Type = Percent
_FsNodeCPUTotal5min_Object = MibTableColumn
fsNodeCPUTotal5min = _FsNodeCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 5),
    _FsNodeCPUTotal5min_Type()
)
fsNodeCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNodeCPUTotal5min.setStatus("current")
_FsNodeCPUTotalWarning_Type = Percent
_FsNodeCPUTotalWarning_Object = MibTableColumn
fsNodeCPUTotalWarning = _FsNodeCPUTotalWarning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 6),
    _FsNodeCPUTotalWarning_Type()
)
fsNodeCPUTotalWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNodeCPUTotalWarning.setStatus("current")
_FsNodeCPUTotalCritical_Type = Percent
_FsNodeCPUTotalCritical_Object = MibTableColumn
fsNodeCPUTotalCritical = _FsNodeCPUTotalCritical_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 2, 1, 7),
    _FsNodeCPUTotalCritical_Type()
)
fsNodeCPUTotalCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNodeCPUTotalCritical.setStatus("current")
_FsLankApCPUTotalTable_Object = MibTable
fsLankApCPUTotalTable = _FsLankApCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    fsLankApCPUTotalTable.setStatus("current")
_FsLankApCPUTotalEntry_Object = MibTableRow
fsLankApCPUTotalEntry = _FsLankApCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1)
)
fsLankApCPUTotalEntry.setIndexNames(
    (0, "FS-PROCESS-MIB", "fsLankApCPUMacAddr"),
)
if mibBuilder.loadTexts:
    fsLankApCPUTotalEntry.setStatus("current")
_FsLankApCPUMacAddr_Type = MacAddress
_FsLankApCPUMacAddr_Object = MibTableColumn
fsLankApCPUMacAddr = _FsLankApCPUMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1, 1),
    _FsLankApCPUMacAddr_Type()
)
fsLankApCPUMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLankApCPUMacAddr.setStatus("current")
_FsLankApCPUUtilizationCollectSwitch_Type = Integer32
_FsLankApCPUUtilizationCollectSwitch_Object = MibTableColumn
fsLankApCPUUtilizationCollectSwitch = _FsLankApCPUUtilizationCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1, 2),
    _FsLankApCPUUtilizationCollectSwitch_Type()
)
fsLankApCPUUtilizationCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLankApCPUUtilizationCollectSwitch.setStatus("current")
_FsLankApCPUUtilizationWarning_Type = Percent
_FsLankApCPUUtilizationWarning_Object = MibTableColumn
fsLankApCPUUtilizationWarning = _FsLankApCPUUtilizationWarning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1, 3),
    _FsLankApCPUUtilizationWarning_Type()
)
fsLankApCPUUtilizationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLankApCPUUtilizationWarning.setStatus("current")
_FsLankApCPUUtilizationCritical_Type = Percent
_FsLankApCPUUtilizationCritical_Object = MibTableColumn
fsLankApCPUUtilizationCritical = _FsLankApCPUUtilizationCritical_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1, 4),
    _FsLankApCPUUtilizationCritical_Type()
)
fsLankApCPUUtilizationCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLankApCPUUtilizationCritical.setStatus("current")
_FsLankApCPUUtilizationCurrent_Type = Percent
_FsLankApCPUUtilizationCurrent_Object = MibTableColumn
fsLankApCPUUtilizationCurrent = _FsLankApCPUUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1, 5),
    _FsLankApCPUUtilizationCurrent_Type()
)
fsLankApCPUUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLankApCPUUtilizationCurrent.setStatus("current")
_FsLankApCPUUtilization5Min_Type = Percent
_FsLankApCPUUtilization5Min_Object = MibTableColumn
fsLankApCPUUtilization5Min = _FsLankApCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 1, 3, 1, 6),
    _FsLankApCPUUtilization5Min_Type()
)
fsLankApCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLankApCPUUtilization5Min.setStatus("current")
_FsProcessMIBConformance_ObjectIdentity = ObjectIdentity
fsProcessMIBConformance = _FsProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 2)
)
_FsProcessMIBCompliances_ObjectIdentity = ObjectIdentity
fsProcessMIBCompliances = _FsProcessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 2, 1)
)
_FsProcessMIBGroups_ObjectIdentity = ObjectIdentity
fsProcessMIBGroups = _FsProcessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 2, 2)
)

# Managed Objects groups

fsCPUUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 2, 2, 1)
)
fsCPUUtilizationMIBGroup.setObjects(
      *(("FS-PROCESS-MIB", "fsCPUUtilization5Sec"),
        ("FS-PROCESS-MIB", "fsCPUUtilization1Min"),
        ("FS-PROCESS-MIB", "fsCPUUtilization5Min"),
        ("FS-PROCESS-MIB", "fsCPUMaxUtilization5Sec"),
        ("FS-PROCESS-MIB", "fsCPUMaxUtilization1Min"),
        ("FS-PROCESS-MIB", "fsCPUMaxUtilization5Min"),
        ("FS-PROCESS-MIB", "fsCPUUtilizationCollectSwitch"),
        ("FS-PROCESS-MIB", "fsCPUUtilizationCurrent"))
)
if mibBuilder.loadTexts:
    fsCPUUtilizationMIBGroup.setStatus("current")

fsNodeCPUTotalGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 2, 2, 2)
)
fsNodeCPUTotalGroups.setObjects(
      *(("FS-PROCESS-MIB", "fsNodeCPUTotalIndex"),
        ("FS-PROCESS-MIB", "fsNodeCPUTotalName"),
        ("FS-PROCESS-MIB", "fsNodeCPUTotal5sec"),
        ("FS-PROCESS-MIB", "fsNodeCPUTotal1min"),
        ("FS-PROCESS-MIB", "fsNodeCPUTotal5min"),
        ("FS-PROCESS-MIB", "fsNodeCPUTotalWarning"),
        ("FS-PROCESS-MIB", "fsNodeCPUTotalCritical"))
)
if mibBuilder.loadTexts:
    fsNodeCPUTotalGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 36, 2, 1, 1)
)
fsProcessMIBCompliance.setObjects(
    ("FS-PROCESS-MIB", "fsCPUUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    fsProcessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PROCESS-MIB",
    **{"Percent": Percent,
       "fsProcessMIB": fsProcessMIB,
       "fsCPUMIBObjects": fsCPUMIBObjects,
       "fsCpuGeneralMibsGroup": fsCpuGeneralMibsGroup,
       "fsCPUUtilization5Sec": fsCPUUtilization5Sec,
       "fsCPUUtilization1Min": fsCPUUtilization1Min,
       "fsCPUUtilization5Min": fsCPUUtilization5Min,
       "fsCPUUtilizationWarning": fsCPUUtilizationWarning,
       "fsCPUUtilizationCritical": fsCPUUtilizationCritical,
       "fsCPUMaxUtilization5Sec": fsCPUMaxUtilization5Sec,
       "fsCPUMaxUtilization1Min": fsCPUMaxUtilization1Min,
       "fsCPUMaxUtilization5Min": fsCPUMaxUtilization5Min,
       "fsCPUUtilizationCollectSwitch": fsCPUUtilizationCollectSwitch,
       "fsCPUUtilizationCurrent": fsCPUUtilizationCurrent,
       "fsNodeCPUTotalTable": fsNodeCPUTotalTable,
       "fsNodeCPUTotalEntry": fsNodeCPUTotalEntry,
       "fsNodeCPUTotalIndex": fsNodeCPUTotalIndex,
       "fsNodeCPUTotalName": fsNodeCPUTotalName,
       "fsNodeCPUTotal5sec": fsNodeCPUTotal5sec,
       "fsNodeCPUTotal1min": fsNodeCPUTotal1min,
       "fsNodeCPUTotal5min": fsNodeCPUTotal5min,
       "fsNodeCPUTotalWarning": fsNodeCPUTotalWarning,
       "fsNodeCPUTotalCritical": fsNodeCPUTotalCritical,
       "fsLankApCPUTotalTable": fsLankApCPUTotalTable,
       "fsLankApCPUTotalEntry": fsLankApCPUTotalEntry,
       "fsLankApCPUMacAddr": fsLankApCPUMacAddr,
       "fsLankApCPUUtilizationCollectSwitch": fsLankApCPUUtilizationCollectSwitch,
       "fsLankApCPUUtilizationWarning": fsLankApCPUUtilizationWarning,
       "fsLankApCPUUtilizationCritical": fsLankApCPUUtilizationCritical,
       "fsLankApCPUUtilizationCurrent": fsLankApCPUUtilizationCurrent,
       "fsLankApCPUUtilization5Min": fsLankApCPUUtilization5Min,
       "fsProcessMIBConformance": fsProcessMIBConformance,
       "fsProcessMIBCompliances": fsProcessMIBCompliances,
       "fsProcessMIBCompliance": fsProcessMIBCompliance,
       "fsProcessMIBGroups": fsProcessMIBGroups,
       "fsCPUUtilizationMIBGroup": fsCPUUtilizationMIBGroup,
       "fsNodeCPUTotalGroups": fsNodeCPUTotalGroups}
)
