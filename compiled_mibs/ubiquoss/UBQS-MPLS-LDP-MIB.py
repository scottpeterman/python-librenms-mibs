# SNMP MIB module (UBQS-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-MPLS-LDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:23 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsLSPID,
 MplsOwner,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex,
 TeHopAddressType,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLSPID",
    "MplsOwner",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex",
    "TeHopAddressType",
    "mplsStdMIB")

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
 IpAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "IpAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(ubiMplsGroupMIB,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMplsGroupMIB")


# MODULE-IDENTITY

ubiLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiLdpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiLdpMIBNotificationPrefix = _UbiLdpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 0)
)
_UbiLdpMIBObjects_ObjectIdentity = ObjectIdentity
ubiLdpMIBObjects = _UbiLdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1)
)
_UbiLdpConfig_ObjectIdentity = ObjectIdentity
ubiLdpConfig = _UbiLdpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1)
)


class _UbiLdpEnable_Type(TruthValue):
    """Custom type ubiLdpEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpEnable_Type.__name__ = "TruthValue"
_UbiLdpEnable_Object = MibScalar
ubiLdpEnable = _UbiLdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 1),
    _UbiLdpEnable_Type()
)
ubiLdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpEnable.setStatus("current")
_UbiLdpRouterId_Type = IpAddress
_UbiLdpRouterId_Object = MibScalar
ubiLdpRouterId = _UbiLdpRouterId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 2),
    _UbiLdpRouterId_Type()
)
ubiLdpRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpRouterId.setStatus("current")


class _UbiLdpFailoverCfmEnable_Type(TruthValue):
    """Custom type ubiLdpFailoverCfmEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpFailoverCfmEnable_Type.__name__ = "TruthValue"
_UbiLdpFailoverCfmEnable_Object = MibScalar
ubiLdpFailoverCfmEnable = _UbiLdpFailoverCfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 3),
    _UbiLdpFailoverCfmEnable_Type()
)
ubiLdpFailoverCfmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpFailoverCfmEnable.setStatus("current")


class _UbiLdpTargetedPeerHelloReceiptEnable_Type(TruthValue):
    """Custom type ubiLdpTargetedPeerHelloReceiptEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpTargetedPeerHelloReceiptEnable_Type.__name__ = "TruthValue"
_UbiLdpTargetedPeerHelloReceiptEnable_Object = MibScalar
ubiLdpTargetedPeerHelloReceiptEnable = _UbiLdpTargetedPeerHelloReceiptEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 4),
    _UbiLdpTargetedPeerHelloReceiptEnable_Type()
)
ubiLdpTargetedPeerHelloReceiptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpTargetedPeerHelloReceiptEnable.setStatus("current")


class _UbiLdpAcUpSignalEnable_Type(TruthValue):
    """Custom type ubiLdpAcUpSignalEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpAcUpSignalEnable_Type.__name__ = "TruthValue"
_UbiLdpAcUpSignalEnable_Object = MibScalar
ubiLdpAcUpSignalEnable = _UbiLdpAcUpSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 5),
    _UbiLdpAcUpSignalEnable_Type()
)
ubiLdpAcUpSignalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpAcUpSignalEnable.setStatus("current")


class _UbiLdpExceedInitSessionNotiEnable_Type(TruthValue):
    """Custom type ubiLdpExceedInitSessionNotiEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpExceedInitSessionNotiEnable_Type.__name__ = "TruthValue"
_UbiLdpExceedInitSessionNotiEnable_Object = MibScalar
ubiLdpExceedInitSessionNotiEnable = _UbiLdpExceedInitSessionNotiEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 6),
    _UbiLdpExceedInitSessionNotiEnable_Type()
)
ubiLdpExceedInitSessionNotiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpExceedInitSessionNotiEnable.setStatus("current")


class _UbiLdpPathVectorLimitMismatchNotiEnable_Type(TruthValue):
    """Custom type ubiLdpPathVectorLimitMismatchNotiEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpPathVectorLimitMismatchNotiEnable_Type.__name__ = "TruthValue"
_UbiLdpPathVectorLimitMismatchNotiEnable_Object = MibScalar
ubiLdpPathVectorLimitMismatchNotiEnable = _UbiLdpPathVectorLimitMismatchNotiEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 7),
    _UbiLdpPathVectorLimitMismatchNotiEnable_Type()
)
ubiLdpPathVectorLimitMismatchNotiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpPathVectorLimitMismatchNotiEnable.setStatus("current")


class _UbiLdpLdpSessionUpDownNotiEnable_Type(TruthValue):
    """Custom type ubiLdpLdpSessionUpDownNotiEnable based on TruthValue"""
    defaultValue = 2


_UbiLdpLdpSessionUpDownNotiEnable_Type.__name__ = "TruthValue"
_UbiLdpLdpSessionUpDownNotiEnable_Object = MibScalar
ubiLdpLdpSessionUpDownNotiEnable = _UbiLdpLdpSessionUpDownNotiEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 1, 8),
    _UbiLdpLdpSessionUpDownNotiEnable_Type()
)
ubiLdpLdpSessionUpDownNotiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpLdpSessionUpDownNotiEnable.setStatus("current")
_UbiLdpInterfaceTable_Object = MibTable
ubiLdpInterfaceTable = _UbiLdpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ubiLdpInterfaceTable.setStatus("current")
_UbiLdpInterfaceEntry_Object = MibTableRow
ubiLdpInterfaceEntry = _UbiLdpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 2, 1)
)
ubiLdpInterfaceEntry.setIndexNames(
    (0, "UBQS-MPLS-LDP-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ubiLdpInterfaceEntry.setStatus("current")


class _UbiLdpIfEnable_Type(Integer32):
    """Custom type ubiLdpIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("both", 3))
    )


_UbiLdpIfEnable_Type.__name__ = "Integer32"
_UbiLdpIfEnable_Object = MibTableColumn
ubiLdpIfEnable = _UbiLdpIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 1, 2, 1, 1),
    _UbiLdpIfEnable_Type()
)
ubiLdpIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLdpIfEnable.setStatus("current")
_UbiLdpMIBConformance_ObjectIdentity = ObjectIdentity
ubiLdpMIBConformance = _UbiLdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 2)
)
_UbiLdpMIBCompliances_ObjectIdentity = ObjectIdentity
ubiLdpMIBCompliances = _UbiLdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 2, 1)
)
_UbiLdpMIBGroups_ObjectIdentity = ObjectIdentity
ubiLdpMIBGroups = _UbiLdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 2, 2)
)

# Managed Objects groups

ubiLdpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 2, 2, 1)
)
ubiLdpMIBGroup.setObjects(
      *(("UBQS-MPLS-LDP-MIB", "ubiLdpEnable"),
        ("UBQS-MPLS-LDP-MIB", "ubiLdpRouterId"),
        ("UBQS-MPLS-LDP-MIB", "ubiLdpFailoverCfmEnable"),
        ("UBQS-MPLS-LDP-MIB", "ubiLdpTargetedPeerHelloReceiptEnable"),
        ("UBQS-MPLS-LDP-MIB", "ubiLdpAcUpSignalEnable"),
        ("UBQS-MPLS-LDP-MIB", "ubiLdpIfEnable"))
)
if mibBuilder.loadTexts:
    ubiLdpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubiLdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 24, 3, 2, 1, 1)
)
ubiLdpMIBCompliance.setObjects(
      *(("UBQS-MPLS-LDP-MIB", "ubiLdpMIBGroup"),
        ("UBQS-MPLS-LDP-MIB", "ubiLdpMIBGroup"))
)
if mibBuilder.loadTexts:
    ubiLdpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-MPLS-LDP-MIB",
    **{"ubiLdpMIB": ubiLdpMIB,
       "ubiLdpMIBNotificationPrefix": ubiLdpMIBNotificationPrefix,
       "ubiLdpMIBObjects": ubiLdpMIBObjects,
       "ubiLdpConfig": ubiLdpConfig,
       "ubiLdpEnable": ubiLdpEnable,
       "ubiLdpRouterId": ubiLdpRouterId,
       "ubiLdpFailoverCfmEnable": ubiLdpFailoverCfmEnable,
       "ubiLdpTargetedPeerHelloReceiptEnable": ubiLdpTargetedPeerHelloReceiptEnable,
       "ubiLdpAcUpSignalEnable": ubiLdpAcUpSignalEnable,
       "ubiLdpExceedInitSessionNotiEnable": ubiLdpExceedInitSessionNotiEnable,
       "ubiLdpPathVectorLimitMismatchNotiEnable": ubiLdpPathVectorLimitMismatchNotiEnable,
       "ubiLdpLdpSessionUpDownNotiEnable": ubiLdpLdpSessionUpDownNotiEnable,
       "ubiLdpInterfaceTable": ubiLdpInterfaceTable,
       "ubiLdpInterfaceEntry": ubiLdpInterfaceEntry,
       "ubiLdpIfEnable": ubiLdpIfEnable,
       "ubiLdpMIBConformance": ubiLdpMIBConformance,
       "ubiLdpMIBCompliances": ubiLdpMIBCompliances,
       "ubiLdpMIBCompliance": ubiLdpMIBCompliance,
       "ubiLdpMIBGroups": ubiLdpMIBGroups,
       "ubiLdpMIBGroup": ubiLdpMIBGroup}
)
