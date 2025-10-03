# SNMP MIB module (DLINKSW-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-NTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:38 2025
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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182)
)
if mibBuilder.loadTexts:
    dlinkSwNtpMIB.setRevisions(
        ("2014-09-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DNtpMIBNotifications_ObjectIdentity = ObjectIdentity
dNtpMIBNotifications = _DNtpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 0)
)
_DNtpMIBObjects_ObjectIdentity = ObjectIdentity
dNtpMIBObjects = _DNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1)
)
_DNtpCtrl_ObjectIdentity = ObjectIdentity
dNtpCtrl = _DNtpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1)
)


class _DNtpServiceEnabled_Type(TruthValue):
    """Custom type dNtpServiceEnabled based on TruthValue"""
    defaultValue = 2


_DNtpServiceEnabled_Type.__name__ = "TruthValue"
_DNtpServiceEnabled_Object = MibScalar
dNtpServiceEnabled = _DNtpServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 1),
    _DNtpServiceEnabled_Type()
)
dNtpServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpServiceEnabled.setStatus("current")


class _DNtpAuthenticateEnabled_Type(TruthValue):
    """Custom type dNtpAuthenticateEnabled based on TruthValue"""
    defaultValue = 1


_DNtpAuthenticateEnabled_Type.__name__ = "TruthValue"
_DNtpAuthenticateEnabled_Object = MibScalar
dNtpAuthenticateEnabled = _DNtpAuthenticateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 2),
    _DNtpAuthenticateEnabled_Type()
)
dNtpAuthenticateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAuthenticateEnabled.setStatus("current")


class _DNtpUpdateCalendarEnabled_Type(TruthValue):
    """Custom type dNtpUpdateCalendarEnabled based on TruthValue"""
    defaultValue = 2


_DNtpUpdateCalendarEnabled_Type.__name__ = "TruthValue"
_DNtpUpdateCalendarEnabled_Object = MibScalar
dNtpUpdateCalendarEnabled = _DNtpUpdateCalendarEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 3),
    _DNtpUpdateCalendarEnabled_Type()
)
dNtpUpdateCalendarEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpUpdateCalendarEnabled.setStatus("current")


class _DNtpMaxAssociations_Type(Integer32):
    """Custom type dNtpMaxAssociations based on Integer32"""
    defaultValue = 32


_DNtpMaxAssociations_Type.__name__ = "Integer32"
_DNtpMaxAssociations_Object = MibScalar
dNtpMaxAssociations = _DNtpMaxAssociations_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 4),
    _DNtpMaxAssociations_Type()
)
dNtpMaxAssociations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpMaxAssociations.setStatus("current")


class _DNtpBroadcastDelay_Type(Integer32):
    """Custom type dNtpBroadcastDelay based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_DNtpBroadcastDelay_Type.__name__ = "Integer32"
_DNtpBroadcastDelay_Object = MibScalar
dNtpBroadcastDelay = _DNtpBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 5),
    _DNtpBroadcastDelay_Type()
)
dNtpBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpBroadcastDelay.setStatus("current")


class _DNtpControlKey_Type(Integer32):
    """Custom type dNtpControlKey based on Integer32"""
    defaultValue = 0


_DNtpControlKey_Type.__name__ = "Integer32"
_DNtpControlKey_Object = MibScalar
dNtpControlKey = _DNtpControlKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 6),
    _DNtpControlKey_Type()
)
dNtpControlKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpControlKey.setStatus("current")


class _DNtpRequestKey_Type(Integer32):
    """Custom type dNtpRequestKey based on Integer32"""
    defaultValue = 0


_DNtpRequestKey_Type.__name__ = "Integer32"
_DNtpRequestKey_Object = MibScalar
dNtpRequestKey = _DNtpRequestKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 7),
    _DNtpRequestKey_Type()
)
dNtpRequestKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpRequestKey.setStatus("current")


class _DNtpMasterStratum_Type(Integer32):
    """Custom type dNtpMasterStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DNtpMasterStratum_Type.__name__ = "Integer32"
_DNtpMasterStratum_Object = MibScalar
dNtpMasterStratum = _DNtpMasterStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 1, 8),
    _DNtpMasterStratum_Type()
)
dNtpMasterStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpMasterStratum.setStatus("current")
_DNtpAccessGroupTable_Object = MibTable
dNtpAccessGroupTable = _DNtpAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2)
)
if mibBuilder.loadTexts:
    dNtpAccessGroupTable.setStatus("current")
_DNtpAccessGroupEntry_Object = MibTableRow
dNtpAccessGroupEntry = _DNtpAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1)
)
dNtpAccessGroupEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpAccessGroupVrfName"),
    (0, "DLINKSW-NTP-MIB", "dNtpAccessGroupIpAddressType"),
    (0, "DLINKSW-NTP-MIB", "dNtpAccessGroupIpAddress"),
    (0, "DLINKSW-NTP-MIB", "dNtpAccessGroupIpAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    dNtpAccessGroupEntry.setStatus("current")


class _DNtpAccessGroupVrfName_Type(DisplayString):
    """Custom type dNtpAccessGroupVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DNtpAccessGroupVrfName_Type.__name__ = "DisplayString"
_DNtpAccessGroupVrfName_Object = MibTableColumn
dNtpAccessGroupVrfName = _DNtpAccessGroupVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 1),
    _DNtpAccessGroupVrfName_Type()
)
dNtpAccessGroupVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpAccessGroupVrfName.setStatus("current")


class _DNtpAccessGroupIpAddressType_Type(InetAddressType):
    """Custom type dNtpAccessGroupIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv6z", 4))
    )


_DNtpAccessGroupIpAddressType_Type.__name__ = "InetAddressType"
_DNtpAccessGroupIpAddressType_Object = MibTableColumn
dNtpAccessGroupIpAddressType = _DNtpAccessGroupIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 2),
    _DNtpAccessGroupIpAddressType_Type()
)
dNtpAccessGroupIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpAccessGroupIpAddressType.setStatus("current")


class _DNtpAccessGroupIpAddress_Type(InetAddress):
    """Custom type dNtpAccessGroupIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_DNtpAccessGroupIpAddress_Type.__name__ = "InetAddress"
_DNtpAccessGroupIpAddress_Object = MibTableColumn
dNtpAccessGroupIpAddress = _DNtpAccessGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 3),
    _DNtpAccessGroupIpAddress_Type()
)
dNtpAccessGroupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpAccessGroupIpAddress.setStatus("current")
_DNtpAccessGroupIpAddressPrefixLength_Type = InetAddressPrefixLength
_DNtpAccessGroupIpAddressPrefixLength_Object = MibTableColumn
dNtpAccessGroupIpAddressPrefixLength = _DNtpAccessGroupIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 4),
    _DNtpAccessGroupIpAddressPrefixLength_Type()
)
dNtpAccessGroupIpAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpAccessGroupIpAddressPrefixLength.setStatus("current")


class _DNtpAccessGroupIgnore_Type(TruthValue):
    """Custom type dNtpAccessGroupIgnore based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupIgnore_Type.__name__ = "TruthValue"
_DNtpAccessGroupIgnore_Object = MibTableColumn
dNtpAccessGroupIgnore = _DNtpAccessGroupIgnore_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 5),
    _DNtpAccessGroupIgnore_Type()
)
dNtpAccessGroupIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupIgnore.setStatus("current")


class _DNtpAccessGroupNoModify_Type(TruthValue):
    """Custom type dNtpAccessGroupNoModify based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupNoModify_Type.__name__ = "TruthValue"
_DNtpAccessGroupNoModify_Object = MibTableColumn
dNtpAccessGroupNoModify = _DNtpAccessGroupNoModify_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 6),
    _DNtpAccessGroupNoModify_Type()
)
dNtpAccessGroupNoModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupNoModify.setStatus("current")


class _DNtpAccessGroupNoQuery_Type(TruthValue):
    """Custom type dNtpAccessGroupNoQuery based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupNoQuery_Type.__name__ = "TruthValue"
_DNtpAccessGroupNoQuery_Object = MibTableColumn
dNtpAccessGroupNoQuery = _DNtpAccessGroupNoQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 7),
    _DNtpAccessGroupNoQuery_Type()
)
dNtpAccessGroupNoQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupNoQuery.setStatus("current")


class _DNtpAccessGroupNoPeer_Type(TruthValue):
    """Custom type dNtpAccessGroupNoPeer based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupNoPeer_Type.__name__ = "TruthValue"
_DNtpAccessGroupNoPeer_Object = MibTableColumn
dNtpAccessGroupNoPeer = _DNtpAccessGroupNoPeer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 8),
    _DNtpAccessGroupNoPeer_Type()
)
dNtpAccessGroupNoPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupNoPeer.setStatus("current")


class _DNtpAccessGroupNoServe_Type(TruthValue):
    """Custom type dNtpAccessGroupNoServe based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupNoServe_Type.__name__ = "TruthValue"
_DNtpAccessGroupNoServe_Object = MibTableColumn
dNtpAccessGroupNoServe = _DNtpAccessGroupNoServe_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 9),
    _DNtpAccessGroupNoServe_Type()
)
dNtpAccessGroupNoServe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupNoServe.setStatus("current")


class _DNtpAccessGroupNoTrust_Type(TruthValue):
    """Custom type dNtpAccessGroupNoTrust based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupNoTrust_Type.__name__ = "TruthValue"
_DNtpAccessGroupNoTrust_Object = MibTableColumn
dNtpAccessGroupNoTrust = _DNtpAccessGroupNoTrust_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 10),
    _DNtpAccessGroupNoTrust_Type()
)
dNtpAccessGroupNoTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupNoTrust.setStatus("current")


class _DNtpAccessGroupVersion_Type(TruthValue):
    """Custom type dNtpAccessGroupVersion based on TruthValue"""
    defaultValue = 2


_DNtpAccessGroupVersion_Type.__name__ = "TruthValue"
_DNtpAccessGroupVersion_Object = MibTableColumn
dNtpAccessGroupVersion = _DNtpAccessGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 11),
    _DNtpAccessGroupVersion_Type()
)
dNtpAccessGroupVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessGroupVersion.setStatus("current")
_DNtpAccessGroupRowStatus_Type = RowStatus
_DNtpAccessGroupRowStatus_Object = MibTableColumn
dNtpAccessGroupRowStatus = _DNtpAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 2, 1, 99),
    _DNtpAccessGroupRowStatus_Type()
)
dNtpAccessGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpAccessGroupRowStatus.setStatus("current")
_DNtpAccessInterfaceTable_Object = MibTable
dNtpAccessInterfaceTable = _DNtpAccessInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 3)
)
if mibBuilder.loadTexts:
    dNtpAccessInterfaceTable.setStatus("current")
_DNtpAccessInterfaceEntry_Object = MibTableRow
dNtpAccessInterfaceEntry = _DNtpAccessInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 3, 1)
)
dNtpAccessInterfaceEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpAccessInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    dNtpAccessInterfaceEntry.setStatus("current")
_DNtpAccessInterfaceIfIndex_Type = InterfaceIndex
_DNtpAccessInterfaceIfIndex_Object = MibTableColumn
dNtpAccessInterfaceIfIndex = _DNtpAccessInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 3, 1, 1),
    _DNtpAccessInterfaceIfIndex_Type()
)
dNtpAccessInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpAccessInterfaceIfIndex.setStatus("current")


class _DNtpAccessInterfaceEnabled_Type(TruthValue):
    """Custom type dNtpAccessInterfaceEnabled based on TruthValue"""
    defaultValue = 1


_DNtpAccessInterfaceEnabled_Type.__name__ = "TruthValue"
_DNtpAccessInterfaceEnabled_Object = MibTableColumn
dNtpAccessInterfaceEnabled = _DNtpAccessInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 3, 1, 2),
    _DNtpAccessInterfaceEnabled_Type()
)
dNtpAccessInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAccessInterfaceEnabled.setStatus("current")
_DNtpAuthenticationKeyTable_Object = MibTable
dNtpAuthenticationKeyTable = _DNtpAuthenticationKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4)
)
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyTable.setStatus("current")
_DNtpAuthenticationKeyEntry_Object = MibTableRow
dNtpAuthenticationKeyEntry = _DNtpAuthenticationKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4, 1)
)
dNtpAuthenticationKeyEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyEntry.setStatus("current")


class _DNtpAuthenticationKeyId_Type(Integer32):
    """Custom type dNtpAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DNtpAuthenticationKeyId_Type.__name__ = "Integer32"
_DNtpAuthenticationKeyId_Object = MibTableColumn
dNtpAuthenticationKeyId = _DNtpAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4, 1, 1),
    _DNtpAuthenticationKeyId_Type()
)
dNtpAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyId.setStatus("current")


class _DNtpAuthenticationKeyType_Type(DisplayString):
    """Custom type dNtpAuthenticationKeyType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_DNtpAuthenticationKeyType_Type.__name__ = "DisplayString"
_DNtpAuthenticationKeyType_Object = MibTableColumn
dNtpAuthenticationKeyType = _DNtpAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4, 1, 2),
    _DNtpAuthenticationKeyType_Type()
)
dNtpAuthenticationKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyType.setStatus("current")


class _DNtpAuthenticationKeyValue_Type(DisplayString):
    """Custom type dNtpAuthenticationKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DNtpAuthenticationKeyValue_Type.__name__ = "DisplayString"
_DNtpAuthenticationKeyValue_Object = MibTableColumn
dNtpAuthenticationKeyValue = _DNtpAuthenticationKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4, 1, 3),
    _DNtpAuthenticationKeyValue_Type()
)
dNtpAuthenticationKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyValue.setStatus("current")


class _DNtpAuthenticationKeyTrusted_Type(TruthValue):
    """Custom type dNtpAuthenticationKeyTrusted based on TruthValue"""
    defaultValue = 2


_DNtpAuthenticationKeyTrusted_Type.__name__ = "TruthValue"
_DNtpAuthenticationKeyTrusted_Object = MibTableColumn
dNtpAuthenticationKeyTrusted = _DNtpAuthenticationKeyTrusted_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4, 1, 4),
    _DNtpAuthenticationKeyTrusted_Type()
)
dNtpAuthenticationKeyTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyTrusted.setStatus("current")
_DNtpAuthenticationKeyStatus_Type = RowStatus
_DNtpAuthenticationKeyStatus_Object = MibTableColumn
dNtpAuthenticationKeyStatus = _DNtpAuthenticationKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 4, 1, 99),
    _DNtpAuthenticationKeyStatus_Type()
)
dNtpAuthenticationKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpAuthenticationKeyStatus.setStatus("current")
_DNtpCfgBroadcastClientTable_Object = MibTable
dNtpCfgBroadcastClientTable = _DNtpCfgBroadcastClientTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 5)
)
if mibBuilder.loadTexts:
    dNtpCfgBroadcastClientTable.setStatus("current")
_DNtpCfgBroadcastClientEntry_Object = MibTableRow
dNtpCfgBroadcastClientEntry = _DNtpCfgBroadcastClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 5, 1)
)
dNtpCfgBroadcastClientEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpCfgBroadcastClientIfIndex"),
)
if mibBuilder.loadTexts:
    dNtpCfgBroadcastClientEntry.setStatus("current")
_DNtpCfgBroadcastClientIfIndex_Type = InterfaceIndex
_DNtpCfgBroadcastClientIfIndex_Object = MibTableColumn
dNtpCfgBroadcastClientIfIndex = _DNtpCfgBroadcastClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 5, 1, 1),
    _DNtpCfgBroadcastClientIfIndex_Type()
)
dNtpCfgBroadcastClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastClientIfIndex.setStatus("current")


class _DNtpCfgBroadcastClientKeyId_Type(Integer32):
    """Custom type dNtpCfgBroadcastClientKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DNtpCfgBroadcastClientKeyId_Type.__name__ = "Integer32"
_DNtpCfgBroadcastClientKeyId_Object = MibTableColumn
dNtpCfgBroadcastClientKeyId = _DNtpCfgBroadcastClientKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 5, 1, 2),
    _DNtpCfgBroadcastClientKeyId_Type()
)
dNtpCfgBroadcastClientKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastClientKeyId.setStatus("current")
_DNtpCfgBroadcastClientStatus_Type = RowStatus
_DNtpCfgBroadcastClientStatus_Object = MibTableColumn
dNtpCfgBroadcastClientStatus = _DNtpCfgBroadcastClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 5, 1, 99),
    _DNtpCfgBroadcastClientStatus_Type()
)
dNtpCfgBroadcastClientStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastClientStatus.setStatus("current")
_DNtpCfgBroadcastServerTable_Object = MibTable
dNtpCfgBroadcastServerTable = _DNtpCfgBroadcastServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 6)
)
if mibBuilder.loadTexts:
    dNtpCfgBroadcastServerTable.setStatus("current")
_DNtpCfgBroadcastServerEntry_Object = MibTableRow
dNtpCfgBroadcastServerEntry = _DNtpCfgBroadcastServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 6, 1)
)
dNtpCfgBroadcastServerEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpCfgBroadcastServerIfIndex"),
)
if mibBuilder.loadTexts:
    dNtpCfgBroadcastServerEntry.setStatus("current")
_DNtpCfgBroadcastServerIfIndex_Type = InterfaceIndex
_DNtpCfgBroadcastServerIfIndex_Object = MibTableColumn
dNtpCfgBroadcastServerIfIndex = _DNtpCfgBroadcastServerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 6, 1, 1),
    _DNtpCfgBroadcastServerIfIndex_Type()
)
dNtpCfgBroadcastServerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastServerIfIndex.setStatus("current")


class _DNtpCfgBroadcastServerVersion_Type(Integer32):
    """Custom type dNtpCfgBroadcastServerVersion based on Integer32"""
    defaultValue = 4


_DNtpCfgBroadcastServerVersion_Type.__name__ = "Integer32"
_DNtpCfgBroadcastServerVersion_Object = MibTableColumn
dNtpCfgBroadcastServerVersion = _DNtpCfgBroadcastServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 6, 1, 2),
    _DNtpCfgBroadcastServerVersion_Type()
)
dNtpCfgBroadcastServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastServerVersion.setStatus("current")


class _DNtpCfgBroadcastServerKeyId_Type(Integer32):
    """Custom type dNtpCfgBroadcastServerKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DNtpCfgBroadcastServerKeyId_Type.__name__ = "Integer32"
_DNtpCfgBroadcastServerKeyId_Object = MibTableColumn
dNtpCfgBroadcastServerKeyId = _DNtpCfgBroadcastServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 6, 1, 3),
    _DNtpCfgBroadcastServerKeyId_Type()
)
dNtpCfgBroadcastServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastServerKeyId.setStatus("current")
_DNtpCfgBroadcastServerStatus_Type = RowStatus
_DNtpCfgBroadcastServerStatus_Object = MibTableColumn
dNtpCfgBroadcastServerStatus = _DNtpCfgBroadcastServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 6, 1, 99),
    _DNtpCfgBroadcastServerStatus_Type()
)
dNtpCfgBroadcastServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpCfgBroadcastServerStatus.setStatus("current")
_DNtpCfgMulticastClientTable_Object = MibTable
dNtpCfgMulticastClientTable = _DNtpCfgMulticastClientTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7)
)
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientTable.setStatus("current")
_DNtpCfgMulticastClientEntry_Object = MibTableRow
dNtpCfgMulticastClientEntry = _DNtpCfgMulticastClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7, 1)
)
dNtpCfgMulticastClientEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpCfgMulticastClientIfIndex"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgMulticastClientIpAddressType"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgMulticastClientIpAddress"),
)
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientEntry.setStatus("current")
_DNtpCfgMulticastClientIfIndex_Type = InterfaceIndex
_DNtpCfgMulticastClientIfIndex_Object = MibTableColumn
dNtpCfgMulticastClientIfIndex = _DNtpCfgMulticastClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7, 1, 1),
    _DNtpCfgMulticastClientIfIndex_Type()
)
dNtpCfgMulticastClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientIfIndex.setStatus("current")


class _DNtpCfgMulticastClientIpAddressType_Type(InetAddressType):
    """Custom type dNtpCfgMulticastClientIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_DNtpCfgMulticastClientIpAddressType_Type.__name__ = "InetAddressType"
_DNtpCfgMulticastClientIpAddressType_Object = MibTableColumn
dNtpCfgMulticastClientIpAddressType = _DNtpCfgMulticastClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7, 1, 2),
    _DNtpCfgMulticastClientIpAddressType_Type()
)
dNtpCfgMulticastClientIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientIpAddressType.setStatus("current")


class _DNtpCfgMulticastClientIpAddress_Type(InetAddress):
    """Custom type dNtpCfgMulticastClientIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_DNtpCfgMulticastClientIpAddress_Type.__name__ = "InetAddress"
_DNtpCfgMulticastClientIpAddress_Object = MibTableColumn
dNtpCfgMulticastClientIpAddress = _DNtpCfgMulticastClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7, 1, 3),
    _DNtpCfgMulticastClientIpAddress_Type()
)
dNtpCfgMulticastClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientIpAddress.setStatus("current")


class _DNtpCfgMulticastClientKeyId_Type(Integer32):
    """Custom type dNtpCfgMulticastClientKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DNtpCfgMulticastClientKeyId_Type.__name__ = "Integer32"
_DNtpCfgMulticastClientKeyId_Object = MibTableColumn
dNtpCfgMulticastClientKeyId = _DNtpCfgMulticastClientKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7, 1, 4),
    _DNtpCfgMulticastClientKeyId_Type()
)
dNtpCfgMulticastClientKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientKeyId.setStatus("current")
_DNtpCfgMulticastClientStatus_Type = RowStatus
_DNtpCfgMulticastClientStatus_Object = MibTableColumn
dNtpCfgMulticastClientStatus = _DNtpCfgMulticastClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 7, 1, 99),
    _DNtpCfgMulticastClientStatus_Type()
)
dNtpCfgMulticastClientStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpCfgMulticastClientStatus.setStatus("current")
_DNtpCfgMulticastServerTable_Object = MibTable
dNtpCfgMulticastServerTable = _DNtpCfgMulticastServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8)
)
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerTable.setStatus("current")
_DNtpCfgMulticastServerEntry_Object = MibTableRow
dNtpCfgMulticastServerEntry = _DNtpCfgMulticastServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1)
)
dNtpCfgMulticastServerEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpCfgMulticastServerIfIndex"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgMulticastServerIpAddressType"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgMulticastServerIpAddress"),
)
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerEntry.setStatus("current")
_DNtpCfgMulticastServerIfIndex_Type = InterfaceIndex
_DNtpCfgMulticastServerIfIndex_Object = MibTableColumn
dNtpCfgMulticastServerIfIndex = _DNtpCfgMulticastServerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 1),
    _DNtpCfgMulticastServerIfIndex_Type()
)
dNtpCfgMulticastServerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerIfIndex.setStatus("current")


class _DNtpCfgMulticastServerIpAddressType_Type(InetAddressType):
    """Custom type dNtpCfgMulticastServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_DNtpCfgMulticastServerIpAddressType_Type.__name__ = "InetAddressType"
_DNtpCfgMulticastServerIpAddressType_Object = MibTableColumn
dNtpCfgMulticastServerIpAddressType = _DNtpCfgMulticastServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 2),
    _DNtpCfgMulticastServerIpAddressType_Type()
)
dNtpCfgMulticastServerIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerIpAddressType.setStatus("current")


class _DNtpCfgMulticastServerIpAddress_Type(InetAddress):
    """Custom type dNtpCfgMulticastServerIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_DNtpCfgMulticastServerIpAddress_Type.__name__ = "InetAddress"
_DNtpCfgMulticastServerIpAddress_Object = MibTableColumn
dNtpCfgMulticastServerIpAddress = _DNtpCfgMulticastServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 3),
    _DNtpCfgMulticastServerIpAddress_Type()
)
dNtpCfgMulticastServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerIpAddress.setStatus("current")


class _DNtpCfgMulticastServerVersion_Type(Integer32):
    """Custom type dNtpCfgMulticastServerVersion based on Integer32"""
    defaultValue = 4


_DNtpCfgMulticastServerVersion_Type.__name__ = "Integer32"
_DNtpCfgMulticastServerVersion_Object = MibTableColumn
dNtpCfgMulticastServerVersion = _DNtpCfgMulticastServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 4),
    _DNtpCfgMulticastServerVersion_Type()
)
dNtpCfgMulticastServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerVersion.setStatus("current")


class _DNtpCfgMulticastServerKeyId_Type(Integer32):
    """Custom type dNtpCfgMulticastServerKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DNtpCfgMulticastServerKeyId_Type.__name__ = "Integer32"
_DNtpCfgMulticastServerKeyId_Object = MibTableColumn
dNtpCfgMulticastServerKeyId = _DNtpCfgMulticastServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 5),
    _DNtpCfgMulticastServerKeyId_Type()
)
dNtpCfgMulticastServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerKeyId.setStatus("current")


class _DNtpCfgMulticastServerTtl_Type(Integer32):
    """Custom type dNtpCfgMulticastServerTtl based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DNtpCfgMulticastServerTtl_Type.__name__ = "Integer32"
_DNtpCfgMulticastServerTtl_Object = MibTableColumn
dNtpCfgMulticastServerTtl = _DNtpCfgMulticastServerTtl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 6),
    _DNtpCfgMulticastServerTtl_Type()
)
dNtpCfgMulticastServerTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerTtl.setStatus("current")
_DNtpCfgMulticastServerStatus_Type = RowStatus
_DNtpCfgMulticastServerStatus_Object = MibTableColumn
dNtpCfgMulticastServerStatus = _DNtpCfgMulticastServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 8, 1, 99),
    _DNtpCfgMulticastServerStatus_Type()
)
dNtpCfgMulticastServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpCfgMulticastServerStatus.setStatus("current")
_DNtpCfgPeerTable_Object = MibTable
dNtpCfgPeerTable = _DNtpCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9)
)
if mibBuilder.loadTexts:
    dNtpCfgPeerTable.setStatus("current")
_DNtpCfgPeerEntry_Object = MibTableRow
dNtpCfgPeerEntry = _DNtpCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1)
)
dNtpCfgPeerEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpCfgPeerVrfName"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgPeerIpAddressType"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgPeerIpAddress"),
)
if mibBuilder.loadTexts:
    dNtpCfgPeerEntry.setStatus("current")


class _DNtpCfgPeerVrfName_Type(DisplayString):
    """Custom type dNtpCfgPeerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DNtpCfgPeerVrfName_Type.__name__ = "DisplayString"
_DNtpCfgPeerVrfName_Object = MibTableColumn
dNtpCfgPeerVrfName = _DNtpCfgPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 1),
    _DNtpCfgPeerVrfName_Type()
)
dNtpCfgPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgPeerVrfName.setStatus("current")


class _DNtpCfgPeerIpAddressType_Type(InetAddressType):
    """Custom type dNtpCfgPeerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv6z", 4))
    )


_DNtpCfgPeerIpAddressType_Type.__name__ = "InetAddressType"
_DNtpCfgPeerIpAddressType_Object = MibTableColumn
dNtpCfgPeerIpAddressType = _DNtpCfgPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 2),
    _DNtpCfgPeerIpAddressType_Type()
)
dNtpCfgPeerIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgPeerIpAddressType.setStatus("current")


class _DNtpCfgPeerIpAddress_Type(InetAddress):
    """Custom type dNtpCfgPeerIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_DNtpCfgPeerIpAddress_Type.__name__ = "InetAddress"
_DNtpCfgPeerIpAddress_Object = MibTableColumn
dNtpCfgPeerIpAddress = _DNtpCfgPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 3),
    _DNtpCfgPeerIpAddress_Type()
)
dNtpCfgPeerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgPeerIpAddress.setStatus("current")


class _DNtpCfgPeerVersion_Type(Integer32):
    """Custom type dNtpCfgPeerVersion based on Integer32"""
    defaultValue = 4


_DNtpCfgPeerVersion_Type.__name__ = "Integer32"
_DNtpCfgPeerVersion_Object = MibTableColumn
dNtpCfgPeerVersion = _DNtpCfgPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 4),
    _DNtpCfgPeerVersion_Type()
)
dNtpCfgPeerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgPeerVersion.setStatus("current")


class _DNtpCfgPeerKeyId_Type(Integer32):
    """Custom type dNtpCfgPeerKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DNtpCfgPeerKeyId_Type.__name__ = "Integer32"
_DNtpCfgPeerKeyId_Object = MibTableColumn
dNtpCfgPeerKeyId = _DNtpCfgPeerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 5),
    _DNtpCfgPeerKeyId_Type()
)
dNtpCfgPeerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgPeerKeyId.setStatus("current")


class _DNtpCfgPeerPrefer_Type(TruthValue):
    """Custom type dNtpCfgPeerPrefer based on TruthValue"""
    defaultValue = 2


_DNtpCfgPeerPrefer_Type.__name__ = "TruthValue"
_DNtpCfgPeerPrefer_Object = MibTableColumn
dNtpCfgPeerPrefer = _DNtpCfgPeerPrefer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 6),
    _DNtpCfgPeerPrefer_Type()
)
dNtpCfgPeerPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgPeerPrefer.setStatus("current")


class _DNtpCfgPeerMinPoll_Type(Integer32):
    """Custom type dNtpCfgPeerMinPoll based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_DNtpCfgPeerMinPoll_Type.__name__ = "Integer32"
_DNtpCfgPeerMinPoll_Object = MibTableColumn
dNtpCfgPeerMinPoll = _DNtpCfgPeerMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 7),
    _DNtpCfgPeerMinPoll_Type()
)
dNtpCfgPeerMinPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgPeerMinPoll.setStatus("current")


class _DNtpCfgPeerMaxPoll_Type(Integer32):
    """Custom type dNtpCfgPeerMaxPoll based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_DNtpCfgPeerMaxPoll_Type.__name__ = "Integer32"
_DNtpCfgPeerMaxPoll_Object = MibTableColumn
dNtpCfgPeerMaxPoll = _DNtpCfgPeerMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 8),
    _DNtpCfgPeerMaxPoll_Type()
)
dNtpCfgPeerMaxPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgPeerMaxPoll.setStatus("current")
_DNtpCfgPeerStatus_Type = RowStatus
_DNtpCfgPeerStatus_Object = MibTableColumn
dNtpCfgPeerStatus = _DNtpCfgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 9, 1, 99),
    _DNtpCfgPeerStatus_Type()
)
dNtpCfgPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpCfgPeerStatus.setStatus("current")
_DNtpCfgSrvTable_Object = MibTable
dNtpCfgSrvTable = _DNtpCfgSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10)
)
if mibBuilder.loadTexts:
    dNtpCfgSrvTable.setStatus("current")
_DNtpCfgSrvEntry_Object = MibTableRow
dNtpCfgSrvEntry = _DNtpCfgSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1)
)
dNtpCfgSrvEntry.setIndexNames(
    (0, "DLINKSW-NTP-MIB", "dNtpCfgSrvVrfName"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgSrvIpAddressType"),
    (0, "DLINKSW-NTP-MIB", "dNtpCfgSrvIpAddress"),
)
if mibBuilder.loadTexts:
    dNtpCfgSrvEntry.setStatus("current")


class _DNtpCfgSrvVrfName_Type(DisplayString):
    """Custom type dNtpCfgSrvVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DNtpCfgSrvVrfName_Type.__name__ = "DisplayString"
_DNtpCfgSrvVrfName_Object = MibTableColumn
dNtpCfgSrvVrfName = _DNtpCfgSrvVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 1),
    _DNtpCfgSrvVrfName_Type()
)
dNtpCfgSrvVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgSrvVrfName.setStatus("current")


class _DNtpCfgSrvIpAddressType_Type(InetAddressType):
    """Custom type dNtpCfgSrvIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv6z", 4))
    )


_DNtpCfgSrvIpAddressType_Type.__name__ = "InetAddressType"
_DNtpCfgSrvIpAddressType_Object = MibTableColumn
dNtpCfgSrvIpAddressType = _DNtpCfgSrvIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 2),
    _DNtpCfgSrvIpAddressType_Type()
)
dNtpCfgSrvIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgSrvIpAddressType.setStatus("current")


class _DNtpCfgSrvIpAddress_Type(InetAddress):
    """Custom type dNtpCfgSrvIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_DNtpCfgSrvIpAddress_Type.__name__ = "InetAddress"
_DNtpCfgSrvIpAddress_Object = MibTableColumn
dNtpCfgSrvIpAddress = _DNtpCfgSrvIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 3),
    _DNtpCfgSrvIpAddress_Type()
)
dNtpCfgSrvIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNtpCfgSrvIpAddress.setStatus("current")


class _DNtpCfgSrvVersion_Type(Integer32):
    """Custom type dNtpCfgSrvVersion based on Integer32"""
    defaultValue = 4


_DNtpCfgSrvVersion_Type.__name__ = "Integer32"
_DNtpCfgSrvVersion_Object = MibTableColumn
dNtpCfgSrvVersion = _DNtpCfgSrvVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 4),
    _DNtpCfgSrvVersion_Type()
)
dNtpCfgSrvVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgSrvVersion.setStatus("current")


class _DNtpCfgSrvKeyId_Type(Integer32):
    """Custom type dNtpCfgSrvKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DNtpCfgSrvKeyId_Type.__name__ = "Integer32"
_DNtpCfgSrvKeyId_Object = MibTableColumn
dNtpCfgSrvKeyId = _DNtpCfgSrvKeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 5),
    _DNtpCfgSrvKeyId_Type()
)
dNtpCfgSrvKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgSrvKeyId.setStatus("current")


class _DNtpCfgSrvPrefer_Type(TruthValue):
    """Custom type dNtpCfgSrvPrefer based on TruthValue"""
    defaultValue = 2


_DNtpCfgSrvPrefer_Type.__name__ = "TruthValue"
_DNtpCfgSrvPrefer_Object = MibTableColumn
dNtpCfgSrvPrefer = _DNtpCfgSrvPrefer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 6),
    _DNtpCfgSrvPrefer_Type()
)
dNtpCfgSrvPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgSrvPrefer.setStatus("current")


class _DNtpCfgSrvMinPoll_Type(Integer32):
    """Custom type dNtpCfgSrvMinPoll based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_DNtpCfgSrvMinPoll_Type.__name__ = "Integer32"
_DNtpCfgSrvMinPoll_Object = MibTableColumn
dNtpCfgSrvMinPoll = _DNtpCfgSrvMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 7),
    _DNtpCfgSrvMinPoll_Type()
)
dNtpCfgSrvMinPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgSrvMinPoll.setStatus("current")


class _DNtpCfgSrvMaxPoll_Type(Integer32):
    """Custom type dNtpCfgSrvMaxPoll based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_DNtpCfgSrvMaxPoll_Type.__name__ = "Integer32"
_DNtpCfgSrvMaxPoll_Object = MibTableColumn
dNtpCfgSrvMaxPoll = _DNtpCfgSrvMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 8),
    _DNtpCfgSrvMaxPoll_Type()
)
dNtpCfgSrvMaxPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNtpCfgSrvMaxPoll.setStatus("current")
_DNtpCfgSrvStatus_Type = RowStatus
_DNtpCfgSrvStatus_Object = MibTableColumn
dNtpCfgSrvStatus = _DNtpCfgSrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 1, 10, 1, 99),
    _DNtpCfgSrvStatus_Type()
)
dNtpCfgSrvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNtpCfgSrvStatus.setStatus("current")
_DNtpMIBConformance_ObjectIdentity = ObjectIdentity
dNtpMIBConformance = _DNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2)
)
_DNtpCompliances_ObjectIdentity = ObjectIdentity
dNtpCompliances = _DNtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 1)
)
_DNtpGroups_ObjectIdentity = ObjectIdentity
dNtpGroups = _DNtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2)
)

# Managed Objects groups

dNtpCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2, 1)
)
dNtpCtrlGroup.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpServiceEnabled"),
        ("DLINKSW-NTP-MIB", "dNtpAuthenticateEnabled"),
        ("DLINKSW-NTP-MIB", "dNtpAccessInterfaceEnabled"),
        ("DLINKSW-NTP-MIB", "dNtpMaxAssociations"),
        ("DLINKSW-NTP-MIB", "dNtpControlKey"),
        ("DLINKSW-NTP-MIB", "dNtpRequestKey"),
        ("DLINKSW-NTP-MIB", "dNtpMasterStratum"))
)
if mibBuilder.loadTexts:
    dNtpCtrlGroup.setStatus("current")

dNtpAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2, 2)
)
dNtpAclGroup.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpAccessGroupIgnore"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupNoModify"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupNoQuery"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupNoPeer"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupNoServe"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupNoTrust"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupVersion"),
        ("DLINKSW-NTP-MIB", "dNtpAccessGroupRowStatus"),
        ("DLINKSW-NTP-MIB", "dNtpAccessInterfaceEnabled"))
)
if mibBuilder.loadTexts:
    dNtpAclGroup.setStatus("current")

dNtpBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2, 3)
)
dNtpBroadcastGroup.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpBroadcastDelay"),
        ("DLINKSW-NTP-MIB", "dNtpCfgBroadcastClientKeyId"),
        ("DLINKSW-NTP-MIB", "dNtpCfgBroadcastClientStatus"),
        ("DLINKSW-NTP-MIB", "dNtpCfgBroadcastServerVersion"),
        ("DLINKSW-NTP-MIB", "dNtpCfgBroadcastServerKeyId"),
        ("DLINKSW-NTP-MIB", "dNtpCfgBroadcastServerStatus"))
)
if mibBuilder.loadTexts:
    dNtpBroadcastGroup.setStatus("current")

dNtpMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2, 4)
)
dNtpMulticastGroup.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpCfgMulticastClientKeyId"),
        ("DLINKSW-NTP-MIB", "dNtpCfgMulticastClientStatus"),
        ("DLINKSW-NTP-MIB", "dNtpCfgMulticastServerVersion"),
        ("DLINKSW-NTP-MIB", "dNtpCfgMulticastServerKeyId"),
        ("DLINKSW-NTP-MIB", "dNtpCfgMulticastServerTtl"),
        ("DLINKSW-NTP-MIB", "dNtpCfgMulticastServerStatus"))
)
if mibBuilder.loadTexts:
    dNtpMulticastGroup.setStatus("current")

dNtpPeerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2, 5)
)
dNtpPeerCfgGroup.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpCfgPeerVersion"),
        ("DLINKSW-NTP-MIB", "dNtpCfgPeerKeyId"),
        ("DLINKSW-NTP-MIB", "dNtpCfgPeerPrefer"),
        ("DLINKSW-NTP-MIB", "dNtpCfgPeerMinPoll"),
        ("DLINKSW-NTP-MIB", "dNtpCfgPeerMaxPoll"),
        ("DLINKSW-NTP-MIB", "dNtpCfgPeerStatus"))
)
if mibBuilder.loadTexts:
    dNtpPeerCfgGroup.setStatus("current")

dNtpSrvCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 2, 6)
)
dNtpSrvCfgGroup.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpCfgSrvVersion"),
        ("DLINKSW-NTP-MIB", "dNtpCfgSrvKeyId"),
        ("DLINKSW-NTP-MIB", "dNtpCfgSrvPrefer"),
        ("DLINKSW-NTP-MIB", "dNtpCfgSrvMinPoll"),
        ("DLINKSW-NTP-MIB", "dNtpCfgSrvMaxPoll"),
        ("DLINKSW-NTP-MIB", "dNtpCfgSrvStatus"))
)
if mibBuilder.loadTexts:
    dNtpSrvCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dNtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 182, 2, 1, 1)
)
dNtpCompliance.setObjects(
      *(("DLINKSW-NTP-MIB", "dNtpCtrlGroup"),
        ("DLINKSW-NTP-MIB", "dNtpCtrlGroup"),
        ("DLINKSW-NTP-MIB", "dNtpAclGroup"),
        ("DLINKSW-NTP-MIB", "dNtpBroadcastGroup"),
        ("DLINKSW-NTP-MIB", "dNtpMulticastGroup"),
        ("DLINKSW-NTP-MIB", "dNtpPeerCfgGroup"),
        ("DLINKSW-NTP-MIB", "dNtpSrvCfgGroup"))
)
if mibBuilder.loadTexts:
    dNtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-NTP-MIB",
    **{"dlinkSwNtpMIB": dlinkSwNtpMIB,
       "dNtpMIBNotifications": dNtpMIBNotifications,
       "dNtpMIBObjects": dNtpMIBObjects,
       "dNtpCtrl": dNtpCtrl,
       "dNtpServiceEnabled": dNtpServiceEnabled,
       "dNtpAuthenticateEnabled": dNtpAuthenticateEnabled,
       "dNtpUpdateCalendarEnabled": dNtpUpdateCalendarEnabled,
       "dNtpMaxAssociations": dNtpMaxAssociations,
       "dNtpBroadcastDelay": dNtpBroadcastDelay,
       "dNtpControlKey": dNtpControlKey,
       "dNtpRequestKey": dNtpRequestKey,
       "dNtpMasterStratum": dNtpMasterStratum,
       "dNtpAccessGroupTable": dNtpAccessGroupTable,
       "dNtpAccessGroupEntry": dNtpAccessGroupEntry,
       "dNtpAccessGroupVrfName": dNtpAccessGroupVrfName,
       "dNtpAccessGroupIpAddressType": dNtpAccessGroupIpAddressType,
       "dNtpAccessGroupIpAddress": dNtpAccessGroupIpAddress,
       "dNtpAccessGroupIpAddressPrefixLength": dNtpAccessGroupIpAddressPrefixLength,
       "dNtpAccessGroupIgnore": dNtpAccessGroupIgnore,
       "dNtpAccessGroupNoModify": dNtpAccessGroupNoModify,
       "dNtpAccessGroupNoQuery": dNtpAccessGroupNoQuery,
       "dNtpAccessGroupNoPeer": dNtpAccessGroupNoPeer,
       "dNtpAccessGroupNoServe": dNtpAccessGroupNoServe,
       "dNtpAccessGroupNoTrust": dNtpAccessGroupNoTrust,
       "dNtpAccessGroupVersion": dNtpAccessGroupVersion,
       "dNtpAccessGroupRowStatus": dNtpAccessGroupRowStatus,
       "dNtpAccessInterfaceTable": dNtpAccessInterfaceTable,
       "dNtpAccessInterfaceEntry": dNtpAccessInterfaceEntry,
       "dNtpAccessInterfaceIfIndex": dNtpAccessInterfaceIfIndex,
       "dNtpAccessInterfaceEnabled": dNtpAccessInterfaceEnabled,
       "dNtpAuthenticationKeyTable": dNtpAuthenticationKeyTable,
       "dNtpAuthenticationKeyEntry": dNtpAuthenticationKeyEntry,
       "dNtpAuthenticationKeyId": dNtpAuthenticationKeyId,
       "dNtpAuthenticationKeyType": dNtpAuthenticationKeyType,
       "dNtpAuthenticationKeyValue": dNtpAuthenticationKeyValue,
       "dNtpAuthenticationKeyTrusted": dNtpAuthenticationKeyTrusted,
       "dNtpAuthenticationKeyStatus": dNtpAuthenticationKeyStatus,
       "dNtpCfgBroadcastClientTable": dNtpCfgBroadcastClientTable,
       "dNtpCfgBroadcastClientEntry": dNtpCfgBroadcastClientEntry,
       "dNtpCfgBroadcastClientIfIndex": dNtpCfgBroadcastClientIfIndex,
       "dNtpCfgBroadcastClientKeyId": dNtpCfgBroadcastClientKeyId,
       "dNtpCfgBroadcastClientStatus": dNtpCfgBroadcastClientStatus,
       "dNtpCfgBroadcastServerTable": dNtpCfgBroadcastServerTable,
       "dNtpCfgBroadcastServerEntry": dNtpCfgBroadcastServerEntry,
       "dNtpCfgBroadcastServerIfIndex": dNtpCfgBroadcastServerIfIndex,
       "dNtpCfgBroadcastServerVersion": dNtpCfgBroadcastServerVersion,
       "dNtpCfgBroadcastServerKeyId": dNtpCfgBroadcastServerKeyId,
       "dNtpCfgBroadcastServerStatus": dNtpCfgBroadcastServerStatus,
       "dNtpCfgMulticastClientTable": dNtpCfgMulticastClientTable,
       "dNtpCfgMulticastClientEntry": dNtpCfgMulticastClientEntry,
       "dNtpCfgMulticastClientIfIndex": dNtpCfgMulticastClientIfIndex,
       "dNtpCfgMulticastClientIpAddressType": dNtpCfgMulticastClientIpAddressType,
       "dNtpCfgMulticastClientIpAddress": dNtpCfgMulticastClientIpAddress,
       "dNtpCfgMulticastClientKeyId": dNtpCfgMulticastClientKeyId,
       "dNtpCfgMulticastClientStatus": dNtpCfgMulticastClientStatus,
       "dNtpCfgMulticastServerTable": dNtpCfgMulticastServerTable,
       "dNtpCfgMulticastServerEntry": dNtpCfgMulticastServerEntry,
       "dNtpCfgMulticastServerIfIndex": dNtpCfgMulticastServerIfIndex,
       "dNtpCfgMulticastServerIpAddressType": dNtpCfgMulticastServerIpAddressType,
       "dNtpCfgMulticastServerIpAddress": dNtpCfgMulticastServerIpAddress,
       "dNtpCfgMulticastServerVersion": dNtpCfgMulticastServerVersion,
       "dNtpCfgMulticastServerKeyId": dNtpCfgMulticastServerKeyId,
       "dNtpCfgMulticastServerTtl": dNtpCfgMulticastServerTtl,
       "dNtpCfgMulticastServerStatus": dNtpCfgMulticastServerStatus,
       "dNtpCfgPeerTable": dNtpCfgPeerTable,
       "dNtpCfgPeerEntry": dNtpCfgPeerEntry,
       "dNtpCfgPeerVrfName": dNtpCfgPeerVrfName,
       "dNtpCfgPeerIpAddressType": dNtpCfgPeerIpAddressType,
       "dNtpCfgPeerIpAddress": dNtpCfgPeerIpAddress,
       "dNtpCfgPeerVersion": dNtpCfgPeerVersion,
       "dNtpCfgPeerKeyId": dNtpCfgPeerKeyId,
       "dNtpCfgPeerPrefer": dNtpCfgPeerPrefer,
       "dNtpCfgPeerMinPoll": dNtpCfgPeerMinPoll,
       "dNtpCfgPeerMaxPoll": dNtpCfgPeerMaxPoll,
       "dNtpCfgPeerStatus": dNtpCfgPeerStatus,
       "dNtpCfgSrvTable": dNtpCfgSrvTable,
       "dNtpCfgSrvEntry": dNtpCfgSrvEntry,
       "dNtpCfgSrvVrfName": dNtpCfgSrvVrfName,
       "dNtpCfgSrvIpAddressType": dNtpCfgSrvIpAddressType,
       "dNtpCfgSrvIpAddress": dNtpCfgSrvIpAddress,
       "dNtpCfgSrvVersion": dNtpCfgSrvVersion,
       "dNtpCfgSrvKeyId": dNtpCfgSrvKeyId,
       "dNtpCfgSrvPrefer": dNtpCfgSrvPrefer,
       "dNtpCfgSrvMinPoll": dNtpCfgSrvMinPoll,
       "dNtpCfgSrvMaxPoll": dNtpCfgSrvMaxPoll,
       "dNtpCfgSrvStatus": dNtpCfgSrvStatus,
       "dNtpMIBConformance": dNtpMIBConformance,
       "dNtpCompliances": dNtpCompliances,
       "dNtpCompliance": dNtpCompliance,
       "dNtpGroups": dNtpGroups,
       "dNtpCtrlGroup": dNtpCtrlGroup,
       "dNtpAclGroup": dNtpAclGroup,
       "dNtpBroadcastGroup": dNtpBroadcastGroup,
       "dNtpMulticastGroup": dNtpMulticastGroup,
       "dNtpPeerCfgGroup": dNtpPeerCfgGroup,
       "dNtpSrvCfgGroup": dNtpSrvCfgGroup}
)
