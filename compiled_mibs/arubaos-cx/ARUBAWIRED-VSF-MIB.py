# SNMP MIB module (ARUBAWIRED-VSF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-VSF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:31 2025
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

arubaWiredVsfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    arubaWiredVsfMIB.setRevisions(
        ("2022-03-03 00:00",
         "2020-03-24 00:00",
         "2019-04-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredVsfObjects_ObjectIdentity = ObjectIdentity
arubaWiredVsfObjects = _ArubaWiredVsfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0)
)
_ArubaWiredVsfConfig_ObjectIdentity = ObjectIdentity
arubaWiredVsfConfig = _ArubaWiredVsfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 1)
)
_ArubaWiredVsfTrapEnable_Type = TruthValue
_ArubaWiredVsfTrapEnable_Object = MibScalar
arubaWiredVsfTrapEnable = _ArubaWiredVsfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 1, 1),
    _ArubaWiredVsfTrapEnable_Type()
)
arubaWiredVsfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsfTrapEnable.setStatus("current")


class _ArubaWiredVsfOobmMADEnable_Type(Integer32):
    """Custom type arubaWiredVsfOobmMADEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mgmt", 2))
    )


_ArubaWiredVsfOobmMADEnable_Type.__name__ = "Integer32"
_ArubaWiredVsfOobmMADEnable_Object = MibScalar
arubaWiredVsfOobmMADEnable = _ArubaWiredVsfOobmMADEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 1, 2),
    _ArubaWiredVsfOobmMADEnable_Type()
)
arubaWiredVsfOobmMADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredVsfOobmMADEnable.setStatus("current")
_ArubaWiredVsfStatus_ObjectIdentity = ObjectIdentity
arubaWiredVsfStatus = _ArubaWiredVsfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 2)
)
_ArubaWiredVsfOperStatus_Type = DisplayString
_ArubaWiredVsfOperStatus_Object = MibScalar
arubaWiredVsfOperStatus = _ArubaWiredVsfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 2, 1),
    _ArubaWiredVsfOperStatus_Type()
)
arubaWiredVsfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfOperStatus.setStatus("current")
_ArubaWiredVsfTopology_Type = DisplayString
_ArubaWiredVsfTopology_Object = MibScalar
arubaWiredVsfTopology = _ArubaWiredVsfTopology_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 2, 2),
    _ArubaWiredVsfTopology_Type()
)
arubaWiredVsfTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfTopology.setStatus("current")
_ArubaWiredVsfMemberTable_Object = MibTable
arubaWiredVsfMemberTable = _ArubaWiredVsfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3)
)
if mibBuilder.loadTexts:
    arubaWiredVsfMemberTable.setStatus("current")
_ArubaWiredVsfMemberEntry_Object = MibTableRow
arubaWiredVsfMemberEntry = _ArubaWiredVsfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1)
)
arubaWiredVsfMemberEntry.setIndexNames(
    (0, "ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredVsfMemberEntry.setStatus("current")


class _ArubaWiredVsfMemberIndex_Type(Integer32):
    """Custom type arubaWiredVsfMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfMemberIndex_Type.__name__ = "Integer32"
_ArubaWiredVsfMemberIndex_Object = MibTableColumn
arubaWiredVsfMemberIndex = _ArubaWiredVsfMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 1),
    _ArubaWiredVsfMemberIndex_Type()
)
arubaWiredVsfMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberIndex.setStatus("current")
_ArubaWiredVsfMemberRole_Type = DisplayString
_ArubaWiredVsfMemberRole_Object = MibTableColumn
arubaWiredVsfMemberRole = _ArubaWiredVsfMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 2),
    _ArubaWiredVsfMemberRole_Type()
)
arubaWiredVsfMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberRole.setStatus("current")
_ArubaWiredVsfMemberStatus_Type = DisplayString
_ArubaWiredVsfMemberStatus_Object = MibTableColumn
arubaWiredVsfMemberStatus = _ArubaWiredVsfMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 3),
    _ArubaWiredVsfMemberStatus_Type()
)
arubaWiredVsfMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberStatus.setStatus("current")
_ArubaWiredVsfMemberPartNumber_Type = DisplayString
_ArubaWiredVsfMemberPartNumber_Object = MibTableColumn
arubaWiredVsfMemberPartNumber = _ArubaWiredVsfMemberPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 4),
    _ArubaWiredVsfMemberPartNumber_Type()
)
arubaWiredVsfMemberPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberPartNumber.setStatus("current")
_ArubaWiredVsfMemberMacAddr_Type = MacAddress
_ArubaWiredVsfMemberMacAddr_Object = MibTableColumn
arubaWiredVsfMemberMacAddr = _ArubaWiredVsfMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 5),
    _ArubaWiredVsfMemberMacAddr_Type()
)
arubaWiredVsfMemberMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberMacAddr.setStatus("current")
_ArubaWiredVsfMemberProductName_Type = DisplayString
_ArubaWiredVsfMemberProductName_Object = MibTableColumn
arubaWiredVsfMemberProductName = _ArubaWiredVsfMemberProductName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 6),
    _ArubaWiredVsfMemberProductName_Type()
)
arubaWiredVsfMemberProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberProductName.setStatus("current")
_ArubaWiredVsfMemberSerialNum_Type = DisplayString
_ArubaWiredVsfMemberSerialNum_Object = MibTableColumn
arubaWiredVsfMemberSerialNum = _ArubaWiredVsfMemberSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 7),
    _ArubaWiredVsfMemberSerialNum_Type()
)
arubaWiredVsfMemberSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberSerialNum.setStatus("current")
_ArubaWiredVsfMemberBootImage_Type = DisplayString
_ArubaWiredVsfMemberBootImage_Object = MibTableColumn
arubaWiredVsfMemberBootImage = _ArubaWiredVsfMemberBootImage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 8),
    _ArubaWiredVsfMemberBootImage_Type()
)
arubaWiredVsfMemberBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberBootImage.setStatus("current")
_ArubaWiredVsfMemberCpuUtil_Type = Integer32
_ArubaWiredVsfMemberCpuUtil_Object = MibTableColumn
arubaWiredVsfMemberCpuUtil = _ArubaWiredVsfMemberCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 9),
    _ArubaWiredVsfMemberCpuUtil_Type()
)
arubaWiredVsfMemberCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberCpuUtil.setStatus("current")
_ArubaWiredVsfMemberMemoryUtil_Type = Integer32
_ArubaWiredVsfMemberMemoryUtil_Object = MibTableColumn
arubaWiredVsfMemberMemoryUtil = _ArubaWiredVsfMemberMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 10),
    _ArubaWiredVsfMemberMemoryUtil_Type()
)
arubaWiredVsfMemberMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberMemoryUtil.setStatus("current")
_ArubaWiredVsfMemberBootTime_Type = TimeTicks
_ArubaWiredVsfMemberBootTime_Object = MibTableColumn
arubaWiredVsfMemberBootTime = _ArubaWiredVsfMemberBootTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 11),
    _ArubaWiredVsfMemberBootTime_Type()
)
arubaWiredVsfMemberBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberBootTime.setStatus("current")
_ArubaWiredVsfMemberBootRomVersion_Type = DisplayString
_ArubaWiredVsfMemberBootRomVersion_Object = MibTableColumn
arubaWiredVsfMemberBootRomVersion = _ArubaWiredVsfMemberBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 12),
    _ArubaWiredVsfMemberBootRomVersion_Type()
)
arubaWiredVsfMemberBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberBootRomVersion.setStatus("current")


class _ArubaWiredVsfMemberTotalMemory_Type(Integer32):
    """Custom type arubaWiredVsfMemberTotalMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfMemberTotalMemory_Type.__name__ = "Integer32"
_ArubaWiredVsfMemberTotalMemory_Object = MibTableColumn
arubaWiredVsfMemberTotalMemory = _ArubaWiredVsfMemberTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 13),
    _ArubaWiredVsfMemberTotalMemory_Type()
)
arubaWiredVsfMemberTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberTotalMemory.setStatus("current")


class _ArubaWiredVsfMemberCurrentUsage_Type(Integer32):
    """Custom type arubaWiredVsfMemberCurrentUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfMemberCurrentUsage_Type.__name__ = "Integer32"
_ArubaWiredVsfMemberCurrentUsage_Object = MibTableColumn
arubaWiredVsfMemberCurrentUsage = _ArubaWiredVsfMemberCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 3, 1, 14),
    _ArubaWiredVsfMemberCurrentUsage_Type()
)
arubaWiredVsfMemberCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfMemberCurrentUsage.setStatus("current")
_ArubaWiredVsfLinkTable_Object = MibTable
arubaWiredVsfLinkTable = _ArubaWiredVsfLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4)
)
if mibBuilder.loadTexts:
    arubaWiredVsfLinkTable.setStatus("current")
_ArubaWiredVsfLinkEntry_Object = MibTableRow
arubaWiredVsfLinkEntry = _ArubaWiredVsfLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1)
)
arubaWiredVsfLinkEntry.setIndexNames(
    (0, "ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkMemberId"),
    (0, "ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkId"),
)
if mibBuilder.loadTexts:
    arubaWiredVsfLinkEntry.setStatus("current")


class _ArubaWiredVsfLinkMemberId_Type(Integer32):
    """Custom type arubaWiredVsfLinkMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfLinkMemberId_Type.__name__ = "Integer32"
_ArubaWiredVsfLinkMemberId_Object = MibTableColumn
arubaWiredVsfLinkMemberId = _ArubaWiredVsfLinkMemberId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1, 1),
    _ArubaWiredVsfLinkMemberId_Type()
)
arubaWiredVsfLinkMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredVsfLinkMemberId.setStatus("current")


class _ArubaWiredVsfLinkId_Type(Integer32):
    """Custom type arubaWiredVsfLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfLinkId_Type.__name__ = "Integer32"
_ArubaWiredVsfLinkId_Object = MibTableColumn
arubaWiredVsfLinkId = _ArubaWiredVsfLinkId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1, 2),
    _ArubaWiredVsfLinkId_Type()
)
arubaWiredVsfLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredVsfLinkId.setStatus("current")
_ArubaWiredVsfLinkOperStatus_Type = DisplayString
_ArubaWiredVsfLinkOperStatus_Object = MibTableColumn
arubaWiredVsfLinkOperStatus = _ArubaWiredVsfLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1, 3),
    _ArubaWiredVsfLinkOperStatus_Type()
)
arubaWiredVsfLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfLinkOperStatus.setStatus("current")


class _ArubaWiredVsfLinkPeerMemberId_Type(Integer32):
    """Custom type arubaWiredVsfLinkPeerMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfLinkPeerMemberId_Type.__name__ = "Integer32"
_ArubaWiredVsfLinkPeerMemberId_Object = MibTableColumn
arubaWiredVsfLinkPeerMemberId = _ArubaWiredVsfLinkPeerMemberId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1, 4),
    _ArubaWiredVsfLinkPeerMemberId_Type()
)
arubaWiredVsfLinkPeerMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfLinkPeerMemberId.setStatus("current")


class _ArubaWiredVsfLinkPeerLinkId_Type(Integer32):
    """Custom type arubaWiredVsfLinkPeerLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArubaWiredVsfLinkPeerLinkId_Type.__name__ = "Integer32"
_ArubaWiredVsfLinkPeerLinkId_Object = MibTableColumn
arubaWiredVsfLinkPeerLinkId = _ArubaWiredVsfLinkPeerLinkId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1, 5),
    _ArubaWiredVsfLinkPeerLinkId_Type()
)
arubaWiredVsfLinkPeerLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfLinkPeerLinkId.setStatus("current")
_ArubaWiredVsfLinkPortList_Type = PortList
_ArubaWiredVsfLinkPortList_Object = MibTableColumn
arubaWiredVsfLinkPortList = _ArubaWiredVsfLinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 0, 4, 1, 6),
    _ArubaWiredVsfLinkPortList_Type()
)
arubaWiredVsfLinkPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredVsfLinkPortList.setStatus("current")
_ArubaWiredVsfNotifications_ObjectIdentity = ObjectIdentity
arubaWiredVsfNotifications = _ArubaWiredVsfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 1)
)
_ArubaWiredVsfConformance_ObjectIdentity = ObjectIdentity
arubaWiredVsfConformance = _ArubaWiredVsfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2)
)
_ArubaWiredVsfCompliances_ObjectIdentity = ObjectIdentity
arubaWiredVsfCompliances = _ArubaWiredVsfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 1)
)
_ArubaWiredVsfGroups_ObjectIdentity = ObjectIdentity
arubaWiredVsfGroups = _ArubaWiredVsfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 2)
)

# Managed Objects groups

arubaWiredVsfConfigScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 2, 1)
)
arubaWiredVsfConfigScalarGroup.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfTopology"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfTrapEnable"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfConfigScalarGroup.setStatus("current")

arubaWiredVsfStatusScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 2, 2)
)
arubaWiredVsfStatusScalarGroup.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfOperStatus"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfOobmMADEnable"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfStatusScalarGroup.setStatus("current")

arubaWiredVsfMemberTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 2, 3)
)
arubaWiredVsfMemberTableGroup.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberIndex"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberRole"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberStatus"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberPartNumber"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberMacAddr"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberProductName"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberSerialNum"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberBootImage"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberCpuUtil"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberMemoryUtil"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberBootTime"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberBootRomVersion"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberTotalMemory"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberCurrentUsage"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfMemberTableGroup.setStatus("current")

arubaWiredVsfLinkTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 2, 4)
)
arubaWiredVsfLinkTableGroup.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkOperStatus"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkPeerMemberId"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkPeerLinkId"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkPortList"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfLinkTableGroup.setStatus("current")


# Notification objects

arubaWiredVsfMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 1, 1)
)
arubaWiredVsfMemberStatusChange.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberIndex"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberRole"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfMemberStatusChange.setStatus(
        "current"
    )

arubaWiredVsfFragmentStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 1, 2)
)
arubaWiredVsfFragmentStatusChange.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberIndex"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfOperStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfFragmentStatusChange.setStatus(
        "current"
    )


# Notifications groups

arubaWiredVsfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 2, 5)
)
arubaWiredVsfNotificationsGroup.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberStatusChange"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfFragmentStatusChange"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredVsfMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10, 2, 1, 1)
)
arubaWiredVsfMibCompliance.setObjects(
      *(("ARUBAWIRED-VSF-MIB", "arubaWiredVsfConfigScalarGroup"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfStatusScalarGroup"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfMemberTableGroup"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfLinkTableGroup"),
        ("ARUBAWIRED-VSF-MIB", "arubaWiredVsfNotificationsGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredVsfMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-VSF-MIB",
    **{"arubaWiredVsfMIB": arubaWiredVsfMIB,
       "arubaWiredVsfObjects": arubaWiredVsfObjects,
       "arubaWiredVsfConfig": arubaWiredVsfConfig,
       "arubaWiredVsfTrapEnable": arubaWiredVsfTrapEnable,
       "arubaWiredVsfOobmMADEnable": arubaWiredVsfOobmMADEnable,
       "arubaWiredVsfStatus": arubaWiredVsfStatus,
       "arubaWiredVsfOperStatus": arubaWiredVsfOperStatus,
       "arubaWiredVsfTopology": arubaWiredVsfTopology,
       "arubaWiredVsfMemberTable": arubaWiredVsfMemberTable,
       "arubaWiredVsfMemberEntry": arubaWiredVsfMemberEntry,
       "arubaWiredVsfMemberIndex": arubaWiredVsfMemberIndex,
       "arubaWiredVsfMemberRole": arubaWiredVsfMemberRole,
       "arubaWiredVsfMemberStatus": arubaWiredVsfMemberStatus,
       "arubaWiredVsfMemberPartNumber": arubaWiredVsfMemberPartNumber,
       "arubaWiredVsfMemberMacAddr": arubaWiredVsfMemberMacAddr,
       "arubaWiredVsfMemberProductName": arubaWiredVsfMemberProductName,
       "arubaWiredVsfMemberSerialNum": arubaWiredVsfMemberSerialNum,
       "arubaWiredVsfMemberBootImage": arubaWiredVsfMemberBootImage,
       "arubaWiredVsfMemberCpuUtil": arubaWiredVsfMemberCpuUtil,
       "arubaWiredVsfMemberMemoryUtil": arubaWiredVsfMemberMemoryUtil,
       "arubaWiredVsfMemberBootTime": arubaWiredVsfMemberBootTime,
       "arubaWiredVsfMemberBootRomVersion": arubaWiredVsfMemberBootRomVersion,
       "arubaWiredVsfMemberTotalMemory": arubaWiredVsfMemberTotalMemory,
       "arubaWiredVsfMemberCurrentUsage": arubaWiredVsfMemberCurrentUsage,
       "arubaWiredVsfLinkTable": arubaWiredVsfLinkTable,
       "arubaWiredVsfLinkEntry": arubaWiredVsfLinkEntry,
       "arubaWiredVsfLinkMemberId": arubaWiredVsfLinkMemberId,
       "arubaWiredVsfLinkId": arubaWiredVsfLinkId,
       "arubaWiredVsfLinkOperStatus": arubaWiredVsfLinkOperStatus,
       "arubaWiredVsfLinkPeerMemberId": arubaWiredVsfLinkPeerMemberId,
       "arubaWiredVsfLinkPeerLinkId": arubaWiredVsfLinkPeerLinkId,
       "arubaWiredVsfLinkPortList": arubaWiredVsfLinkPortList,
       "arubaWiredVsfNotifications": arubaWiredVsfNotifications,
       "arubaWiredVsfMemberStatusChange": arubaWiredVsfMemberStatusChange,
       "arubaWiredVsfFragmentStatusChange": arubaWiredVsfFragmentStatusChange,
       "arubaWiredVsfConformance": arubaWiredVsfConformance,
       "arubaWiredVsfCompliances": arubaWiredVsfCompliances,
       "arubaWiredVsfMibCompliance": arubaWiredVsfMibCompliance,
       "arubaWiredVsfGroups": arubaWiredVsfGroups,
       "arubaWiredVsfConfigScalarGroup": arubaWiredVsfConfigScalarGroup,
       "arubaWiredVsfStatusScalarGroup": arubaWiredVsfStatusScalarGroup,
       "arubaWiredVsfMemberTableGroup": arubaWiredVsfMemberTableGroup,
       "arubaWiredVsfLinkTableGroup": arubaWiredVsfLinkTableGroup,
       "arubaWiredVsfNotificationsGroup": arubaWiredVsfNotificationsGroup}
)
