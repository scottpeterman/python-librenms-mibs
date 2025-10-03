# SNMP MIB module (CPPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\CPPM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:43 2025
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

(clearpass,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "clearpass")

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
 snmpModules) = mibBuilder.importSymbols(
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
    "snmpModules")

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

cppmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cppmMIB.setRevisions(
        ("1906-11-27 20:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CppmServerInfoGroup_ObjectIdentity = ObjectIdentity
cppmServerInfoGroup = _CppmServerInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1)
)
_CppmSystemTable_Object = MibTable
cppmSystemTable = _CppmSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cppmSystemTable.setStatus("current")
_CppmSystemTableEntry_Object = MibTableRow
cppmSystemTableEntry = _CppmSystemTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1)
)
cppmSystemTableEntry.setIndexNames(
    (0, "CPPM-MIB", "cppmSystemIdx"),
)
if mibBuilder.loadTexts:
    cppmSystemTableEntry.setStatus("current")


class _CppmSystemModel_Type(DisplayString):
    """Custom type cppmSystemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CppmSystemModel_Type.__name__ = "DisplayString"
_CppmSystemModel_Object = MibTableColumn
cppmSystemModel = _CppmSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 1),
    _CppmSystemModel_Type()
)
cppmSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemModel.setStatus("current")


class _CppmSystemSerialNumber_Type(DisplayString):
    """Custom type cppmSystemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmSystemSerialNumber_Type.__name__ = "DisplayString"
_CppmSystemSerialNumber_Object = MibTableColumn
cppmSystemSerialNumber = _CppmSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 2),
    _CppmSystemSerialNumber_Type()
)
cppmSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemSerialNumber.setStatus("current")


class _CppmSystemVersion_Type(DisplayString):
    """Custom type cppmSystemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CppmSystemVersion_Type.__name__ = "DisplayString"
_CppmSystemVersion_Object = MibTableColumn
cppmSystemVersion = _CppmSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 3),
    _CppmSystemVersion_Type()
)
cppmSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemVersion.setStatus("current")


class _CppmSystemHostname_Type(DisplayString):
    """Custom type cppmSystemHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CppmSystemHostname_Type.__name__ = "DisplayString"
_CppmSystemHostname_Object = MibTableColumn
cppmSystemHostname = _CppmSystemHostname_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 4),
    _CppmSystemHostname_Type()
)
cppmSystemHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemHostname.setStatus("current")


class _CppmClusterNodeType_Type(DisplayString):
    """Custom type cppmClusterNodeType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CppmClusterNodeType_Type.__name__ = "DisplayString"
_CppmClusterNodeType_Object = MibTableColumn
cppmClusterNodeType = _CppmClusterNodeType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 5),
    _CppmClusterNodeType_Type()
)
cppmClusterNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmClusterNodeType.setStatus("current")


class _CppmZoneName_Type(DisplayString):
    """Custom type cppmZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CppmZoneName_Type.__name__ = "DisplayString"
_CppmZoneName_Object = MibTableColumn
cppmZoneName = _CppmZoneName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 6),
    _CppmZoneName_Type()
)
cppmZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmZoneName.setStatus("current")
_CppmNumClusterNodes_Type = Integer32
_CppmNumClusterNodes_Object = MibTableColumn
cppmNumClusterNodes = _CppmNumClusterNodes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 7),
    _CppmNumClusterNodes_Type()
)
cppmNumClusterNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNumClusterNodes.setStatus("current")
_CppmNwMgmtPortIPAddress_Type = IpAddress
_CppmNwMgmtPortIPAddress_Object = MibTableColumn
cppmNwMgmtPortIPAddress = _CppmNwMgmtPortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 8),
    _CppmNwMgmtPortIPAddress_Type()
)
cppmNwMgmtPortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNwMgmtPortIPAddress.setStatus("current")


class _CppmNwMgmtPortMACAddress_Type(DisplayString):
    """Custom type cppmNwMgmtPortMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CppmNwMgmtPortMACAddress_Type.__name__ = "DisplayString"
_CppmNwMgmtPortMACAddress_Object = MibTableColumn
cppmNwMgmtPortMACAddress = _CppmNwMgmtPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 9),
    _CppmNwMgmtPortMACAddress_Type()
)
cppmNwMgmtPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNwMgmtPortMACAddress.setStatus("current")
_CppmNwDataPortIPAddress_Type = IpAddress
_CppmNwDataPortIPAddress_Object = MibTableColumn
cppmNwDataPortIPAddress = _CppmNwDataPortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 10),
    _CppmNwDataPortIPAddress_Type()
)
cppmNwDataPortIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNwDataPortIPAddress.setStatus("current")


class _CppmNwDataPortMACAddress_Type(DisplayString):
    """Custom type cppmNwDataPortMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CppmNwDataPortMACAddress_Type.__name__ = "DisplayString"
_CppmNwDataPortMACAddress_Object = MibTableColumn
cppmNwDataPortMACAddress = _CppmNwDataPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 11),
    _CppmNwDataPortMACAddress_Type()
)
cppmNwDataPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNwDataPortMACAddress.setStatus("current")
_CppmSystemMemoryTotal_Type = Counter64
_CppmSystemMemoryTotal_Object = MibTableColumn
cppmSystemMemoryTotal = _CppmSystemMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 12),
    _CppmSystemMemoryTotal_Type()
)
cppmSystemMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemMemoryTotal.setStatus("current")
_CppmSystemMemoryFree_Type = Counter64
_CppmSystemMemoryFree_Object = MibTableColumn
cppmSystemMemoryFree = _CppmSystemMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 13),
    _CppmSystemMemoryFree_Type()
)
cppmSystemMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemMemoryFree.setStatus("current")
_CppmSystemDiskSpaceTotal_Type = Counter64
_CppmSystemDiskSpaceTotal_Object = MibTableColumn
cppmSystemDiskSpaceTotal = _CppmSystemDiskSpaceTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 14),
    _CppmSystemDiskSpaceTotal_Type()
)
cppmSystemDiskSpaceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemDiskSpaceTotal.setStatus("current")
_CppmSystemDiskSpaceFree_Type = Counter64
_CppmSystemDiskSpaceFree_Object = MibTableColumn
cppmSystemDiskSpaceFree = _CppmSystemDiskSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 15),
    _CppmSystemDiskSpaceFree_Type()
)
cppmSystemDiskSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemDiskSpaceFree.setStatus("current")
_CppmSystemNumCPUs_Type = Integer32
_CppmSystemNumCPUs_Object = MibTableColumn
cppmSystemNumCPUs = _CppmSystemNumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 16),
    _CppmSystemNumCPUs_Type()
)
cppmSystemNumCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemNumCPUs.setStatus("current")
_CppmSystemUptime_Type = TimeTicks
_CppmSystemUptime_Object = MibTableColumn
cppmSystemUptime = _CppmSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 17),
    _CppmSystemUptime_Type()
)
cppmSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmSystemUptime.setStatus("current")


class _CppmSystemIdx_Type(Integer32):
    """Custom type cppmSystemIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CppmSystemIdx_Type.__name__ = "Integer32"
_CppmSystemIdx_Object = MibTableColumn
cppmSystemIdx = _CppmSystemIdx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 18),
    _CppmSystemIdx_Type()
)
cppmSystemIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cppmSystemIdx.setStatus("current")


class _CppmHardwareFanStatus_Type(DisplayString):
    """Custom type cppmHardwareFanStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmHardwareFanStatus_Type.__name__ = "DisplayString"
_CppmHardwareFanStatus_Object = MibTableColumn
cppmHardwareFanStatus = _CppmHardwareFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 19),
    _CppmHardwareFanStatus_Type()
)
cppmHardwareFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmHardwareFanStatus.setStatus("current")


class _CppmHardwarePowerStatus_Type(DisplayString):
    """Custom type cppmHardwarePowerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmHardwarePowerStatus_Type.__name__ = "DisplayString"
_CppmHardwarePowerStatus_Object = MibTableColumn
cppmHardwarePowerStatus = _CppmHardwarePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 20),
    _CppmHardwarePowerStatus_Type()
)
cppmHardwarePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmHardwarePowerStatus.setStatus("current")


class _CppmHardwarePowerStatusDetails_Type(DisplayString):
    """Custom type cppmHardwarePowerStatusDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmHardwarePowerStatusDetails_Type.__name__ = "DisplayString"
_CppmHardwarePowerStatusDetails_Object = MibTableColumn
cppmHardwarePowerStatusDetails = _CppmHardwarePowerStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 21),
    _CppmHardwarePowerStatusDetails_Type()
)
cppmHardwarePowerStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmHardwarePowerStatusDetails.setStatus("current")


class _CppmHardwareDiskStatus_Type(DisplayString):
    """Custom type cppmHardwareDiskStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmHardwareDiskStatus_Type.__name__ = "DisplayString"
_CppmHardwareDiskStatus_Object = MibTableColumn
cppmHardwareDiskStatus = _CppmHardwareDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 1, 1, 1, 22),
    _CppmHardwareDiskStatus_Type()
)
cppmHardwareDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmHardwareDiskStatus.setStatus("current")
_CppmProcInfoGroup_ObjectIdentity = ObjectIdentity
cppmProcInfoGroup = _CppmProcInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2)
)
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerTableEntry_Object = MibTableRow
radiusServerTableEntry = _RadiusServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1, 1)
)
radiusServerTableEntry.setIndexNames(
    (0, "CPPM-MIB", "cppmSystemHostname"),
)
if mibBuilder.loadTexts:
    radiusServerTableEntry.setStatus("current")
_RadPolicyEvalTime_Type = Integer32
_RadPolicyEvalTime_Object = MibTableColumn
radPolicyEvalTime = _RadPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1, 1, 1),
    _RadPolicyEvalTime_Type()
)
radPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radPolicyEvalTime.setStatus("current")
_RadAuthRequestTime_Type = Integer32
_RadAuthRequestTime_Object = MibTableColumn
radAuthRequestTime = _RadAuthRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1, 1, 2),
    _RadAuthRequestTime_Type()
)
radAuthRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthRequestTime.setStatus("current")
_RadServerCounterSuccess_Type = Integer32
_RadServerCounterSuccess_Object = MibTableColumn
radServerCounterSuccess = _RadServerCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1, 1, 3),
    _RadServerCounterSuccess_Type()
)
radServerCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radServerCounterSuccess.setStatus("current")
_RadServerCounterFailure_Type = Integer32
_RadServerCounterFailure_Object = MibTableColumn
radServerCounterFailure = _RadServerCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1, 1, 4),
    _RadServerCounterFailure_Type()
)
radServerCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radServerCounterFailure.setStatus("current")
_RadServerCounterCount_Type = Integer32
_RadServerCounterCount_Object = MibTableColumn
radServerCounterCount = _RadServerCounterCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 1, 1, 5),
    _RadServerCounterCount_Type()
)
radServerCounterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radServerCounterCount.setStatus("current")
_RadiusServerAuthTable_Object = MibTable
radiusServerAuthTable = _RadiusServerAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    radiusServerAuthTable.setStatus("current")
_RadiusServerAuthTableEntry_Object = MibTableRow
radiusServerAuthTableEntry = _RadiusServerAuthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1)
)
radiusServerAuthTableEntry.setIndexNames(
    (0, "CPPM-MIB", "radAuthSourceIdx"),
)
if mibBuilder.loadTexts:
    radiusServerAuthTableEntry.setStatus("current")


class _RadAuthSourceIdx_Type(Integer32):
    """Custom type radAuthSourceIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadAuthSourceIdx_Type.__name__ = "Integer32"
_RadAuthSourceIdx_Object = MibTableColumn
radAuthSourceIdx = _RadAuthSourceIdx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1, 1),
    _RadAuthSourceIdx_Type()
)
radAuthSourceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthSourceIdx.setStatus("current")


class _RadAuthSourceName_Type(DisplayString):
    """Custom type radAuthSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RadAuthSourceName_Type.__name__ = "DisplayString"
_RadAuthSourceName_Object = MibTableColumn
radAuthSourceName = _RadAuthSourceName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1, 2),
    _RadAuthSourceName_Type()
)
radAuthSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthSourceName.setStatus("current")
_RadAuthCounterSuccess_Type = Integer32
_RadAuthCounterSuccess_Object = MibTableColumn
radAuthCounterSuccess = _RadAuthCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1, 3),
    _RadAuthCounterSuccess_Type()
)
radAuthCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthCounterSuccess.setStatus("current")
_RadAuthCounterFailure_Type = Integer32
_RadAuthCounterFailure_Object = MibTableColumn
radAuthCounterFailure = _RadAuthCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1, 4),
    _RadAuthCounterFailure_Type()
)
radAuthCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthCounterFailure.setStatus("current")
_RadAuthCounterCount_Type = Integer32
_RadAuthCounterCount_Object = MibTableColumn
radAuthCounterCount = _RadAuthCounterCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1, 5),
    _RadAuthCounterCount_Type()
)
radAuthCounterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthCounterCount.setStatus("current")
_RadAuthCounterTime_Type = Integer32
_RadAuthCounterTime_Object = MibTableColumn
radAuthCounterTime = _RadAuthCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 2, 1, 6),
    _RadAuthCounterTime_Type()
)
radAuthCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radAuthCounterTime.setStatus("current")
_PolicyServerTable_Object = MibTable
policyServerTable = _PolicyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    policyServerTable.setStatus("current")
_PolicyServerTableEntry_Object = MibTableRow
policyServerTableEntry = _PolicyServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1)
)
policyServerTableEntry.setIndexNames(
    (0, "CPPM-MIB", "cppmSystemHostname"),
)
if mibBuilder.loadTexts:
    policyServerTableEntry.setStatus("current")
_PsServicePolicyEvalCount_Type = Integer32
_PsServicePolicyEvalCount_Object = MibTableColumn
psServicePolicyEvalCount = _PsServicePolicyEvalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 1),
    _PsServicePolicyEvalCount_Type()
)
psServicePolicyEvalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psServicePolicyEvalCount.setStatus("current")
_PsRolemappingPolicyEvalCount_Type = Integer32
_PsRolemappingPolicyEvalCount_Object = MibTableColumn
psRolemappingPolicyEvalCount = _PsRolemappingPolicyEvalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 2),
    _PsRolemappingPolicyEvalCount_Type()
)
psRolemappingPolicyEvalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRolemappingPolicyEvalCount.setStatus("current")
_PsPosturePolicyEvalCount_Type = Integer32
_PsPosturePolicyEvalCount_Object = MibTableColumn
psPosturePolicyEvalCount = _PsPosturePolicyEvalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 3),
    _PsPosturePolicyEvalCount_Type()
)
psPosturePolicyEvalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPosturePolicyEvalCount.setStatus("current")
_PsAuditPolicyEvalCount_Type = Integer32
_PsAuditPolicyEvalCount_Object = MibTableColumn
psAuditPolicyEvalCount = _PsAuditPolicyEvalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 4),
    _PsAuditPolicyEvalCount_Type()
)
psAuditPolicyEvalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuditPolicyEvalCount.setStatus("current")
_PsRestrictionPolicyEvalCount_Type = Integer32
_PsRestrictionPolicyEvalCount_Object = MibTableColumn
psRestrictionPolicyEvalCount = _PsRestrictionPolicyEvalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 5),
    _PsRestrictionPolicyEvalCount_Type()
)
psRestrictionPolicyEvalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRestrictionPolicyEvalCount.setStatus("current")
_PsEnforcementPolicyEvalCount_Type = Integer32
_PsEnforcementPolicyEvalCount_Object = MibTableColumn
psEnforcementPolicyEvalCount = _PsEnforcementPolicyEvalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 6),
    _PsEnforcementPolicyEvalCount_Type()
)
psEnforcementPolicyEvalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnforcementPolicyEvalCount.setStatus("current")
_PsServicePolicyEvalTime_Type = Integer32
_PsServicePolicyEvalTime_Object = MibTableColumn
psServicePolicyEvalTime = _PsServicePolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 7),
    _PsServicePolicyEvalTime_Type()
)
psServicePolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psServicePolicyEvalTime.setStatus("current")
_PsRolemappingPolicyEvalTime_Type = Integer32
_PsRolemappingPolicyEvalTime_Object = MibTableColumn
psRolemappingPolicyEvalTime = _PsRolemappingPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 8),
    _PsRolemappingPolicyEvalTime_Type()
)
psRolemappingPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRolemappingPolicyEvalTime.setStatus("current")
_PsPosturePolicyEvalTime_Type = Integer32
_PsPosturePolicyEvalTime_Object = MibTableColumn
psPosturePolicyEvalTime = _PsPosturePolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 9),
    _PsPosturePolicyEvalTime_Type()
)
psPosturePolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPosturePolicyEvalTime.setStatus("current")
_PsAuditPolicyEvalTime_Type = Integer32
_PsAuditPolicyEvalTime_Object = MibTableColumn
psAuditPolicyEvalTime = _PsAuditPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 10),
    _PsAuditPolicyEvalTime_Type()
)
psAuditPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuditPolicyEvalTime.setStatus("current")
_PsRestrictionPolicyEvalTime_Type = Integer32
_PsRestrictionPolicyEvalTime_Object = MibTableColumn
psRestrictionPolicyEvalTime = _PsRestrictionPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 11),
    _PsRestrictionPolicyEvalTime_Type()
)
psRestrictionPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRestrictionPolicyEvalTime.setStatus("current")
_PsEnforcementPolicyEvalTime_Type = Integer32
_PsEnforcementPolicyEvalTime_Object = MibTableColumn
psEnforcementPolicyEvalTime = _PsEnforcementPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 12),
    _PsEnforcementPolicyEvalTime_Type()
)
psEnforcementPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEnforcementPolicyEvalTime.setStatus("current")
_PsSessionlogTime_Type = Integer32
_PsSessionlogTime_Object = MibTableColumn
psSessionlogTime = _PsSessionlogTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 13),
    _PsSessionlogTime_Type()
)
psSessionlogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSessionlogTime.setStatus("current")
_PsAuthCounterSuccess_Type = Integer32
_PsAuthCounterSuccess_Object = MibTableColumn
psAuthCounterSuccess = _PsAuthCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 14),
    _PsAuthCounterSuccess_Type()
)
psAuthCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuthCounterSuccess.setStatus("current")
_PsAuthCounterFailure_Type = Integer32
_PsAuthCounterFailure_Object = MibTableColumn
psAuthCounterFailure = _PsAuthCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 15),
    _PsAuthCounterFailure_Type()
)
psAuthCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuthCounterFailure.setStatus("current")
_PsAuthCounterTotal_Type = Integer32
_PsAuthCounterTotal_Object = MibTableColumn
psAuthCounterTotal = _PsAuthCounterTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 16),
    _PsAuthCounterTotal_Type()
)
psAuthCounterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuthCounterTotal.setStatus("current")
_DailySuccessAuthCount_Type = Integer32
_DailySuccessAuthCount_Object = MibTableColumn
dailySuccessAuthCount = _DailySuccessAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 17),
    _DailySuccessAuthCount_Type()
)
dailySuccessAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailySuccessAuthCount.setStatus("current")
_DailyFailedAuthCount_Type = Integer32
_DailyFailedAuthCount_Object = MibTableColumn
dailyFailedAuthCount = _DailyFailedAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 18),
    _DailyFailedAuthCount_Type()
)
dailyFailedAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyFailedAuthCount.setStatus("current")
_DailyTotalAuthCount_Type = Integer32
_DailyTotalAuthCount_Object = MibTableColumn
dailyTotalAuthCount = _DailyTotalAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 3, 1, 19),
    _DailyTotalAuthCount_Type()
)
dailyTotalAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dailyTotalAuthCount.setStatus("current")
_PolicyServerProtoTable_Object = MibTable
policyServerProtoTable = _PolicyServerProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    policyServerProtoTable.setStatus("current")
_PolicyServerProtoTableEntry_Object = MibTableRow
policyServerProtoTableEntry = _PolicyServerProtoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 4, 1)
)
policyServerProtoTableEntry.setIndexNames(
    (0, "CPPM-MIB", "psProtocolIdx"),
)
if mibBuilder.loadTexts:
    policyServerProtoTableEntry.setStatus("current")


class _PsProtocolIdx_Type(Integer32):
    """Custom type psProtocolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PsProtocolIdx_Type.__name__ = "Integer32"
_PsProtocolIdx_Object = MibTableColumn
psProtocolIdx = _PsProtocolIdx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 4, 1, 1),
    _PsProtocolIdx_Type()
)
psProtocolIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProtocolIdx.setStatus("current")


class _PsProtocolName_Type(DisplayString):
    """Custom type psProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PsProtocolName_Type.__name__ = "DisplayString"
_PsProtocolName_Object = MibTableColumn
psProtocolName = _PsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 4, 1, 2),
    _PsProtocolName_Type()
)
psProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProtocolName.setStatus("current")
_PsPolicyEvalTime_Type = Integer32
_PsPolicyEvalTime_Object = MibTableColumn
psPolicyEvalTime = _PsPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 4, 1, 3),
    _PsPolicyEvalTime_Type()
)
psPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPolicyEvalTime.setStatus("current")
_PolicyServerAutzTable_Object = MibTable
policyServerAutzTable = _PolicyServerAutzTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    policyServerAutzTable.setStatus("current")
_PolicyServerAutzTableEntry_Object = MibTableRow
policyServerAutzTableEntry = _PolicyServerAutzTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1)
)
policyServerAutzTableEntry.setIndexNames(
    (0, "CPPM-MIB", "psAutzSourceIdx"),
)
if mibBuilder.loadTexts:
    policyServerAutzTableEntry.setStatus("current")


class _PsAutzSourceIdx_Type(Integer32):
    """Custom type psAutzSourceIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PsAutzSourceIdx_Type.__name__ = "Integer32"
_PsAutzSourceIdx_Object = MibTableColumn
psAutzSourceIdx = _PsAutzSourceIdx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1, 1),
    _PsAutzSourceIdx_Type()
)
psAutzSourceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAutzSourceIdx.setStatus("current")


class _PsAutzSourceName_Type(DisplayString):
    """Custom type psAutzSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsAutzSourceName_Type.__name__ = "DisplayString"
_PsAutzSourceName_Object = MibTableColumn
psAutzSourceName = _PsAutzSourceName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1, 2),
    _PsAutzSourceName_Type()
)
psAutzSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAutzSourceName.setStatus("current")
_PsAutzCounterSuccess_Type = Integer32
_PsAutzCounterSuccess_Object = MibTableColumn
psAutzCounterSuccess = _PsAutzCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1, 3),
    _PsAutzCounterSuccess_Type()
)
psAutzCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAutzCounterSuccess.setStatus("current")
_PsAutzCounterFailure_Type = Integer32
_PsAutzCounterFailure_Object = MibTableColumn
psAutzCounterFailure = _PsAutzCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1, 4),
    _PsAutzCounterFailure_Type()
)
psAutzCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAutzCounterFailure.setStatus("current")
_PsAutzCounterCount_Type = Integer32
_PsAutzCounterCount_Object = MibTableColumn
psAutzCounterCount = _PsAutzCounterCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1, 5),
    _PsAutzCounterCount_Type()
)
psAutzCounterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAutzCounterCount.setStatus("current")
_PsAutzCounterTime_Type = Integer32
_PsAutzCounterTime_Object = MibTableColumn
psAutzCounterTime = _PsAutzCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 5, 1, 6),
    _PsAutzCounterTime_Type()
)
psAutzCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAutzCounterTime.setStatus("current")
_WebAuthProtoTable_Object = MibTable
webAuthProtoTable = _WebAuthProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    webAuthProtoTable.setStatus("current")
_WebAuthProtoTableEntry_Object = MibTableRow
webAuthProtoTableEntry = _WebAuthProtoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1)
)
webAuthProtoTableEntry.setIndexNames(
    (0, "CPPM-MIB", "waProtocolIdx"),
)
if mibBuilder.loadTexts:
    webAuthProtoTableEntry.setStatus("current")


class _WaProtocolIdx_Type(Integer32):
    """Custom type waProtocolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WaProtocolIdx_Type.__name__ = "Integer32"
_WaProtocolIdx_Object = MibTableColumn
waProtocolIdx = _WaProtocolIdx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 1),
    _WaProtocolIdx_Type()
)
waProtocolIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waProtocolIdx.setStatus("current")


class _WaProtocolName_Type(DisplayString):
    """Custom type waProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WaProtocolName_Type.__name__ = "DisplayString"
_WaProtocolName_Object = MibTableColumn
waProtocolName = _WaProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 2),
    _WaProtocolName_Type()
)
waProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waProtocolName.setStatus("current")
_WaAuthCounterSuccess_Type = Integer32
_WaAuthCounterSuccess_Object = MibTableColumn
waAuthCounterSuccess = _WaAuthCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 3),
    _WaAuthCounterSuccess_Type()
)
waAuthCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waAuthCounterSuccess.setStatus("current")
_WaAuthCounterFailure_Type = Integer32
_WaAuthCounterFailure_Object = MibTableColumn
waAuthCounterFailure = _WaAuthCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 4),
    _WaAuthCounterFailure_Type()
)
waAuthCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waAuthCounterFailure.setStatus("current")
_WaAuthCounterCount_Type = Integer32
_WaAuthCounterCount_Object = MibTableColumn
waAuthCounterCount = _WaAuthCounterCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 5),
    _WaAuthCounterCount_Type()
)
waAuthCounterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waAuthCounterCount.setStatus("current")
_WaAuthCounterTime_Type = Integer32
_WaAuthCounterTime_Object = MibTableColumn
waAuthCounterTime = _WaAuthCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 6),
    _WaAuthCounterTime_Type()
)
waAuthCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waAuthCounterTime.setStatus("current")
_WaAuthCounterAuthTime_Type = Integer32
_WaAuthCounterAuthTime_Object = MibTableColumn
waAuthCounterAuthTime = _WaAuthCounterAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 7),
    _WaAuthCounterAuthTime_Type()
)
waAuthCounterAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waAuthCounterAuthTime.setStatus("current")
_WaServicePolicyEvalTime_Type = Integer32
_WaServicePolicyEvalTime_Object = MibTableColumn
waServicePolicyEvalTime = _WaServicePolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 8),
    _WaServicePolicyEvalTime_Type()
)
waServicePolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waServicePolicyEvalTime.setStatus("current")
_WaPolicyEvalTime_Type = Integer32
_WaPolicyEvalTime_Object = MibTableColumn
waPolicyEvalTime = _WaPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 6, 1, 9),
    _WaPolicyEvalTime_Type()
)
waPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waPolicyEvalTime.setStatus("current")
_TacacsAuthTable_Object = MibTable
tacacsAuthTable = _TacacsAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tacacsAuthTable.setStatus("current")
_TacacsAuthTableEntry_Object = MibTableRow
tacacsAuthTableEntry = _TacacsAuthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1)
)
tacacsAuthTableEntry.setIndexNames(
    (0, "CPPM-MIB", "cppmSystemHostname"),
)
if mibBuilder.loadTexts:
    tacacsAuthTableEntry.setStatus("current")
_TacAuthCounterSuccess_Type = Integer32
_TacAuthCounterSuccess_Object = MibTableColumn
tacAuthCounterSuccess = _TacAuthCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 1),
    _TacAuthCounterSuccess_Type()
)
tacAuthCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAuthCounterSuccess.setStatus("current")
_TacAuthCounterFailure_Type = Integer32
_TacAuthCounterFailure_Object = MibTableColumn
tacAuthCounterFailure = _TacAuthCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 2),
    _TacAuthCounterFailure_Type()
)
tacAuthCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAuthCounterFailure.setStatus("current")
_TacAuthCounterCount_Type = Integer32
_TacAuthCounterCount_Object = MibTableColumn
tacAuthCounterCount = _TacAuthCounterCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 3),
    _TacAuthCounterCount_Type()
)
tacAuthCounterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAuthCounterCount.setStatus("current")
_TacAuthCounterTime_Type = Integer32
_TacAuthCounterTime_Object = MibTableColumn
tacAuthCounterTime = _TacAuthCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 4),
    _TacAuthCounterTime_Type()
)
tacAuthCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAuthCounterTime.setStatus("current")
_TacAuthCounterAuthTime_Type = Integer32
_TacAuthCounterAuthTime_Object = MibTableColumn
tacAuthCounterAuthTime = _TacAuthCounterAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 5),
    _TacAuthCounterAuthTime_Type()
)
tacAuthCounterAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAuthCounterAuthTime.setStatus("current")
_TacServicePolicyEvalTime_Type = Integer32
_TacServicePolicyEvalTime_Object = MibTableColumn
tacServicePolicyEvalTime = _TacServicePolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 6),
    _TacServicePolicyEvalTime_Type()
)
tacServicePolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacServicePolicyEvalTime.setStatus("current")
_TacPolicyEvalTime_Type = Integer32
_TacPolicyEvalTime_Object = MibTableColumn
tacPolicyEvalTime = _TacPolicyEvalTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 7, 1, 7),
    _TacPolicyEvalTime_Type()
)
tacPolicyEvalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacPolicyEvalTime.setStatus("current")
_TacacsAutzTable_Object = MibTable
tacacsAutzTable = _TacacsAutzTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tacacsAutzTable.setStatus("current")
_TacacsAutzTableEntry_Object = MibTableRow
tacacsAutzTableEntry = _TacacsAutzTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 8, 1)
)
tacacsAutzTableEntry.setIndexNames(
    (0, "CPPM-MIB", "cppmSystemHostname"),
)
if mibBuilder.loadTexts:
    tacacsAutzTableEntry.setStatus("current")
_TacAutzCounterSuccess_Type = Integer32
_TacAutzCounterSuccess_Object = MibTableColumn
tacAutzCounterSuccess = _TacAutzCounterSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 8, 1, 1),
    _TacAutzCounterSuccess_Type()
)
tacAutzCounterSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAutzCounterSuccess.setStatus("current")
_TacAutzCounterFailure_Type = Integer32
_TacAutzCounterFailure_Object = MibTableColumn
tacAutzCounterFailure = _TacAutzCounterFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 8, 1, 2),
    _TacAutzCounterFailure_Type()
)
tacAutzCounterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAutzCounterFailure.setStatus("current")
_TacAutzCounterCount_Type = Integer32
_TacAutzCounterCount_Object = MibTableColumn
tacAutzCounterCount = _TacAutzCounterCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 8, 1, 3),
    _TacAutzCounterCount_Type()
)
tacAutzCounterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAutzCounterCount.setStatus("current")
_TacAutzCounterTime_Type = Integer32
_TacAutzCounterTime_Object = MibTableColumn
tacAutzCounterTime = _TacAutzCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 2, 8, 1, 4),
    _TacAutzCounterTime_Type()
)
tacAutzCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacAutzCounterTime.setStatus("current")
_CppmNetworkInfoGroup_ObjectIdentity = ObjectIdentity
cppmNetworkInfoGroup = _CppmNetworkInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3)
)
_NetworkTrafficTable_Object = MibTable
networkTrafficTable = _NetworkTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    networkTrafficTable.setStatus("current")
_NetworkTrafficTableEntry_Object = MibTableRow
networkTrafficTableEntry = _NetworkTrafficTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3, 1, 1)
)
networkTrafficTableEntry.setIndexNames(
    (0, "CPPM-MIB", "nwAppIdx"),
)
if mibBuilder.loadTexts:
    networkTrafficTableEntry.setStatus("current")


class _NwAppIdx_Type(Integer32):
    """Custom type nwAppIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppIdx_Type.__name__ = "Integer32"
_NwAppIdx_Object = MibTableColumn
nwAppIdx = _NwAppIdx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3, 1, 1, 1),
    _NwAppIdx_Type()
)
nwAppIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppIdx.setStatus("current")


class _NwAppName_Type(DisplayString):
    """Custom type nwAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NwAppName_Type.__name__ = "DisplayString"
_NwAppName_Object = MibTableColumn
nwAppName = _NwAppName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3, 1, 1, 2),
    _NwAppName_Type()
)
nwAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppName.setStatus("current")


class _NwAppPort_Type(Integer32):
    """Custom type nwAppPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwAppPort_Type.__name__ = "Integer32"
_NwAppPort_Object = MibTableColumn
nwAppPort = _NwAppPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3, 1, 1, 3),
    _NwAppPort_Type()
)
nwAppPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAppPort.setStatus("current")
_NwTrafficTotal_Type = Counter64
_NwTrafficTotal_Object = MibTableColumn
nwTrafficTotal = _NwTrafficTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 3, 1, 1, 4),
    _NwTrafficTotal_Type()
)
nwTrafficTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwTrafficTotal.setStatus("current")
_CppmTraps_ObjectIdentity = ObjectIdentity
cppmTraps = _CppmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200)
)
_ClearpassTrapObjectsGroup_ObjectIdentity = ObjectIdentity
clearpassTrapObjectsGroup = _ClearpassTrapObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100)
)


class _CppmNodeName_Type(DisplayString):
    """Custom type cppmNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CppmNodeName_Type.__name__ = "DisplayString"
_CppmNodeName_Object = MibScalar
cppmNodeName = _CppmNodeName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 1),
    _CppmNodeName_Type()
)
cppmNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNodeName.setStatus("current")
_CppmNodeIp_Type = IpAddress
_CppmNodeIp_Object = MibScalar
cppmNodeIp = _CppmNodeIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 2),
    _CppmNodeIp_Type()
)
cppmNodeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNodeIp.setStatus("current")
_CppmClusterServerIp_Type = IpAddress
_CppmClusterServerIp_Object = MibScalar
cppmClusterServerIp = _CppmClusterServerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 3),
    _CppmClusterServerIp_Type()
)
cppmClusterServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmClusterServerIp.setStatus("current")


class _CppmNodeApplicationName_Type(DisplayString):
    """Custom type cppmNodeApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmNodeApplicationName_Type.__name__ = "DisplayString"
_CppmNodeApplicationName_Object = MibScalar
cppmNodeApplicationName = _CppmNodeApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 4),
    _CppmNodeApplicationName_Type()
)
cppmNodeApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNodeApplicationName.setStatus("current")


class _CppmNodeCertApplicationName_Type(DisplayString):
    """Custom type cppmNodeCertApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmNodeCertApplicationName_Type.__name__ = "DisplayString"
_CppmNodeCertApplicationName_Object = MibScalar
cppmNodeCertApplicationName = _CppmNodeCertApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 5),
    _CppmNodeCertApplicationName_Type()
)
cppmNodeCertApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmNodeCertApplicationName.setStatus("current")
_CppmLicenseDaysRemaining_Type = Integer32
_CppmLicenseDaysRemaining_Object = MibScalar
cppmLicenseDaysRemaining = _CppmLicenseDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 6),
    _CppmLicenseDaysRemaining_Type()
)
cppmLicenseDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmLicenseDaysRemaining.setStatus("current")
_CppmActivationDaysRemaining_Type = Integer32
_CppmActivationDaysRemaining_Object = MibScalar
cppmActivationDaysRemaining = _CppmActivationDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 7),
    _CppmActivationDaysRemaining_Type()
)
cppmActivationDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmActivationDaysRemaining.setStatus("current")
_CppmCertDaysRemaining_Type = Integer32
_CppmCertDaysRemaining_Object = MibScalar
cppmCertDaysRemaining = _CppmCertDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 8),
    _CppmCertDaysRemaining_Type()
)
cppmCertDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmCertDaysRemaining.setStatus("current")
_CppmDiskSpaceRemaining_Type = Integer32
_CppmDiskSpaceRemaining_Object = MibScalar
cppmDiskSpaceRemaining = _CppmDiskSpaceRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 9),
    _CppmDiskSpaceRemaining_Type()
)
cppmDiskSpaceRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmDiskSpaceRemaining.setStatus("current")
_CppmMemoryRemaining_Type = Integer32
_CppmMemoryRemaining_Object = MibScalar
cppmMemoryRemaining = _CppmMemoryRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 10),
    _CppmMemoryRemaining_Type()
)
cppmMemoryRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmMemoryRemaining.setStatus("current")
_CppmClusterOutOfSyncMinutes_Type = Integer32
_CppmClusterOutOfSyncMinutes_Object = MibScalar
cppmClusterOutOfSyncMinutes = _CppmClusterOutOfSyncMinutes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 11),
    _CppmClusterOutOfSyncMinutes_Type()
)
cppmClusterOutOfSyncMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmClusterOutOfSyncMinutes.setStatus("current")
_CppmClusterLicenseTotalCount_Type = Integer32
_CppmClusterLicenseTotalCount_Object = MibScalar
cppmClusterLicenseTotalCount = _CppmClusterLicenseTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 12),
    _CppmClusterLicenseTotalCount_Type()
)
cppmClusterLicenseTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmClusterLicenseTotalCount.setStatus("current")
_CppmClusterLicenseUsageCount_Type = Integer32
_CppmClusterLicenseUsageCount_Object = MibScalar
cppmClusterLicenseUsageCount = _CppmClusterLicenseUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 13),
    _CppmClusterLicenseUsageCount_Type()
)
cppmClusterLicenseUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmClusterLicenseUsageCount.setStatus("current")


class _CppmResourceUnit_Type(DisplayString):
    """Custom type cppmResourceUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CppmResourceUnit_Type.__name__ = "DisplayString"
_CppmResourceUnit_Object = MibScalar
cppmResourceUnit = _CppmResourceUnit_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 14),
    _CppmResourceUnit_Type()
)
cppmResourceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmResourceUnit.setStatus("current")


class _CppmImageFile_Type(DisplayString):
    """Custom type cppmImageFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmImageFile_Type.__name__ = "DisplayString"
_CppmImageFile_Object = MibScalar
cppmImageFile = _CppmImageFile_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 15),
    _CppmImageFile_Type()
)
cppmImageFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmImageFile.setStatus("current")
_CppmImageInstallStatus_Type = Integer32
_CppmImageInstallStatus_Object = MibScalar
cppmImageInstallStatus = _CppmImageInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 16),
    _CppmImageInstallStatus_Type()
)
cppmImageInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmImageInstallStatus.setStatus("current")


class _CppmServiceName_Type(DisplayString):
    """Custom type cppmServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmServiceName_Type.__name__ = "DisplayString"
_CppmServiceName_Object = MibScalar
cppmServiceName = _CppmServiceName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 17),
    _CppmServiceName_Type()
)
cppmServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmServiceName.setStatus("current")
_CppmServiceStatus_Type = Integer32
_CppmServiceStatus_Object = MibScalar
cppmServiceStatus = _CppmServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 18),
    _CppmServiceStatus_Type()
)
cppmServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmServiceStatus.setStatus("current")


class _CppmLicenseApplicationName_Type(DisplayString):
    """Custom type cppmLicenseApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CppmLicenseApplicationName_Type.__name__ = "DisplayString"
_CppmLicenseApplicationName_Object = MibScalar
cppmLicenseApplicationName = _CppmLicenseApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 19),
    _CppmLicenseApplicationName_Type()
)
cppmLicenseApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmLicenseApplicationName.setStatus("current")
_CppmLicenseOverrunDailyCount_Type = Integer32
_CppmLicenseOverrunDailyCount_Object = MibScalar
cppmLicenseOverrunDailyCount = _CppmLicenseOverrunDailyCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 20),
    _CppmLicenseOverrunDailyCount_Type()
)
cppmLicenseOverrunDailyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmLicenseOverrunDailyCount.setStatus("current")


class _CppmTrapMessage_Type(DisplayString):
    """Custom type cppmTrapMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_CppmTrapMessage_Type.__name__ = "DisplayString"
_CppmTrapMessage_Object = MibScalar
cppmTrapMessage = _CppmTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 35),
    _CppmTrapMessage_Type()
)
cppmTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmTrapMessage.setStatus("current")


class _CppmCPUAverageLoad_Type(DisplayString):
    """Custom type cppmCPUAverageLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CppmCPUAverageLoad_Type.__name__ = "DisplayString"
_CppmCPUAverageLoad_Object = MibScalar
cppmCPUAverageLoad = _CppmCPUAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 100, 37),
    _CppmCPUAverageLoad_Type()
)
cppmCPUAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppmCPUAverageLoad.setStatus("current")

# Managed Objects groups


# Notification objects

cppmLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1001)
)
cppmLicenseExpiry.setObjects(
      *(("CPPM-MIB", "cppmLicenseDaysRemaining"),
        ("CPPM-MIB", "cppmNodeApplicationName"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmLicenseExpiry.setStatus(
        "current"
    )

cppmActivationExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1002)
)
cppmActivationExpiry.setObjects(
      *(("CPPM-MIB", "cppmActivationDaysRemaining"),
        ("CPPM-MIB", "cppmNodeApplicationName"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmActivationExpiry.setStatus(
        "current"
    )

cppmNodeCertExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1003)
)
cppmNodeCertExpiry.setObjects(
      *(("CPPM-MIB", "cppmNodeCertApplicationName"),
        ("CPPM-MIB", "cppmCertDaysRemaining"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmNodeCertExpiry.setStatus(
        "current"
    )

cppmLowDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1004)
)
cppmLowDiskSpace.setObjects(
      *(("CPPM-MIB", "cppmDiskSpaceRemaining"),
        ("CPPM-MIB", "cppmResourceUnit"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmLowDiskSpace.setStatus(
        "current"
    )

cppmLowMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1005)
)
cppmLowMemory.setObjects(
      *(("CPPM-MIB", "cppmMemoryRemaining"),
        ("CPPM-MIB", "cppmResourceUnit"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmLowMemory.setStatus(
        "current"
    )

cppmClusterNodeAddNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1006)
)
cppmClusterNodeAddNotification.setObjects(
      *(("CPPM-MIB", "cppmClusterServerIp"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterNodeAddNotification.setStatus(
        "current"
    )

cppmClusterNodeDelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1007)
)
cppmClusterNodeDelNotification.setObjects(
      *(("CPPM-MIB", "cppmClusterServerIp"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterNodeDelNotification.setStatus(
        "current"
    )

cppmClusterNodePromNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1008)
)
cppmClusterNodePromNotification.setObjects(
      *(("CPPM-MIB", "cppmClusterServerIp"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterNodePromNotification.setStatus(
        "current"
    )

cppmClusterNodeDbldNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1009)
)
cppmClusterNodeDbldNotification.setObjects(
      *(("CPPM-MIB", "cppmClusterServerIp"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterNodeDbldNotification.setStatus(
        "current"
    )

cppmClusterNodeNSyncNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1010)
)
cppmClusterNodeNSyncNotification.setObjects(
      *(("CPPM-MIB", "cppmClusterServerIp"),
        ("CPPM-MIB", "cppmClusterOutOfSyncMinutes"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterNodeNSyncNotification.setStatus(
        "current"
    )

cppmClusterPwdChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1011)
)
cppmClusterPwdChangeNotification.setObjects(
    ("CPPM-MIB", "cppmTrapMessage")
)
if mibBuilder.loadTexts:
    cppmClusterPwdChangeNotification.setStatus(
        "current"
    )

cppmConfigReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1012)
)
cppmConfigReset.setObjects(
    ("CPPM-MIB", "cppmTrapMessage")
)
if mibBuilder.loadTexts:
    cppmConfigReset.setStatus(
        "current"
    )

cppmConfigRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1013)
)
cppmConfigRestore.setObjects(
    ("CPPM-MIB", "cppmTrapMessage")
)
if mibBuilder.loadTexts:
    cppmConfigRestore.setStatus(
        "current"
    )

cppmUpdateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1014)
)
cppmUpdateNotification.setObjects(
      *(("CPPM-MIB", "cppmImageFile"),
        ("CPPM-MIB", "cppmImageInstallStatus"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmUpdateNotification.setStatus(
        "current"
    )

cppmUpgradeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1015)
)
cppmUpgradeNotification.setObjects(
      *(("CPPM-MIB", "cppmImageFile"),
        ("CPPM-MIB", "cppmImageInstallStatus"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmUpgradeNotification.setStatus(
        "current"
    )

cppmClusterLicenseUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1016)
)
cppmClusterLicenseUsage.setObjects(
      *(("CPPM-MIB", "cppmNodeApplicationName"),
        ("CPPM-MIB", "cppmClusterLicenseTotalCount"),
        ("CPPM-MIB", "cppmClusterLicenseUsageCount"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterLicenseUsage.setStatus(
        "current"
    )

cppmServiceStopNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1017)
)
cppmServiceStopNotification.setObjects(
      *(("CPPM-MIB", "cppmServiceName"),
        ("CPPM-MIB", "cppmServiceStatus"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmServiceStopNotification.setStatus(
        "current"
    )

cppmServiceStartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1018)
)
cppmServiceStartNotification.setObjects(
      *(("CPPM-MIB", "cppmServiceName"),
        ("CPPM-MIB", "cppmServiceStatus"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmServiceStartNotification.setStatus(
        "current"
    )

cppmServiceRestartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1019)
)
cppmServiceRestartNotification.setObjects(
      *(("CPPM-MIB", "cppmServiceName"),
        ("CPPM-MIB", "cppmServiceStatus"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmServiceRestartNotification.setStatus(
        "current"
    )

cppmHighCPULoadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1021)
)
cppmHighCPULoadNotification.setObjects(
      *(("CPPM-MIB", "cppmCPUAverageLoad"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmHighCPULoadNotification.setStatus(
        "current"
    )

cppmCoreDumpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1022)
)
cppmCoreDumpNotification.setObjects(
    ("CPPM-MIB", "cppmTrapMessage")
)
if mibBuilder.loadTexts:
    cppmCoreDumpNotification.setStatus(
        "current"
    )

cppmClusterLicenseOverrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 1, 6, 1, 1, 200, 1023)
)
cppmClusterLicenseOverrun.setObjects(
      *(("CPPM-MIB", "cppmLicenseApplicationName"),
        ("CPPM-MIB", "cppmLicenseOverrunDailyCount"),
        ("CPPM-MIB", "cppmTrapMessage"))
)
if mibBuilder.loadTexts:
    cppmClusterLicenseOverrun.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPPM-MIB",
    **{"cppmMIB": cppmMIB,
       "cppmServerInfoGroup": cppmServerInfoGroup,
       "cppmSystemTable": cppmSystemTable,
       "cppmSystemTableEntry": cppmSystemTableEntry,
       "cppmSystemModel": cppmSystemModel,
       "cppmSystemSerialNumber": cppmSystemSerialNumber,
       "cppmSystemVersion": cppmSystemVersion,
       "cppmSystemHostname": cppmSystemHostname,
       "cppmClusterNodeType": cppmClusterNodeType,
       "cppmZoneName": cppmZoneName,
       "cppmNumClusterNodes": cppmNumClusterNodes,
       "cppmNwMgmtPortIPAddress": cppmNwMgmtPortIPAddress,
       "cppmNwMgmtPortMACAddress": cppmNwMgmtPortMACAddress,
       "cppmNwDataPortIPAddress": cppmNwDataPortIPAddress,
       "cppmNwDataPortMACAddress": cppmNwDataPortMACAddress,
       "cppmSystemMemoryTotal": cppmSystemMemoryTotal,
       "cppmSystemMemoryFree": cppmSystemMemoryFree,
       "cppmSystemDiskSpaceTotal": cppmSystemDiskSpaceTotal,
       "cppmSystemDiskSpaceFree": cppmSystemDiskSpaceFree,
       "cppmSystemNumCPUs": cppmSystemNumCPUs,
       "cppmSystemUptime": cppmSystemUptime,
       "cppmSystemIdx": cppmSystemIdx,
       "cppmHardwareFanStatus": cppmHardwareFanStatus,
       "cppmHardwarePowerStatus": cppmHardwarePowerStatus,
       "cppmHardwarePowerStatusDetails": cppmHardwarePowerStatusDetails,
       "cppmHardwareDiskStatus": cppmHardwareDiskStatus,
       "cppmProcInfoGroup": cppmProcInfoGroup,
       "radiusServerTable": radiusServerTable,
       "radiusServerTableEntry": radiusServerTableEntry,
       "radPolicyEvalTime": radPolicyEvalTime,
       "radAuthRequestTime": radAuthRequestTime,
       "radServerCounterSuccess": radServerCounterSuccess,
       "radServerCounterFailure": radServerCounterFailure,
       "radServerCounterCount": radServerCounterCount,
       "radiusServerAuthTable": radiusServerAuthTable,
       "radiusServerAuthTableEntry": radiusServerAuthTableEntry,
       "radAuthSourceIdx": radAuthSourceIdx,
       "radAuthSourceName": radAuthSourceName,
       "radAuthCounterSuccess": radAuthCounterSuccess,
       "radAuthCounterFailure": radAuthCounterFailure,
       "radAuthCounterCount": radAuthCounterCount,
       "radAuthCounterTime": radAuthCounterTime,
       "policyServerTable": policyServerTable,
       "policyServerTableEntry": policyServerTableEntry,
       "psServicePolicyEvalCount": psServicePolicyEvalCount,
       "psRolemappingPolicyEvalCount": psRolemappingPolicyEvalCount,
       "psPosturePolicyEvalCount": psPosturePolicyEvalCount,
       "psAuditPolicyEvalCount": psAuditPolicyEvalCount,
       "psRestrictionPolicyEvalCount": psRestrictionPolicyEvalCount,
       "psEnforcementPolicyEvalCount": psEnforcementPolicyEvalCount,
       "psServicePolicyEvalTime": psServicePolicyEvalTime,
       "psRolemappingPolicyEvalTime": psRolemappingPolicyEvalTime,
       "psPosturePolicyEvalTime": psPosturePolicyEvalTime,
       "psAuditPolicyEvalTime": psAuditPolicyEvalTime,
       "psRestrictionPolicyEvalTime": psRestrictionPolicyEvalTime,
       "psEnforcementPolicyEvalTime": psEnforcementPolicyEvalTime,
       "psSessionlogTime": psSessionlogTime,
       "psAuthCounterSuccess": psAuthCounterSuccess,
       "psAuthCounterFailure": psAuthCounterFailure,
       "psAuthCounterTotal": psAuthCounterTotal,
       "dailySuccessAuthCount": dailySuccessAuthCount,
       "dailyFailedAuthCount": dailyFailedAuthCount,
       "dailyTotalAuthCount": dailyTotalAuthCount,
       "policyServerProtoTable": policyServerProtoTable,
       "policyServerProtoTableEntry": policyServerProtoTableEntry,
       "psProtocolIdx": psProtocolIdx,
       "psProtocolName": psProtocolName,
       "psPolicyEvalTime": psPolicyEvalTime,
       "policyServerAutzTable": policyServerAutzTable,
       "policyServerAutzTableEntry": policyServerAutzTableEntry,
       "psAutzSourceIdx": psAutzSourceIdx,
       "psAutzSourceName": psAutzSourceName,
       "psAutzCounterSuccess": psAutzCounterSuccess,
       "psAutzCounterFailure": psAutzCounterFailure,
       "psAutzCounterCount": psAutzCounterCount,
       "psAutzCounterTime": psAutzCounterTime,
       "webAuthProtoTable": webAuthProtoTable,
       "webAuthProtoTableEntry": webAuthProtoTableEntry,
       "waProtocolIdx": waProtocolIdx,
       "waProtocolName": waProtocolName,
       "waAuthCounterSuccess": waAuthCounterSuccess,
       "waAuthCounterFailure": waAuthCounterFailure,
       "waAuthCounterCount": waAuthCounterCount,
       "waAuthCounterTime": waAuthCounterTime,
       "waAuthCounterAuthTime": waAuthCounterAuthTime,
       "waServicePolicyEvalTime": waServicePolicyEvalTime,
       "waPolicyEvalTime": waPolicyEvalTime,
       "tacacsAuthTable": tacacsAuthTable,
       "tacacsAuthTableEntry": tacacsAuthTableEntry,
       "tacAuthCounterSuccess": tacAuthCounterSuccess,
       "tacAuthCounterFailure": tacAuthCounterFailure,
       "tacAuthCounterCount": tacAuthCounterCount,
       "tacAuthCounterTime": tacAuthCounterTime,
       "tacAuthCounterAuthTime": tacAuthCounterAuthTime,
       "tacServicePolicyEvalTime": tacServicePolicyEvalTime,
       "tacPolicyEvalTime": tacPolicyEvalTime,
       "tacacsAutzTable": tacacsAutzTable,
       "tacacsAutzTableEntry": tacacsAutzTableEntry,
       "tacAutzCounterSuccess": tacAutzCounterSuccess,
       "tacAutzCounterFailure": tacAutzCounterFailure,
       "tacAutzCounterCount": tacAutzCounterCount,
       "tacAutzCounterTime": tacAutzCounterTime,
       "cppmNetworkInfoGroup": cppmNetworkInfoGroup,
       "networkTrafficTable": networkTrafficTable,
       "networkTrafficTableEntry": networkTrafficTableEntry,
       "nwAppIdx": nwAppIdx,
       "nwAppName": nwAppName,
       "nwAppPort": nwAppPort,
       "nwTrafficTotal": nwTrafficTotal,
       "cppmTraps": cppmTraps,
       "clearpassTrapObjectsGroup": clearpassTrapObjectsGroup,
       "cppmNodeName": cppmNodeName,
       "cppmNodeIp": cppmNodeIp,
       "cppmClusterServerIp": cppmClusterServerIp,
       "cppmNodeApplicationName": cppmNodeApplicationName,
       "cppmNodeCertApplicationName": cppmNodeCertApplicationName,
       "cppmLicenseDaysRemaining": cppmLicenseDaysRemaining,
       "cppmActivationDaysRemaining": cppmActivationDaysRemaining,
       "cppmCertDaysRemaining": cppmCertDaysRemaining,
       "cppmDiskSpaceRemaining": cppmDiskSpaceRemaining,
       "cppmMemoryRemaining": cppmMemoryRemaining,
       "cppmClusterOutOfSyncMinutes": cppmClusterOutOfSyncMinutes,
       "cppmClusterLicenseTotalCount": cppmClusterLicenseTotalCount,
       "cppmClusterLicenseUsageCount": cppmClusterLicenseUsageCount,
       "cppmResourceUnit": cppmResourceUnit,
       "cppmImageFile": cppmImageFile,
       "cppmImageInstallStatus": cppmImageInstallStatus,
       "cppmServiceName": cppmServiceName,
       "cppmServiceStatus": cppmServiceStatus,
       "cppmLicenseApplicationName": cppmLicenseApplicationName,
       "cppmLicenseOverrunDailyCount": cppmLicenseOverrunDailyCount,
       "cppmTrapMessage": cppmTrapMessage,
       "cppmCPUAverageLoad": cppmCPUAverageLoad,
       "cppmLicenseExpiry": cppmLicenseExpiry,
       "cppmActivationExpiry": cppmActivationExpiry,
       "cppmNodeCertExpiry": cppmNodeCertExpiry,
       "cppmLowDiskSpace": cppmLowDiskSpace,
       "cppmLowMemory": cppmLowMemory,
       "cppmClusterNodeAddNotification": cppmClusterNodeAddNotification,
       "cppmClusterNodeDelNotification": cppmClusterNodeDelNotification,
       "cppmClusterNodePromNotification": cppmClusterNodePromNotification,
       "cppmClusterNodeDbldNotification": cppmClusterNodeDbldNotification,
       "cppmClusterNodeNSyncNotification": cppmClusterNodeNSyncNotification,
       "cppmClusterPwdChangeNotification": cppmClusterPwdChangeNotification,
       "cppmConfigReset": cppmConfigReset,
       "cppmConfigRestore": cppmConfigRestore,
       "cppmUpdateNotification": cppmUpdateNotification,
       "cppmUpgradeNotification": cppmUpgradeNotification,
       "cppmClusterLicenseUsage": cppmClusterLicenseUsage,
       "cppmServiceStopNotification": cppmServiceStopNotification,
       "cppmServiceStartNotification": cppmServiceStartNotification,
       "cppmServiceRestartNotification": cppmServiceRestartNotification,
       "cppmHighCPULoadNotification": cppmHighCPULoadNotification,
       "cppmCoreDumpNotification": cppmCoreDumpNotification,
       "cppmClusterLicenseOverrun": cppmClusterLicenseOverrun}
)
