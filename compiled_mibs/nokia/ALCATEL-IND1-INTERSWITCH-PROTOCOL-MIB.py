# SNMP MIB module (ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:28 2025
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

(aipAMAPTraps,
 aipGMAPTraps,
 softentIND1Aip) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "aipAMAPTraps",
    "aipGMAPTraps",
    "softentIND1Aip")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

alcatelIND1InterswitchProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1InterswitchProtocolMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBObjects = _AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1)
)
_AipGMAPconfig_ObjectIdentity = ObjectIdentity
aipGMAPconfig = _AipGMAPconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1)
)


class _AipGMAPstate_Type(Integer32):
    """Custom type aipGMAPstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AipGMAPstate_Type.__name__ = "Integer32"
_AipGMAPstate_Object = MibScalar
aipGMAPstate = _AipGMAPstate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 1),
    _AipGMAPstate_Type()
)
aipGMAPstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipGMAPstate.setStatus("current")


class _AipGMAPgaptime_Type(Integer32):
    """Custom type aipGMAPgaptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipGMAPgaptime_Type.__name__ = "Integer32"
_AipGMAPgaptime_Object = MibScalar
aipGMAPgaptime = _AipGMAPgaptime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 2),
    _AipGMAPgaptime_Type()
)
aipGMAPgaptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipGMAPgaptime.setStatus("current")


class _AipGMAPupdatetime_Type(Integer32):
    """Custom type aipGMAPupdatetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipGMAPupdatetime_Type.__name__ = "Integer32"
_AipGMAPupdatetime_Object = MibScalar
aipGMAPupdatetime = _AipGMAPupdatetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 3),
    _AipGMAPupdatetime_Type()
)
aipGMAPupdatetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipGMAPupdatetime.setStatus("current")


class _AipGMAPholdtime_Type(Integer32):
    """Custom type aipGMAPholdtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipGMAPholdtime_Type.__name__ = "Integer32"
_AipGMAPholdtime_Object = MibScalar
aipGMAPholdtime = _AipGMAPholdtime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 4),
    _AipGMAPholdtime_Type()
)
aipGMAPholdtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipGMAPholdtime.setStatus("current")


class _AipGMAPLastTrapReason_Type(Integer32):
    """Custom type aipGMAPLastTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authenticatedVlan", 1),
          ("conflictingBindingRule", 2),
          ("sameProtoDifferentVlansConflict", 3),
          ("sameVlanDifferentProtocolsConflict", 4),
          ("nonMobileVlan", 5),
          ("none", 6))
    )


_AipGMAPLastTrapReason_Type.__name__ = "Integer32"
_AipGMAPLastTrapReason_Object = MibScalar
aipGMAPLastTrapReason = _AipGMAPLastTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 5),
    _AipGMAPLastTrapReason_Type()
)
aipGMAPLastTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPLastTrapReason.setStatus("current")


class _AipGMAPLastTrapPort_Type(Integer32):
    """Custom type aipGMAPLastTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipGMAPLastTrapPort_Type.__name__ = "Integer32"
_AipGMAPLastTrapPort_Object = MibScalar
aipGMAPLastTrapPort = _AipGMAPLastTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 6),
    _AipGMAPLastTrapPort_Type()
)
aipGMAPLastTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPLastTrapPort.setStatus("current")
_AipGMAPLastTrapMac_Type = MacAddress
_AipGMAPLastTrapMac_Object = MibScalar
aipGMAPLastTrapMac = _AipGMAPLastTrapMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 7),
    _AipGMAPLastTrapMac_Type()
)
aipGMAPLastTrapMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPLastTrapMac.setStatus("current")


class _AipGMAPLastTrapProtocol_Type(Integer32):
    """Custom type aipGMAPLastTrapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipGMAPLastTrapProtocol_Type.__name__ = "Integer32"
_AipGMAPLastTrapProtocol_Object = MibScalar
aipGMAPLastTrapProtocol = _AipGMAPLastTrapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 8),
    _AipGMAPLastTrapProtocol_Type()
)
aipGMAPLastTrapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPLastTrapProtocol.setStatus("current")


class _AipGMAPLastTrapVlan_Type(Integer32):
    """Custom type aipGMAPLastTrapVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipGMAPLastTrapVlan_Type.__name__ = "Integer32"
_AipGMAPLastTrapVlan_Object = MibScalar
aipGMAPLastTrapVlan = _AipGMAPLastTrapVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 9),
    _AipGMAPLastTrapVlan_Type()
)
aipGMAPLastTrapVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPLastTrapVlan.setStatus("current")
_AipGMAPTable_Object = MibTable
aipGMAPTable = _AipGMAPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    aipGMAPTable.setStatus("current")
_AipGMAPTableEntry_Object = MibTableRow
aipGMAPTableEntry = _AipGMAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1)
)
aipGMAPTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPMacAddr"),
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPProtocol"),
)
if mibBuilder.loadTexts:
    aipGMAPTableEntry.setStatus("current")
_AipGMAPMacAddr_Type = MacAddress
_AipGMAPMacAddr_Object = MibTableColumn
aipGMAPMacAddr = _AipGMAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1, 1),
    _AipGMAPMacAddr_Type()
)
aipGMAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPMacAddr.setStatus("current")
_AipGMAPProtocol_Type = Unsigned32
_AipGMAPProtocol_Object = MibTableColumn
aipGMAPProtocol = _AipGMAPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1, 2),
    _AipGMAPProtocol_Type()
)
aipGMAPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPProtocol.setStatus("current")


class _AipGMAPVlan_Type(Integer32):
    """Custom type aipGMAPVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipGMAPVlan_Type.__name__ = "Integer32"
_AipGMAPVlan_Object = MibTableColumn
aipGMAPVlan = _AipGMAPVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1, 3),
    _AipGMAPVlan_Type()
)
aipGMAPVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPVlan.setStatus("current")
_AipGMAPSrcSwitch_Type = MacAddress
_AipGMAPSrcSwitch_Object = MibTableColumn
aipGMAPSrcSwitch = _AipGMAPSrcSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1, 4),
    _AipGMAPSrcSwitch_Type()
)
aipGMAPSrcSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPSrcSwitch.setStatus("current")


class _AipGMAPFlags_Type(OctetString):
    """Custom type aipGMAPFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AipGMAPFlags_Type.__name__ = "OctetString"
_AipGMAPFlags_Object = MibTableColumn
aipGMAPFlags = _AipGMAPFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1, 5),
    _AipGMAPFlags_Type()
)
aipGMAPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPFlags.setStatus("current")


class _AipGMAPTimeout_Type(Integer32):
    """Custom type aipGMAPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipGMAPTimeout_Type.__name__ = "Integer32"
_AipGMAPTimeout_Object = MibTableColumn
aipGMAPTimeout = _AipGMAPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 1, 10, 1, 6),
    _AipGMAPTimeout_Type()
)
aipGMAPTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipGMAPTimeout.setStatus("current")
_AipAMAPconfig_ObjectIdentity = ObjectIdentity
aipAMAPconfig = _AipAMAPconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2)
)


class _AipAMAPstate_Type(Integer32):
    """Custom type aipAMAPstate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AipAMAPstate_Type.__name__ = "Integer32"
_AipAMAPstate_Object = MibScalar
aipAMAPstate = _AipAMAPstate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 1),
    _AipAMAPstate_Type()
)
aipAMAPstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipAMAPstate.setStatus("current")


class _AipAMAPdisctime_Type(Integer32):
    """Custom type aipAMAPdisctime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipAMAPdisctime_Type.__name__ = "Integer32"
_AipAMAPdisctime_Object = MibScalar
aipAMAPdisctime = _AipAMAPdisctime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 2),
    _AipAMAPdisctime_Type()
)
aipAMAPdisctime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipAMAPdisctime.setStatus("current")


class _AipAMAPcommontime_Type(Integer32):
    """Custom type aipAMAPcommontime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AipAMAPcommontime_Type.__name__ = "Integer32"
_AipAMAPcommontime_Object = MibScalar
aipAMAPcommontime = _AipAMAPcommontime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 3),
    _AipAMAPcommontime_Type()
)
aipAMAPcommontime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipAMAPcommontime.setStatus("current")


class _AipAMAPLastTrapReason_Type(Integer32):
    """Custom type aipAMAPLastTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("change", 2),
          ("remove", 3),
          ("none", 4))
    )


_AipAMAPLastTrapReason_Type.__name__ = "Integer32"
_AipAMAPLastTrapReason_Object = MibScalar
aipAMAPLastTrapReason = _AipAMAPLastTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 4),
    _AipAMAPLastTrapReason_Type()
)
aipAMAPLastTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPLastTrapReason.setStatus("current")


class _AipAMAPLastTrapPort_Type(Integer32):
    """Custom type aipAMAPLastTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPLastTrapPort_Type.__name__ = "Integer32"
_AipAMAPLastTrapPort_Object = MibScalar
aipAMAPLastTrapPort = _AipAMAPLastTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 5),
    _AipAMAPLastTrapPort_Type()
)
aipAMAPLastTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPLastTrapPort.setStatus("current")
_AipAMAPportConnectionTable_Object = MibTable
aipAMAPportConnectionTable = _AipAMAPportConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    aipAMAPportConnectionTable.setStatus("current")
_AipAMAPportConnectionentry_Object = MibTableRow
aipAMAPportConnectionentry = _AipAMAPportConnectionentry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1)
)
aipAMAPportConnectionentry.setIndexNames(
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLocalConnectionIndex"),
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemMac"),
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemConnectionIndex"),
)
if mibBuilder.loadTexts:
    aipAMAPportConnectionentry.setStatus("current")


class _AipAMAPLocalConnectionIndex_Type(Integer32):
    """Custom type aipAMAPLocalConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPLocalConnectionIndex_Type.__name__ = "Integer32"
_AipAMAPLocalConnectionIndex_Object = MibTableColumn
aipAMAPLocalConnectionIndex = _AipAMAPLocalConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 1),
    _AipAMAPLocalConnectionIndex_Type()
)
aipAMAPLocalConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPLocalConnectionIndex.setStatus("current")
_AipAMAPRemMac_Type = MacAddress
_AipAMAPRemMac_Object = MibTableColumn
aipAMAPRemMac = _AipAMAPRemMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 2),
    _AipAMAPRemMac_Type()
)
aipAMAPRemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemMac.setStatus("current")


class _AipAMAPRemConnectionIndex_Type(Integer32):
    """Custom type aipAMAPRemConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPRemConnectionIndex_Type.__name__ = "Integer32"
_AipAMAPRemConnectionIndex_Object = MibTableColumn
aipAMAPRemConnectionIndex = _AipAMAPRemConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 3),
    _AipAMAPRemConnectionIndex_Type()
)
aipAMAPRemConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemConnectionIndex.setStatus("current")


class _AipAMAPRemVlan_Type(Integer32):
    """Custom type aipAMAPRemVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPRemVlan_Type.__name__ = "Integer32"
_AipAMAPRemVlan_Object = MibTableColumn
aipAMAPRemVlan = _AipAMAPRemVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 4),
    _AipAMAPRemVlan_Type()
)
aipAMAPRemVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemVlan.setStatus("current")


class _AipAMAPRemHostname_Type(DisplayString):
    """Custom type aipAMAPRemHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AipAMAPRemHostname_Type.__name__ = "DisplayString"
_AipAMAPRemHostname_Object = MibTableColumn
aipAMAPRemHostname = _AipAMAPRemHostname_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 5),
    _AipAMAPRemHostname_Type()
)
aipAMAPRemHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemHostname.setStatus("current")
_AipAMAPLocalIfindex_Type = InterfaceIndex
_AipAMAPLocalIfindex_Object = MibTableColumn
aipAMAPLocalIfindex = _AipAMAPLocalIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 6),
    _AipAMAPLocalIfindex_Type()
)
aipAMAPLocalIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPLocalIfindex.setStatus("current")


class _AipAMAPLocalSlot_Type(Integer32):
    """Custom type aipAMAPLocalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPLocalSlot_Type.__name__ = "Integer32"
_AipAMAPLocalSlot_Object = MibTableColumn
aipAMAPLocalSlot = _AipAMAPLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 7),
    _AipAMAPLocalSlot_Type()
)
aipAMAPLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPLocalSlot.setStatus("current")


class _AipAMAPLocalPort_Type(Integer32):
    """Custom type aipAMAPLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPLocalPort_Type.__name__ = "Integer32"
_AipAMAPLocalPort_Object = MibTableColumn
aipAMAPLocalPort = _AipAMAPLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 8),
    _AipAMAPLocalPort_Type()
)
aipAMAPLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPLocalPort.setStatus("current")


class _AipAMAPRemSlot_Type(Integer32):
    """Custom type aipAMAPRemSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPRemSlot_Type.__name__ = "Integer32"
_AipAMAPRemSlot_Object = MibTableColumn
aipAMAPRemSlot = _AipAMAPRemSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 9),
    _AipAMAPRemSlot_Type()
)
aipAMAPRemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemSlot.setStatus("current")


class _AipAMAPRemPort_Type(Integer32):
    """Custom type aipAMAPRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AipAMAPRemPort_Type.__name__ = "Integer32"
_AipAMAPRemPort_Object = MibTableColumn
aipAMAPRemPort = _AipAMAPRemPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 10),
    _AipAMAPRemPort_Type()
)
aipAMAPRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemPort.setStatus("current")


class _AipAMAPRemDeviceType_Type(Integer32):
    """Custom type aipAMAPRemDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              20,
              21,
              22,
              23,
              24,
              30,
              31,
              32,
              34,
              35,
              36,
              40,
              41,
              42,
              43,
              44,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              60,
              61,
              62,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              227,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknownDevice", 1),
          ("omniSwitch7700", 2),
          ("omniSwitch7800", 3),
          ("omniSwitch9600", 4),
          ("omniSwitch9700", 5),
          ("omniSwitch9800", 6),
          ("omniSwitch9600E", 7),
          ("omniSwitch9700E", 8),
          ("omniSwitch9800E", 9),
          ("omniSwitch8800", 10),
          ("omniSwitch6624", 20),
          ("omniSwitch6648", 21),
          ("omniSwitch6624Fiber", 22),
          ("omniSwitch6624Ver2", 23),
          ("omniSwitch6648Ver2", 24),
          ("omniSwitch6824", 30),
          ("omniSwitch6848", 31),
          ("omniSwitch6824Fiber", 32),
          ("omniSwitch6850-24", 34),
          ("omniSwitch6850-48", 35),
          ("omniSwitch6850-24Fiber", 36),
          ("omniSwitch5slotXOS", 40),
          ("omniSwitch9slotXOS", 41),
          ("omniSwitchRouterXOS", 42),
          ("omniAccess408", 43),
          ("omniAccess512", 44),
          ("omniStack2032", 50),
          ("omniStack4024", 51),
          ("omniStack5024", 52),
          ("omniStack6024", 53),
          ("omniStack6048", 54),
          ("omniStack6124", 55),
          ("omniStack6148", 56),
          ("omniStack8008", 57),
          ("omniAccess210", 60),
          ("omniAccess250", 61),
          ("omniAccess280", 62),
          ("ipPhone", 70),
          ("omniPCX4400", 71),
          ("omniSwitch6855-14", 72),
          ("omniSwitch6855-U10", 73),
          ("omniSwitch6855-24", 74),
          ("omniSwitch6855-U24", 75),
          ("omniSwitch6424", 76),
          ("omniSwitch6448", 77),
          ("omniSwitch6424Fiber", 78),
          ("omniSwitch6855-U24X", 79),
          ("omniSwitch62508ME", 80),
          ("omniSwitch625024ME", 81),
          ("omniSwitch625024SMB", 82),
          ("omniSwitch6200-MIXED-STACK", 214),
          ("omniSwitch6224", 215),
          ("omniSwitch6224P", 216),
          ("omniSwitch6248", 217),
          ("omniSwitch6248P", 218),
          ("omniSwitch6224-DC", 219),
          ("omniSwitch6248-DC", 220),
          ("omniSwitch6212", 221),
          ("omniSwitch6212P", 222),
          ("omniSwitch6224U", 223),
          ("omniSwitch6324", 227),
          ("omniAccess5000", 249),
          ("omniAccess4324", 250),
          ("omniAccess4308", 251),
          ("omniAccess6000", 252),
          ("omniAccessAP60", 253),
          ("omniAccessAP61", 254),
          ("omniAccessAP70", 255))
    )


_AipAMAPRemDeviceType_Type.__name__ = "Integer32"
_AipAMAPRemDeviceType_Object = MibTableColumn
aipAMAPRemDeviceType = _AipAMAPRemDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 11),
    _AipAMAPRemDeviceType_Type()
)
aipAMAPRemDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemDeviceType.setStatus("current")


class _AipAMAPRemDevModelName_Type(DisplayString):
    """Custom type aipAMAPRemDevModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AipAMAPRemDevModelName_Type.__name__ = "DisplayString"
_AipAMAPRemDevModelName_Object = MibTableColumn
aipAMAPRemDevModelName = _AipAMAPRemDevModelName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 12),
    _AipAMAPRemDevModelName_Type()
)
aipAMAPRemDevModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemDevModelName.setStatus("current")


class _AipAMAPRemProductType_Type(Integer32):
    """Custom type aipAMAPRemProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("chassis", 1),
          ("stack", 2),
          ("accessPoint", 3),
          ("pcx", 4),
          ("ipPhone", 5),
          ("standAlone", 6))
    )


_AipAMAPRemProductType_Type.__name__ = "Integer32"
_AipAMAPRemProductType_Object = MibTableColumn
aipAMAPRemProductType = _AipAMAPRemProductType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 6, 1, 13),
    _AipAMAPRemProductType_Type()
)
aipAMAPRemProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPRemProductType.setStatus("current")
_AipAMAPhostsTable_Object = MibTable
aipAMAPhostsTable = _AipAMAPhostsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    aipAMAPhostsTable.setStatus("current")
_AipAMAPHostentry_Object = MibTableRow
aipAMAPHostentry = _AipAMAPHostentry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 7, 1)
)
aipAMAPHostentry.setIndexNames(
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPHostMac"),
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPIpAddr"),
)
if mibBuilder.loadTexts:
    aipAMAPHostentry.setStatus("current")
_AipAMAPHostMac_Type = MacAddress
_AipAMAPHostMac_Object = MibTableColumn
aipAMAPHostMac = _AipAMAPHostMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 7, 1, 1),
    _AipAMAPHostMac_Type()
)
aipAMAPHostMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPHostMac.setStatus("current")
_AipAMAPIpAddr_Type = IpAddress
_AipAMAPIpAddr_Object = MibTableColumn
aipAMAPIpAddr = _AipAMAPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 7, 1, 2),
    _AipAMAPIpAddr_Type()
)
aipAMAPIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipAMAPIpAddr.setStatus("current")


class _AipAMAPVoiceVlan_Type(Integer32):
    """Custom type aipAMAPVoiceVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AipAMAPVoiceVlan_Type.__name__ = "Integer32"
_AipAMAPVoiceVlan_Object = MibScalar
aipAMAPVoiceVlan = _AipAMAPVoiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 2, 8),
    _AipAMAPVoiceVlan_Type()
)
aipAMAPVoiceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipAMAPVoiceVlan.setStatus("current")
_AipLLDPConfig_ObjectIdentity = ObjectIdentity
aipLLDPConfig = _AipLLDPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 3)
)
_AipLLDPConfigManAddrTable_Object = MibTable
aipLLDPConfigManAddrTable = _AipLLDPConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrTable.setStatus("current")
_AipLLDPConfigManAddrEntry_Object = MibTableRow
aipLLDPConfigManAddrEntry = _AipLLDPConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 3, 1, 1)
)
aipLLDPConfigManAddrEntry.setIndexNames(
    (0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrPortNum"),
)
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrEntry.setStatus("current")
_AipLLDPConfigManAddrPortNum_Type = InterfaceIndex
_AipLLDPConfigManAddrPortNum_Object = MibTableColumn
aipLLDPConfigManAddrPortNum = _AipLLDPConfigManAddrPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 3, 1, 1, 1),
    _AipLLDPConfigManAddrPortNum_Type()
)
aipLLDPConfigManAddrPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrPortNum.setStatus("current")


class _AipLLDPConfigManAddrTlvTxEnable_Type(TruthValue):
    """Custom type aipLLDPConfigManAddrTlvTxEnable based on TruthValue"""
    defaultValue = 2


_AipLLDPConfigManAddrTlvTxEnable_Type.__name__ = "TruthValue"
_AipLLDPConfigManAddrTlvTxEnable_Object = MibTableColumn
aipLLDPConfigManAddrTlvTxEnable = _AipLLDPConfigManAddrTlvTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 1, 3, 1, 1, 2),
    _AipLLDPConfigManAddrTlvTxEnable_Type()
)
aipLLDPConfigManAddrTlvTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrTlvTxEnable.setStatus("current")
_AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBConformance = _AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2)
)
_AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBGroups = _AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2, 1)
)
_AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBCompliances = _AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2, 2)
)

# Managed Objects groups

aipGMAPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2, 1, 1)
)
aipGMAPConfGroup.setObjects(
      *(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPstate"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPgaptime"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPupdatetime"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPholdtime"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapReason"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapPort"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapMac"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapProtocol"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapVlan"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPMacAddr"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPProtocol"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPVlan"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPSrcSwitch"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPFlags"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPTimeout"))
)
if mibBuilder.loadTexts:
    aipGMAPConfGroup.setStatus("current")

aipAMAPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2, 1, 2)
)
aipAMAPConfGroup.setObjects(
      *(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPstate"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPdisctime"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPcommontime"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLastTrapReason"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLastTrapPort"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLocalConnectionIndex"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemMac"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemConnectionIndex"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemVlan"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemHostname"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPVoiceVlan"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLocalIfindex"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLocalSlot"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLocalPort"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemSlot"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPRemPort"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPHostMac"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPIpAddr"))
)
if mibBuilder.loadTexts:
    aipAMAPConfGroup.setStatus("current")


# Notification objects

aipAMAPStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 1, 0, 1)
)
aipAMAPStatusTrap.setObjects(
      *(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLastTrapReason"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPLastTrapPort"))
)
if mibBuilder.loadTexts:
    aipAMAPStatusTrap.setStatus(
        "current"
    )

aipGMAPConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 2, 0, 1)
)
aipGMAPConflictTrap.setObjects(
      *(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapReason"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapPort"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapMac"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapProtocol"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPLastTrapVlan"))
)
if mibBuilder.loadTexts:
    aipGMAPConflictTrap.setStatus(
        "current"
    )


# Notifications groups

aipNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2, 1, 3)
)
aipNotificationGroup.setObjects(
      *(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPStatusTrap"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPConflictTrap"))
)
if mibBuilder.loadTexts:
    aipNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1InterswitchProtocolMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 9, 1, 2, 2, 1)
)
alcatelIND1InterswitchProtocolMIBCompliance.setObjects(
      *(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipGMAPConfGroup"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipAMAPConfGroup"),
        ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipNotificationGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1InterswitchProtocolMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB",
    **{"alcatelIND1InterswitchProtocolMIB": alcatelIND1InterswitchProtocolMIB,
       "alcatelIND1InterswitchProtocolMIBObjects": alcatelIND1InterswitchProtocolMIBObjects,
       "aipGMAPconfig": aipGMAPconfig,
       "aipGMAPstate": aipGMAPstate,
       "aipGMAPgaptime": aipGMAPgaptime,
       "aipGMAPupdatetime": aipGMAPupdatetime,
       "aipGMAPholdtime": aipGMAPholdtime,
       "aipGMAPLastTrapReason": aipGMAPLastTrapReason,
       "aipGMAPLastTrapPort": aipGMAPLastTrapPort,
       "aipGMAPLastTrapMac": aipGMAPLastTrapMac,
       "aipGMAPLastTrapProtocol": aipGMAPLastTrapProtocol,
       "aipGMAPLastTrapVlan": aipGMAPLastTrapVlan,
       "aipGMAPTable": aipGMAPTable,
       "aipGMAPTableEntry": aipGMAPTableEntry,
       "aipGMAPMacAddr": aipGMAPMacAddr,
       "aipGMAPProtocol": aipGMAPProtocol,
       "aipGMAPVlan": aipGMAPVlan,
       "aipGMAPSrcSwitch": aipGMAPSrcSwitch,
       "aipGMAPFlags": aipGMAPFlags,
       "aipGMAPTimeout": aipGMAPTimeout,
       "aipAMAPconfig": aipAMAPconfig,
       "aipAMAPstate": aipAMAPstate,
       "aipAMAPdisctime": aipAMAPdisctime,
       "aipAMAPcommontime": aipAMAPcommontime,
       "aipAMAPLastTrapReason": aipAMAPLastTrapReason,
       "aipAMAPLastTrapPort": aipAMAPLastTrapPort,
       "aipAMAPportConnectionTable": aipAMAPportConnectionTable,
       "aipAMAPportConnectionentry": aipAMAPportConnectionentry,
       "aipAMAPLocalConnectionIndex": aipAMAPLocalConnectionIndex,
       "aipAMAPRemMac": aipAMAPRemMac,
       "aipAMAPRemConnectionIndex": aipAMAPRemConnectionIndex,
       "aipAMAPRemVlan": aipAMAPRemVlan,
       "aipAMAPRemHostname": aipAMAPRemHostname,
       "aipAMAPLocalIfindex": aipAMAPLocalIfindex,
       "aipAMAPLocalSlot": aipAMAPLocalSlot,
       "aipAMAPLocalPort": aipAMAPLocalPort,
       "aipAMAPRemSlot": aipAMAPRemSlot,
       "aipAMAPRemPort": aipAMAPRemPort,
       "aipAMAPRemDeviceType": aipAMAPRemDeviceType,
       "aipAMAPRemDevModelName": aipAMAPRemDevModelName,
       "aipAMAPRemProductType": aipAMAPRemProductType,
       "aipAMAPhostsTable": aipAMAPhostsTable,
       "aipAMAPHostentry": aipAMAPHostentry,
       "aipAMAPHostMac": aipAMAPHostMac,
       "aipAMAPIpAddr": aipAMAPIpAddr,
       "aipAMAPVoiceVlan": aipAMAPVoiceVlan,
       "aipLLDPConfig": aipLLDPConfig,
       "aipLLDPConfigManAddrTable": aipLLDPConfigManAddrTable,
       "aipLLDPConfigManAddrEntry": aipLLDPConfigManAddrEntry,
       "aipLLDPConfigManAddrPortNum": aipLLDPConfigManAddrPortNum,
       "aipLLDPConfigManAddrTlvTxEnable": aipLLDPConfigManAddrTlvTxEnable,
       "alcatelIND1InterswitchProtocolMIBConformance": alcatelIND1InterswitchProtocolMIBConformance,
       "alcatelIND1InterswitchProtocolMIBGroups": alcatelIND1InterswitchProtocolMIBGroups,
       "aipGMAPConfGroup": aipGMAPConfGroup,
       "aipAMAPConfGroup": aipAMAPConfGroup,
       "aipNotificationGroup": aipNotificationGroup,
       "alcatelIND1InterswitchProtocolMIBCompliances": alcatelIND1InterswitchProtocolMIBCompliances,
       "alcatelIND1InterswitchProtocolMIBCompliance": alcatelIND1InterswitchProtocolMIBCompliance,
       "aipAMAPStatusTrap": aipAMAPStatusTrap,
       "aipGMAPConflictTrap": aipGMAPConflictTrap}
)
