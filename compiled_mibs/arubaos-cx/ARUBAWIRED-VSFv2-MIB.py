# SNMP MIB module (ARUBAWIRED-VSFv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-VSFv2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:33 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredVsfv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2MIB.setRevisions(
        ("2025-01-16 00:00",
         "2023-05-16 00:00",
         "2022-03-03 00:00",
         "2021-11-21 00:00",
         "2020-11-18 00:00",
         "2020-09-09 00:00",
         "2020-07-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredVsfv2Notifications_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Notifications = _ArubaWiredVsfv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 0)
)
_ArubaWiredVsfv2Objects_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Objects = _ArubaWiredVsfv2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1)
)
_ArubaWiredVsfv2Config_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Config = _ArubaWiredVsfv2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 0)
)
_ArubaWiredVsfv2TrapEnable_Type = TruthValue
_ArubaWiredVsfv2TrapEnable_Object = MibScalar
arubaWiredVsfv2TrapEnable = _ArubaWiredVsfv2TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 0, 1),
    _ArubaWiredVsfv2TrapEnable_Type()
)
arubaWiredVsfv2TrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsfv2TrapEnable.setStatus("current")


class _ArubaWiredVsfv2SplitDetectConfigured_Type(Integer32):
    """Custom type arubaWiredVsfv2SplitDetectConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mgmt", 2),
          ("vlan", 3))
    )


_ArubaWiredVsfv2SplitDetectConfigured_Type.__name__ = "Integer32"
_ArubaWiredVsfv2SplitDetectConfigured_Object = MibScalar
arubaWiredVsfv2SplitDetectConfigured = _ArubaWiredVsfv2SplitDetectConfigured_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 0, 2),
    _ArubaWiredVsfv2SplitDetectConfigured_Type()
)
arubaWiredVsfv2SplitDetectConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectConfigured.setStatus("current")


class _ArubaWiredVsfv2SplitDetectVlanId_Type(DisplayString):
    """Custom type arubaWiredVsfv2SplitDetectVlanId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ArubaWiredVsfv2SplitDetectVlanId_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2SplitDetectVlanId_Object = MibScalar
arubaWiredVsfv2SplitDetectVlanId = _ArubaWiredVsfv2SplitDetectVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 0, 3),
    _ArubaWiredVsfv2SplitDetectVlanId_Type()
)
arubaWiredVsfv2SplitDetectVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectVlanId.setStatus("current")
_ArubaWiredVsfv2Status_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Status = _ArubaWiredVsfv2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1)
)
_ArubaWiredVsfv2OperStatus_Type = DisplayString
_ArubaWiredVsfv2OperStatus_Object = MibScalar
arubaWiredVsfv2OperStatus = _ArubaWiredVsfv2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 1),
    _ArubaWiredVsfv2OperStatus_Type()
)
arubaWiredVsfv2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2OperStatus.setStatus("current")
_ArubaWiredVsfv2Topology_Type = DisplayString
_ArubaWiredVsfv2Topology_Object = MibScalar
arubaWiredVsfv2Topology = _ArubaWiredVsfv2Topology_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 2),
    _ArubaWiredVsfv2Topology_Type()
)
arubaWiredVsfv2Topology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2Topology.setStatus("current")
_ArubaWiredVsfv2StackMacAddr_Type = MacAddress
_ArubaWiredVsfv2StackMacAddr_Object = MibScalar
arubaWiredVsfv2StackMacAddr = _ArubaWiredVsfv2StackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 3),
    _ArubaWiredVsfv2StackMacAddr_Type()
)
arubaWiredVsfv2StackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2StackMacAddr.setStatus("current")


class _ArubaWiredVsfv2DomainId_Type(DisplayString):
    """Custom type arubaWiredVsfv2DomainId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_ArubaWiredVsfv2DomainId_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2DomainId_Object = MibScalar
arubaWiredVsfv2DomainId = _ArubaWiredVsfv2DomainId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 4),
    _ArubaWiredVsfv2DomainId_Type()
)
arubaWiredVsfv2DomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2DomainId.setStatus("current")


class _ArubaWiredVsfv2Secondary_Type(DisplayString):
    """Custom type arubaWiredVsfv2Secondary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ArubaWiredVsfv2Secondary_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2Secondary_Object = MibScalar
arubaWiredVsfv2Secondary = _ArubaWiredVsfv2Secondary_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 5),
    _ArubaWiredVsfv2Secondary_Type()
)
arubaWiredVsfv2Secondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2Secondary.setStatus("current")


class _ArubaWiredVsfv2SplitDetectOperStatus_Type(DisplayString):
    """Custom type arubaWiredVsfv2SplitDetectOperStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ArubaWiredVsfv2SplitDetectOperStatus_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2SplitDetectOperStatus_Object = MibScalar
arubaWiredVsfv2SplitDetectOperStatus = _ArubaWiredVsfv2SplitDetectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 6),
    _ArubaWiredVsfv2SplitDetectOperStatus_Type()
)
arubaWiredVsfv2SplitDetectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectOperStatus.setStatus("current")


class _ArubaWiredVsfv2SplitDetectStatusDownReason_Type(DisplayString):
    """Custom type arubaWiredVsfv2SplitDetectStatusDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArubaWiredVsfv2SplitDetectStatusDownReason_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2SplitDetectStatusDownReason_Object = MibScalar
arubaWiredVsfv2SplitDetectStatusDownReason = _ArubaWiredVsfv2SplitDetectStatusDownReason_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 1, 7),
    _ArubaWiredVsfv2SplitDetectStatusDownReason_Type()
)
arubaWiredVsfv2SplitDetectStatusDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectStatusDownReason.setStatus("current")
_ArubaWiredVsfv2MemberTable_Object = MibTable
arubaWiredVsfv2MemberTable = _ArubaWiredVsfv2MemberTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberTable.setStatus("current")
_ArubaWiredVsfv2MemberEntry_Object = MibTableRow
arubaWiredVsfv2MemberEntry = _ArubaWiredVsfv2MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1)
)
arubaWiredVsfv2MemberEntry.setIndexNames(
    (0, "ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberEntry.setStatus("current")


class _ArubaWiredVsfv2MemberIndex_Type(Integer32):
    """Custom type arubaWiredVsfv2MemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2MemberIndex_Type.__name__ = "Integer32"
_ArubaWiredVsfv2MemberIndex_Object = MibTableColumn
arubaWiredVsfv2MemberIndex = _ArubaWiredVsfv2MemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 1),
    _ArubaWiredVsfv2MemberIndex_Type()
)
arubaWiredVsfv2MemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberIndex.setStatus("current")


class _ArubaWiredVsfv2MemberRole_Type(DisplayString):
    """Custom type arubaWiredVsfv2MemberRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredVsfv2MemberRole_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2MemberRole_Object = MibTableColumn
arubaWiredVsfv2MemberRole = _ArubaWiredVsfv2MemberRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 2),
    _ArubaWiredVsfv2MemberRole_Type()
)
arubaWiredVsfv2MemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberRole.setStatus("current")


class _ArubaWiredVsfv2MemberStatus_Type(DisplayString):
    """Custom type arubaWiredVsfv2MemberStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredVsfv2MemberStatus_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2MemberStatus_Object = MibTableColumn
arubaWiredVsfv2MemberStatus = _ArubaWiredVsfv2MemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 3),
    _ArubaWiredVsfv2MemberStatus_Type()
)
arubaWiredVsfv2MemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberStatus.setStatus("current")


class _ArubaWiredVsfv2MemberPartNumber_Type(DisplayString):
    """Custom type arubaWiredVsfv2MemberPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredVsfv2MemberPartNumber_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2MemberPartNumber_Object = MibTableColumn
arubaWiredVsfv2MemberPartNumber = _ArubaWiredVsfv2MemberPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 4),
    _ArubaWiredVsfv2MemberPartNumber_Type()
)
arubaWiredVsfv2MemberPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberPartNumber.setStatus("current")
_ArubaWiredVsfv2MemberMacAddr_Type = MacAddress
_ArubaWiredVsfv2MemberMacAddr_Object = MibTableColumn
arubaWiredVsfv2MemberMacAddr = _ArubaWiredVsfv2MemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 5),
    _ArubaWiredVsfv2MemberMacAddr_Type()
)
arubaWiredVsfv2MemberMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberMacAddr.setStatus("current")
_ArubaWiredVsfv2MemberProductName_Type = DisplayString
_ArubaWiredVsfv2MemberProductName_Object = MibTableColumn
arubaWiredVsfv2MemberProductName = _ArubaWiredVsfv2MemberProductName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 6),
    _ArubaWiredVsfv2MemberProductName_Type()
)
arubaWiredVsfv2MemberProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberProductName.setStatus("current")


class _ArubaWiredVsfv2MemberSerialNum_Type(DisplayString):
    """Custom type arubaWiredVsfv2MemberSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredVsfv2MemberSerialNum_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2MemberSerialNum_Object = MibTableColumn
arubaWiredVsfv2MemberSerialNum = _ArubaWiredVsfv2MemberSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 7),
    _ArubaWiredVsfv2MemberSerialNum_Type()
)
arubaWiredVsfv2MemberSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberSerialNum.setStatus("current")


class _ArubaWiredVsfv2MemberBootImage_Type(DisplayString):
    """Custom type arubaWiredVsfv2MemberBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredVsfv2MemberBootImage_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2MemberBootImage_Object = MibTableColumn
arubaWiredVsfv2MemberBootImage = _ArubaWiredVsfv2MemberBootImage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 8),
    _ArubaWiredVsfv2MemberBootImage_Type()
)
arubaWiredVsfv2MemberBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberBootImage.setStatus("current")


class _ArubaWiredVsfv2MemberCpuUtil_Type(Integer32):
    """Custom type arubaWiredVsfv2MemberCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArubaWiredVsfv2MemberCpuUtil_Type.__name__ = "Integer32"
_ArubaWiredVsfv2MemberCpuUtil_Object = MibTableColumn
arubaWiredVsfv2MemberCpuUtil = _ArubaWiredVsfv2MemberCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 9),
    _ArubaWiredVsfv2MemberCpuUtil_Type()
)
arubaWiredVsfv2MemberCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberCpuUtil.setStatus("current")


class _ArubaWiredVsfv2MemberMemoryUtil_Type(Integer32):
    """Custom type arubaWiredVsfv2MemberMemoryUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArubaWiredVsfv2MemberMemoryUtil_Type.__name__ = "Integer32"
_ArubaWiredVsfv2MemberMemoryUtil_Object = MibTableColumn
arubaWiredVsfv2MemberMemoryUtil = _ArubaWiredVsfv2MemberMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 10),
    _ArubaWiredVsfv2MemberMemoryUtil_Type()
)
arubaWiredVsfv2MemberMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberMemoryUtil.setStatus("current")
_ArubaWiredVsfv2MemberBootTime_Type = TimeTicks
_ArubaWiredVsfv2MemberBootTime_Object = MibTableColumn
arubaWiredVsfv2MemberBootTime = _ArubaWiredVsfv2MemberBootTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 11),
    _ArubaWiredVsfv2MemberBootTime_Type()
)
arubaWiredVsfv2MemberBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberBootTime.setStatus("current")


class _ArubaWiredVsfv2MemberBootRomVersion_Type(DisplayString):
    """Custom type arubaWiredVsfv2MemberBootRomVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArubaWiredVsfv2MemberBootRomVersion_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2MemberBootRomVersion_Object = MibTableColumn
arubaWiredVsfv2MemberBootRomVersion = _ArubaWiredVsfv2MemberBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 12),
    _ArubaWiredVsfv2MemberBootRomVersion_Type()
)
arubaWiredVsfv2MemberBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberBootRomVersion.setStatus("current")


class _ArubaWiredVsfv2MemberTotalMemory_Type(Integer32):
    """Custom type arubaWiredVsfv2MemberTotalMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2MemberTotalMemory_Type.__name__ = "Integer32"
_ArubaWiredVsfv2MemberTotalMemory_Object = MibTableColumn
arubaWiredVsfv2MemberTotalMemory = _ArubaWiredVsfv2MemberTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 13),
    _ArubaWiredVsfv2MemberTotalMemory_Type()
)
arubaWiredVsfv2MemberTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberTotalMemory.setStatus("current")


class _ArubaWiredVsfv2MemberCurrentUsage_Type(Integer32):
    """Custom type arubaWiredVsfv2MemberCurrentUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2MemberCurrentUsage_Type.__name__ = "Integer32"
_ArubaWiredVsfv2MemberCurrentUsage_Object = MibTableColumn
arubaWiredVsfv2MemberCurrentUsage = _ArubaWiredVsfv2MemberCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 14),
    _ArubaWiredVsfv2MemberCurrentUsage_Type()
)
arubaWiredVsfv2MemberCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberCurrentUsage.setStatus("current")


class _ArubaWiredVsfv2MemberEntPhysicalIndex_Type(Integer32):
    """Custom type arubaWiredVsfv2MemberEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredVsfv2MemberEntPhysicalIndex_Type.__name__ = "Integer32"
_ArubaWiredVsfv2MemberEntPhysicalIndex_Object = MibTableColumn
arubaWiredVsfv2MemberEntPhysicalIndex = _ArubaWiredVsfv2MemberEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 2, 1, 15),
    _ArubaWiredVsfv2MemberEntPhysicalIndex_Type()
)
arubaWiredVsfv2MemberEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberEntPhysicalIndex.setStatus("current")
_ArubaWiredVsfv2LinkTable_Object = MibTable
arubaWiredVsfv2LinkTable = _ArubaWiredVsfv2LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3)
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkTable.setStatus("current")
_ArubaWiredVsfv2LinkEntry_Object = MibTableRow
arubaWiredVsfv2LinkEntry = _ArubaWiredVsfv2LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1)
)
arubaWiredVsfv2LinkEntry.setIndexNames(
    (0, "ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkMemberId"),
    (0, "ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkId"),
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkEntry.setStatus("current")


class _ArubaWiredVsfv2LinkMemberId_Type(Integer32):
    """Custom type arubaWiredVsfv2LinkMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2LinkMemberId_Type.__name__ = "Integer32"
_ArubaWiredVsfv2LinkMemberId_Object = MibTableColumn
arubaWiredVsfv2LinkMemberId = _ArubaWiredVsfv2LinkMemberId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1, 1),
    _ArubaWiredVsfv2LinkMemberId_Type()
)
arubaWiredVsfv2LinkMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkMemberId.setStatus("current")


class _ArubaWiredVsfv2LinkId_Type(Integer32):
    """Custom type arubaWiredVsfv2LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2LinkId_Type.__name__ = "Integer32"
_ArubaWiredVsfv2LinkId_Object = MibTableColumn
arubaWiredVsfv2LinkId = _ArubaWiredVsfv2LinkId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1, 2),
    _ArubaWiredVsfv2LinkId_Type()
)
arubaWiredVsfv2LinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkId.setStatus("current")
_ArubaWiredVsfv2LinkOperStatus_Type = DisplayString
_ArubaWiredVsfv2LinkOperStatus_Object = MibTableColumn
arubaWiredVsfv2LinkOperStatus = _ArubaWiredVsfv2LinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1, 3),
    _ArubaWiredVsfv2LinkOperStatus_Type()
)
arubaWiredVsfv2LinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkOperStatus.setStatus("current")


class _ArubaWiredVsfv2LinkPeerMemberId_Type(Integer32):
    """Custom type arubaWiredVsfv2LinkPeerMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2LinkPeerMemberId_Type.__name__ = "Integer32"
_ArubaWiredVsfv2LinkPeerMemberId_Object = MibTableColumn
arubaWiredVsfv2LinkPeerMemberId = _ArubaWiredVsfv2LinkPeerMemberId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1, 4),
    _ArubaWiredVsfv2LinkPeerMemberId_Type()
)
arubaWiredVsfv2LinkPeerMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkPeerMemberId.setStatus("current")


class _ArubaWiredVsfv2LinkPeerLinkId_Type(Integer32):
    """Custom type arubaWiredVsfv2LinkPeerLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2LinkPeerLinkId_Type.__name__ = "Integer32"
_ArubaWiredVsfv2LinkPeerLinkId_Object = MibTableColumn
arubaWiredVsfv2LinkPeerLinkId = _ArubaWiredVsfv2LinkPeerLinkId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1, 5),
    _ArubaWiredVsfv2LinkPeerLinkId_Type()
)
arubaWiredVsfv2LinkPeerLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkPeerLinkId.setStatus("current")
_ArubaWiredVsfv2LinkPortList_Type = PortList
_ArubaWiredVsfv2LinkPortList_Object = MibTableColumn
arubaWiredVsfv2LinkPortList = _ArubaWiredVsfv2LinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 3, 1, 6),
    _ArubaWiredVsfv2LinkPortList_Type()
)
arubaWiredVsfv2LinkPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkPortList.setStatus("current")
_ArubaWiredVsfv2PortTable_Object = MibTable
arubaWiredVsfv2PortTable = _ArubaWiredVsfv2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4)
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortTable.setStatus("current")
_ArubaWiredVsfv2PortEntry_Object = MibTableRow
arubaWiredVsfv2PortEntry = _ArubaWiredVsfv2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1)
)
arubaWiredVsfv2PortEntry.setIndexNames(
    (0, "ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortIfIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortEntry.setStatus("current")


class _ArubaWiredVsfv2PortIfIndex_Type(Integer32):
    """Custom type arubaWiredVsfv2PortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfv2PortIfIndex_Type.__name__ = "Integer32"
_ArubaWiredVsfv2PortIfIndex_Object = MibTableColumn
arubaWiredVsfv2PortIfIndex = _ArubaWiredVsfv2PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1, 1),
    _ArubaWiredVsfv2PortIfIndex_Type()
)
arubaWiredVsfv2PortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortIfIndex.setStatus("current")


class _ArubaWiredVsfv2PortOperStatus_Type(DisplayString):
    """Custom type arubaWiredVsfv2PortOperStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredVsfv2PortOperStatus_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2PortOperStatus_Object = MibTableColumn
arubaWiredVsfv2PortOperStatus = _ArubaWiredVsfv2PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1, 2),
    _ArubaWiredVsfv2PortOperStatus_Type()
)
arubaWiredVsfv2PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortOperStatus.setStatus("current")


class _ArubaWiredVsfv2PortStatusStr_Type(DisplayString):
    """Custom type arubaWiredVsfv2PortStatusStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArubaWiredVsfv2PortStatusStr_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2PortStatusStr_Object = MibTableColumn
arubaWiredVsfv2PortStatusStr = _ArubaWiredVsfv2PortStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1, 3),
    _ArubaWiredVsfv2PortStatusStr_Type()
)
arubaWiredVsfv2PortStatusStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortStatusStr.setStatus("current")
_ArubaWiredVsfv2PortPeerInterface_Type = PortList
_ArubaWiredVsfv2PortPeerInterface_Object = MibTableColumn
arubaWiredVsfv2PortPeerInterface = _ArubaWiredVsfv2PortPeerInterface_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1, 4),
    _ArubaWiredVsfv2PortPeerInterface_Type()
)
arubaWiredVsfv2PortPeerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortPeerInterface.setStatus("current")
_ArubaWiredVsfv2PortPeerSysMac_Type = MacAddress
_ArubaWiredVsfv2PortPeerSysMac_Object = MibTableColumn
arubaWiredVsfv2PortPeerSysMac = _ArubaWiredVsfv2PortPeerSysMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1, 5),
    _ArubaWiredVsfv2PortPeerSysMac_Type()
)
arubaWiredVsfv2PortPeerSysMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortPeerSysMac.setStatus("current")


class _ArubaWiredVsfv2PortPeerProductType_Type(DisplayString):
    """Custom type arubaWiredVsfv2PortPeerProductType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ArubaWiredVsfv2PortPeerProductType_Type.__name__ = "DisplayString"
_ArubaWiredVsfv2PortPeerProductType_Object = MibTableColumn
arubaWiredVsfv2PortPeerProductType = _ArubaWiredVsfv2PortPeerProductType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 4, 1, 6),
    _ArubaWiredVsfv2PortPeerProductType_Type()
)
arubaWiredVsfv2PortPeerProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortPeerProductType.setStatus("current")
_ArubaWiredVsfv2Counters_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Counters = _ArubaWiredVsfv2Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 5)
)
_ArubaWiredVsfv2SplitDetectCountersTx_Type = DisplayString
_ArubaWiredVsfv2SplitDetectCountersTx_Object = MibScalar
arubaWiredVsfv2SplitDetectCountersTx = _ArubaWiredVsfv2SplitDetectCountersTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 5, 1),
    _ArubaWiredVsfv2SplitDetectCountersTx_Type()
)
arubaWiredVsfv2SplitDetectCountersTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectCountersTx.setStatus("current")
_ArubaWiredVsfv2SplitDetectCountersRx_Type = DisplayString
_ArubaWiredVsfv2SplitDetectCountersRx_Object = MibScalar
arubaWiredVsfv2SplitDetectCountersRx = _ArubaWiredVsfv2SplitDetectCountersRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 5, 2),
    _ArubaWiredVsfv2SplitDetectCountersRx_Type()
)
arubaWiredVsfv2SplitDetectCountersRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectCountersRx.setStatus("current")
_ArubaWiredVsfv2SplitDetectCountersRxDrop_Type = DisplayString
_ArubaWiredVsfv2SplitDetectCountersRxDrop_Object = MibScalar
arubaWiredVsfv2SplitDetectCountersRxDrop = _ArubaWiredVsfv2SplitDetectCountersRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 1, 5, 3),
    _ArubaWiredVsfv2SplitDetectCountersRxDrop_Type()
)
arubaWiredVsfv2SplitDetectCountersRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfv2SplitDetectCountersRxDrop.setStatus("current")
_ArubaWiredVsfv2Conformance_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Conformance = _ArubaWiredVsfv2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2)
)
_ArubaWiredVsfv2Compliances_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Compliances = _ArubaWiredVsfv2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 1)
)
_ArubaWiredVsfv2Groups_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2Groups = _ArubaWiredVsfv2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2)
)

# Managed Objects groups

arubaWiredVsfv2ConfigScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 1)
)
arubaWiredVsfv2ConfigScalarGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2Topology"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2TrapEnable"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2StackMacAddr"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2DomainId"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2Secondary"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectVlanId"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2ConfigScalarGroup.setStatus("current")

arubaWiredVsfv2StatusScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 2)
)
arubaWiredVsfv2StatusScalarGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2OperStatus"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectConfigured"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectOperStatus"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectStatusDownReason"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2StatusScalarGroup.setStatus("current")

arubaWiredVsfv2MemberTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 3)
)
arubaWiredVsfv2MemberTableGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberIndex"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberRole"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberStatus"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberPartNumber"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberMacAddr"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberProductName"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberSerialNum"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberBootImage"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberCpuUtil"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberMemoryUtil"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberBootTime"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberBootRomVersion"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberTotalMemory"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberCurrentUsage"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberEntPhysicalIndex"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberTableGroup.setStatus("current")

arubaWiredVsfv2LinkTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 4)
)
arubaWiredVsfv2LinkTableGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkOperStatus"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkPeerMemberId"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkPeerLinkId"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkPortList"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2LinkTableGroup.setStatus("current")

arubaWiredVsfv2PortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 5)
)
arubaWiredVsfv2PortTableGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortIfIndex"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortOperStatus"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortStatusStr"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortPeerInterface"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortPeerSysMac"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortPeerProductType"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2PortTableGroup.setStatus("current")

arubaWiredVsfv2CountersScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 7)
)
arubaWiredVsfv2CountersScalarGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectCountersTx"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectCountersRx"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2SplitDetectCountersRxDrop"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2CountersScalarGroup.setStatus("current")


# Notification objects

arubaWiredVsfv2MemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 0, 1)
)
arubaWiredVsfv2MemberStatusChange.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberIndex"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberRole"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2MemberStatusChange.setStatus(
        "current"
    )

arubaWiredVsfv2FragmentStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 0, 2)
)
arubaWiredVsfv2FragmentStatusChange.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberIndex"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2OperStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2FragmentStatusChange.setStatus(
        "current"
    )


# Notifications groups

arubaWiredVsfv2NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 2, 6)
)
arubaWiredVsfv2NotificationsGroup.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberStatusChange"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2FragmentStatusChange"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredVsfv2MibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15, 2, 1, 1)
)
arubaWiredVsfv2MibCompliance.setObjects(
      *(("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2ConfigScalarGroup"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2StatusScalarGroup"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2MemberTableGroup"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2LinkTableGroup"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2PortTableGroup"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2NotificationsGroup"),
        ("ARUBAWIRED-VSFv2-MIB", "arubaWiredVsfv2CountersScalarGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfv2MibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-VSFv2-MIB",
    **{"arubaWiredVsfv2MIB": arubaWiredVsfv2MIB,
       "arubaWiredVsfv2Notifications": arubaWiredVsfv2Notifications,
       "arubaWiredVsfv2MemberStatusChange": arubaWiredVsfv2MemberStatusChange,
       "arubaWiredVsfv2FragmentStatusChange": arubaWiredVsfv2FragmentStatusChange,
       "arubaWiredVsfv2Objects": arubaWiredVsfv2Objects,
       "arubaWiredVsfv2Config": arubaWiredVsfv2Config,
       "arubaWiredVsfv2TrapEnable": arubaWiredVsfv2TrapEnable,
       "arubaWiredVsfv2SplitDetectConfigured": arubaWiredVsfv2SplitDetectConfigured,
       "arubaWiredVsfv2SplitDetectVlanId": arubaWiredVsfv2SplitDetectVlanId,
       "arubaWiredVsfv2Status": arubaWiredVsfv2Status,
       "arubaWiredVsfv2OperStatus": arubaWiredVsfv2OperStatus,
       "arubaWiredVsfv2Topology": arubaWiredVsfv2Topology,
       "arubaWiredVsfv2StackMacAddr": arubaWiredVsfv2StackMacAddr,
       "arubaWiredVsfv2DomainId": arubaWiredVsfv2DomainId,
       "arubaWiredVsfv2Secondary": arubaWiredVsfv2Secondary,
       "arubaWiredVsfv2SplitDetectOperStatus": arubaWiredVsfv2SplitDetectOperStatus,
       "arubaWiredVsfv2SplitDetectStatusDownReason": arubaWiredVsfv2SplitDetectStatusDownReason,
       "arubaWiredVsfv2MemberTable": arubaWiredVsfv2MemberTable,
       "arubaWiredVsfv2MemberEntry": arubaWiredVsfv2MemberEntry,
       "arubaWiredVsfv2MemberIndex": arubaWiredVsfv2MemberIndex,
       "arubaWiredVsfv2MemberRole": arubaWiredVsfv2MemberRole,
       "arubaWiredVsfv2MemberStatus": arubaWiredVsfv2MemberStatus,
       "arubaWiredVsfv2MemberPartNumber": arubaWiredVsfv2MemberPartNumber,
       "arubaWiredVsfv2MemberMacAddr": arubaWiredVsfv2MemberMacAddr,
       "arubaWiredVsfv2MemberProductName": arubaWiredVsfv2MemberProductName,
       "arubaWiredVsfv2MemberSerialNum": arubaWiredVsfv2MemberSerialNum,
       "arubaWiredVsfv2MemberBootImage": arubaWiredVsfv2MemberBootImage,
       "arubaWiredVsfv2MemberCpuUtil": arubaWiredVsfv2MemberCpuUtil,
       "arubaWiredVsfv2MemberMemoryUtil": arubaWiredVsfv2MemberMemoryUtil,
       "arubaWiredVsfv2MemberBootTime": arubaWiredVsfv2MemberBootTime,
       "arubaWiredVsfv2MemberBootRomVersion": arubaWiredVsfv2MemberBootRomVersion,
       "arubaWiredVsfv2MemberTotalMemory": arubaWiredVsfv2MemberTotalMemory,
       "arubaWiredVsfv2MemberCurrentUsage": arubaWiredVsfv2MemberCurrentUsage,
       "arubaWiredVsfv2MemberEntPhysicalIndex": arubaWiredVsfv2MemberEntPhysicalIndex,
       "arubaWiredVsfv2LinkTable": arubaWiredVsfv2LinkTable,
       "arubaWiredVsfv2LinkEntry": arubaWiredVsfv2LinkEntry,
       "arubaWiredVsfv2LinkMemberId": arubaWiredVsfv2LinkMemberId,
       "arubaWiredVsfv2LinkId": arubaWiredVsfv2LinkId,
       "arubaWiredVsfv2LinkOperStatus": arubaWiredVsfv2LinkOperStatus,
       "arubaWiredVsfv2LinkPeerMemberId": arubaWiredVsfv2LinkPeerMemberId,
       "arubaWiredVsfv2LinkPeerLinkId": arubaWiredVsfv2LinkPeerLinkId,
       "arubaWiredVsfv2LinkPortList": arubaWiredVsfv2LinkPortList,
       "arubaWiredVsfv2PortTable": arubaWiredVsfv2PortTable,
       "arubaWiredVsfv2PortEntry": arubaWiredVsfv2PortEntry,
       "arubaWiredVsfv2PortIfIndex": arubaWiredVsfv2PortIfIndex,
       "arubaWiredVsfv2PortOperStatus": arubaWiredVsfv2PortOperStatus,
       "arubaWiredVsfv2PortStatusStr": arubaWiredVsfv2PortStatusStr,
       "arubaWiredVsfv2PortPeerInterface": arubaWiredVsfv2PortPeerInterface,
       "arubaWiredVsfv2PortPeerSysMac": arubaWiredVsfv2PortPeerSysMac,
       "arubaWiredVsfv2PortPeerProductType": arubaWiredVsfv2PortPeerProductType,
       "arubaWiredVsfv2Counters": arubaWiredVsfv2Counters,
       "arubaWiredVsfv2SplitDetectCountersTx": arubaWiredVsfv2SplitDetectCountersTx,
       "arubaWiredVsfv2SplitDetectCountersRx": arubaWiredVsfv2SplitDetectCountersRx,
       "arubaWiredVsfv2SplitDetectCountersRxDrop": arubaWiredVsfv2SplitDetectCountersRxDrop,
       "arubaWiredVsfv2Conformance": arubaWiredVsfv2Conformance,
       "arubaWiredVsfv2Compliances": arubaWiredVsfv2Compliances,
       "arubaWiredVsfv2MibCompliance": arubaWiredVsfv2MibCompliance,
       "arubaWiredVsfv2Groups": arubaWiredVsfv2Groups,
       "arubaWiredVsfv2ConfigScalarGroup": arubaWiredVsfv2ConfigScalarGroup,
       "arubaWiredVsfv2StatusScalarGroup": arubaWiredVsfv2StatusScalarGroup,
       "arubaWiredVsfv2MemberTableGroup": arubaWiredVsfv2MemberTableGroup,
       "arubaWiredVsfv2LinkTableGroup": arubaWiredVsfv2LinkTableGroup,
       "arubaWiredVsfv2PortTableGroup": arubaWiredVsfv2PortTableGroup,
       "arubaWiredVsfv2NotificationsGroup": arubaWiredVsfv2NotificationsGroup,
       "arubaWiredVsfv2CountersScalarGroup": arubaWiredVsfv2CountersScalarGroup}
)
