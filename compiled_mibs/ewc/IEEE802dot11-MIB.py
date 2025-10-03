# SNMP MIB module (IEEE802dot11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\IEEE802dot11-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:56 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ieee802dot11 = ModuleIdentity(
    (1, 2, 840, 10036)
)


# Types definitions



class WEPKeytype(OctetString):
    """Custom type WEPKeytype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Member_body_ObjectIdentity = ObjectIdentity
member_body = _Member_body_ObjectIdentity(
    (1, 2)
)
_Us_ObjectIdentity = ObjectIdentity
us = _Us_ObjectIdentity(
    (1, 2, 840)
)
_Dot11smt_ObjectIdentity = ObjectIdentity
dot11smt = _Dot11smt_ObjectIdentity(
    (1, 2, 840, 10036, 1)
)
_Dot11StationConfigTable_Object = MibTable
dot11StationConfigTable = _Dot11StationConfigTable_Object(
    (1, 2, 840, 10036, 1, 1)
)
if mibBuilder.loadTexts:
    dot11StationConfigTable.setStatus("current")
_Dot11StationConfigEntry_Object = MibTableRow
dot11StationConfigEntry = _Dot11StationConfigEntry_Object(
    (1, 2, 840, 10036, 1, 1, 1)
)
dot11StationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11StationConfigEntry.setStatus("current")
_Dot11StationID_Type = MacAddress
_Dot11StationID_Object = MibTableColumn
dot11StationID = _Dot11StationID_Object(
    (1, 2, 840, 10036, 1, 1, 1, 1),
    _Dot11StationID_Type()
)
dot11StationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationID.setStatus("deprecated")


class _Dot11MediumOccupancyLimit_Type(Integer32):
    """Custom type dot11MediumOccupancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dot11MediumOccupancyLimit_Type.__name__ = "Integer32"
_Dot11MediumOccupancyLimit_Object = MibTableColumn
dot11MediumOccupancyLimit = _Dot11MediumOccupancyLimit_Object(
    (1, 2, 840, 10036, 1, 1, 1, 2),
    _Dot11MediumOccupancyLimit_Type()
)
dot11MediumOccupancyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MediumOccupancyLimit.setStatus("current")
_Dot11CFPollable_Type = TruthValue
_Dot11CFPollable_Object = MibTableColumn
dot11CFPollable = _Dot11CFPollable_Object(
    (1, 2, 840, 10036, 1, 1, 1, 3),
    _Dot11CFPollable_Type()
)
dot11CFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CFPollable.setStatus("current")


class _Dot11CFPPeriod_Type(Integer32):
    """Custom type dot11CFPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11CFPPeriod_Type.__name__ = "Integer32"
_Dot11CFPPeriod_Object = MibTableColumn
dot11CFPPeriod = _Dot11CFPPeriod_Object(
    (1, 2, 840, 10036, 1, 1, 1, 4),
    _Dot11CFPPeriod_Type()
)
dot11CFPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CFPPeriod.setStatus("current")


class _Dot11CFPMaxDuration_Type(Integer32):
    """Custom type dot11CFPMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11CFPMaxDuration_Type.__name__ = "Integer32"
_Dot11CFPMaxDuration_Object = MibTableColumn
dot11CFPMaxDuration = _Dot11CFPMaxDuration_Object(
    (1, 2, 840, 10036, 1, 1, 1, 5),
    _Dot11CFPMaxDuration_Type()
)
dot11CFPMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CFPMaxDuration.setStatus("current")


class _Dot11AuthenticationResponseTimeOut_Type(Unsigned32):
    """Custom type dot11AuthenticationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11AuthenticationResponseTimeOut_Type.__name__ = "Unsigned32"
_Dot11AuthenticationResponseTimeOut_Object = MibTableColumn
dot11AuthenticationResponseTimeOut = _Dot11AuthenticationResponseTimeOut_Object(
    (1, 2, 840, 10036, 1, 1, 1, 6),
    _Dot11AuthenticationResponseTimeOut_Type()
)
dot11AuthenticationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationResponseTimeOut.setStatus("current")
_Dot11PrivacyOptionImplemented_Type = TruthValue
_Dot11PrivacyOptionImplemented_Object = MibTableColumn
dot11PrivacyOptionImplemented = _Dot11PrivacyOptionImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 7),
    _Dot11PrivacyOptionImplemented_Type()
)
dot11PrivacyOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PrivacyOptionImplemented.setStatus("current")


class _Dot11PowerManagementMode_Type(Integer32):
    """Custom type dot11PowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_Dot11PowerManagementMode_Type.__name__ = "Integer32"
_Dot11PowerManagementMode_Object = MibTableColumn
dot11PowerManagementMode = _Dot11PowerManagementMode_Object(
    (1, 2, 840, 10036, 1, 1, 1, 8),
    _Dot11PowerManagementMode_Type()
)
dot11PowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PowerManagementMode.setStatus("current")


class _Dot11DesiredSSID_Type(OctetString):
    """Custom type dot11DesiredSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11DesiredSSID_Type.__name__ = "OctetString"
_Dot11DesiredSSID_Object = MibTableColumn
dot11DesiredSSID = _Dot11DesiredSSID_Object(
    (1, 2, 840, 10036, 1, 1, 1, 9),
    _Dot11DesiredSSID_Type()
)
dot11DesiredSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredSSID.setStatus("current")


class _Dot11DesiredBSSType_Type(Integer32):
    """Custom type dot11DesiredBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infrastructure", 1),
          ("independent", 2),
          ("any", 3))
    )


_Dot11DesiredBSSType_Type.__name__ = "Integer32"
_Dot11DesiredBSSType_Object = MibTableColumn
dot11DesiredBSSType = _Dot11DesiredBSSType_Object(
    (1, 2, 840, 10036, 1, 1, 1, 10),
    _Dot11DesiredBSSType_Type()
)
dot11DesiredBSSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredBSSType.setStatus("current")


class _Dot11OperationalRateSet_Type(OctetString):
    """Custom type dot11OperationalRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Dot11OperationalRateSet_Type.__name__ = "OctetString"
_Dot11OperationalRateSet_Object = MibTableColumn
dot11OperationalRateSet = _Dot11OperationalRateSet_Object(
    (1, 2, 840, 10036, 1, 1, 1, 11),
    _Dot11OperationalRateSet_Type()
)
dot11OperationalRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11OperationalRateSet.setStatus("current")


class _Dot11BeaconPeriod_Type(Integer32):
    """Custom type dot11BeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11BeaconPeriod_Type.__name__ = "Integer32"
_Dot11BeaconPeriod_Object = MibTableColumn
dot11BeaconPeriod = _Dot11BeaconPeriod_Object(
    (1, 2, 840, 10036, 1, 1, 1, 12),
    _Dot11BeaconPeriod_Type()
)
dot11BeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BeaconPeriod.setStatus("current")


class _Dot11DTIMPeriod_Type(Integer32):
    """Custom type dot11DTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11DTIMPeriod_Type.__name__ = "Integer32"
_Dot11DTIMPeriod_Object = MibTableColumn
dot11DTIMPeriod = _Dot11DTIMPeriod_Object(
    (1, 2, 840, 10036, 1, 1, 1, 13),
    _Dot11DTIMPeriod_Type()
)
dot11DTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DTIMPeriod.setStatus("current")


class _Dot11AssociationResponseTimeOut_Type(Unsigned32):
    """Custom type dot11AssociationResponseTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11AssociationResponseTimeOut_Type.__name__ = "Unsigned32"
_Dot11AssociationResponseTimeOut_Object = MibTableColumn
dot11AssociationResponseTimeOut = _Dot11AssociationResponseTimeOut_Object(
    (1, 2, 840, 10036, 1, 1, 1, 14),
    _Dot11AssociationResponseTimeOut_Type()
)
dot11AssociationResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AssociationResponseTimeOut.setStatus("current")


class _Dot11DisassociateReason_Type(Integer32):
    """Custom type dot11DisassociateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11DisassociateReason_Type.__name__ = "Integer32"
_Dot11DisassociateReason_Object = MibTableColumn
dot11DisassociateReason = _Dot11DisassociateReason_Object(
    (1, 2, 840, 10036, 1, 1, 1, 15),
    _Dot11DisassociateReason_Type()
)
dot11DisassociateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DisassociateReason.setStatus("current")
_Dot11DisassociateStation_Type = MacAddress
_Dot11DisassociateStation_Object = MibTableColumn
dot11DisassociateStation = _Dot11DisassociateStation_Object(
    (1, 2, 840, 10036, 1, 1, 1, 16),
    _Dot11DisassociateStation_Type()
)
dot11DisassociateStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DisassociateStation.setStatus("current")


class _Dot11DeauthenticateReason_Type(Integer32):
    """Custom type dot11DeauthenticateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11DeauthenticateReason_Type.__name__ = "Integer32"
_Dot11DeauthenticateReason_Object = MibTableColumn
dot11DeauthenticateReason = _Dot11DeauthenticateReason_Object(
    (1, 2, 840, 10036, 1, 1, 1, 17),
    _Dot11DeauthenticateReason_Type()
)
dot11DeauthenticateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DeauthenticateReason.setStatus("current")
_Dot11DeauthenticateStation_Type = MacAddress
_Dot11DeauthenticateStation_Object = MibTableColumn
dot11DeauthenticateStation = _Dot11DeauthenticateStation_Object(
    (1, 2, 840, 10036, 1, 1, 1, 18),
    _Dot11DeauthenticateStation_Type()
)
dot11DeauthenticateStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DeauthenticateStation.setStatus("current")


class _Dot11AuthenticateFailStatus_Type(Integer32):
    """Custom type dot11AuthenticateFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11AuthenticateFailStatus_Type.__name__ = "Integer32"
_Dot11AuthenticateFailStatus_Object = MibTableColumn
dot11AuthenticateFailStatus = _Dot11AuthenticateFailStatus_Object(
    (1, 2, 840, 10036, 1, 1, 1, 19),
    _Dot11AuthenticateFailStatus_Type()
)
dot11AuthenticateFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticateFailStatus.setStatus("current")
_Dot11AuthenticateFailStation_Type = MacAddress
_Dot11AuthenticateFailStation_Object = MibTableColumn
dot11AuthenticateFailStation = _Dot11AuthenticateFailStation_Object(
    (1, 2, 840, 10036, 1, 1, 1, 20),
    _Dot11AuthenticateFailStation_Type()
)
dot11AuthenticateFailStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticateFailStation.setStatus("current")
_Dot11MultiDomainCapabilityImplemented_Type = TruthValue
_Dot11MultiDomainCapabilityImplemented_Object = MibTableColumn
dot11MultiDomainCapabilityImplemented = _Dot11MultiDomainCapabilityImplemented_Object(
    (1, 2, 840, 10036, 1, 1, 1, 21),
    _Dot11MultiDomainCapabilityImplemented_Type()
)
dot11MultiDomainCapabilityImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityImplemented.setStatus("current")
_Dot11MultiDomainCapabilityEnabled_Type = TruthValue
_Dot11MultiDomainCapabilityEnabled_Object = MibTableColumn
dot11MultiDomainCapabilityEnabled = _Dot11MultiDomainCapabilityEnabled_Object(
    (1, 2, 840, 10036, 1, 1, 1, 22),
    _Dot11MultiDomainCapabilityEnabled_Type()
)
dot11MultiDomainCapabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityEnabled.setStatus("current")


class _Dot11CountryString_Type(OctetString):
    """Custom type dot11CountryString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_Dot11CountryString_Type.__name__ = "OctetString"
_Dot11CountryString_Object = MibTableColumn
dot11CountryString = _Dot11CountryString_Object(
    (1, 2, 840, 10036, 1, 1, 1, 23),
    _Dot11CountryString_Type()
)
dot11CountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CountryString.setStatus("current")
_Dot11AuthenticationAlgorithmsTable_Object = MibTable
dot11AuthenticationAlgorithmsTable = _Dot11AuthenticationAlgorithmsTable_Object(
    (1, 2, 840, 10036, 1, 2)
)
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsTable.setStatus("current")
_Dot11AuthenticationAlgorithmsEntry_Object = MibTableRow
dot11AuthenticationAlgorithmsEntry = _Dot11AuthenticationAlgorithmsEntry_Object(
    (1, 2, 840, 10036, 1, 2, 1)
)
dot11AuthenticationAlgorithmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsEntry.setStatus("current")
_Dot11AuthenticationAlgorithmsIndex_Type = Integer32
_Dot11AuthenticationAlgorithmsIndex_Object = MibTableColumn
dot11AuthenticationAlgorithmsIndex = _Dot11AuthenticationAlgorithmsIndex_Object(
    (1, 2, 840, 10036, 1, 2, 1, 1),
    _Dot11AuthenticationAlgorithmsIndex_Type()
)
dot11AuthenticationAlgorithmsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsIndex.setStatus("current")


class _Dot11AuthenticationAlgorithm_Type(Integer32):
    """Custom type dot11AuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_Dot11AuthenticationAlgorithm_Type.__name__ = "Integer32"
_Dot11AuthenticationAlgorithm_Object = MibTableColumn
dot11AuthenticationAlgorithm = _Dot11AuthenticationAlgorithm_Object(
    (1, 2, 840, 10036, 1, 2, 1, 2),
    _Dot11AuthenticationAlgorithm_Type()
)
dot11AuthenticationAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithm.setStatus("current")
_Dot11AuthenticationAlgorithmsEnable_Type = TruthValue
_Dot11AuthenticationAlgorithmsEnable_Object = MibTableColumn
dot11AuthenticationAlgorithmsEnable = _Dot11AuthenticationAlgorithmsEnable_Object(
    (1, 2, 840, 10036, 1, 2, 1, 3),
    _Dot11AuthenticationAlgorithmsEnable_Type()
)
dot11AuthenticationAlgorithmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsEnable.setStatus("current")
_Dot11WEPDefaultKeysTable_Object = MibTable
dot11WEPDefaultKeysTable = _Dot11WEPDefaultKeysTable_Object(
    (1, 2, 840, 10036, 1, 3)
)
if mibBuilder.loadTexts:
    dot11WEPDefaultKeysTable.setStatus("current")
_Dot11WEPDefaultKeysEntry_Object = MibTableRow
dot11WEPDefaultKeysEntry = _Dot11WEPDefaultKeysEntry_Object(
    (1, 2, 840, 10036, 1, 3, 1)
)
dot11WEPDefaultKeysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11WEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    dot11WEPDefaultKeysEntry.setStatus("current")


class _Dot11WEPDefaultKeyIndex_Type(Integer32):
    """Custom type dot11WEPDefaultKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Dot11WEPDefaultKeyIndex_Type.__name__ = "Integer32"
_Dot11WEPDefaultKeyIndex_Object = MibTableColumn
dot11WEPDefaultKeyIndex = _Dot11WEPDefaultKeyIndex_Object(
    (1, 2, 840, 10036, 1, 3, 1, 1),
    _Dot11WEPDefaultKeyIndex_Type()
)
dot11WEPDefaultKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyIndex.setStatus("current")
_Dot11WEPDefaultKeyValue_Type = WEPKeytype
_Dot11WEPDefaultKeyValue_Object = MibTableColumn
dot11WEPDefaultKeyValue = _Dot11WEPDefaultKeyValue_Object(
    (1, 2, 840, 10036, 1, 3, 1, 2),
    _Dot11WEPDefaultKeyValue_Type()
)
dot11WEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyValue.setStatus("current")
_Dot11WEPKeyMappingsTable_Object = MibTable
dot11WEPKeyMappingsTable = _Dot11WEPKeyMappingsTable_Object(
    (1, 2, 840, 10036, 1, 4)
)
if mibBuilder.loadTexts:
    dot11WEPKeyMappingsTable.setStatus("current")
_Dot11WEPKeyMappingsEntry_Object = MibTableRow
dot11WEPKeyMappingsEntry = _Dot11WEPKeyMappingsEntry_Object(
    (1, 2, 840, 10036, 1, 4, 1)
)
dot11WEPKeyMappingsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11WEPKeyMappingIndex"),
)
if mibBuilder.loadTexts:
    dot11WEPKeyMappingsEntry.setStatus("current")
_Dot11WEPKeyMappingIndex_Type = Integer32
_Dot11WEPKeyMappingIndex_Object = MibTableColumn
dot11WEPKeyMappingIndex = _Dot11WEPKeyMappingIndex_Object(
    (1, 2, 840, 10036, 1, 4, 1, 1),
    _Dot11WEPKeyMappingIndex_Type()
)
dot11WEPKeyMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingIndex.setStatus("current")
_Dot11WEPKeyMappingAddress_Type = MacAddress
_Dot11WEPKeyMappingAddress_Object = MibTableColumn
dot11WEPKeyMappingAddress = _Dot11WEPKeyMappingAddress_Object(
    (1, 2, 840, 10036, 1, 4, 1, 2),
    _Dot11WEPKeyMappingAddress_Type()
)
dot11WEPKeyMappingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingAddress.setStatus("current")
_Dot11WEPKeyMappingWEPOn_Type = TruthValue
_Dot11WEPKeyMappingWEPOn_Object = MibTableColumn
dot11WEPKeyMappingWEPOn = _Dot11WEPKeyMappingWEPOn_Object(
    (1, 2, 840, 10036, 1, 4, 1, 3),
    _Dot11WEPKeyMappingWEPOn_Type()
)
dot11WEPKeyMappingWEPOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingWEPOn.setStatus("current")
_Dot11WEPKeyMappingValue_Type = WEPKeytype
_Dot11WEPKeyMappingValue_Object = MibTableColumn
dot11WEPKeyMappingValue = _Dot11WEPKeyMappingValue_Object(
    (1, 2, 840, 10036, 1, 4, 1, 4),
    _Dot11WEPKeyMappingValue_Type()
)
dot11WEPKeyMappingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingValue.setStatus("current")


class _Dot11WEPKeyMappingStatus_Type(RowStatus):
    """Custom type dot11WEPKeyMappingStatus based on RowStatus"""
    defaultValue = 1


_Dot11WEPKeyMappingStatus_Type.__name__ = "RowStatus"
_Dot11WEPKeyMappingStatus_Object = MibTableColumn
dot11WEPKeyMappingStatus = _Dot11WEPKeyMappingStatus_Object(
    (1, 2, 840, 10036, 1, 4, 1, 5),
    _Dot11WEPKeyMappingStatus_Type()
)
dot11WEPKeyMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingStatus.setStatus("current")
_Dot11PrivacyTable_Object = MibTable
dot11PrivacyTable = _Dot11PrivacyTable_Object(
    (1, 2, 840, 10036, 1, 5)
)
if mibBuilder.loadTexts:
    dot11PrivacyTable.setStatus("current")
_Dot11PrivacyEntry_Object = MibTableRow
dot11PrivacyEntry = _Dot11PrivacyEntry_Object(
    (1, 2, 840, 10036, 1, 5, 1)
)
dot11PrivacyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PrivacyEntry.setStatus("current")
_Dot11PrivacyInvoked_Type = TruthValue
_Dot11PrivacyInvoked_Object = MibTableColumn
dot11PrivacyInvoked = _Dot11PrivacyInvoked_Object(
    (1, 2, 840, 10036, 1, 5, 1, 1),
    _Dot11PrivacyInvoked_Type()
)
dot11PrivacyInvoked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrivacyInvoked.setStatus("current")


class _Dot11WEPDefaultKeyID_Type(Integer32):
    """Custom type dot11WEPDefaultKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11WEPDefaultKeyID_Type.__name__ = "Integer32"
_Dot11WEPDefaultKeyID_Object = MibTableColumn
dot11WEPDefaultKeyID = _Dot11WEPDefaultKeyID_Object(
    (1, 2, 840, 10036, 1, 5, 1, 2),
    _Dot11WEPDefaultKeyID_Type()
)
dot11WEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyID.setStatus("current")


class _Dot11WEPKeyMappingLength_Type(Unsigned32):
    """Custom type dot11WEPKeyMappingLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4294967295),
    )


_Dot11WEPKeyMappingLength_Type.__name__ = "Unsigned32"
_Dot11WEPKeyMappingLength_Object = MibTableColumn
dot11WEPKeyMappingLength = _Dot11WEPKeyMappingLength_Object(
    (1, 2, 840, 10036, 1, 5, 1, 3),
    _Dot11WEPKeyMappingLength_Type()
)
dot11WEPKeyMappingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPKeyMappingLength.setStatus("current")
_Dot11ExcludeUnencrypted_Type = TruthValue
_Dot11ExcludeUnencrypted_Object = MibTableColumn
dot11ExcludeUnencrypted = _Dot11ExcludeUnencrypted_Object(
    (1, 2, 840, 10036, 1, 5, 1, 4),
    _Dot11ExcludeUnencrypted_Type()
)
dot11ExcludeUnencrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ExcludeUnencrypted.setStatus("current")
_Dot11WEPICVErrorCount_Type = Counter32
_Dot11WEPICVErrorCount_Object = MibTableColumn
dot11WEPICVErrorCount = _Dot11WEPICVErrorCount_Object(
    (1, 2, 840, 10036, 1, 5, 1, 5),
    _Dot11WEPICVErrorCount_Type()
)
dot11WEPICVErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPICVErrorCount.setStatus("current")
_Dot11WEPExcludedCount_Type = Counter32
_Dot11WEPExcludedCount_Object = MibTableColumn
dot11WEPExcludedCount = _Dot11WEPExcludedCount_Object(
    (1, 2, 840, 10036, 1, 5, 1, 6),
    _Dot11WEPExcludedCount_Type()
)
dot11WEPExcludedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPExcludedCount.setStatus("current")
_Dot11SMTnotification_ObjectIdentity = ObjectIdentity
dot11SMTnotification = _Dot11SMTnotification_ObjectIdentity(
    (1, 2, 840, 10036, 1, 6)
)
_Dot11MultiDomainCapabilityTable_Object = MibTable
dot11MultiDomainCapabilityTable = _Dot11MultiDomainCapabilityTable_Object(
    (1, 2, 840, 10036, 1, 7)
)
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityTable.setStatus("current")
_Dot11MultiDomainCapabilityEntry_Object = MibTableRow
dot11MultiDomainCapabilityEntry = _Dot11MultiDomainCapabilityEntry_Object(
    (1, 2, 840, 10036, 1, 7, 1)
)
dot11MultiDomainCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11MultiDomainCapabilityIndex"),
)
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityEntry.setStatus("current")
_Dot11MultiDomainCapabilityIndex_Type = Integer32
_Dot11MultiDomainCapabilityIndex_Object = MibTableColumn
dot11MultiDomainCapabilityIndex = _Dot11MultiDomainCapabilityIndex_Object(
    (1, 2, 840, 10036, 1, 7, 1, 1),
    _Dot11MultiDomainCapabilityIndex_Type()
)
dot11MultiDomainCapabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityIndex.setStatus("current")
_Dot11FirstChannelNumber_Type = Integer32
_Dot11FirstChannelNumber_Object = MibTableColumn
dot11FirstChannelNumber = _Dot11FirstChannelNumber_Object(
    (1, 2, 840, 10036, 1, 7, 1, 2),
    _Dot11FirstChannelNumber_Type()
)
dot11FirstChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FirstChannelNumber.setStatus("current")
_Dot11NumberofChannels_Type = Integer32
_Dot11NumberofChannels_Object = MibTableColumn
dot11NumberofChannels = _Dot11NumberofChannels_Object(
    (1, 2, 840, 10036, 1, 7, 1, 3),
    _Dot11NumberofChannels_Type()
)
dot11NumberofChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11NumberofChannels.setStatus("current")
_Dot11MaximumTransmitPowerLevel_Type = Integer32
_Dot11MaximumTransmitPowerLevel_Object = MibTableColumn
dot11MaximumTransmitPowerLevel = _Dot11MaximumTransmitPowerLevel_Object(
    (1, 2, 840, 10036, 1, 7, 1, 4),
    _Dot11MaximumTransmitPowerLevel_Type()
)
dot11MaximumTransmitPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaximumTransmitPowerLevel.setStatus("current")
_Dot11mac_ObjectIdentity = ObjectIdentity
dot11mac = _Dot11mac_ObjectIdentity(
    (1, 2, 840, 10036, 2)
)
_Dot11OperationTable_Object = MibTable
dot11OperationTable = _Dot11OperationTable_Object(
    (1, 2, 840, 10036, 2, 1)
)
if mibBuilder.loadTexts:
    dot11OperationTable.setStatus("current")
_Dot11OperationEntry_Object = MibTableRow
dot11OperationEntry = _Dot11OperationEntry_Object(
    (1, 2, 840, 10036, 2, 1, 1)
)
dot11OperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11OperationEntry.setStatus("current")
_Dot11MACAddress_Type = MacAddress
_Dot11MACAddress_Object = MibTableColumn
dot11MACAddress = _Dot11MACAddress_Object(
    (1, 2, 840, 10036, 2, 1, 1, 1),
    _Dot11MACAddress_Type()
)
dot11MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MACAddress.setStatus("current")


class _Dot11RTSThreshold_Type(Integer32):
    """Custom type dot11RTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_Dot11RTSThreshold_Type.__name__ = "Integer32"
_Dot11RTSThreshold_Object = MibTableColumn
dot11RTSThreshold = _Dot11RTSThreshold_Object(
    (1, 2, 840, 10036, 2, 1, 1, 2),
    _Dot11RTSThreshold_Type()
)
dot11RTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RTSThreshold.setStatus("current")


class _Dot11ShortRetryLimit_Type(Integer32):
    """Custom type dot11ShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11ShortRetryLimit_Type.__name__ = "Integer32"
_Dot11ShortRetryLimit_Object = MibTableColumn
dot11ShortRetryLimit = _Dot11ShortRetryLimit_Object(
    (1, 2, 840, 10036, 2, 1, 1, 3),
    _Dot11ShortRetryLimit_Type()
)
dot11ShortRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortRetryLimit.setStatus("current")


class _Dot11LongRetryLimit_Type(Integer32):
    """Custom type dot11LongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11LongRetryLimit_Type.__name__ = "Integer32"
_Dot11LongRetryLimit_Object = MibTableColumn
dot11LongRetryLimit = _Dot11LongRetryLimit_Object(
    (1, 2, 840, 10036, 2, 1, 1, 4),
    _Dot11LongRetryLimit_Type()
)
dot11LongRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LongRetryLimit.setStatus("current")


class _Dot11FragmentationThreshold_Type(Integer32):
    """Custom type dot11FragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_Dot11FragmentationThreshold_Type.__name__ = "Integer32"
_Dot11FragmentationThreshold_Object = MibTableColumn
dot11FragmentationThreshold = _Dot11FragmentationThreshold_Object(
    (1, 2, 840, 10036, 2, 1, 1, 5),
    _Dot11FragmentationThreshold_Type()
)
dot11FragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FragmentationThreshold.setStatus("current")


class _Dot11MaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type dot11MaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11MaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_Dot11MaxTransmitMSDULifetime_Object = MibTableColumn
dot11MaxTransmitMSDULifetime = _Dot11MaxTransmitMSDULifetime_Object(
    (1, 2, 840, 10036, 2, 1, 1, 6),
    _Dot11MaxTransmitMSDULifetime_Type()
)
dot11MaxTransmitMSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaxTransmitMSDULifetime.setStatus("current")


class _Dot11MaxReceiveLifetime_Type(Unsigned32):
    """Custom type dot11MaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot11MaxReceiveLifetime_Type.__name__ = "Unsigned32"
_Dot11MaxReceiveLifetime_Object = MibTableColumn
dot11MaxReceiveLifetime = _Dot11MaxReceiveLifetime_Object(
    (1, 2, 840, 10036, 2, 1, 1, 7),
    _Dot11MaxReceiveLifetime_Type()
)
dot11MaxReceiveLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaxReceiveLifetime.setStatus("current")


class _Dot11ManufacturerID_Type(DisplayString):
    """Custom type dot11ManufacturerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11ManufacturerID_Type.__name__ = "DisplayString"
_Dot11ManufacturerID_Object = MibTableColumn
dot11ManufacturerID = _Dot11ManufacturerID_Object(
    (1, 2, 840, 10036, 2, 1, 1, 8),
    _Dot11ManufacturerID_Type()
)
dot11ManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ManufacturerID.setStatus("current")


class _Dot11ProductID_Type(DisplayString):
    """Custom type dot11ProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11ProductID_Type.__name__ = "DisplayString"
_Dot11ProductID_Object = MibTableColumn
dot11ProductID = _Dot11ProductID_Object(
    (1, 2, 840, 10036, 2, 1, 1, 9),
    _Dot11ProductID_Type()
)
dot11ProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ProductID.setStatus("current")
_Dot11CountersTable_Object = MibTable
dot11CountersTable = _Dot11CountersTable_Object(
    (1, 2, 840, 10036, 2, 2)
)
if mibBuilder.loadTexts:
    dot11CountersTable.setStatus("current")
_Dot11CountersEntry_Object = MibTableRow
dot11CountersEntry = _Dot11CountersEntry_Object(
    (1, 2, 840, 10036, 2, 2, 1)
)
dot11CountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11CountersEntry.setStatus("current")
_Dot11TransmittedFragmentCount_Type = Counter32
_Dot11TransmittedFragmentCount_Object = MibTableColumn
dot11TransmittedFragmentCount = _Dot11TransmittedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 1),
    _Dot11TransmittedFragmentCount_Type()
)
dot11TransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFragmentCount.setStatus("current")
_Dot11MulticastTransmittedFrameCount_Type = Counter32
_Dot11MulticastTransmittedFrameCount_Object = MibTableColumn
dot11MulticastTransmittedFrameCount = _Dot11MulticastTransmittedFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 2),
    _Dot11MulticastTransmittedFrameCount_Type()
)
dot11MulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastTransmittedFrameCount.setStatus("current")
_Dot11FailedCount_Type = Counter32
_Dot11FailedCount_Object = MibTableColumn
dot11FailedCount = _Dot11FailedCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 3),
    _Dot11FailedCount_Type()
)
dot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FailedCount.setStatus("current")
_Dot11RetryCount_Type = Counter32
_Dot11RetryCount_Object = MibTableColumn
dot11RetryCount = _Dot11RetryCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 4),
    _Dot11RetryCount_Type()
)
dot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RetryCount.setStatus("current")
_Dot11MultipleRetryCount_Type = Counter32
_Dot11MultipleRetryCount_Object = MibTableColumn
dot11MultipleRetryCount = _Dot11MultipleRetryCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 5),
    _Dot11MultipleRetryCount_Type()
)
dot11MultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MultipleRetryCount.setStatus("current")
_Dot11FrameDuplicateCount_Type = Counter32
_Dot11FrameDuplicateCount_Object = MibTableColumn
dot11FrameDuplicateCount = _Dot11FrameDuplicateCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 6),
    _Dot11FrameDuplicateCount_Type()
)
dot11FrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FrameDuplicateCount.setStatus("current")
_Dot11RTSSuccessCount_Type = Counter32
_Dot11RTSSuccessCount_Object = MibTableColumn
dot11RTSSuccessCount = _Dot11RTSSuccessCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 7),
    _Dot11RTSSuccessCount_Type()
)
dot11RTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RTSSuccessCount.setStatus("current")
_Dot11RTSFailureCount_Type = Counter32
_Dot11RTSFailureCount_Object = MibTableColumn
dot11RTSFailureCount = _Dot11RTSFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 8),
    _Dot11RTSFailureCount_Type()
)
dot11RTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RTSFailureCount.setStatus("current")
_Dot11ACKFailureCount_Type = Counter32
_Dot11ACKFailureCount_Object = MibTableColumn
dot11ACKFailureCount = _Dot11ACKFailureCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 9),
    _Dot11ACKFailureCount_Type()
)
dot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ACKFailureCount.setStatus("current")
_Dot11ReceivedFragmentCount_Type = Counter32
_Dot11ReceivedFragmentCount_Object = MibTableColumn
dot11ReceivedFragmentCount = _Dot11ReceivedFragmentCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 10),
    _Dot11ReceivedFragmentCount_Type()
)
dot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFragmentCount.setStatus("current")
_Dot11MulticastReceivedFrameCount_Type = Counter32
_Dot11MulticastReceivedFrameCount_Object = MibTableColumn
dot11MulticastReceivedFrameCount = _Dot11MulticastReceivedFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 11),
    _Dot11MulticastReceivedFrameCount_Type()
)
dot11MulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastReceivedFrameCount.setStatus("current")
_Dot11FCSErrorCount_Type = Counter32
_Dot11FCSErrorCount_Object = MibTableColumn
dot11FCSErrorCount = _Dot11FCSErrorCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 12),
    _Dot11FCSErrorCount_Type()
)
dot11FCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FCSErrorCount.setStatus("current")
_Dot11TransmittedFrameCount_Type = Counter32
_Dot11TransmittedFrameCount_Object = MibTableColumn
dot11TransmittedFrameCount = _Dot11TransmittedFrameCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 13),
    _Dot11TransmittedFrameCount_Type()
)
dot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFrameCount.setStatus("current")
_Dot11WEPUndecryptableCount_Type = Counter32
_Dot11WEPUndecryptableCount_Object = MibTableColumn
dot11WEPUndecryptableCount = _Dot11WEPUndecryptableCount_Object(
    (1, 2, 840, 10036, 2, 2, 1, 14),
    _Dot11WEPUndecryptableCount_Type()
)
dot11WEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WEPUndecryptableCount.setStatus("current")
_Dot11GroupAddressesTable_Object = MibTable
dot11GroupAddressesTable = _Dot11GroupAddressesTable_Object(
    (1, 2, 840, 10036, 2, 3)
)
if mibBuilder.loadTexts:
    dot11GroupAddressesTable.setStatus("current")
_Dot11GroupAddressesEntry_Object = MibTableRow
dot11GroupAddressesEntry = _Dot11GroupAddressesEntry_Object(
    (1, 2, 840, 10036, 2, 3, 1)
)
dot11GroupAddressesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11GroupAddressesIndex"),
)
if mibBuilder.loadTexts:
    dot11GroupAddressesEntry.setStatus("current")
_Dot11GroupAddressesIndex_Type = Integer32
_Dot11GroupAddressesIndex_Object = MibTableColumn
dot11GroupAddressesIndex = _Dot11GroupAddressesIndex_Object(
    (1, 2, 840, 10036, 2, 3, 1, 1),
    _Dot11GroupAddressesIndex_Type()
)
dot11GroupAddressesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11GroupAddressesIndex.setStatus("current")
_Dot11Address_Type = MacAddress
_Dot11Address_Object = MibTableColumn
dot11Address = _Dot11Address_Object(
    (1, 2, 840, 10036, 2, 3, 1, 2),
    _Dot11Address_Type()
)
dot11Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11Address.setStatus("current")


class _Dot11GroupAddressesStatus_Type(RowStatus):
    """Custom type dot11GroupAddressesStatus based on RowStatus"""
    defaultValue = 1


_Dot11GroupAddressesStatus_Type.__name__ = "RowStatus"
_Dot11GroupAddressesStatus_Object = MibTableColumn
dot11GroupAddressesStatus = _Dot11GroupAddressesStatus_Object(
    (1, 2, 840, 10036, 2, 3, 1, 3),
    _Dot11GroupAddressesStatus_Type()
)
dot11GroupAddressesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot11GroupAddressesStatus.setStatus("current")
_Dot11res_ObjectIdentity = ObjectIdentity
dot11res = _Dot11res_ObjectIdentity(
    (1, 2, 840, 10036, 3)
)
_Dot11resAttribute_ObjectIdentity = ObjectIdentity
dot11resAttribute = _Dot11resAttribute_ObjectIdentity(
    (1, 2, 840, 10036, 3, 1)
)


class _Dot11ResourceTypeIDName_Type(DisplayString):
    """Custom type dot11ResourceTypeIDName based on DisplayString"""
    defaultValue = OctetString("RTID")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dot11ResourceTypeIDName_Type.__name__ = "DisplayString"
_Dot11ResourceTypeIDName_Object = MibScalar
dot11ResourceTypeIDName = _Dot11ResourceTypeIDName_Object(
    (1, 2, 840, 10036, 3, 1, 1),
    _Dot11ResourceTypeIDName_Type()
)
dot11ResourceTypeIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ResourceTypeIDName.setStatus("current")
_Dot11ResourceInfoTable_Object = MibTable
dot11ResourceInfoTable = _Dot11ResourceInfoTable_Object(
    (1, 2, 840, 10036, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dot11ResourceInfoTable.setStatus("current")
_Dot11ResourceInfoEntry_Object = MibTableRow
dot11ResourceInfoEntry = _Dot11ResourceInfoEntry_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1)
)
dot11ResourceInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ResourceInfoEntry.setStatus("current")


class _Dot11manufacturerOUI_Type(OctetString):
    """Custom type dot11manufacturerOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_Dot11manufacturerOUI_Type.__name__ = "OctetString"
_Dot11manufacturerOUI_Object = MibTableColumn
dot11manufacturerOUI = _Dot11manufacturerOUI_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 1),
    _Dot11manufacturerOUI_Type()
)
dot11manufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerOUI.setStatus("current")


class _Dot11manufacturerName_Type(DisplayString):
    """Custom type dot11manufacturerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11manufacturerName_Type.__name__ = "DisplayString"
_Dot11manufacturerName_Object = MibTableColumn
dot11manufacturerName = _Dot11manufacturerName_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 2),
    _Dot11manufacturerName_Type()
)
dot11manufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerName.setStatus("current")


class _Dot11manufacturerProductName_Type(DisplayString):
    """Custom type dot11manufacturerProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11manufacturerProductName_Type.__name__ = "DisplayString"
_Dot11manufacturerProductName_Object = MibTableColumn
dot11manufacturerProductName = _Dot11manufacturerProductName_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 3),
    _Dot11manufacturerProductName_Type()
)
dot11manufacturerProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerProductName.setStatus("current")


class _Dot11manufacturerProductVersion_Type(DisplayString):
    """Custom type dot11manufacturerProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Dot11manufacturerProductVersion_Type.__name__ = "DisplayString"
_Dot11manufacturerProductVersion_Object = MibTableColumn
dot11manufacturerProductVersion = _Dot11manufacturerProductVersion_Object(
    (1, 2, 840, 10036, 3, 1, 2, 1, 4),
    _Dot11manufacturerProductVersion_Type()
)
dot11manufacturerProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerProductVersion.setStatus("current")
_Dot11phy_ObjectIdentity = ObjectIdentity
dot11phy = _Dot11phy_ObjectIdentity(
    (1, 2, 840, 10036, 4)
)
_Dot11PhyOperationTable_Object = MibTable
dot11PhyOperationTable = _Dot11PhyOperationTable_Object(
    (1, 2, 840, 10036, 4, 1)
)
if mibBuilder.loadTexts:
    dot11PhyOperationTable.setStatus("current")
_Dot11PhyOperationEntry_Object = MibTableRow
dot11PhyOperationEntry = _Dot11PhyOperationEntry_Object(
    (1, 2, 840, 10036, 4, 1, 1)
)
dot11PhyOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyOperationEntry.setStatus("current")


class _Dot11PHYType_Type(Integer32):
    """Custom type dot11PHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fhss", 1),
          ("dsss", 2),
          ("irbaseband", 3),
          ("ofdm", 4),
          ("hrdsss", 5))
    )


_Dot11PHYType_Type.__name__ = "Integer32"
_Dot11PHYType_Object = MibTableColumn
dot11PHYType = _Dot11PHYType_Object(
    (1, 2, 840, 10036, 4, 1, 1, 1),
    _Dot11PHYType_Type()
)
dot11PHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PHYType.setStatus("current")
_Dot11CurrentRegDomain_Type = Integer32
_Dot11CurrentRegDomain_Object = MibTableColumn
dot11CurrentRegDomain = _Dot11CurrentRegDomain_Object(
    (1, 2, 840, 10036, 4, 1, 1, 2),
    _Dot11CurrentRegDomain_Type()
)
dot11CurrentRegDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentRegDomain.setStatus("current")


class _Dot11TempType_Type(Integer32):
    """Custom type dot11TempType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempType1", 1),
          ("tempType2", 2))
    )


_Dot11TempType_Type.__name__ = "Integer32"
_Dot11TempType_Object = MibTableColumn
dot11TempType = _Dot11TempType_Object(
    (1, 2, 840, 10036, 4, 1, 1, 3),
    _Dot11TempType_Type()
)
dot11TempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TempType.setStatus("current")
_Dot11PhyAntennaTable_Object = MibTable
dot11PhyAntennaTable = _Dot11PhyAntennaTable_Object(
    (1, 2, 840, 10036, 4, 2)
)
if mibBuilder.loadTexts:
    dot11PhyAntennaTable.setStatus("current")
_Dot11PhyAntennaEntry_Object = MibTableRow
dot11PhyAntennaEntry = _Dot11PhyAntennaEntry_Object(
    (1, 2, 840, 10036, 4, 2, 1)
)
dot11PhyAntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyAntennaEntry.setStatus("current")


class _Dot11CurrentTxAntenna_Type(Integer32):
    """Custom type dot11CurrentTxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentTxAntenna_Type.__name__ = "Integer32"
_Dot11CurrentTxAntenna_Object = MibTableColumn
dot11CurrentTxAntenna = _Dot11CurrentTxAntenna_Object(
    (1, 2, 840, 10036, 4, 2, 1, 1),
    _Dot11CurrentTxAntenna_Type()
)
dot11CurrentTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentTxAntenna.setStatus("current")


class _Dot11DiversitySupport_Type(Integer32):
    """Custom type dot11DiversitySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedlist", 1),
          ("notsupported", 2),
          ("dynamic", 3))
    )


_Dot11DiversitySupport_Type.__name__ = "Integer32"
_Dot11DiversitySupport_Object = MibTableColumn
dot11DiversitySupport = _Dot11DiversitySupport_Object(
    (1, 2, 840, 10036, 4, 2, 1, 2),
    _Dot11DiversitySupport_Type()
)
dot11DiversitySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DiversitySupport.setStatus("current")


class _Dot11CurrentRxAntenna_Type(Integer32):
    """Custom type dot11CurrentRxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentRxAntenna_Type.__name__ = "Integer32"
_Dot11CurrentRxAntenna_Object = MibTableColumn
dot11CurrentRxAntenna = _Dot11CurrentRxAntenna_Object(
    (1, 2, 840, 10036, 4, 2, 1, 3),
    _Dot11CurrentRxAntenna_Type()
)
dot11CurrentRxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentRxAntenna.setStatus("current")
_Dot11PhyTxPowerTable_Object = MibTable
dot11PhyTxPowerTable = _Dot11PhyTxPowerTable_Object(
    (1, 2, 840, 10036, 4, 3)
)
if mibBuilder.loadTexts:
    dot11PhyTxPowerTable.setStatus("current")
_Dot11PhyTxPowerEntry_Object = MibTableRow
dot11PhyTxPowerEntry = _Dot11PhyTxPowerEntry_Object(
    (1, 2, 840, 10036, 4, 3, 1)
)
dot11PhyTxPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyTxPowerEntry.setStatus("current")


class _Dot11NumberSupportedPowerLevels_Type(Integer32):
    """Custom type dot11NumberSupportedPowerLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11NumberSupportedPowerLevels_Type.__name__ = "Integer32"
_Dot11NumberSupportedPowerLevels_Object = MibTableColumn
dot11NumberSupportedPowerLevels = _Dot11NumberSupportedPowerLevels_Object(
    (1, 2, 840, 10036, 4, 3, 1, 1),
    _Dot11NumberSupportedPowerLevels_Type()
)
dot11NumberSupportedPowerLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberSupportedPowerLevels.setStatus("current")


class _Dot11TxPowerLevel1_Type(Integer32):
    """Custom type dot11TxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel1_Type.__name__ = "Integer32"
_Dot11TxPowerLevel1_Object = MibTableColumn
dot11TxPowerLevel1 = _Dot11TxPowerLevel1_Object(
    (1, 2, 840, 10036, 4, 3, 1, 2),
    _Dot11TxPowerLevel1_Type()
)
dot11TxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel1.setStatus("current")


class _Dot11TxPowerLevel2_Type(Integer32):
    """Custom type dot11TxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel2_Type.__name__ = "Integer32"
_Dot11TxPowerLevel2_Object = MibTableColumn
dot11TxPowerLevel2 = _Dot11TxPowerLevel2_Object(
    (1, 2, 840, 10036, 4, 3, 1, 3),
    _Dot11TxPowerLevel2_Type()
)
dot11TxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel2.setStatus("current")


class _Dot11TxPowerLevel3_Type(Integer32):
    """Custom type dot11TxPowerLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel3_Type.__name__ = "Integer32"
_Dot11TxPowerLevel3_Object = MibTableColumn
dot11TxPowerLevel3 = _Dot11TxPowerLevel3_Object(
    (1, 2, 840, 10036, 4, 3, 1, 4),
    _Dot11TxPowerLevel3_Type()
)
dot11TxPowerLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel3.setStatus("current")


class _Dot11TxPowerLevel4_Type(Integer32):
    """Custom type dot11TxPowerLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel4_Type.__name__ = "Integer32"
_Dot11TxPowerLevel4_Object = MibTableColumn
dot11TxPowerLevel4 = _Dot11TxPowerLevel4_Object(
    (1, 2, 840, 10036, 4, 3, 1, 5),
    _Dot11TxPowerLevel4_Type()
)
dot11TxPowerLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel4.setStatus("current")


class _Dot11TxPowerLevel5_Type(Integer32):
    """Custom type dot11TxPowerLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel5_Type.__name__ = "Integer32"
_Dot11TxPowerLevel5_Object = MibTableColumn
dot11TxPowerLevel5 = _Dot11TxPowerLevel5_Object(
    (1, 2, 840, 10036, 4, 3, 1, 6),
    _Dot11TxPowerLevel5_Type()
)
dot11TxPowerLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel5.setStatus("current")


class _Dot11TxPowerLevel6_Type(Integer32):
    """Custom type dot11TxPowerLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel6_Type.__name__ = "Integer32"
_Dot11TxPowerLevel6_Object = MibTableColumn
dot11TxPowerLevel6 = _Dot11TxPowerLevel6_Object(
    (1, 2, 840, 10036, 4, 3, 1, 7),
    _Dot11TxPowerLevel6_Type()
)
dot11TxPowerLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel6.setStatus("current")


class _Dot11TxPowerLevel7_Type(Integer32):
    """Custom type dot11TxPowerLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel7_Type.__name__ = "Integer32"
_Dot11TxPowerLevel7_Object = MibTableColumn
dot11TxPowerLevel7 = _Dot11TxPowerLevel7_Object(
    (1, 2, 840, 10036, 4, 3, 1, 8),
    _Dot11TxPowerLevel7_Type()
)
dot11TxPowerLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel7.setStatus("current")


class _Dot11TxPowerLevel8_Type(Integer32):
    """Custom type dot11TxPowerLevel8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Dot11TxPowerLevel8_Type.__name__ = "Integer32"
_Dot11TxPowerLevel8_Object = MibTableColumn
dot11TxPowerLevel8 = _Dot11TxPowerLevel8_Object(
    (1, 2, 840, 10036, 4, 3, 1, 9),
    _Dot11TxPowerLevel8_Type()
)
dot11TxPowerLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TxPowerLevel8.setStatus("current")


class _Dot11CurrentTxPowerLevel_Type(Integer32):
    """Custom type dot11CurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11CurrentTxPowerLevel_Type.__name__ = "Integer32"
_Dot11CurrentTxPowerLevel_Object = MibTableColumn
dot11CurrentTxPowerLevel = _Dot11CurrentTxPowerLevel_Object(
    (1, 2, 840, 10036, 4, 3, 1, 10),
    _Dot11CurrentTxPowerLevel_Type()
)
dot11CurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentTxPowerLevel.setStatus("current")
_Dot11PhyFHSSTable_Object = MibTable
dot11PhyFHSSTable = _Dot11PhyFHSSTable_Object(
    (1, 2, 840, 10036, 4, 4)
)
if mibBuilder.loadTexts:
    dot11PhyFHSSTable.setStatus("current")
_Dot11PhyFHSSEntry_Object = MibTableRow
dot11PhyFHSSEntry = _Dot11PhyFHSSEntry_Object(
    (1, 2, 840, 10036, 4, 4, 1)
)
dot11PhyFHSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyFHSSEntry.setStatus("current")


class _Dot11HopTime_Type(Integer32):
    """Custom type dot11HopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(224, 224),
    )


_Dot11HopTime_Type.__name__ = "Integer32"
_Dot11HopTime_Object = MibTableColumn
dot11HopTime = _Dot11HopTime_Object(
    (1, 2, 840, 10036, 4, 4, 1, 1),
    _Dot11HopTime_Type()
)
dot11HopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HopTime.setStatus("current")


class _Dot11CurrentChannelNumber_Type(Integer32):
    """Custom type dot11CurrentChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Dot11CurrentChannelNumber_Type.__name__ = "Integer32"
_Dot11CurrentChannelNumber_Object = MibTableColumn
dot11CurrentChannelNumber = _Dot11CurrentChannelNumber_Object(
    (1, 2, 840, 10036, 4, 4, 1, 2),
    _Dot11CurrentChannelNumber_Type()
)
dot11CurrentChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentChannelNumber.setStatus("current")


class _Dot11MaxDwellTime_Type(Integer32):
    """Custom type dot11MaxDwellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MaxDwellTime_Type.__name__ = "Integer32"
_Dot11MaxDwellTime_Object = MibTableColumn
dot11MaxDwellTime = _Dot11MaxDwellTime_Object(
    (1, 2, 840, 10036, 4, 4, 1, 3),
    _Dot11MaxDwellTime_Type()
)
dot11MaxDwellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MaxDwellTime.setStatus("current")


class _Dot11CurrentDwellTime_Type(Integer32):
    """Custom type dot11CurrentDwellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11CurrentDwellTime_Type.__name__ = "Integer32"
_Dot11CurrentDwellTime_Object = MibTableColumn
dot11CurrentDwellTime = _Dot11CurrentDwellTime_Object(
    (1, 2, 840, 10036, 4, 4, 1, 4),
    _Dot11CurrentDwellTime_Type()
)
dot11CurrentDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentDwellTime.setStatus("current")


class _Dot11CurrentSet_Type(Integer32):
    """Custom type dot11CurrentSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentSet_Type.__name__ = "Integer32"
_Dot11CurrentSet_Object = MibTableColumn
dot11CurrentSet = _Dot11CurrentSet_Object(
    (1, 2, 840, 10036, 4, 4, 1, 5),
    _Dot11CurrentSet_Type()
)
dot11CurrentSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentSet.setStatus("current")


class _Dot11CurrentPattern_Type(Integer32):
    """Custom type dot11CurrentPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11CurrentPattern_Type.__name__ = "Integer32"
_Dot11CurrentPattern_Object = MibTableColumn
dot11CurrentPattern = _Dot11CurrentPattern_Object(
    (1, 2, 840, 10036, 4, 4, 1, 6),
    _Dot11CurrentPattern_Type()
)
dot11CurrentPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentPattern.setStatus("current")


class _Dot11CurrentIndex_Type(Integer32):
    """Custom type dot11CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11CurrentIndex_Type.__name__ = "Integer32"
_Dot11CurrentIndex_Object = MibTableColumn
dot11CurrentIndex = _Dot11CurrentIndex_Object(
    (1, 2, 840, 10036, 4, 4, 1, 7),
    _Dot11CurrentIndex_Type()
)
dot11CurrentIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentIndex.setStatus("current")
_Dot11EHCCPrimeRadix_Type = Integer32
_Dot11EHCCPrimeRadix_Object = MibTableColumn
dot11EHCCPrimeRadix = _Dot11EHCCPrimeRadix_Object(
    (1, 2, 840, 10036, 4, 4, 1, 8),
    _Dot11EHCCPrimeRadix_Type()
)
dot11EHCCPrimeRadix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCPrimeRadix.setStatus("current")
_Dot11EHCCNumberofChannelsFamilyIndex_Type = Integer32
_Dot11EHCCNumberofChannelsFamilyIndex_Object = MibTableColumn
dot11EHCCNumberofChannelsFamilyIndex = _Dot11EHCCNumberofChannelsFamilyIndex_Object(
    (1, 2, 840, 10036, 4, 4, 1, 9),
    _Dot11EHCCNumberofChannelsFamilyIndex_Type()
)
dot11EHCCNumberofChannelsFamilyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCNumberofChannelsFamilyIndex.setStatus("current")
_Dot11EHCCCapabilityImplemented_Type = TruthValue
_Dot11EHCCCapabilityImplemented_Object = MibTableColumn
dot11EHCCCapabilityImplemented = _Dot11EHCCCapabilityImplemented_Object(
    (1, 2, 840, 10036, 4, 4, 1, 10),
    _Dot11EHCCCapabilityImplemented_Type()
)
dot11EHCCCapabilityImplemented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCCapabilityImplemented.setStatus("current")
_Dot11EHCCCapabilityEnabled_Type = TruthValue
_Dot11EHCCCapabilityEnabled_Object = MibTableColumn
dot11EHCCCapabilityEnabled = _Dot11EHCCCapabilityEnabled_Object(
    (1, 2, 840, 10036, 4, 4, 1, 11),
    _Dot11EHCCCapabilityEnabled_Type()
)
dot11EHCCCapabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EHCCCapabilityEnabled.setStatus("current")


class _Dot11HopAlgorithmAdopted_Type(Integer32):
    """Custom type dot11HopAlgorithmAdopted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crnt", 1),
          ("hopindex", 2),
          ("hcc", 3))
    )


_Dot11HopAlgorithmAdopted_Type.__name__ = "Integer32"
_Dot11HopAlgorithmAdopted_Object = MibTableColumn
dot11HopAlgorithmAdopted = _Dot11HopAlgorithmAdopted_Object(
    (1, 2, 840, 10036, 4, 4, 1, 12),
    _Dot11HopAlgorithmAdopted_Type()
)
dot11HopAlgorithmAdopted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HopAlgorithmAdopted.setStatus("current")
_Dot11RandomTableFlag_Type = TruthValue
_Dot11RandomTableFlag_Object = MibTableColumn
dot11RandomTableFlag = _Dot11RandomTableFlag_Object(
    (1, 2, 840, 10036, 4, 4, 1, 13),
    _Dot11RandomTableFlag_Type()
)
dot11RandomTableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RandomTableFlag.setStatus("current")
_Dot11NumberofHoppingSets_Type = Integer32
_Dot11NumberofHoppingSets_Object = MibTableColumn
dot11NumberofHoppingSets = _Dot11NumberofHoppingSets_Object(
    (1, 2, 840, 10036, 4, 4, 1, 14),
    _Dot11NumberofHoppingSets_Type()
)
dot11NumberofHoppingSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11NumberofHoppingSets.setStatus("current")
_Dot11HopModulus_Type = Integer32
_Dot11HopModulus_Object = MibTableColumn
dot11HopModulus = _Dot11HopModulus_Object(
    (1, 2, 840, 10036, 4, 4, 1, 15),
    _Dot11HopModulus_Type()
)
dot11HopModulus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HopModulus.setStatus("current")
_Dot11HopOffset_Type = Integer32
_Dot11HopOffset_Object = MibTableColumn
dot11HopOffset = _Dot11HopOffset_Object(
    (1, 2, 840, 10036, 4, 4, 1, 16),
    _Dot11HopOffset_Type()
)
dot11HopOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HopOffset.setStatus("current")
_Dot11PhyDSSSTable_Object = MibTable
dot11PhyDSSSTable = _Dot11PhyDSSSTable_Object(
    (1, 2, 840, 10036, 4, 5)
)
if mibBuilder.loadTexts:
    dot11PhyDSSSTable.setStatus("current")
_Dot11PhyDSSSEntry_Object = MibTableRow
dot11PhyDSSSEntry = _Dot11PhyDSSSEntry_Object(
    (1, 2, 840, 10036, 4, 5, 1)
)
dot11PhyDSSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyDSSSEntry.setStatus("current")


class _Dot11CurrentChannel_Type(Integer32):
    """Custom type dot11CurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Dot11CurrentChannel_Type.__name__ = "Integer32"
_Dot11CurrentChannel_Object = MibTableColumn
dot11CurrentChannel = _Dot11CurrentChannel_Object(
    (1, 2, 840, 10036, 4, 5, 1, 1),
    _Dot11CurrentChannel_Type()
)
dot11CurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentChannel.setStatus("current")


class _Dot11CCAModeSupported_Type(Integer32):
    """Custom type dot11CCAModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Dot11CCAModeSupported_Type.__name__ = "Integer32"
_Dot11CCAModeSupported_Object = MibTableColumn
dot11CCAModeSupported = _Dot11CCAModeSupported_Object(
    (1, 2, 840, 10036, 4, 5, 1, 2),
    _Dot11CCAModeSupported_Type()
)
dot11CCAModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CCAModeSupported.setStatus("current")


class _Dot11CurrentCCAMode_Type(Integer32):
    """Custom type dot11CurrentCCAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("edonly", 1),
          ("csonly", 2),
          ("edandcs", 4),
          ("cswithtimer", 8),
          ("hrcsanded", 16))
    )


_Dot11CurrentCCAMode_Type.__name__ = "Integer32"
_Dot11CurrentCCAMode_Object = MibTableColumn
dot11CurrentCCAMode = _Dot11CurrentCCAMode_Object(
    (1, 2, 840, 10036, 4, 5, 1, 3),
    _Dot11CurrentCCAMode_Type()
)
dot11CurrentCCAMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentCCAMode.setStatus("current")
_Dot11EDThreshold_Type = Integer32
_Dot11EDThreshold_Object = MibTableColumn
dot11EDThreshold = _Dot11EDThreshold_Object(
    (1, 2, 840, 10036, 4, 5, 1, 4),
    _Dot11EDThreshold_Type()
)
dot11EDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EDThreshold.setStatus("current")
_Dot11PhyIRTable_Object = MibTable
dot11PhyIRTable = _Dot11PhyIRTable_Object(
    (1, 2, 840, 10036, 4, 6)
)
if mibBuilder.loadTexts:
    dot11PhyIRTable.setStatus("current")
_Dot11PhyIREntry_Object = MibTableRow
dot11PhyIREntry = _Dot11PhyIREntry_Object(
    (1, 2, 840, 10036, 4, 6, 1)
)
dot11PhyIREntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyIREntry.setStatus("current")
_Dot11CCAWatchdogTimerMax_Type = Integer32
_Dot11CCAWatchdogTimerMax_Object = MibTableColumn
dot11CCAWatchdogTimerMax = _Dot11CCAWatchdogTimerMax_Object(
    (1, 2, 840, 10036, 4, 6, 1, 1),
    _Dot11CCAWatchdogTimerMax_Type()
)
dot11CCAWatchdogTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogTimerMax.setStatus("current")
_Dot11CCAWatchdogCountMax_Type = Integer32
_Dot11CCAWatchdogCountMax_Object = MibTableColumn
dot11CCAWatchdogCountMax = _Dot11CCAWatchdogCountMax_Object(
    (1, 2, 840, 10036, 4, 6, 1, 2),
    _Dot11CCAWatchdogCountMax_Type()
)
dot11CCAWatchdogCountMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogCountMax.setStatus("current")
_Dot11CCAWatchdogTimerMin_Type = Integer32
_Dot11CCAWatchdogTimerMin_Object = MibTableColumn
dot11CCAWatchdogTimerMin = _Dot11CCAWatchdogTimerMin_Object(
    (1, 2, 840, 10036, 4, 6, 1, 3),
    _Dot11CCAWatchdogTimerMin_Type()
)
dot11CCAWatchdogTimerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogTimerMin.setStatus("current")
_Dot11CCAWatchdogCountMin_Type = Integer32
_Dot11CCAWatchdogCountMin_Object = MibTableColumn
dot11CCAWatchdogCountMin = _Dot11CCAWatchdogCountMin_Object(
    (1, 2, 840, 10036, 4, 6, 1, 4),
    _Dot11CCAWatchdogCountMin_Type()
)
dot11CCAWatchdogCountMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CCAWatchdogCountMin.setStatus("current")
_Dot11RegDomainsSupportedTable_Object = MibTable
dot11RegDomainsSupportedTable = _Dot11RegDomainsSupportedTable_Object(
    (1, 2, 840, 10036, 4, 7)
)
if mibBuilder.loadTexts:
    dot11RegDomainsSupportedTable.setStatus("current")
_Dot11RegDomainsSupportedEntry_Object = MibTableRow
dot11RegDomainsSupportedEntry = _Dot11RegDomainsSupportedEntry_Object(
    (1, 2, 840, 10036, 4, 7, 1)
)
dot11RegDomainsSupportedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11RegDomainsSupportedIndex"),
)
if mibBuilder.loadTexts:
    dot11RegDomainsSupportedEntry.setStatus("current")
_Dot11RegDomainsSupportedIndex_Type = Integer32
_Dot11RegDomainsSupportedIndex_Object = MibTableColumn
dot11RegDomainsSupportedIndex = _Dot11RegDomainsSupportedIndex_Object(
    (1, 2, 840, 10036, 4, 7, 1, 1),
    _Dot11RegDomainsSupportedIndex_Type()
)
dot11RegDomainsSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RegDomainsSupportedIndex.setStatus("current")


class _Dot11RegDomainsSupportedValue_Type(Integer32):
    """Custom type dot11RegDomainsSupportedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              49,
              50,
              64)
        )
    )
    namedValues = NamedValues(
        *(("fcc", 16),
          ("doc", 32),
          ("etsi", 48),
          ("spain", 49),
          ("france", 50),
          ("mkk", 64))
    )


_Dot11RegDomainsSupportedValue_Type.__name__ = "Integer32"
_Dot11RegDomainsSupportedValue_Object = MibTableColumn
dot11RegDomainsSupportedValue = _Dot11RegDomainsSupportedValue_Object(
    (1, 2, 840, 10036, 4, 7, 1, 2),
    _Dot11RegDomainsSupportedValue_Type()
)
dot11RegDomainsSupportedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RegDomainsSupportedValue.setStatus("current")
_Dot11AntennasListTable_Object = MibTable
dot11AntennasListTable = _Dot11AntennasListTable_Object(
    (1, 2, 840, 10036, 4, 8)
)
if mibBuilder.loadTexts:
    dot11AntennasListTable.setStatus("current")
_Dot11AntennasListEntry_Object = MibTableRow
dot11AntennasListEntry = _Dot11AntennasListEntry_Object(
    (1, 2, 840, 10036, 4, 8, 1)
)
dot11AntennasListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11AntennaListIndex"),
)
if mibBuilder.loadTexts:
    dot11AntennasListEntry.setStatus("current")


class _Dot11AntennaListIndex_Type(Integer32):
    """Custom type dot11AntennaListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11AntennaListIndex_Type.__name__ = "Integer32"
_Dot11AntennaListIndex_Object = MibTableColumn
dot11AntennaListIndex = _Dot11AntennaListIndex_Object(
    (1, 2, 840, 10036, 4, 8, 1, 1),
    _Dot11AntennaListIndex_Type()
)
dot11AntennaListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11AntennaListIndex.setStatus("current")
_Dot11SupportedTxAntenna_Type = TruthValue
_Dot11SupportedTxAntenna_Object = MibTableColumn
dot11SupportedTxAntenna = _Dot11SupportedTxAntenna_Object(
    (1, 2, 840, 10036, 4, 8, 1, 2),
    _Dot11SupportedTxAntenna_Type()
)
dot11SupportedTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SupportedTxAntenna.setStatus("current")
_Dot11SupportedRxAntenna_Type = TruthValue
_Dot11SupportedRxAntenna_Object = MibTableColumn
dot11SupportedRxAntenna = _Dot11SupportedRxAntenna_Object(
    (1, 2, 840, 10036, 4, 8, 1, 3),
    _Dot11SupportedRxAntenna_Type()
)
dot11SupportedRxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SupportedRxAntenna.setStatus("current")
_Dot11DiversitySelectionRx_Type = TruthValue
_Dot11DiversitySelectionRx_Object = MibTableColumn
dot11DiversitySelectionRx = _Dot11DiversitySelectionRx_Object(
    (1, 2, 840, 10036, 4, 8, 1, 4),
    _Dot11DiversitySelectionRx_Type()
)
dot11DiversitySelectionRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiversitySelectionRx.setStatus("current")
_Dot11SupportedDataRatesTxTable_Object = MibTable
dot11SupportedDataRatesTxTable = _Dot11SupportedDataRatesTxTable_Object(
    (1, 2, 840, 10036, 4, 9)
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxTable.setStatus("current")
_Dot11SupportedDataRatesTxEntry_Object = MibTableRow
dot11SupportedDataRatesTxEntry = _Dot11SupportedDataRatesTxEntry_Object(
    (1, 2, 840, 10036, 4, 9, 1)
)
dot11SupportedDataRatesTxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SupportedDataRatesTxIndex"),
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxEntry.setStatus("current")


class _Dot11SupportedDataRatesTxIndex_Type(Integer32):
    """Custom type dot11SupportedDataRatesTxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11SupportedDataRatesTxIndex_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesTxIndex_Object = MibTableColumn
dot11SupportedDataRatesTxIndex = _Dot11SupportedDataRatesTxIndex_Object(
    (1, 2, 840, 10036, 4, 9, 1, 1),
    _Dot11SupportedDataRatesTxIndex_Type()
)
dot11SupportedDataRatesTxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxIndex.setStatus("current")


class _Dot11SupportedDataRatesTxValue_Type(Integer32):
    """Custom type dot11SupportedDataRatesTxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Dot11SupportedDataRatesTxValue_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesTxValue_Object = MibTableColumn
dot11SupportedDataRatesTxValue = _Dot11SupportedDataRatesTxValue_Object(
    (1, 2, 840, 10036, 4, 9, 1, 2),
    _Dot11SupportedDataRatesTxValue_Type()
)
dot11SupportedDataRatesTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesTxValue.setStatus("current")
_Dot11SupportedDataRatesRxTable_Object = MibTable
dot11SupportedDataRatesRxTable = _Dot11SupportedDataRatesRxTable_Object(
    (1, 2, 840, 10036, 4, 10)
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxTable.setStatus("current")
_Dot11SupportedDataRatesRxEntry_Object = MibTableRow
dot11SupportedDataRatesRxEntry = _Dot11SupportedDataRatesRxEntry_Object(
    (1, 2, 840, 10036, 4, 10, 1)
)
dot11SupportedDataRatesRxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11SupportedDataRatesRxIndex"),
)
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxEntry.setStatus("current")


class _Dot11SupportedDataRatesRxIndex_Type(Integer32):
    """Custom type dot11SupportedDataRatesRxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11SupportedDataRatesRxIndex_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesRxIndex_Object = MibTableColumn
dot11SupportedDataRatesRxIndex = _Dot11SupportedDataRatesRxIndex_Object(
    (1, 2, 840, 10036, 4, 10, 1, 1),
    _Dot11SupportedDataRatesRxIndex_Type()
)
dot11SupportedDataRatesRxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxIndex.setStatus("current")


class _Dot11SupportedDataRatesRxValue_Type(Integer32):
    """Custom type dot11SupportedDataRatesRxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Dot11SupportedDataRatesRxValue_Type.__name__ = "Integer32"
_Dot11SupportedDataRatesRxValue_Object = MibTableColumn
dot11SupportedDataRatesRxValue = _Dot11SupportedDataRatesRxValue_Object(
    (1, 2, 840, 10036, 4, 10, 1, 2),
    _Dot11SupportedDataRatesRxValue_Type()
)
dot11SupportedDataRatesRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SupportedDataRatesRxValue.setStatus("current")
_Dot11PhyOFDMTable_Object = MibTable
dot11PhyOFDMTable = _Dot11PhyOFDMTable_Object(
    (1, 2, 840, 10036, 4, 11)
)
if mibBuilder.loadTexts:
    dot11PhyOFDMTable.setStatus("current")
_Dot11PhyOFDMEntry_Object = MibTableRow
dot11PhyOFDMEntry = _Dot11PhyOFDMEntry_Object(
    (1, 2, 840, 10036, 4, 11, 1)
)
dot11PhyOFDMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyOFDMEntry.setStatus("current")


class _Dot11CurrentFrequency_Type(Integer32):
    """Custom type dot11CurrentFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Dot11CurrentFrequency_Type.__name__ = "Integer32"
_Dot11CurrentFrequency_Object = MibTableColumn
dot11CurrentFrequency = _Dot11CurrentFrequency_Object(
    (1, 2, 840, 10036, 4, 11, 1, 1),
    _Dot11CurrentFrequency_Type()
)
dot11CurrentFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentFrequency.setStatus("current")
_Dot11TIThreshold_Type = Integer32
_Dot11TIThreshold_Object = MibTableColumn
dot11TIThreshold = _Dot11TIThreshold_Object(
    (1, 2, 840, 10036, 4, 11, 1, 2),
    _Dot11TIThreshold_Type()
)
dot11TIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TIThreshold.setStatus("current")


class _Dot11FrequencyBandsSupported_Type(Integer32):
    """Custom type dot11FrequencyBandsSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Dot11FrequencyBandsSupported_Type.__name__ = "Integer32"
_Dot11FrequencyBandsSupported_Object = MibTableColumn
dot11FrequencyBandsSupported = _Dot11FrequencyBandsSupported_Object(
    (1, 2, 840, 10036, 4, 11, 1, 3),
    _Dot11FrequencyBandsSupported_Type()
)
dot11FrequencyBandsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11FrequencyBandsSupported.setStatus("current")
_Dot11PhyHRDSSSTable_Object = MibTable
dot11PhyHRDSSSTable = _Dot11PhyHRDSSSTable_Object(
    (1, 2, 840, 10036, 4, 12)
)
if mibBuilder.loadTexts:
    dot11PhyHRDSSSTable.setStatus("current")
_Dot11PhyHRDSSSEntry_Object = MibTableRow
dot11PhyHRDSSSEntry = _Dot11PhyHRDSSSEntry_Object(
    (1, 2, 840, 10036, 4, 12, 1)
)
dot11PhyHRDSSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PhyHRDSSSEntry.setStatus("current")
_Dot11ShortPreambleOptionImplemented_Type = TruthValue
_Dot11ShortPreambleOptionImplemented_Object = MibTableColumn
dot11ShortPreambleOptionImplemented = _Dot11ShortPreambleOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 12, 1, 1),
    _Dot11ShortPreambleOptionImplemented_Type()
)
dot11ShortPreambleOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ShortPreambleOptionImplemented.setStatus("current")
_Dot11PBCCOptionImplemented_Type = TruthValue
_Dot11PBCCOptionImplemented_Object = MibTableColumn
dot11PBCCOptionImplemented = _Dot11PBCCOptionImplemented_Object(
    (1, 2, 840, 10036, 4, 12, 1, 2),
    _Dot11PBCCOptionImplemented_Type()
)
dot11PBCCOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PBCCOptionImplemented.setStatus("current")
_Dot11ChannelAgilityPresent_Type = TruthValue
_Dot11ChannelAgilityPresent_Object = MibTableColumn
dot11ChannelAgilityPresent = _Dot11ChannelAgilityPresent_Object(
    (1, 2, 840, 10036, 4, 12, 1, 3),
    _Dot11ChannelAgilityPresent_Type()
)
dot11ChannelAgilityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelAgilityPresent.setStatus("current")
_Dot11ChannelAgilityEnabled_Type = TruthValue
_Dot11ChannelAgilityEnabled_Object = MibTableColumn
dot11ChannelAgilityEnabled = _Dot11ChannelAgilityEnabled_Object(
    (1, 2, 840, 10036, 4, 12, 1, 4),
    _Dot11ChannelAgilityEnabled_Type()
)
dot11ChannelAgilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelAgilityEnabled.setStatus("current")


class _Dot11HRCCAModeSupported_Type(Integer32):
    """Custom type dot11HRCCAModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Dot11HRCCAModeSupported_Type.__name__ = "Integer32"
_Dot11HRCCAModeSupported_Object = MibTableColumn
dot11HRCCAModeSupported = _Dot11HRCCAModeSupported_Object(
    (1, 2, 840, 10036, 4, 12, 1, 5),
    _Dot11HRCCAModeSupported_Type()
)
dot11HRCCAModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11HRCCAModeSupported.setStatus("current")
_Dot11HoppingPatternTable_Object = MibTable
dot11HoppingPatternTable = _Dot11HoppingPatternTable_Object(
    (1, 2, 840, 10036, 4, 13)
)
if mibBuilder.loadTexts:
    dot11HoppingPatternTable.setStatus("current")
_Dot11HoppingPatternEntry_Object = MibTableRow
dot11HoppingPatternEntry = _Dot11HoppingPatternEntry_Object(
    (1, 2, 840, 10036, 4, 13, 1)
)
dot11HoppingPatternEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11HoppingPatternIndex"),
)
if mibBuilder.loadTexts:
    dot11HoppingPatternEntry.setStatus("current")
_Dot11HoppingPatternIndex_Type = Integer32
_Dot11HoppingPatternIndex_Object = MibTableColumn
dot11HoppingPatternIndex = _Dot11HoppingPatternIndex_Object(
    (1, 2, 840, 10036, 4, 13, 1, 1),
    _Dot11HoppingPatternIndex_Type()
)
dot11HoppingPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11HoppingPatternIndex.setStatus("current")
_Dot11RandomTableFieldNumber_Type = Integer32
_Dot11RandomTableFieldNumber_Object = MibTableColumn
dot11RandomTableFieldNumber = _Dot11RandomTableFieldNumber_Object(
    (1, 2, 840, 10036, 4, 13, 1, 2),
    _Dot11RandomTableFieldNumber_Type()
)
dot11RandomTableFieldNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RandomTableFieldNumber.setStatus("current")
_Dot11Conformance_ObjectIdentity = ObjectIdentity
dot11Conformance = _Dot11Conformance_ObjectIdentity(
    (1, 2, 840, 10036, 5)
)
_Dot11Groups_ObjectIdentity = ObjectIdentity
dot11Groups = _Dot11Groups_ObjectIdentity(
    (1, 2, 840, 10036, 5, 1)
)
_Dot11Compliances_ObjectIdentity = ObjectIdentity
dot11Compliances = _Dot11Compliances_ObjectIdentity(
    (1, 2, 840, 10036, 5, 2)
)

# Managed Objects groups

dot11SMTbase = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 1)
)
dot11SMTbase.setObjects(
      *(("IEEE802dot11-MIB", "dot11StationID"),
        ("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"))
)
if mibBuilder.loadTexts:
    dot11SMTbase.setStatus("deprecated")

dot11SMTprivacy = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 2)
)
dot11SMTprivacy.setObjects(
      *(("IEEE802dot11-MIB", "dot11PrivacyInvoked"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingLength"),
        ("IEEE802dot11-MIB", "dot11ExcludeUnencrypted"),
        ("IEEE802dot11-MIB", "dot11WEPICVErrorCount"),
        ("IEEE802dot11-MIB", "dot11WEPExcludedCount"),
        ("IEEE802dot11-MIB", "dot11WEPDefaultKeyID"),
        ("IEEE802dot11-MIB", "dot11WEPDefaultKeyValue"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingWEPOn"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingValue"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingAddress"),
        ("IEEE802dot11-MIB", "dot11WEPKeyMappingStatus"))
)
if mibBuilder.loadTexts:
    dot11SMTprivacy.setStatus("current")

dot11MACbase = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 3)
)
dot11MACbase.setObjects(
      *(("IEEE802dot11-MIB", "dot11MACAddress"),
        ("IEEE802dot11-MIB", "dot11Address"),
        ("IEEE802dot11-MIB", "dot11GroupAddressesStatus"),
        ("IEEE802dot11-MIB", "dot11RTSThreshold"),
        ("IEEE802dot11-MIB", "dot11ShortRetryLimit"),
        ("IEEE802dot11-MIB", "dot11LongRetryLimit"),
        ("IEEE802dot11-MIB", "dot11FragmentationThreshold"),
        ("IEEE802dot11-MIB", "dot11MaxTransmitMSDULifetime"),
        ("IEEE802dot11-MIB", "dot11MaxReceiveLifetime"),
        ("IEEE802dot11-MIB", "dot11ManufacturerID"),
        ("IEEE802dot11-MIB", "dot11ProductID"))
)
if mibBuilder.loadTexts:
    dot11MACbase.setStatus("current")

dot11MACStatistics = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 4)
)
dot11MACStatistics.setObjects(
      *(("IEEE802dot11-MIB", "dot11RetryCount"),
        ("IEEE802dot11-MIB", "dot11MultipleRetryCount"),
        ("IEEE802dot11-MIB", "dot11RTSSuccessCount"),
        ("IEEE802dot11-MIB", "dot11RTSFailureCount"),
        ("IEEE802dot11-MIB", "dot11ACKFailureCount"),
        ("IEEE802dot11-MIB", "dot11FrameDuplicateCount"))
)
if mibBuilder.loadTexts:
    dot11MACStatistics.setStatus("current")

dot11ResourceTypeID = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 5)
)
dot11ResourceTypeID.setObjects(
      *(("IEEE802dot11-MIB", "dot11ResourceTypeIDName"),
        ("IEEE802dot11-MIB", "dot11manufacturerOUI"),
        ("IEEE802dot11-MIB", "dot11manufacturerName"),
        ("IEEE802dot11-MIB", "dot11manufacturerProductName"),
        ("IEEE802dot11-MIB", "dot11manufacturerProductVersion"))
)
if mibBuilder.loadTexts:
    dot11ResourceTypeID.setStatus("current")

dot11SmtAuthenticationAlgorithms = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 6)
)
dot11SmtAuthenticationAlgorithms.setObjects(
      *(("IEEE802dot11-MIB", "dot11AuthenticationAlgorithm"),
        ("IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsEnable"))
)
if mibBuilder.loadTexts:
    dot11SmtAuthenticationAlgorithms.setStatus("current")

dot11PhyOperationComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 7)
)
dot11PhyOperationComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11PHYType"),
        ("IEEE802dot11-MIB", "dot11CurrentRegDomain"),
        ("IEEE802dot11-MIB", "dot11TempType"))
)
if mibBuilder.loadTexts:
    dot11PhyOperationComplianceGroup.setStatus("current")

dot11PhyAntennaComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 8)
)
dot11PhyAntennaComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentTxAntenna"),
        ("IEEE802dot11-MIB", "dot11DiversitySupport"),
        ("IEEE802dot11-MIB", "dot11CurrentRxAntenna"))
)
if mibBuilder.loadTexts:
    dot11PhyAntennaComplianceGroup.setStatus("current")

dot11PhyTxPowerComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 9)
)
dot11PhyTxPowerComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11NumberSupportedPowerLevels"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel1"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel2"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel3"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel4"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel5"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel6"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel7"),
        ("IEEE802dot11-MIB", "dot11TxPowerLevel8"),
        ("IEEE802dot11-MIB", "dot11CurrentTxPowerLevel"))
)
if mibBuilder.loadTexts:
    dot11PhyTxPowerComplianceGroup.setStatus("current")

dot11PhyFHSSComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 10)
)
dot11PhyFHSSComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11HopTime"),
        ("IEEE802dot11-MIB", "dot11CurrentChannelNumber"),
        ("IEEE802dot11-MIB", "dot11MaxDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentSet"),
        ("IEEE802dot11-MIB", "dot11CurrentPattern"),
        ("IEEE802dot11-MIB", "dot11CurrentIndex"))
)
if mibBuilder.loadTexts:
    dot11PhyFHSSComplianceGroup.setStatus("current")

dot11PhyDSSSComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 11)
)
dot11PhyDSSSComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentChannel"),
        ("IEEE802dot11-MIB", "dot11CCAModeSupported"),
        ("IEEE802dot11-MIB", "dot11CurrentCCAMode"),
        ("IEEE802dot11-MIB", "dot11EDThreshold"))
)
if mibBuilder.loadTexts:
    dot11PhyDSSSComplianceGroup.setStatus("current")

dot11PhyIRComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 12)
)
dot11PhyIRComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CCAWatchdogTimerMax"),
        ("IEEE802dot11-MIB", "dot11CCAWatchdogCountMax"),
        ("IEEE802dot11-MIB", "dot11CCAWatchdogTimerMin"),
        ("IEEE802dot11-MIB", "dot11CCAWatchdogCountMin"))
)
if mibBuilder.loadTexts:
    dot11PhyIRComplianceGroup.setStatus("current")

dot11PhyRegDomainsSupportGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 13)
)
dot11PhyRegDomainsSupportGroup.setObjects(
    ("IEEE802dot11-MIB", "dot11RegDomainsSupportedValue")
)
if mibBuilder.loadTexts:
    dot11PhyRegDomainsSupportGroup.setStatus("current")

dot11PhyAntennasListGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 14)
)
dot11PhyAntennasListGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11SupportedTxAntenna"),
        ("IEEE802dot11-MIB", "dot11SupportedRxAntenna"),
        ("IEEE802dot11-MIB", "dot11DiversitySelectionRx"))
)
if mibBuilder.loadTexts:
    dot11PhyAntennasListGroup.setStatus("current")

dot11PhyRateGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 15)
)
dot11PhyRateGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11SupportedDataRatesTxValue"),
        ("IEEE802dot11-MIB", "dot11SupportedDataRatesRxValue"))
)
if mibBuilder.loadTexts:
    dot11PhyRateGroup.setStatus("current")

dot11CountersGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 16)
)
dot11CountersGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11TransmittedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastTransmittedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FailedCount"),
        ("IEEE802dot11-MIB", "dot11ReceivedFragmentCount"),
        ("IEEE802dot11-MIB", "dot11MulticastReceivedFrameCount"),
        ("IEEE802dot11-MIB", "dot11FCSErrorCount"),
        ("IEEE802dot11-MIB", "dot11WEPUndecryptableCount"),
        ("IEEE802dot11-MIB", "dot11TransmittedFrameCount"))
)
if mibBuilder.loadTexts:
    dot11CountersGroup.setStatus("current")

dot11SMTbase2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 18)
)
dot11SMTbase2.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"))
)
if mibBuilder.loadTexts:
    dot11SMTbase2.setStatus("current")

dot11PhyOFDMComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 19)
)
dot11PhyOFDMComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentFrequency"),
        ("IEEE802dot11-MIB", "dot11TIThreshold"),
        ("IEEE802dot11-MIB", "dot11FrequencyBandsSupported"))
)
if mibBuilder.loadTexts:
    dot11PhyOFDMComplianceGroup.setStatus("current")

dot11SMTbase3 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 20)
)
dot11SMTbase3.setObjects(
      *(("IEEE802dot11-MIB", "dot11MediumOccupancyLimit"),
        ("IEEE802dot11-MIB", "dot11CFPollable"),
        ("IEEE802dot11-MIB", "dot11CFPPeriod"),
        ("IEEE802dot11-MIB", "dot11CFPMaxDuration"),
        ("IEEE802dot11-MIB", "dot11AuthenticationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11PrivacyOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PowerManagementMode"),
        ("IEEE802dot11-MIB", "dot11DesiredSSID"),
        ("IEEE802dot11-MIB", "dot11DesiredBSSType"),
        ("IEEE802dot11-MIB", "dot11OperationalRateSet"),
        ("IEEE802dot11-MIB", "dot11BeaconPeriod"),
        ("IEEE802dot11-MIB", "dot11DTIMPeriod"),
        ("IEEE802dot11-MIB", "dot11AssociationResponseTimeOut"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11MultiDomainCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11CountryString"))
)
if mibBuilder.loadTexts:
    dot11SMTbase3.setStatus("current")

dot11MultiDomainCapabilityGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 21)
)
dot11MultiDomainCapabilityGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11FirstChannelNumber"),
        ("IEEE802dot11-MIB", "dot11NumberofChannels"),
        ("IEEE802dot11-MIB", "dot11MaximumTransmitPowerLevel"))
)
if mibBuilder.loadTexts:
    dot11MultiDomainCapabilityGroup.setStatus("current")

dot11PhyFHSSComplianceGroup2 = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 22)
)
dot11PhyFHSSComplianceGroup2.setObjects(
      *(("IEEE802dot11-MIB", "dot11HopTime"),
        ("IEEE802dot11-MIB", "dot11CurrentChannelNumber"),
        ("IEEE802dot11-MIB", "dot11MaxDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentDwellTime"),
        ("IEEE802dot11-MIB", "dot11CurrentSet"),
        ("IEEE802dot11-MIB", "dot11CurrentPattern"),
        ("IEEE802dot11-MIB", "dot11CurrentIndex"),
        ("IEEE802dot11-MIB", "dot11EHCCPrimeRadix"),
        ("IEEE802dot11-MIB", "dot11EHCCNumberofChannelsFamilyIndex"),
        ("IEEE802dot11-MIB", "dot11EHCCCapabilityImplemented"),
        ("IEEE802dot11-MIB", "dot11EHCCCapabilityEnabled"),
        ("IEEE802dot11-MIB", "dot11HopAlgorithmAdopted"),
        ("IEEE802dot11-MIB", "dot11RandomTableFlag"),
        ("IEEE802dot11-MIB", "dot11NumberofHoppingSets"),
        ("IEEE802dot11-MIB", "dot11HopModulus"),
        ("IEEE802dot11-MIB", "dot11HopOffset"),
        ("IEEE802dot11-MIB", "dot11RandomTableFieldNumber"))
)
if mibBuilder.loadTexts:
    dot11PhyFHSSComplianceGroup2.setStatus("current")

dot11PhyHRDSSSComplianceGroup = ObjectGroup(
    (1, 2, 840, 10036, 5, 1, 23)
)
dot11PhyHRDSSSComplianceGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11CurrentChannel"),
        ("IEEE802dot11-MIB", "dot11CCAModeSupported"),
        ("IEEE802dot11-MIB", "dot11CurrentCCAMode"),
        ("IEEE802dot11-MIB", "dot11EDThreshold"),
        ("IEEE802dot11-MIB", "dot11ShortPreambleOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11PBCCOptionImplemented"),
        ("IEEE802dot11-MIB", "dot11ChannelAgilityPresent"),
        ("IEEE802dot11-MIB", "dot11ChannelAgilityEnabled"),
        ("IEEE802dot11-MIB", "dot11HRCCAModeSupported"))
)
if mibBuilder.loadTexts:
    dot11PhyHRDSSSComplianceGroup.setStatus("current")


# Notification objects

dot11Disassociate = NotificationType(
    (1, 2, 840, 10036, 1, 6, 0, 1)
)
dot11Disassociate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IEEE802dot11-MIB", "dot11DisassociateReason"),
        ("IEEE802dot11-MIB", "dot11DisassociateStation"))
)
if mibBuilder.loadTexts:
    dot11Disassociate.setStatus(
        "current"
    )

dot11Deauthenticate = NotificationType(
    (1, 2, 840, 10036, 1, 6, 0, 2)
)
dot11Deauthenticate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateReason"),
        ("IEEE802dot11-MIB", "dot11DeauthenticateStation"))
)
if mibBuilder.loadTexts:
    dot11Deauthenticate.setStatus(
        "current"
    )

dot11AuthenticateFail = NotificationType(
    (1, 2, 840, 10036, 1, 6, 0, 3)
)
dot11AuthenticateFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStatus"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFailStation"))
)
if mibBuilder.loadTexts:
    dot11AuthenticateFail.setStatus(
        "current"
    )


# Notifications groups

dot11NotificationGroup = NotificationGroup(
    (1, 2, 840, 10036, 5, 1, 17)
)
dot11NotificationGroup.setObjects(
      *(("IEEE802dot11-MIB", "dot11Disassociate"),
        ("IEEE802dot11-MIB", "dot11Deauthenticate"),
        ("IEEE802dot11-MIB", "dot11AuthenticateFail"))
)
if mibBuilder.loadTexts:
    dot11NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dot11Compliance = ModuleCompliance(
    (1, 2, 840, 10036, 5, 2, 1)
)
dot11Compliance.setObjects(
      *(("IEEE802dot11-MIB", "dot11SMTbase2"),
        ("IEEE802dot11-MIB", "dot11MACbase"),
        ("IEEE802dot11-MIB", "dot11CountersGroup"),
        ("IEEE802dot11-MIB", "dot11SmtAuthenticationAlgorithms"),
        ("IEEE802dot11-MIB", "dot11ResourceTypeID"),
        ("IEEE802dot11-MIB", "dot11PhyOperationComplianceGroup"),
        ("IEEE802dot11-MIB", "dot11PhyDSSSComplianceGroup"),
        ("IEEE802dot11-MIB", "dot11PhyIRComplianceGroup"),
        ("IEEE802dot11-MIB", "dot11PhyFHSSComplianceGroup"),
        ("IEEE802dot11-MIB", "dot11PhyOFDMComplianceGroup"),
        ("IEEE802dot11-MIB", "dot11PhyHRDSSSComplianceGroup"))
)
if mibBuilder.loadTexts:
    dot11Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE802dot11-MIB",
    **{"WEPKeytype": WEPKeytype,
       "member-body": member_body,
       "us": us,
       "ieee802dot11": ieee802dot11,
       "dot11smt": dot11smt,
       "dot11StationConfigTable": dot11StationConfigTable,
       "dot11StationConfigEntry": dot11StationConfigEntry,
       "dot11StationID": dot11StationID,
       "dot11MediumOccupancyLimit": dot11MediumOccupancyLimit,
       "dot11CFPollable": dot11CFPollable,
       "dot11CFPPeriod": dot11CFPPeriod,
       "dot11CFPMaxDuration": dot11CFPMaxDuration,
       "dot11AuthenticationResponseTimeOut": dot11AuthenticationResponseTimeOut,
       "dot11PrivacyOptionImplemented": dot11PrivacyOptionImplemented,
       "dot11PowerManagementMode": dot11PowerManagementMode,
       "dot11DesiredSSID": dot11DesiredSSID,
       "dot11DesiredBSSType": dot11DesiredBSSType,
       "dot11OperationalRateSet": dot11OperationalRateSet,
       "dot11BeaconPeriod": dot11BeaconPeriod,
       "dot11DTIMPeriod": dot11DTIMPeriod,
       "dot11AssociationResponseTimeOut": dot11AssociationResponseTimeOut,
       "dot11DisassociateReason": dot11DisassociateReason,
       "dot11DisassociateStation": dot11DisassociateStation,
       "dot11DeauthenticateReason": dot11DeauthenticateReason,
       "dot11DeauthenticateStation": dot11DeauthenticateStation,
       "dot11AuthenticateFailStatus": dot11AuthenticateFailStatus,
       "dot11AuthenticateFailStation": dot11AuthenticateFailStation,
       "dot11MultiDomainCapabilityImplemented": dot11MultiDomainCapabilityImplemented,
       "dot11MultiDomainCapabilityEnabled": dot11MultiDomainCapabilityEnabled,
       "dot11CountryString": dot11CountryString,
       "dot11AuthenticationAlgorithmsTable": dot11AuthenticationAlgorithmsTable,
       "dot11AuthenticationAlgorithmsEntry": dot11AuthenticationAlgorithmsEntry,
       "dot11AuthenticationAlgorithmsIndex": dot11AuthenticationAlgorithmsIndex,
       "dot11AuthenticationAlgorithm": dot11AuthenticationAlgorithm,
       "dot11AuthenticationAlgorithmsEnable": dot11AuthenticationAlgorithmsEnable,
       "dot11WEPDefaultKeysTable": dot11WEPDefaultKeysTable,
       "dot11WEPDefaultKeysEntry": dot11WEPDefaultKeysEntry,
       "dot11WEPDefaultKeyIndex": dot11WEPDefaultKeyIndex,
       "dot11WEPDefaultKeyValue": dot11WEPDefaultKeyValue,
       "dot11WEPKeyMappingsTable": dot11WEPKeyMappingsTable,
       "dot11WEPKeyMappingsEntry": dot11WEPKeyMappingsEntry,
       "dot11WEPKeyMappingIndex": dot11WEPKeyMappingIndex,
       "dot11WEPKeyMappingAddress": dot11WEPKeyMappingAddress,
       "dot11WEPKeyMappingWEPOn": dot11WEPKeyMappingWEPOn,
       "dot11WEPKeyMappingValue": dot11WEPKeyMappingValue,
       "dot11WEPKeyMappingStatus": dot11WEPKeyMappingStatus,
       "dot11PrivacyTable": dot11PrivacyTable,
       "dot11PrivacyEntry": dot11PrivacyEntry,
       "dot11PrivacyInvoked": dot11PrivacyInvoked,
       "dot11WEPDefaultKeyID": dot11WEPDefaultKeyID,
       "dot11WEPKeyMappingLength": dot11WEPKeyMappingLength,
       "dot11ExcludeUnencrypted": dot11ExcludeUnencrypted,
       "dot11WEPICVErrorCount": dot11WEPICVErrorCount,
       "dot11WEPExcludedCount": dot11WEPExcludedCount,
       "dot11SMTnotification": dot11SMTnotification,
       "dot11Disassociate": dot11Disassociate,
       "dot11Deauthenticate": dot11Deauthenticate,
       "dot11AuthenticateFail": dot11AuthenticateFail,
       "dot11MultiDomainCapabilityTable": dot11MultiDomainCapabilityTable,
       "dot11MultiDomainCapabilityEntry": dot11MultiDomainCapabilityEntry,
       "dot11MultiDomainCapabilityIndex": dot11MultiDomainCapabilityIndex,
       "dot11FirstChannelNumber": dot11FirstChannelNumber,
       "dot11NumberofChannels": dot11NumberofChannels,
       "dot11MaximumTransmitPowerLevel": dot11MaximumTransmitPowerLevel,
       "dot11mac": dot11mac,
       "dot11OperationTable": dot11OperationTable,
       "dot11OperationEntry": dot11OperationEntry,
       "dot11MACAddress": dot11MACAddress,
       "dot11RTSThreshold": dot11RTSThreshold,
       "dot11ShortRetryLimit": dot11ShortRetryLimit,
       "dot11LongRetryLimit": dot11LongRetryLimit,
       "dot11FragmentationThreshold": dot11FragmentationThreshold,
       "dot11MaxTransmitMSDULifetime": dot11MaxTransmitMSDULifetime,
       "dot11MaxReceiveLifetime": dot11MaxReceiveLifetime,
       "dot11ManufacturerID": dot11ManufacturerID,
       "dot11ProductID": dot11ProductID,
       "dot11CountersTable": dot11CountersTable,
       "dot11CountersEntry": dot11CountersEntry,
       "dot11TransmittedFragmentCount": dot11TransmittedFragmentCount,
       "dot11MulticastTransmittedFrameCount": dot11MulticastTransmittedFrameCount,
       "dot11FailedCount": dot11FailedCount,
       "dot11RetryCount": dot11RetryCount,
       "dot11MultipleRetryCount": dot11MultipleRetryCount,
       "dot11FrameDuplicateCount": dot11FrameDuplicateCount,
       "dot11RTSSuccessCount": dot11RTSSuccessCount,
       "dot11RTSFailureCount": dot11RTSFailureCount,
       "dot11ACKFailureCount": dot11ACKFailureCount,
       "dot11ReceivedFragmentCount": dot11ReceivedFragmentCount,
       "dot11MulticastReceivedFrameCount": dot11MulticastReceivedFrameCount,
       "dot11FCSErrorCount": dot11FCSErrorCount,
       "dot11TransmittedFrameCount": dot11TransmittedFrameCount,
       "dot11WEPUndecryptableCount": dot11WEPUndecryptableCount,
       "dot11GroupAddressesTable": dot11GroupAddressesTable,
       "dot11GroupAddressesEntry": dot11GroupAddressesEntry,
       "dot11GroupAddressesIndex": dot11GroupAddressesIndex,
       "dot11Address": dot11Address,
       "dot11GroupAddressesStatus": dot11GroupAddressesStatus,
       "dot11res": dot11res,
       "dot11resAttribute": dot11resAttribute,
       "dot11ResourceTypeIDName": dot11ResourceTypeIDName,
       "dot11ResourceInfoTable": dot11ResourceInfoTable,
       "dot11ResourceInfoEntry": dot11ResourceInfoEntry,
       "dot11manufacturerOUI": dot11manufacturerOUI,
       "dot11manufacturerName": dot11manufacturerName,
       "dot11manufacturerProductName": dot11manufacturerProductName,
       "dot11manufacturerProductVersion": dot11manufacturerProductVersion,
       "dot11phy": dot11phy,
       "dot11PhyOperationTable": dot11PhyOperationTable,
       "dot11PhyOperationEntry": dot11PhyOperationEntry,
       "dot11PHYType": dot11PHYType,
       "dot11CurrentRegDomain": dot11CurrentRegDomain,
       "dot11TempType": dot11TempType,
       "dot11PhyAntennaTable": dot11PhyAntennaTable,
       "dot11PhyAntennaEntry": dot11PhyAntennaEntry,
       "dot11CurrentTxAntenna": dot11CurrentTxAntenna,
       "dot11DiversitySupport": dot11DiversitySupport,
       "dot11CurrentRxAntenna": dot11CurrentRxAntenna,
       "dot11PhyTxPowerTable": dot11PhyTxPowerTable,
       "dot11PhyTxPowerEntry": dot11PhyTxPowerEntry,
       "dot11NumberSupportedPowerLevels": dot11NumberSupportedPowerLevels,
       "dot11TxPowerLevel1": dot11TxPowerLevel1,
       "dot11TxPowerLevel2": dot11TxPowerLevel2,
       "dot11TxPowerLevel3": dot11TxPowerLevel3,
       "dot11TxPowerLevel4": dot11TxPowerLevel4,
       "dot11TxPowerLevel5": dot11TxPowerLevel5,
       "dot11TxPowerLevel6": dot11TxPowerLevel6,
       "dot11TxPowerLevel7": dot11TxPowerLevel7,
       "dot11TxPowerLevel8": dot11TxPowerLevel8,
       "dot11CurrentTxPowerLevel": dot11CurrentTxPowerLevel,
       "dot11PhyFHSSTable": dot11PhyFHSSTable,
       "dot11PhyFHSSEntry": dot11PhyFHSSEntry,
       "dot11HopTime": dot11HopTime,
       "dot11CurrentChannelNumber": dot11CurrentChannelNumber,
       "dot11MaxDwellTime": dot11MaxDwellTime,
       "dot11CurrentDwellTime": dot11CurrentDwellTime,
       "dot11CurrentSet": dot11CurrentSet,
       "dot11CurrentPattern": dot11CurrentPattern,
       "dot11CurrentIndex": dot11CurrentIndex,
       "dot11EHCCPrimeRadix": dot11EHCCPrimeRadix,
       "dot11EHCCNumberofChannelsFamilyIndex": dot11EHCCNumberofChannelsFamilyIndex,
       "dot11EHCCCapabilityImplemented": dot11EHCCCapabilityImplemented,
       "dot11EHCCCapabilityEnabled": dot11EHCCCapabilityEnabled,
       "dot11HopAlgorithmAdopted": dot11HopAlgorithmAdopted,
       "dot11RandomTableFlag": dot11RandomTableFlag,
       "dot11NumberofHoppingSets": dot11NumberofHoppingSets,
       "dot11HopModulus": dot11HopModulus,
       "dot11HopOffset": dot11HopOffset,
       "dot11PhyDSSSTable": dot11PhyDSSSTable,
       "dot11PhyDSSSEntry": dot11PhyDSSSEntry,
       "dot11CurrentChannel": dot11CurrentChannel,
       "dot11CCAModeSupported": dot11CCAModeSupported,
       "dot11CurrentCCAMode": dot11CurrentCCAMode,
       "dot11EDThreshold": dot11EDThreshold,
       "dot11PhyIRTable": dot11PhyIRTable,
       "dot11PhyIREntry": dot11PhyIREntry,
       "dot11CCAWatchdogTimerMax": dot11CCAWatchdogTimerMax,
       "dot11CCAWatchdogCountMax": dot11CCAWatchdogCountMax,
       "dot11CCAWatchdogTimerMin": dot11CCAWatchdogTimerMin,
       "dot11CCAWatchdogCountMin": dot11CCAWatchdogCountMin,
       "dot11RegDomainsSupportedTable": dot11RegDomainsSupportedTable,
       "dot11RegDomainsSupportedEntry": dot11RegDomainsSupportedEntry,
       "dot11RegDomainsSupportedIndex": dot11RegDomainsSupportedIndex,
       "dot11RegDomainsSupportedValue": dot11RegDomainsSupportedValue,
       "dot11AntennasListTable": dot11AntennasListTable,
       "dot11AntennasListEntry": dot11AntennasListEntry,
       "dot11AntennaListIndex": dot11AntennaListIndex,
       "dot11SupportedTxAntenna": dot11SupportedTxAntenna,
       "dot11SupportedRxAntenna": dot11SupportedRxAntenna,
       "dot11DiversitySelectionRx": dot11DiversitySelectionRx,
       "dot11SupportedDataRatesTxTable": dot11SupportedDataRatesTxTable,
       "dot11SupportedDataRatesTxEntry": dot11SupportedDataRatesTxEntry,
       "dot11SupportedDataRatesTxIndex": dot11SupportedDataRatesTxIndex,
       "dot11SupportedDataRatesTxValue": dot11SupportedDataRatesTxValue,
       "dot11SupportedDataRatesRxTable": dot11SupportedDataRatesRxTable,
       "dot11SupportedDataRatesRxEntry": dot11SupportedDataRatesRxEntry,
       "dot11SupportedDataRatesRxIndex": dot11SupportedDataRatesRxIndex,
       "dot11SupportedDataRatesRxValue": dot11SupportedDataRatesRxValue,
       "dot11PhyOFDMTable": dot11PhyOFDMTable,
       "dot11PhyOFDMEntry": dot11PhyOFDMEntry,
       "dot11CurrentFrequency": dot11CurrentFrequency,
       "dot11TIThreshold": dot11TIThreshold,
       "dot11FrequencyBandsSupported": dot11FrequencyBandsSupported,
       "dot11PhyHRDSSSTable": dot11PhyHRDSSSTable,
       "dot11PhyHRDSSSEntry": dot11PhyHRDSSSEntry,
       "dot11ShortPreambleOptionImplemented": dot11ShortPreambleOptionImplemented,
       "dot11PBCCOptionImplemented": dot11PBCCOptionImplemented,
       "dot11ChannelAgilityPresent": dot11ChannelAgilityPresent,
       "dot11ChannelAgilityEnabled": dot11ChannelAgilityEnabled,
       "dot11HRCCAModeSupported": dot11HRCCAModeSupported,
       "dot11HoppingPatternTable": dot11HoppingPatternTable,
       "dot11HoppingPatternEntry": dot11HoppingPatternEntry,
       "dot11HoppingPatternIndex": dot11HoppingPatternIndex,
       "dot11RandomTableFieldNumber": dot11RandomTableFieldNumber,
       "dot11Conformance": dot11Conformance,
       "dot11Groups": dot11Groups,
       "dot11SMTbase": dot11SMTbase,
       "dot11SMTprivacy": dot11SMTprivacy,
       "dot11MACbase": dot11MACbase,
       "dot11MACStatistics": dot11MACStatistics,
       "dot11ResourceTypeID": dot11ResourceTypeID,
       "dot11SmtAuthenticationAlgorithms": dot11SmtAuthenticationAlgorithms,
       "dot11PhyOperationComplianceGroup": dot11PhyOperationComplianceGroup,
       "dot11PhyAntennaComplianceGroup": dot11PhyAntennaComplianceGroup,
       "dot11PhyTxPowerComplianceGroup": dot11PhyTxPowerComplianceGroup,
       "dot11PhyFHSSComplianceGroup": dot11PhyFHSSComplianceGroup,
       "dot11PhyDSSSComplianceGroup": dot11PhyDSSSComplianceGroup,
       "dot11PhyIRComplianceGroup": dot11PhyIRComplianceGroup,
       "dot11PhyRegDomainsSupportGroup": dot11PhyRegDomainsSupportGroup,
       "dot11PhyAntennasListGroup": dot11PhyAntennasListGroup,
       "dot11PhyRateGroup": dot11PhyRateGroup,
       "dot11CountersGroup": dot11CountersGroup,
       "dot11NotificationGroup": dot11NotificationGroup,
       "dot11SMTbase2": dot11SMTbase2,
       "dot11PhyOFDMComplianceGroup": dot11PhyOFDMComplianceGroup,
       "dot11SMTbase3": dot11SMTbase3,
       "dot11MultiDomainCapabilityGroup": dot11MultiDomainCapabilityGroup,
       "dot11PhyFHSSComplianceGroup2": dot11PhyFHSSComplianceGroup2,
       "dot11PhyHRDSSSComplianceGroup": dot11PhyHRDSSSComplianceGroup,
       "dot11Compliances": dot11Compliances,
       "dot11Compliance": dot11Compliance}
)
