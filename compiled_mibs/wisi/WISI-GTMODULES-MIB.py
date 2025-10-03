# SNMP MIB module (WISI-GTMODULES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wisi\WISI-GTMODULES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:17 2025
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

(gtUnit,) = mibBuilder.importSymbols(
    "WISI-TANGRAM-MIB",
    "gtUnit")


# MODULE-IDENTITY

gtModulesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    gtModulesMIB.setRevisions(
        ("2016-09-08 00:00",
         "2016-06-08 00:00",
         "2015-06-16 00:00",
         "2013-07-29 00:00",
         "2013-06-26 00:00",
         "2012-10-31 00:00",
         "2011-12-13 00:00",
         "2011-09-08 00:00",
         "2011-04-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GtModulesNotifications_ObjectIdentity = ObjectIdentity
gtModulesNotifications = _GtModulesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0)
)
_GtModulesObjects_ObjectIdentity = ObjectIdentity
gtModulesObjects = _GtModulesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1)
)


class _GtThisModuleSlot_Type(Unsigned32):
    """Custom type gtThisModuleSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GtThisModuleSlot_Type.__name__ = "Unsigned32"
_GtThisModuleSlot_Object = MibScalar
gtThisModuleSlot = _GtThisModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 1),
    _GtThisModuleSlot_Type()
)
gtThisModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtThisModuleSlot.setStatus("current")


class _GtNumModules_Type(Unsigned32):
    """Custom type gtNumModules based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GtNumModules_Type.__name__ = "Unsigned32"
_GtNumModules_Object = MibScalar
gtNumModules = _GtNumModules_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 2),
    _GtNumModules_Type()
)
gtNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNumModules.setStatus("current")
_GtModulesTable_Object = MibTable
gtModulesTable = _GtModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    gtModulesTable.setStatus("current")
_GtModulesEntry_Object = MibTableRow
gtModulesEntry = _GtModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1)
)
gtModulesEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
)
if mibBuilder.loadTexts:
    gtModulesEntry.setStatus("current")


class _GtModule_Type(Unsigned32):
    """Custom type gtModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GtModule_Type.__name__ = "Unsigned32"
_GtModule_Object = MibTableColumn
gtModule = _GtModule_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 1),
    _GtModule_Type()
)
gtModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtModule.setStatus("current")
_GtModuleName_Type = DisplayString
_GtModuleName_Object = MibTableColumn
gtModuleName = _GtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 2),
    _GtModuleName_Type()
)
gtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleName.setStatus("current")
_GtModuleHWID_Type = DisplayString
_GtModuleHWID_Object = MibTableColumn
gtModuleHWID = _GtModuleHWID_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 3),
    _GtModuleHWID_Type()
)
gtModuleHWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleHWID.setStatus("current")
_GtModuleFWID_Type = DisplayString
_GtModuleFWID_Object = MibTableColumn
gtModuleFWID = _GtModuleFWID_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 4),
    _GtModuleFWID_Type()
)
gtModuleFWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleFWID.setStatus("current")
_GtModuleSerNo_Type = DisplayString
_GtModuleSerNo_Object = MibTableColumn
gtModuleSerNo = _GtModuleSerNo_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 5),
    _GtModuleSerNo_Type()
)
gtModuleSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleSerNo.setStatus("current")
_GtModuleUptime_Type = Counter32
_GtModuleUptime_Object = MibTableColumn
gtModuleUptime = _GtModuleUptime_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 6),
    _GtModuleUptime_Type()
)
gtModuleUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleUptime.setStatus("current")
if mibBuilder.loadTexts:
    gtModuleUptime.setUnits("s")
_GtModuleLifetime_Type = Counter32
_GtModuleLifetime_Object = MibTableColumn
gtModuleLifetime = _GtModuleLifetime_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 7),
    _GtModuleLifetime_Type()
)
gtModuleLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleLifetime.setStatus("current")
if mibBuilder.loadTexts:
    gtModuleLifetime.setUnits("s")


class _GtModulePower_Type(Integer32):
    """Custom type gtModulePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_GtModulePower_Type.__name__ = "Integer32"
_GtModulePower_Object = MibTableColumn
gtModulePower = _GtModulePower_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 8),
    _GtModulePower_Type()
)
gtModulePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtModulePower.setStatus("current")
_GtModuleMode_Type = DisplayString
_GtModuleMode_Object = MibTableColumn
gtModuleMode = _GtModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 9),
    _GtModuleMode_Type()
)
gtModuleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleMode.setStatus("current")
_GtModuleStatus_Type = DisplayString
_GtModuleStatus_Object = MibTableColumn
gtModuleStatus = _GtModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 10),
    _GtModuleStatus_Type()
)
gtModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleStatus.setStatus("current")


class _GtModuleSlot_Type(Unsigned32):
    """Custom type gtModuleSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_GtModuleSlot_Type.__name__ = "Unsigned32"
_GtModuleSlot_Object = MibTableColumn
gtModuleSlot = _GtModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 11),
    _GtModuleSlot_Type()
)
gtModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleSlot.setStatus("deprecated")
_GtModuleFWIDUploaded_Type = DisplayString
_GtModuleFWIDUploaded_Object = MibTableColumn
gtModuleFWIDUploaded = _GtModuleFWIDUploaded_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 12),
    _GtModuleFWIDUploaded_Type()
)
gtModuleFWIDUploaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtModuleFWIDUploaded.setStatus("current")


class _GtModuleReboot_Type(Integer32):
    """Custom type gtModuleReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("reboot", 1))
    )


_GtModuleReboot_Type.__name__ = "Integer32"
_GtModuleReboot_Object = MibTableColumn
gtModuleReboot = _GtModuleReboot_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 13),
    _GtModuleReboot_Type()
)
gtModuleReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtModuleReboot.setStatus("current")


class _GtNumCapabilities_Type(Unsigned32):
    """Custom type gtNumCapabilities based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GtNumCapabilities_Type.__name__ = "Unsigned32"
_GtNumCapabilities_Object = MibScalar
gtNumCapabilities = _GtNumCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 4),
    _GtNumCapabilities_Type()
)
gtNumCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtNumCapabilities.setStatus("current")
_GtCapabilitiesTable_Object = MibTable
gtCapabilitiesTable = _GtCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gtCapabilitiesTable.setStatus("current")
_GtCapabilitiesEntry_Object = MibTableRow
gtCapabilitiesEntry = _GtCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1)
)
gtCapabilitiesEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTMODULES-MIB", "gtChannel"),
    (0, "WISI-GTMODULES-MIB", "gtCapability"),
)
if mibBuilder.loadTexts:
    gtCapabilitiesEntry.setStatus("current")


class _GtChannel_Type(Unsigned32):
    """Custom type gtChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_GtChannel_Type.__name__ = "Unsigned32"
_GtChannel_Object = MibTableColumn
gtChannel = _GtChannel_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1, 1),
    _GtChannel_Type()
)
gtChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtChannel.setStatus("current")


class _GtCapability_Type(Unsigned32):
    """Custom type gtCapability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GtCapability_Type.__name__ = "Unsigned32"
_GtCapability_Object = MibTableColumn
gtCapability = _GtCapability_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1, 2),
    _GtCapability_Type()
)
gtCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtCapability.setStatus("current")
_GtInputsTable_Object = MibTable
gtInputsTable = _GtInputsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    gtInputsTable.setStatus("current")
_GtInputsEntry_Object = MibTableRow
gtInputsEntry = _GtInputsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1)
)
gtInputsEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTMODULES-MIB", "gtInputsTableIdx"),
)
if mibBuilder.loadTexts:
    gtInputsEntry.setStatus("current")


class _GtInputsTableIdx_Type(Unsigned32):
    """Custom type gtInputsTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_GtInputsTableIdx_Type.__name__ = "Unsigned32"
_GtInputsTableIdx_Object = MibTableColumn
gtInputsTableIdx = _GtInputsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 1),
    _GtInputsTableIdx_Type()
)
gtInputsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtInputsTableIdx.setStatus("current")
_GtInputChannel_Type = ObjectIdentifier
_GtInputChannel_Object = MibTableColumn
gtInputChannel = _GtInputChannel_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 2),
    _GtInputChannel_Type()
)
gtInputChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtInputChannel.setStatus("current")


class _GtInputName_Type(DisplayString):
    """Custom type gtInputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GtInputName_Type.__name__ = "DisplayString"
_GtInputName_Object = MibTableColumn
gtInputName = _GtInputName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 3),
    _GtInputName_Type()
)
gtInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtInputName.setStatus("current")
_GtOutputsTable_Object = MibTable
gtOutputsTable = _GtOutputsTable_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    gtOutputsTable.setStatus("current")
_GtOutputsEntry_Object = MibTableRow
gtOutputsEntry = _GtOutputsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1)
)
gtOutputsEntry.setIndexNames(
    (0, "WISI-GTMODULES-MIB", "gtModule"),
    (0, "WISI-GTMODULES-MIB", "gtOutputsTableIdx"),
)
if mibBuilder.loadTexts:
    gtOutputsEntry.setStatus("current")


class _GtOutputsTableIdx_Type(Unsigned32):
    """Custom type gtOutputsTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_GtOutputsTableIdx_Type.__name__ = "Unsigned32"
_GtOutputsTableIdx_Object = MibTableColumn
gtOutputsTableIdx = _GtOutputsTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 1),
    _GtOutputsTableIdx_Type()
)
gtOutputsTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtOutputsTableIdx.setStatus("current")
_GtOutputChannel_Type = ObjectIdentifier
_GtOutputChannel_Object = MibTableColumn
gtOutputChannel = _GtOutputChannel_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 2),
    _GtOutputChannel_Type()
)
gtOutputChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtOutputChannel.setStatus("current")


class _GtOutputName_Type(DisplayString):
    """Custom type gtOutputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GtOutputName_Type.__name__ = "DisplayString"
_GtOutputName_Object = MibTableColumn
gtOutputName = _GtOutputName_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 3),
    _GtOutputName_Type()
)
gtOutputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtOutputName.setStatus("current")
_GtModulesConformance_ObjectIdentity = ObjectIdentity
gtModulesConformance = _GtModulesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2)
)
_GtModulesCompliances_ObjectIdentity = ObjectIdentity
gtModulesCompliances = _GtModulesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 1)
)
_GtModulesGroups_ObjectIdentity = ObjectIdentity
gtModulesGroups = _GtModulesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2)
)
_GtModulesTrapGroup_ObjectIdentity = ObjectIdentity
gtModulesTrapGroup = _GtModulesTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 4)
)
_GtModulesSetGroup_ObjectIdentity = ObjectIdentity
gtModulesSetGroup = _GtModulesSetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 5)
)

# Managed Objects groups

gtModulesV1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 1)
)
gtModulesV1Group.setObjects(
      *(("WISI-GTMODULES-MIB", "gtThisModuleSlot"),
        ("WISI-GTMODULES-MIB", "gtNumModules"),
        ("WISI-GTMODULES-MIB", "gtModuleName"),
        ("WISI-GTMODULES-MIB", "gtModuleHWID"),
        ("WISI-GTMODULES-MIB", "gtModuleFWID"),
        ("WISI-GTMODULES-MIB", "gtModuleSerNo"))
)
if mibBuilder.loadTexts:
    gtModulesV1Group.setStatus("current")

gtModulesSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 2)
)
gtModulesSystemGroup.setObjects(
      *(("WISI-GTMODULES-MIB", "gtThisModuleSlot"),
        ("WISI-GTMODULES-MIB", "gtNumModules"),
        ("WISI-GTMODULES-MIB", "gtModuleName"),
        ("WISI-GTMODULES-MIB", "gtModuleHWID"),
        ("WISI-GTMODULES-MIB", "gtModuleFWID"),
        ("WISI-GTMODULES-MIB", "gtModuleSerNo"),
        ("WISI-GTMODULES-MIB", "gtCapability"))
)
if mibBuilder.loadTexts:
    gtModulesSystemGroup.setStatus("current")

gtModulesStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 3)
)
gtModulesStatsGroup.setObjects(
      *(("WISI-GTMODULES-MIB", "gtNumModules"),
        ("WISI-GTMODULES-MIB", "gtModuleUptime"),
        ("WISI-GTMODULES-MIB", "gtModuleLifetime"),
        ("WISI-GTMODULES-MIB", "gtNumCapabilities"))
)
if mibBuilder.loadTexts:
    gtModulesStatsGroup.setStatus("current")


# Notification objects

gtModulesNotifyPlugin = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    gtModulesNotifyPlugin.setStatus(
        "current"
    )

gtModulesNotifyPlugout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    gtModulesNotifyPlugout.setStatus(
        "current"
    )

gtModulesNotifyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    gtModulesNotifyFailure.setStatus(
        "current"
    )

gtModulesNotifyRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    gtModulesNotifyRedundancy.setStatus(
        "current"
    )

gtModulesNotifyRedundancyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    gtModulesNotifyRedundancyClear.setStatus(
        "current"
    )

gtModulesNotifyFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    gtModulesNotifyFailureClear.setStatus(
        "current"
    )


# Notifications groups

gtModulesBasicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 6)
)
gtModulesBasicNotificationsGroup.setObjects(
      *(("WISI-GTMODULES-MIB", "gtModulesNotifyPlugin"),
        ("WISI-GTMODULES-MIB", "gtModulesNotifyPlugout"))
)
if mibBuilder.loadTexts:
    gtModulesBasicNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gtModulesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 1, 1)
)
gtModulesMIBCompliance.setObjects(
      *(("WISI-GTMODULES-MIB", "gtModulesV1Group"),
        ("WISI-GTMODULES-MIB", "gtModulesSystemGroup"),
        ("WISI-GTMODULES-MIB", "gtModulesStatsGroup"),
        ("WISI-GTMODULES-MIB", "gtModulesTrapGroup"),
        ("WISI-GTMODULES-MIB", "gtModulesSetGroup"),
        ("WISI-GTMODULES-MIB", "gtModulesBasicNotificationsGroup"))
)
if mibBuilder.loadTexts:
    gtModulesMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WISI-GTMODULES-MIB",
    **{"gtModulesMIB": gtModulesMIB,
       "gtModulesNotifications": gtModulesNotifications,
       "gtModulesNotifyPlugin": gtModulesNotifyPlugin,
       "gtModulesNotifyPlugout": gtModulesNotifyPlugout,
       "gtModulesNotifyFailure": gtModulesNotifyFailure,
       "gtModulesNotifyRedundancy": gtModulesNotifyRedundancy,
       "gtModulesNotifyRedundancyClear": gtModulesNotifyRedundancyClear,
       "gtModulesNotifyFailureClear": gtModulesNotifyFailureClear,
       "gtModulesObjects": gtModulesObjects,
       "gtThisModuleSlot": gtThisModuleSlot,
       "gtNumModules": gtNumModules,
       "gtModulesTable": gtModulesTable,
       "gtModulesEntry": gtModulesEntry,
       "gtModule": gtModule,
       "gtModuleName": gtModuleName,
       "gtModuleHWID": gtModuleHWID,
       "gtModuleFWID": gtModuleFWID,
       "gtModuleSerNo": gtModuleSerNo,
       "gtModuleUptime": gtModuleUptime,
       "gtModuleLifetime": gtModuleLifetime,
       "gtModulePower": gtModulePower,
       "gtModuleMode": gtModuleMode,
       "gtModuleStatus": gtModuleStatus,
       "gtModuleSlot": gtModuleSlot,
       "gtModuleFWIDUploaded": gtModuleFWIDUploaded,
       "gtModuleReboot": gtModuleReboot,
       "gtNumCapabilities": gtNumCapabilities,
       "gtCapabilitiesTable": gtCapabilitiesTable,
       "gtCapabilitiesEntry": gtCapabilitiesEntry,
       "gtChannel": gtChannel,
       "gtCapability": gtCapability,
       "gtInputsTable": gtInputsTable,
       "gtInputsEntry": gtInputsEntry,
       "gtInputsTableIdx": gtInputsTableIdx,
       "gtInputChannel": gtInputChannel,
       "gtInputName": gtInputName,
       "gtOutputsTable": gtOutputsTable,
       "gtOutputsEntry": gtOutputsEntry,
       "gtOutputsTableIdx": gtOutputsTableIdx,
       "gtOutputChannel": gtOutputChannel,
       "gtOutputName": gtOutputName,
       "gtModulesConformance": gtModulesConformance,
       "gtModulesCompliances": gtModulesCompliances,
       "gtModulesMIBCompliance": gtModulesMIBCompliance,
       "gtModulesGroups": gtModulesGroups,
       "gtModulesV1Group": gtModulesV1Group,
       "gtModulesSystemGroup": gtModulesSystemGroup,
       "gtModulesStatsGroup": gtModulesStatsGroup,
       "gtModulesTrapGroup": gtModulesTrapGroup,
       "gtModulesSetGroup": gtModulesSetGroup,
       "gtModulesBasicNotificationsGroup": gtModulesBasicNotificationsGroup}
)
