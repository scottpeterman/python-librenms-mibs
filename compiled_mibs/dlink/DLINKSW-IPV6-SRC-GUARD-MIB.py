# SNMP MIB module (DLINKSW-IPV6-SRC-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IPV6-SRC-GUARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:22 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwIpv6SourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145)
)
if mibBuilder.loadTexts:
    dlinkSwIpv6SourceGuardMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIpv6sgNotifications_ObjectIdentity = ObjectIdentity
dIpv6sgNotifications = _DIpv6sgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 0)
)
_DIpv6sgObjects_ObjectIdentity = ObjectIdentity
dIpv6sgObjects = _DIpv6sgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1)
)
_DIpv6sgPolicy_ObjectIdentity = ObjectIdentity
dIpv6sgPolicy = _DIpv6sgPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1)
)
_DIpv6sgPolicyNumber_Type = Unsigned32
_DIpv6sgPolicyNumber_Object = MibScalar
dIpv6sgPolicyNumber = _DIpv6sgPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 1),
    _DIpv6sgPolicyNumber_Type()
)
dIpv6sgPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpv6sgPolicyNumber.setStatus("current")
_DIpv6sgPolicyTable_Object = MibTable
dIpv6sgPolicyTable = _DIpv6sgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dIpv6sgPolicyTable.setStatus("current")
_DIpv6sgPolicyEntry_Object = MibTableRow
dIpv6sgPolicyEntry = _DIpv6sgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 2, 1)
)
dIpv6sgPolicyEntry.setIndexNames(
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgPolicyName"),
)
if mibBuilder.loadTexts:
    dIpv6sgPolicyEntry.setStatus("current")


class _DIpv6sgPolicyName_Type(DisplayString):
    """Custom type dIpv6sgPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DIpv6sgPolicyName_Type.__name__ = "DisplayString"
_DIpv6sgPolicyName_Object = MibTableColumn
dIpv6sgPolicyName = _DIpv6sgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 2, 1, 1),
    _DIpv6sgPolicyName_Type()
)
dIpv6sgPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgPolicyName.setStatus("current")


class _DIpv6sgPolicyDenyAutoConfig_Type(TruthValue):
    """Custom type dIpv6sgPolicyDenyAutoConfig based on TruthValue"""
    defaultValue = 2


_DIpv6sgPolicyDenyAutoConfig_Type.__name__ = "TruthValue"
_DIpv6sgPolicyDenyAutoConfig_Object = MibTableColumn
dIpv6sgPolicyDenyAutoConfig = _DIpv6sgPolicyDenyAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 2, 1, 2),
    _DIpv6sgPolicyDenyAutoConfig_Type()
)
dIpv6sgPolicyDenyAutoConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6sgPolicyDenyAutoConfig.setStatus("current")


class _DIpv6sgPolicyPermitLinkLocal_Type(TruthValue):
    """Custom type dIpv6sgPolicyPermitLinkLocal based on TruthValue"""
    defaultValue = 2


_DIpv6sgPolicyPermitLinkLocal_Type.__name__ = "TruthValue"
_DIpv6sgPolicyPermitLinkLocal_Object = MibTableColumn
dIpv6sgPolicyPermitLinkLocal = _DIpv6sgPolicyPermitLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 2, 1, 3),
    _DIpv6sgPolicyPermitLinkLocal_Type()
)
dIpv6sgPolicyPermitLinkLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6sgPolicyPermitLinkLocal.setStatus("current")
_DIpv6sgPolicyRowStatus_Type = RowStatus
_DIpv6sgPolicyRowStatus_Object = MibTableColumn
dIpv6sgPolicyRowStatus = _DIpv6sgPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 1, 2, 1, 99),
    _DIpv6sgPolicyRowStatus_Type()
)
dIpv6sgPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6sgPolicyRowStatus.setStatus("current")
_DIpv6sgInterface_ObjectIdentity = ObjectIdentity
dIpv6sgInterface = _DIpv6sgInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2)
)
_DIpv6sgIfConfigTable_Object = MibTable
dIpv6sgIfConfigTable = _DIpv6sgIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dIpv6sgIfConfigTable.setStatus("current")
_DIpv6sgIfConfigEntry_Object = MibTableRow
dIpv6sgIfConfigEntry = _DIpv6sgIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 1, 1)
)
dIpv6sgIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIpv6sgIfConfigEntry.setStatus("current")
_DIpv6sgIfEnabled_Type = TruthValue
_DIpv6sgIfEnabled_Object = MibTableColumn
dIpv6sgIfEnabled = _DIpv6sgIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 1, 1, 1),
    _DIpv6sgIfEnabled_Type()
)
dIpv6sgIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpv6sgIfEnabled.setStatus("current")
_DIpv6sgIfAttachTable_Object = MibTable
dIpv6sgIfAttachTable = _DIpv6sgIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dIpv6sgIfAttachTable.setStatus("current")
_DIpv6sgIfAttachEntry_Object = MibTableRow
dIpv6sgIfAttachEntry = _DIpv6sgIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 2, 1)
)
dIpv6sgIfAttachEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dIpv6sgIfAttachEntry.setStatus("current")


class _DIpv6sgIfAttachPolicy_Type(DisplayString):
    """Custom type dIpv6sgIfAttachPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DIpv6sgIfAttachPolicy_Type.__name__ = "DisplayString"
_DIpv6sgIfAttachPolicy_Object = MibTableColumn
dIpv6sgIfAttachPolicy = _DIpv6sgIfAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 2, 1, 1),
    _DIpv6sgIfAttachPolicy_Type()
)
dIpv6sgIfAttachPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6sgIfAttachPolicy.setStatus("current")
_DIpv6sgIfAttachRowStatus_Type = RowStatus
_DIpv6sgIfAttachRowStatus_Object = MibTableColumn
dIpv6sgIfAttachRowStatus = _DIpv6sgIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 2, 2, 1, 99),
    _DIpv6sgIfAttachRowStatus_Type()
)
dIpv6sgIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6sgIfAttachRowStatus.setStatus("current")
_DIpv6sgBindings_ObjectIdentity = ObjectIdentity
dIpv6sgBindings = _DIpv6sgBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3)
)
_DIpv6sgStaticBindingsTable_Object = MibTable
dIpv6sgStaticBindingsTable = _DIpv6sgStaticBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsTable.setStatus("current")
_DIpv6sgStaticBindingsEntry_Object = MibTableRow
dIpv6sgStaticBindingsEntry = _DIpv6sgStaticBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1, 1)
)
dIpv6sgStaticBindingsEntry.setIndexNames(
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgStaticBindingsVlan"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgStaticBindingsMacAddress"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgStaticBindingsIpAddress"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgStaticBindingsInterface"),
)
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsEntry.setStatus("current")
_DIpv6sgStaticBindingsVlan_Type = VlanId
_DIpv6sgStaticBindingsVlan_Object = MibTableColumn
dIpv6sgStaticBindingsVlan = _DIpv6sgStaticBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1, 1, 1),
    _DIpv6sgStaticBindingsVlan_Type()
)
dIpv6sgStaticBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsVlan.setStatus("current")
_DIpv6sgStaticBindingsMacAddress_Type = MacAddress
_DIpv6sgStaticBindingsMacAddress_Object = MibTableColumn
dIpv6sgStaticBindingsMacAddress = _DIpv6sgStaticBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1, 1, 2),
    _DIpv6sgStaticBindingsMacAddress_Type()
)
dIpv6sgStaticBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsMacAddress.setStatus("current")
_DIpv6sgStaticBindingsIpAddress_Type = InetAddressIPv6
_DIpv6sgStaticBindingsIpAddress_Object = MibTableColumn
dIpv6sgStaticBindingsIpAddress = _DIpv6sgStaticBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1, 1, 3),
    _DIpv6sgStaticBindingsIpAddress_Type()
)
dIpv6sgStaticBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsIpAddress.setStatus("current")
_DIpv6sgStaticBindingsInterface_Type = InterfaceIndex
_DIpv6sgStaticBindingsInterface_Object = MibTableColumn
dIpv6sgStaticBindingsInterface = _DIpv6sgStaticBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1, 1, 4),
    _DIpv6sgStaticBindingsInterface_Type()
)
dIpv6sgStaticBindingsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsInterface.setStatus("current")
_DIpv6sgStaticBindingsRowStatus_Type = RowStatus
_DIpv6sgStaticBindingsRowStatus_Object = MibTableColumn
dIpv6sgStaticBindingsRowStatus = _DIpv6sgStaticBindingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 1, 1, 99),
    _DIpv6sgStaticBindingsRowStatus_Type()
)
dIpv6sgStaticBindingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsRowStatus.setStatus("current")
_DIpv6sgBindingsTable_Object = MibTable
dIpv6sgBindingsTable = _DIpv6sgBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dIpv6sgBindingsTable.setStatus("current")
_DIpv6sgBindingsEntry_Object = MibTableRow
dIpv6sgBindingsEntry = _DIpv6sgBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1)
)
dIpv6sgBindingsEntry.setIndexNames(
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgBindingsOwner"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgBindingsIpAddress"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgBindingsMacAddress"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgBindingsInterface"),
    (0, "DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgBindingsVlan"),
)
if mibBuilder.loadTexts:
    dIpv6sgBindingsEntry.setStatus("current")


class _DIpv6sgBindingsOwner_Type(Integer32):
    """Custom type dIpv6sgBindingsOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("ndp", 2),
          ("dhcp", 3))
    )


_DIpv6sgBindingsOwner_Type.__name__ = "Integer32"
_DIpv6sgBindingsOwner_Object = MibTableColumn
dIpv6sgBindingsOwner = _DIpv6sgBindingsOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1, 1),
    _DIpv6sgBindingsOwner_Type()
)
dIpv6sgBindingsOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgBindingsOwner.setStatus("current")
_DIpv6sgBindingsIpAddress_Type = InetAddressIPv6
_DIpv6sgBindingsIpAddress_Object = MibTableColumn
dIpv6sgBindingsIpAddress = _DIpv6sgBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1, 2),
    _DIpv6sgBindingsIpAddress_Type()
)
dIpv6sgBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgBindingsIpAddress.setStatus("current")
_DIpv6sgBindingsMacAddress_Type = MacAddress
_DIpv6sgBindingsMacAddress_Object = MibTableColumn
dIpv6sgBindingsMacAddress = _DIpv6sgBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1, 3),
    _DIpv6sgBindingsMacAddress_Type()
)
dIpv6sgBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgBindingsMacAddress.setStatus("current")
_DIpv6sgBindingsInterface_Type = InterfaceIndex
_DIpv6sgBindingsInterface_Object = MibTableColumn
dIpv6sgBindingsInterface = _DIpv6sgBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1, 4),
    _DIpv6sgBindingsInterface_Type()
)
dIpv6sgBindingsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgBindingsInterface.setStatus("current")
_DIpv6sgBindingsVlan_Type = VlanId
_DIpv6sgBindingsVlan_Object = MibTableColumn
dIpv6sgBindingsVlan = _DIpv6sgBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1, 5),
    _DIpv6sgBindingsVlan_Type()
)
dIpv6sgBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6sgBindingsVlan.setStatus("current")
_DIpv6sgBindingsTimeleft_Type = Unsigned32
_DIpv6sgBindingsTimeleft_Object = MibTableColumn
dIpv6sgBindingsTimeleft = _DIpv6sgBindingsTimeleft_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 1, 3, 2, 1, 6),
    _DIpv6sgBindingsTimeleft_Type()
)
dIpv6sgBindingsTimeleft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpv6sgBindingsTimeleft.setStatus("current")
_DIpv6sgConformance_ObjectIdentity = ObjectIdentity
dIpv6sgConformance = _DIpv6sgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2)
)
_DIpv6sgMIBCompliances_ObjectIdentity = ObjectIdentity
dIpv6sgMIBCompliances = _DIpv6sgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 1)
)
_DIpv6sgMIBGroups_ObjectIdentity = ObjectIdentity
dIpv6sgMIBGroups = _DIpv6sgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 2)
)

# Managed Objects groups

dIpv6sgIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 2, 1)
)
dIpv6sgIfConfigGroup.setObjects(
    ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgIfEnabled")
)
if mibBuilder.loadTexts:
    dIpv6sgIfConfigGroup.setStatus("current")

dIpv6sgBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 2, 2)
)
dIpv6sgBindingsGroup.setObjects(
    ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgBindingsTimeleft")
)
if mibBuilder.loadTexts:
    dIpv6sgBindingsGroup.setStatus("current")

dIpv6sgPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 2, 3)
)
dIpv6sgPolicyGroup.setObjects(
      *(("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgPolicyNumber"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgPolicyDenyAutoConfig"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgPolicyPermitLinkLocal"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    dIpv6sgPolicyGroup.setStatus("current")

dIpv6sgIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 2, 4)
)
dIpv6sgIfAttachGroup.setObjects(
      *(("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgIfAttachPolicy"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgIfAttachRowStatus"))
)
if mibBuilder.loadTexts:
    dIpv6sgIfAttachGroup.setStatus("current")

dIpv6sgStaticBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 2, 5)
)
dIpv6sgStaticBindingsGroup.setObjects(
    ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgStaticBindingsRowStatus")
)
if mibBuilder.loadTexts:
    dIpv6sgStaticBindingsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dIpv6sgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 145, 2, 1, 1)
)
dIpv6sgMIBCompliance.setObjects(
      *(("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgIfConfigGroup"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgPolicyGroup"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgIfAttachGroup"),
        ("DLINKSW-IPV6-SRC-GUARD-MIB", "dIpv6sgStaticBindingsGroup"))
)
if mibBuilder.loadTexts:
    dIpv6sgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IPV6-SRC-GUARD-MIB",
    **{"dlinkSwIpv6SourceGuardMIB": dlinkSwIpv6SourceGuardMIB,
       "dIpv6sgNotifications": dIpv6sgNotifications,
       "dIpv6sgObjects": dIpv6sgObjects,
       "dIpv6sgPolicy": dIpv6sgPolicy,
       "dIpv6sgPolicyNumber": dIpv6sgPolicyNumber,
       "dIpv6sgPolicyTable": dIpv6sgPolicyTable,
       "dIpv6sgPolicyEntry": dIpv6sgPolicyEntry,
       "dIpv6sgPolicyName": dIpv6sgPolicyName,
       "dIpv6sgPolicyDenyAutoConfig": dIpv6sgPolicyDenyAutoConfig,
       "dIpv6sgPolicyPermitLinkLocal": dIpv6sgPolicyPermitLinkLocal,
       "dIpv6sgPolicyRowStatus": dIpv6sgPolicyRowStatus,
       "dIpv6sgInterface": dIpv6sgInterface,
       "dIpv6sgIfConfigTable": dIpv6sgIfConfigTable,
       "dIpv6sgIfConfigEntry": dIpv6sgIfConfigEntry,
       "dIpv6sgIfEnabled": dIpv6sgIfEnabled,
       "dIpv6sgIfAttachTable": dIpv6sgIfAttachTable,
       "dIpv6sgIfAttachEntry": dIpv6sgIfAttachEntry,
       "dIpv6sgIfAttachPolicy": dIpv6sgIfAttachPolicy,
       "dIpv6sgIfAttachRowStatus": dIpv6sgIfAttachRowStatus,
       "dIpv6sgBindings": dIpv6sgBindings,
       "dIpv6sgStaticBindingsTable": dIpv6sgStaticBindingsTable,
       "dIpv6sgStaticBindingsEntry": dIpv6sgStaticBindingsEntry,
       "dIpv6sgStaticBindingsVlan": dIpv6sgStaticBindingsVlan,
       "dIpv6sgStaticBindingsMacAddress": dIpv6sgStaticBindingsMacAddress,
       "dIpv6sgStaticBindingsIpAddress": dIpv6sgStaticBindingsIpAddress,
       "dIpv6sgStaticBindingsInterface": dIpv6sgStaticBindingsInterface,
       "dIpv6sgStaticBindingsRowStatus": dIpv6sgStaticBindingsRowStatus,
       "dIpv6sgBindingsTable": dIpv6sgBindingsTable,
       "dIpv6sgBindingsEntry": dIpv6sgBindingsEntry,
       "dIpv6sgBindingsOwner": dIpv6sgBindingsOwner,
       "dIpv6sgBindingsIpAddress": dIpv6sgBindingsIpAddress,
       "dIpv6sgBindingsMacAddress": dIpv6sgBindingsMacAddress,
       "dIpv6sgBindingsInterface": dIpv6sgBindingsInterface,
       "dIpv6sgBindingsVlan": dIpv6sgBindingsVlan,
       "dIpv6sgBindingsTimeleft": dIpv6sgBindingsTimeleft,
       "dIpv6sgConformance": dIpv6sgConformance,
       "dIpv6sgMIBCompliances": dIpv6sgMIBCompliances,
       "dIpv6sgMIBCompliance": dIpv6sgMIBCompliance,
       "dIpv6sgMIBGroups": dIpv6sgMIBGroups,
       "dIpv6sgIfConfigGroup": dIpv6sgIfConfigGroup,
       "dIpv6sgBindingsGroup": dIpv6sgBindingsGroup,
       "dIpv6sgPolicyGroup": dIpv6sgPolicyGroup,
       "dIpv6sgIfAttachGroup": dIpv6sgIfAttachGroup,
       "dIpv6sgStaticBindingsGroup": dIpv6sgStaticBindingsGroup}
)
