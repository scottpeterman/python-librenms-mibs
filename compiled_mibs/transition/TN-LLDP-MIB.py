# SNMP MIB module (TN-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-LLDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:48 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNDisplayString,
 TNInteger64,
 TNInterfaceIndex,
 TNRowEditorState,
 TNUnsigned16,
 TNUnsigned64,
 TNUnsigned8) = mibBuilder.importSymbols(
    "TN-TC",
    "TNDisplayString",
    "TNInteger64",
    "TNInterfaceIndex",
    "TNRowEditorState",
    "TNUnsigned16",
    "TNUnsigned64",
    "TNUnsigned8")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnLldpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151)
)
if mibBuilder.loadTexts:
    tnLldpMib.setRevisions(
        ("2015-06-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNlldpAdminState(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 0),
          ("txAndRx", 1),
          ("txOnly", 2),
          ("rxOnly", 3))
    )



class TNlldpmedAltitudeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meters", 1),
          ("floors", 2))
    )



class TNlldpmedCivicAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("state", 1),
          ("county", 2),
          ("city", 3),
          ("district", 4),
          ("block", 5),
          ("street", 6),
          ("leadingStreetDirection", 16),
          ("trailingStreetSuffix", 17),
          ("streetSuffix", 18),
          ("houseNo", 19),
          ("houseNoSuffix", 20),
          ("landmark", 21),
          ("additionalInformation", 22),
          ("name", 23),
          ("zipCode", 24),
          ("building", 25),
          ("apartment", 26),
          ("floor", 27),
          ("roomNumber", 28),
          ("placeType", 29),
          ("postalCommunityName", 30),
          ("poBox", 31),
          ("additionalCode", 32))
    )



class TNlldpmedDatumType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wgs84", 1),
          ("nad83navd88", 2),
          ("nad83mllw", 3))
    )



class TNlldpmedDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 0),
          ("endpoint", 1))
    )



class TNlldpmedRemoteDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("endpointClassI", 1),
          ("endpointClassII", 2),
          ("endpointClassIII", 3),
          ("networkConnectivity", 4),
          ("reserved", 5))
    )



class TNlldpmedRemoteNetworkPolicyApplicationType(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("voice", 1),
          ("voiceSignaling", 2),
          ("guestVoice", 3),
          ("guestVoiceSignaling", 4),
          ("softphoneVoice", 5),
          ("videoConferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )



# MIB Managed Objects in the order of their OIDs

_TnLldpMibObjects_ObjectIdentity = ObjectIdentity
tnLldpMibObjects = _TnLldpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1)
)
_TnLldpConfig_ObjectIdentity = ObjectIdentity
tnLldpConfig = _TnLldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2)
)
_TnLldpConfigGlobal_ObjectIdentity = ObjectIdentity
tnLldpConfigGlobal = _TnLldpConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 1)
)
_TnLldpConfigGlobalReInitDelay_Type = TNUnsigned16
_TnLldpConfigGlobalReInitDelay_Object = MibScalar
tnLldpConfigGlobalReInitDelay = _TnLldpConfigGlobalReInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 1, 1),
    _TnLldpConfigGlobalReInitDelay_Type()
)
tnLldpConfigGlobalReInitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigGlobalReInitDelay.setStatus("current")
_TnLldpConfigGlobalMsgTxHold_Type = TNUnsigned16
_TnLldpConfigGlobalMsgTxHold_Object = MibScalar
tnLldpConfigGlobalMsgTxHold = _TnLldpConfigGlobalMsgTxHold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 1, 2),
    _TnLldpConfigGlobalMsgTxHold_Type()
)
tnLldpConfigGlobalMsgTxHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigGlobalMsgTxHold.setStatus("current")
_TnLldpConfigGlobalMsgTxInterval_Type = TNUnsigned16
_TnLldpConfigGlobalMsgTxInterval_Object = MibScalar
tnLldpConfigGlobalMsgTxInterval = _TnLldpConfigGlobalMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 1, 3),
    _TnLldpConfigGlobalMsgTxInterval_Type()
)
tnLldpConfigGlobalMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigGlobalMsgTxInterval.setStatus("current")
_TnLldpConfigGlobalTxDelay_Type = TNUnsigned16
_TnLldpConfigGlobalTxDelay_Object = MibScalar
tnLldpConfigGlobalTxDelay = _TnLldpConfigGlobalTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 1, 4),
    _TnLldpConfigGlobalTxDelay_Type()
)
tnLldpConfigGlobalTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigGlobalTxDelay.setStatus("current")
_TnLldpConfigTable_Object = MibTable
tnLldpConfigTable = _TnLldpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnLldpConfigTable.setStatus("current")
_TnLldpConfigEntry_Object = MibTableRow
tnLldpConfigEntry = _TnLldpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 2, 1)
)
tnLldpConfigEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpConfigIfIndex"),
)
if mibBuilder.loadTexts:
    tnLldpConfigEntry.setStatus("current")
_TnLldpConfigIfIndex_Type = TNInterfaceIndex
_TnLldpConfigIfIndex_Object = MibTableColumn
tnLldpConfigIfIndex = _TnLldpConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 2, 1, 1),
    _TnLldpConfigIfIndex_Type()
)
tnLldpConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpConfigIfIndex.setStatus("current")
_TnLldpConfigAdminState_Type = TNlldpAdminState
_TnLldpConfigAdminState_Object = MibTableColumn
tnLldpConfigAdminState = _TnLldpConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 2, 1, 3),
    _TnLldpConfigAdminState_Type()
)
tnLldpConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigAdminState.setStatus("current")
_TnLldpConfigCdpAware_Type = TruthValue
_TnLldpConfigCdpAware_Object = MibTableColumn
tnLldpConfigCdpAware = _TnLldpConfigCdpAware_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 2, 1, 4),
    _TnLldpConfigCdpAware_Type()
)
tnLldpConfigCdpAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigCdpAware.setStatus("current")
_TnLldpConfigOptionalTlvs_Type = TNUnsigned8
_TnLldpConfigOptionalTlvs_Object = MibTableColumn
tnLldpConfigOptionalTlvs = _TnLldpConfigOptionalTlvs_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 2, 1, 5),
    _TnLldpConfigOptionalTlvs_Type()
)
tnLldpConfigOptionalTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigOptionalTlvs.setStatus("current")
_TnLldpConfigMed_ObjectIdentity = ObjectIdentity
tnLldpConfigMed = _TnLldpConfigMed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3)
)
_TnLldpConfigMedTable_Object = MibTable
tnLldpConfigMedTable = _TnLldpConfigMedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnLldpConfigMedTable.setStatus("current")
_TnLldpConfigMedEntry_Object = MibTableRow
tnLldpConfigMedEntry = _TnLldpConfigMedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 1, 1)
)
tnLldpConfigMedEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpConfigMedIfIndex"),
)
if mibBuilder.loadTexts:
    tnLldpConfigMedEntry.setStatus("current")
_TnLldpConfigMedIfIndex_Type = TNInterfaceIndex
_TnLldpConfigMedIfIndex_Object = MibTableColumn
tnLldpConfigMedIfIndex = _TnLldpConfigMedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 1, 1, 1),
    _TnLldpConfigMedIfIndex_Type()
)
tnLldpConfigMedIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpConfigMedIfIndex.setStatus("current")
_TnLldpConfigMedOptionalTlvs_Type = TNUnsigned8
_TnLldpConfigMedOptionalTlvs_Object = MibTableColumn
tnLldpConfigMedOptionalTlvs = _TnLldpConfigMedOptionalTlvs_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 1, 1, 3),
    _TnLldpConfigMedOptionalTlvs_Type()
)
tnLldpConfigMedOptionalTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedOptionalTlvs.setStatus("current")
_TnLldpConfigMedDeviceType_Type = TNlldpmedDeviceType
_TnLldpConfigMedDeviceType_Object = MibTableColumn
tnLldpConfigMedDeviceType = _TnLldpConfigMedDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 1, 1, 4),
    _TnLldpConfigMedDeviceType_Type()
)
tnLldpConfigMedDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedDeviceType.setStatus("current")
_TnLldpConfigMedPolicyTable_Object = MibTable
tnLldpConfigMedPolicyTable = _TnLldpConfigMedPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyTable.setStatus("current")
_TnLldpConfigMedPolicyEntry_Object = MibTableRow
tnLldpConfigMedPolicyEntry = _TnLldpConfigMedPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1)
)
tnLldpConfigMedPolicyEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpConfigMedPolicyLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyEntry.setStatus("current")


class _TnLldpConfigMedPolicyLldpmedPolicy_Type(Integer32):
    """Custom type tnLldpConfigMedPolicyLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnLldpConfigMedPolicyLldpmedPolicy_Type.__name__ = "Integer32"
_TnLldpConfigMedPolicyLldpmedPolicy_Object = MibTableColumn
tnLldpConfigMedPolicyLldpmedPolicy = _TnLldpConfigMedPolicyLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 1),
    _TnLldpConfigMedPolicyLldpmedPolicy_Type()
)
tnLldpConfigMedPolicyLldpmedPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyLldpmedPolicy.setStatus("current")
_TnLldpConfigMedPolicyApplicationType_Type = TNlldpmedRemoteNetworkPolicyApplicationType
_TnLldpConfigMedPolicyApplicationType_Object = MibTableColumn
tnLldpConfigMedPolicyApplicationType = _TnLldpConfigMedPolicyApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 3),
    _TnLldpConfigMedPolicyApplicationType_Type()
)
tnLldpConfigMedPolicyApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyApplicationType.setStatus("current")
_TnLldpConfigMedPolicyTagged_Type = TruthValue
_TnLldpConfigMedPolicyTagged_Object = MibTableColumn
tnLldpConfigMedPolicyTagged = _TnLldpConfigMedPolicyTagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 4),
    _TnLldpConfigMedPolicyTagged_Type()
)
tnLldpConfigMedPolicyTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyTagged.setStatus("current")


class _TnLldpConfigMedPolicyVlanId_Type(TNUnsigned16):
    """Custom type tnLldpConfigMedPolicyVlanId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnLldpConfigMedPolicyVlanId_Type.__name__ = "TNUnsigned16"
_TnLldpConfigMedPolicyVlanId_Object = MibTableColumn
tnLldpConfigMedPolicyVlanId = _TnLldpConfigMedPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 5),
    _TnLldpConfigMedPolicyVlanId_Type()
)
tnLldpConfigMedPolicyVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyVlanId.setStatus("current")


class _TnLldpConfigMedPolicyL2Priority_Type(TNUnsigned8):
    """Custom type tnLldpConfigMedPolicyL2Priority based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnLldpConfigMedPolicyL2Priority_Type.__name__ = "TNUnsigned8"
_TnLldpConfigMedPolicyL2Priority_Object = MibTableColumn
tnLldpConfigMedPolicyL2Priority = _TnLldpConfigMedPolicyL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 6),
    _TnLldpConfigMedPolicyL2Priority_Type()
)
tnLldpConfigMedPolicyL2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyL2Priority.setStatus("current")


class _TnLldpConfigMedPolicyDscp_Type(TNUnsigned8):
    """Custom type tnLldpConfigMedPolicyDscp based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnLldpConfigMedPolicyDscp_Type.__name__ = "TNUnsigned8"
_TnLldpConfigMedPolicyDscp_Object = MibTableColumn
tnLldpConfigMedPolicyDscp = _TnLldpConfigMedPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 7),
    _TnLldpConfigMedPolicyDscp_Type()
)
tnLldpConfigMedPolicyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyDscp.setStatus("current")
_TnLldpConfigMedPolicyAction_Type = TNRowEditorState
_TnLldpConfigMedPolicyAction_Object = MibTableColumn
tnLldpConfigMedPolicyAction = _TnLldpConfigMedPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 2, 1, 100),
    _TnLldpConfigMedPolicyAction_Type()
)
tnLldpConfigMedPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyAction.setStatus("current")
_TnLldpConfigMedPolicyListTable_Object = MibTable
tnLldpConfigMedPolicyListTable = _TnLldpConfigMedPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyListTable.setStatus("current")
_TnLldpConfigMedPolicyListEntry_Object = MibTableRow
tnLldpConfigMedPolicyListEntry = _TnLldpConfigMedPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 3, 1)
)
tnLldpConfigMedPolicyListEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpConfigMedPolicyListIfIndex"),
    (0, "TN-LLDP-MIB", "tnLldpConfigMedPolicyListLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyListEntry.setStatus("current")
_TnLldpConfigMedPolicyListIfIndex_Type = TNInterfaceIndex
_TnLldpConfigMedPolicyListIfIndex_Object = MibTableColumn
tnLldpConfigMedPolicyListIfIndex = _TnLldpConfigMedPolicyListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 3, 1, 1),
    _TnLldpConfigMedPolicyListIfIndex_Type()
)
tnLldpConfigMedPolicyListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyListIfIndex.setStatus("current")


class _TnLldpConfigMedPolicyListLldpmedPolicy_Type(Integer32):
    """Custom type tnLldpConfigMedPolicyListLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnLldpConfigMedPolicyListLldpmedPolicy_Type.__name__ = "Integer32"
_TnLldpConfigMedPolicyListLldpmedPolicy_Object = MibTableColumn
tnLldpConfigMedPolicyListLldpmedPolicy = _TnLldpConfigMedPolicyListLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 3, 1, 3),
    _TnLldpConfigMedPolicyListLldpmedPolicy_Type()
)
tnLldpConfigMedPolicyListLldpmedPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyListLldpmedPolicy.setStatus("current")
_TnLldpConfigMedPolicyListLldpmedPoliciesList_Type = TruthValue
_TnLldpConfigMedPolicyListLldpmedPoliciesList_Object = MibTableColumn
tnLldpConfigMedPolicyListLldpmedPoliciesList = _TnLldpConfigMedPolicyListLldpmedPoliciesList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 3, 1, 4),
    _TnLldpConfigMedPolicyListLldpmedPoliciesList_Type()
)
tnLldpConfigMedPolicyListLldpmedPoliciesList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyListLldpmedPoliciesList.setStatus("current")
_TnLldpConfigMedGlobal_ObjectIdentity = ObjectIdentity
tnLldpConfigMedGlobal = _TnLldpConfigMedGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4)
)


class _TnLldpConfigMedGlobalFastRepeatCount_Type(TNUnsigned8):
    """Custom type tnLldpConfigMedGlobalFastRepeatCount based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnLldpConfigMedGlobalFastRepeatCount_Type.__name__ = "TNUnsigned8"
_TnLldpConfigMedGlobalFastRepeatCount_Object = MibScalar
tnLldpConfigMedGlobalFastRepeatCount = _TnLldpConfigMedGlobalFastRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 1),
    _TnLldpConfigMedGlobalFastRepeatCount_Type()
)
tnLldpConfigMedGlobalFastRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalFastRepeatCount.setStatus("current")
_TnLldpConfigMedGlobalLatitude_Type = TNInteger64
_TnLldpConfigMedGlobalLatitude_Object = MibScalar
tnLldpConfigMedGlobalLatitude = _TnLldpConfigMedGlobalLatitude_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 2),
    _TnLldpConfigMedGlobalLatitude_Type()
)
tnLldpConfigMedGlobalLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalLatitude.setStatus("current")
_TnLldpConfigMedGlobalLongitude_Type = TNInteger64
_TnLldpConfigMedGlobalLongitude_Object = MibScalar
tnLldpConfigMedGlobalLongitude = _TnLldpConfigMedGlobalLongitude_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 3),
    _TnLldpConfigMedGlobalLongitude_Type()
)
tnLldpConfigMedGlobalLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalLongitude.setStatus("current")
_TnLldpConfigMedGlobalAltitudeType_Type = TNlldpmedAltitudeType
_TnLldpConfigMedGlobalAltitudeType_Object = MibScalar
tnLldpConfigMedGlobalAltitudeType = _TnLldpConfigMedGlobalAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 4),
    _TnLldpConfigMedGlobalAltitudeType_Type()
)
tnLldpConfigMedGlobalAltitudeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalAltitudeType.setStatus("current")
_TnLldpConfigMedGlobalAltitude_Type = Integer32
_TnLldpConfigMedGlobalAltitude_Object = MibScalar
tnLldpConfigMedGlobalAltitude = _TnLldpConfigMedGlobalAltitude_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 5),
    _TnLldpConfigMedGlobalAltitude_Type()
)
tnLldpConfigMedGlobalAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalAltitude.setStatus("current")


class _TnLldpConfigMedGlobalElinAddr_Type(TNDisplayString):
    """Custom type tnLldpConfigMedGlobalElinAddr based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TnLldpConfigMedGlobalElinAddr_Type.__name__ = "TNDisplayString"
_TnLldpConfigMedGlobalElinAddr_Object = MibScalar
tnLldpConfigMedGlobalElinAddr = _TnLldpConfigMedGlobalElinAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 6),
    _TnLldpConfigMedGlobalElinAddr_Type()
)
tnLldpConfigMedGlobalElinAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalElinAddr.setStatus("current")
_TnLldpConfigMedGlobalDatum_Type = TNlldpmedDatumType
_TnLldpConfigMedGlobalDatum_Object = MibScalar
tnLldpConfigMedGlobalDatum = _TnLldpConfigMedGlobalDatum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 7),
    _TnLldpConfigMedGlobalDatum_Type()
)
tnLldpConfigMedGlobalDatum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalDatum.setStatus("current")


class _TnLldpConfigMedGlobalCountryCode_Type(TNDisplayString):
    """Custom type tnLldpConfigMedGlobalCountryCode based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TnLldpConfigMedGlobalCountryCode_Type.__name__ = "TNDisplayString"
_TnLldpConfigMedGlobalCountryCode_Object = MibScalar
tnLldpConfigMedGlobalCountryCode = _TnLldpConfigMedGlobalCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 4, 8),
    _TnLldpConfigMedGlobalCountryCode_Type()
)
tnLldpConfigMedGlobalCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalCountryCode.setStatus("current")
_TnLldpConfigMedLocationInformationTable_Object = MibTable
tnLldpConfigMedLocationInformationTable = _TnLldpConfigMedLocationInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tnLldpConfigMedLocationInformationTable.setStatus("current")
_TnLldpConfigMedLocationInformationEntry_Object = MibTableRow
tnLldpConfigMedLocationInformationEntry = _TnLldpConfigMedLocationInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 5, 1)
)
tnLldpConfigMedLocationInformationEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpConfigMedLocationInformationLldpmedIndex"),
)
if mibBuilder.loadTexts:
    tnLldpConfigMedLocationInformationEntry.setStatus("current")
_TnLldpConfigMedLocationInformationLldpmedIndex_Type = TNlldpmedCivicAddressType
_TnLldpConfigMedLocationInformationLldpmedIndex_Object = MibTableColumn
tnLldpConfigMedLocationInformationLldpmedIndex = _TnLldpConfigMedLocationInformationLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 5, 1, 2),
    _TnLldpConfigMedLocationInformationLldpmedIndex_Type()
)
tnLldpConfigMedLocationInformationLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpConfigMedLocationInformationLldpmedIndex.setStatus("current")


class _TnLldpConfigMedLocationInformationCivicAddress_Type(TNDisplayString):
    """Custom type tnLldpConfigMedLocationInformationCivicAddress based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpConfigMedLocationInformationCivicAddress_Type.__name__ = "TNDisplayString"
_TnLldpConfigMedLocationInformationCivicAddress_Object = MibTableColumn
tnLldpConfigMedLocationInformationCivicAddress = _TnLldpConfigMedLocationInformationCivicAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 5, 1, 3),
    _TnLldpConfigMedLocationInformationCivicAddress_Type()
)
tnLldpConfigMedLocationInformationCivicAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedLocationInformationCivicAddress.setStatus("current")
_TnLldpConfigMedPolicyRowEditor_ObjectIdentity = ObjectIdentity
tnLldpConfigMedPolicyRowEditor = _TnLldpConfigMedPolicyRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6)
)


class _TnLldpConfigMedPolicyRowEditorLldpmedPolicy_Type(Integer32):
    """Custom type tnLldpConfigMedPolicyRowEditorLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnLldpConfigMedPolicyRowEditorLldpmedPolicy_Type.__name__ = "Integer32"
_TnLldpConfigMedPolicyRowEditorLldpmedPolicy_Object = MibScalar
tnLldpConfigMedPolicyRowEditorLldpmedPolicy = _TnLldpConfigMedPolicyRowEditorLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 1),
    _TnLldpConfigMedPolicyRowEditorLldpmedPolicy_Type()
)
tnLldpConfigMedPolicyRowEditorLldpmedPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorLldpmedPolicy.setStatus("current")
_TnLldpConfigMedPolicyRowEditorApplicationType_Type = TNlldpmedRemoteNetworkPolicyApplicationType
_TnLldpConfigMedPolicyRowEditorApplicationType_Object = MibScalar
tnLldpConfigMedPolicyRowEditorApplicationType = _TnLldpConfigMedPolicyRowEditorApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 3),
    _TnLldpConfigMedPolicyRowEditorApplicationType_Type()
)
tnLldpConfigMedPolicyRowEditorApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorApplicationType.setStatus("current")
_TnLldpConfigMedPolicyRowEditorTagged_Type = TruthValue
_TnLldpConfigMedPolicyRowEditorTagged_Object = MibScalar
tnLldpConfigMedPolicyRowEditorTagged = _TnLldpConfigMedPolicyRowEditorTagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 4),
    _TnLldpConfigMedPolicyRowEditorTagged_Type()
)
tnLldpConfigMedPolicyRowEditorTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorTagged.setStatus("current")


class _TnLldpConfigMedPolicyRowEditorVlanId_Type(TNUnsigned16):
    """Custom type tnLldpConfigMedPolicyRowEditorVlanId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnLldpConfigMedPolicyRowEditorVlanId_Type.__name__ = "TNUnsigned16"
_TnLldpConfigMedPolicyRowEditorVlanId_Object = MibScalar
tnLldpConfigMedPolicyRowEditorVlanId = _TnLldpConfigMedPolicyRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 5),
    _TnLldpConfigMedPolicyRowEditorVlanId_Type()
)
tnLldpConfigMedPolicyRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorVlanId.setStatus("current")


class _TnLldpConfigMedPolicyRowEditorL2Priority_Type(TNUnsigned8):
    """Custom type tnLldpConfigMedPolicyRowEditorL2Priority based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnLldpConfigMedPolicyRowEditorL2Priority_Type.__name__ = "TNUnsigned8"
_TnLldpConfigMedPolicyRowEditorL2Priority_Object = MibScalar
tnLldpConfigMedPolicyRowEditorL2Priority = _TnLldpConfigMedPolicyRowEditorL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 6),
    _TnLldpConfigMedPolicyRowEditorL2Priority_Type()
)
tnLldpConfigMedPolicyRowEditorL2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorL2Priority.setStatus("current")


class _TnLldpConfigMedPolicyRowEditorDscp_Type(TNUnsigned8):
    """Custom type tnLldpConfigMedPolicyRowEditorDscp based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnLldpConfigMedPolicyRowEditorDscp_Type.__name__ = "TNUnsigned8"
_TnLldpConfigMedPolicyRowEditorDscp_Object = MibScalar
tnLldpConfigMedPolicyRowEditorDscp = _TnLldpConfigMedPolicyRowEditorDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 7),
    _TnLldpConfigMedPolicyRowEditorDscp_Type()
)
tnLldpConfigMedPolicyRowEditorDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorDscp.setStatus("current")
_TnLldpConfigMedPolicyRowEditorAction_Type = TNRowEditorState
_TnLldpConfigMedPolicyRowEditorAction_Object = MibScalar
tnLldpConfigMedPolicyRowEditorAction = _TnLldpConfigMedPolicyRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 2, 3, 6, 100),
    _TnLldpConfigMedPolicyRowEditorAction_Type()
)
tnLldpConfigMedPolicyRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorAction.setStatus("current")
_TnLldpStatus_ObjectIdentity = ObjectIdentity
tnLldpStatus = _TnLldpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3)
)
_TnLldpStatusStatistics_ObjectIdentity = ObjectIdentity
tnLldpStatusStatistics = _TnLldpStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1)
)
_TnLldpStatusStatisticsGlobalCounters_ObjectIdentity = ObjectIdentity
tnLldpStatusStatisticsGlobalCounters = _TnLldpStatusStatisticsGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 1)
)
_TnLldpStatusStatisticsGlobalCountersTableInserts_Type = Unsigned32
_TnLldpStatusStatisticsGlobalCountersTableInserts_Object = MibScalar
tnLldpStatusStatisticsGlobalCountersTableInserts = _TnLldpStatusStatisticsGlobalCountersTableInserts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 1, 1),
    _TnLldpStatusStatisticsGlobalCountersTableInserts_Type()
)
tnLldpStatusStatisticsGlobalCountersTableInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsGlobalCountersTableInserts.setStatus("current")
_TnLldpStatusStatisticsGlobalCountersTableDeletes_Type = Unsigned32
_TnLldpStatusStatisticsGlobalCountersTableDeletes_Object = MibScalar
tnLldpStatusStatisticsGlobalCountersTableDeletes = _TnLldpStatusStatisticsGlobalCountersTableDeletes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 1, 2),
    _TnLldpStatusStatisticsGlobalCountersTableDeletes_Type()
)
tnLldpStatusStatisticsGlobalCountersTableDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsGlobalCountersTableDeletes.setStatus("current")
_TnLldpStatusStatisticsGlobalCountersTableDrops_Type = Unsigned32
_TnLldpStatusStatisticsGlobalCountersTableDrops_Object = MibScalar
tnLldpStatusStatisticsGlobalCountersTableDrops = _TnLldpStatusStatisticsGlobalCountersTableDrops_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 1, 3),
    _TnLldpStatusStatisticsGlobalCountersTableDrops_Type()
)
tnLldpStatusStatisticsGlobalCountersTableDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsGlobalCountersTableDrops.setStatus("current")
_TnLldpStatusStatisticsGlobalCountersTableAgeOuts_Type = Unsigned32
_TnLldpStatusStatisticsGlobalCountersTableAgeOuts_Object = MibScalar
tnLldpStatusStatisticsGlobalCountersTableAgeOuts = _TnLldpStatusStatisticsGlobalCountersTableAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 1, 4),
    _TnLldpStatusStatisticsGlobalCountersTableAgeOuts_Type()
)
tnLldpStatusStatisticsGlobalCountersTableAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsGlobalCountersTableAgeOuts.setStatus("current")
_TnLldpStatusStatisticsGlobalCountersLastChangeTime_Type = TNUnsigned64
_TnLldpStatusStatisticsGlobalCountersLastChangeTime_Object = MibScalar
tnLldpStatusStatisticsGlobalCountersLastChangeTime = _TnLldpStatusStatisticsGlobalCountersLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 1, 5),
    _TnLldpStatusStatisticsGlobalCountersLastChangeTime_Type()
)
tnLldpStatusStatisticsGlobalCountersLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsGlobalCountersLastChangeTime.setStatus("current")
_TnLldpStatusStatisticsTable_Object = MibTable
tnLldpStatusStatisticsTable = _TnLldpStatusStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsTable.setStatus("current")
_TnLldpStatusStatisticsEntry_Object = MibTableRow
tnLldpStatusStatisticsEntry = _TnLldpStatusStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1)
)
tnLldpStatusStatisticsEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpStatusStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsEntry.setStatus("current")
_TnLldpStatusStatisticsIfIndex_Type = TNInterfaceIndex
_TnLldpStatusStatisticsIfIndex_Object = MibTableColumn
tnLldpStatusStatisticsIfIndex = _TnLldpStatusStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 1),
    _TnLldpStatusStatisticsIfIndex_Type()
)
tnLldpStatusStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsIfIndex.setStatus("current")
_TnLldpStatusStatisticsTxTotal_Type = Unsigned32
_TnLldpStatusStatisticsTxTotal_Object = MibTableColumn
tnLldpStatusStatisticsTxTotal = _TnLldpStatusStatisticsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 2),
    _TnLldpStatusStatisticsTxTotal_Type()
)
tnLldpStatusStatisticsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsTxTotal.setStatus("current")
_TnLldpStatusStatisticsRxTotal_Type = Unsigned32
_TnLldpStatusStatisticsRxTotal_Object = MibTableColumn
tnLldpStatusStatisticsRxTotal = _TnLldpStatusStatisticsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 3),
    _TnLldpStatusStatisticsRxTotal_Type()
)
tnLldpStatusStatisticsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsRxTotal.setStatus("current")
_TnLldpStatusStatisticsRxError_Type = Unsigned32
_TnLldpStatusStatisticsRxError_Object = MibTableColumn
tnLldpStatusStatisticsRxError = _TnLldpStatusStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 4),
    _TnLldpStatusStatisticsRxError_Type()
)
tnLldpStatusStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsRxError.setStatus("current")
_TnLldpStatusStatisticsRxDiscarded_Type = Unsigned32
_TnLldpStatusStatisticsRxDiscarded_Object = MibTableColumn
tnLldpStatusStatisticsRxDiscarded = _TnLldpStatusStatisticsRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 5),
    _TnLldpStatusStatisticsRxDiscarded_Type()
)
tnLldpStatusStatisticsRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsRxDiscarded.setStatus("current")
_TnLldpStatusStatisticsTLVsDiscarded_Type = Unsigned32
_TnLldpStatusStatisticsTLVsDiscarded_Object = MibTableColumn
tnLldpStatusStatisticsTLVsDiscarded = _TnLldpStatusStatisticsTLVsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 6),
    _TnLldpStatusStatisticsTLVsDiscarded_Type()
)
tnLldpStatusStatisticsTLVsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsTLVsDiscarded.setStatus("current")
_TnLldpStatusStatisticsTLVsUnrecognized_Type = Unsigned32
_TnLldpStatusStatisticsTLVsUnrecognized_Object = MibTableColumn
tnLldpStatusStatisticsTLVsUnrecognized = _TnLldpStatusStatisticsTLVsUnrecognized_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 7),
    _TnLldpStatusStatisticsTLVsUnrecognized_Type()
)
tnLldpStatusStatisticsTLVsUnrecognized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsTLVsUnrecognized.setStatus("current")
_TnLldpStatusStatisticsTLVsOrgDiscarded_Type = Unsigned32
_TnLldpStatusStatisticsTLVsOrgDiscarded_Object = MibTableColumn
tnLldpStatusStatisticsTLVsOrgDiscarded = _TnLldpStatusStatisticsTLVsOrgDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 8),
    _TnLldpStatusStatisticsTLVsOrgDiscarded_Type()
)
tnLldpStatusStatisticsTLVsOrgDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsTLVsOrgDiscarded.setStatus("current")
_TnLldpStatusStatisticsAgeOuts_Type = Unsigned32
_TnLldpStatusStatisticsAgeOuts_Object = MibTableColumn
tnLldpStatusStatisticsAgeOuts = _TnLldpStatusStatisticsAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 1, 2, 1, 9),
    _TnLldpStatusStatisticsAgeOuts_Type()
)
tnLldpStatusStatisticsAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsAgeOuts.setStatus("current")
_TnLldpStatusNeighborsInformationTable_Object = MibTable
tnLldpStatusNeighborsInformationTable = _TnLldpStatusNeighborsInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationTable.setStatus("current")
_TnLldpStatusNeighborsInformationEntry_Object = MibTableRow
tnLldpStatusNeighborsInformationEntry = _TnLldpStatusNeighborsInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1)
)
tnLldpStatusNeighborsInformationEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpStatusNeighborsInformationIfIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusNeighborsInformationLldpmedIndex"),
)
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationEntry.setStatus("current")
_TnLldpStatusNeighborsInformationIfIndex_Type = TNInterfaceIndex
_TnLldpStatusNeighborsInformationIfIndex_Object = MibTableColumn
tnLldpStatusNeighborsInformationIfIndex = _TnLldpStatusNeighborsInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 1),
    _TnLldpStatusNeighborsInformationIfIndex_Type()
)
tnLldpStatusNeighborsInformationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationIfIndex.setStatus("current")


class _TnLldpStatusNeighborsInformationLldpmedIndex_Type(Integer32):
    """Custom type tnLldpStatusNeighborsInformationLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_TnLldpStatusNeighborsInformationLldpmedIndex_Type.__name__ = "Integer32"
_TnLldpStatusNeighborsInformationLldpmedIndex_Object = MibTableColumn
tnLldpStatusNeighborsInformationLldpmedIndex = _TnLldpStatusNeighborsInformationLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 2),
    _TnLldpStatusNeighborsInformationLldpmedIndex_Type()
)
tnLldpStatusNeighborsInformationLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationLldpmedIndex.setStatus("current")


class _TnLldpStatusNeighborsInformationChassisId_Type(TNDisplayString):
    """Custom type tnLldpStatusNeighborsInformationChassisId based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnLldpStatusNeighborsInformationChassisId_Type.__name__ = "TNDisplayString"
_TnLldpStatusNeighborsInformationChassisId_Object = MibTableColumn
tnLldpStatusNeighborsInformationChassisId = _TnLldpStatusNeighborsInformationChassisId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 4),
    _TnLldpStatusNeighborsInformationChassisId_Type()
)
tnLldpStatusNeighborsInformationChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationChassisId.setStatus("current")


class _TnLldpStatusNeighborsInformationPortId_Type(TNDisplayString):
    """Custom type tnLldpStatusNeighborsInformationPortId based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnLldpStatusNeighborsInformationPortId_Type.__name__ = "TNDisplayString"
_TnLldpStatusNeighborsInformationPortId_Object = MibTableColumn
tnLldpStatusNeighborsInformationPortId = _TnLldpStatusNeighborsInformationPortId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 5),
    _TnLldpStatusNeighborsInformationPortId_Type()
)
tnLldpStatusNeighborsInformationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationPortId.setStatus("current")


class _TnLldpStatusNeighborsInformationPortDescription_Type(TNDisplayString):
    """Custom type tnLldpStatusNeighborsInformationPortDescription based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnLldpStatusNeighborsInformationPortDescription_Type.__name__ = "TNDisplayString"
_TnLldpStatusNeighborsInformationPortDescription_Object = MibTableColumn
tnLldpStatusNeighborsInformationPortDescription = _TnLldpStatusNeighborsInformationPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 6),
    _TnLldpStatusNeighborsInformationPortDescription_Type()
)
tnLldpStatusNeighborsInformationPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationPortDescription.setStatus("current")


class _TnLldpStatusNeighborsInformationSystemName_Type(TNDisplayString):
    """Custom type tnLldpStatusNeighborsInformationSystemName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnLldpStatusNeighborsInformationSystemName_Type.__name__ = "TNDisplayString"
_TnLldpStatusNeighborsInformationSystemName_Object = MibTableColumn
tnLldpStatusNeighborsInformationSystemName = _TnLldpStatusNeighborsInformationSystemName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 7),
    _TnLldpStatusNeighborsInformationSystemName_Type()
)
tnLldpStatusNeighborsInformationSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationSystemName.setStatus("current")


class _TnLldpStatusNeighborsInformationSystemDescription_Type(TNDisplayString):
    """Custom type tnLldpStatusNeighborsInformationSystemDescription based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TnLldpStatusNeighborsInformationSystemDescription_Type.__name__ = "TNDisplayString"
_TnLldpStatusNeighborsInformationSystemDescription_Object = MibTableColumn
tnLldpStatusNeighborsInformationSystemDescription = _TnLldpStatusNeighborsInformationSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 8),
    _TnLldpStatusNeighborsInformationSystemDescription_Type()
)
tnLldpStatusNeighborsInformationSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationSystemDescription.setStatus("current")
_TnLldpStatusNeighborsInformationSystemCapabilities_Type = TNUnsigned16
_TnLldpStatusNeighborsInformationSystemCapabilities_Object = MibTableColumn
tnLldpStatusNeighborsInformationSystemCapabilities = _TnLldpStatusNeighborsInformationSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 9),
    _TnLldpStatusNeighborsInformationSystemCapabilities_Type()
)
tnLldpStatusNeighborsInformationSystemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationSystemCapabilities.setStatus("current")
_TnLldpStatusNeighborsInformationSystemCapabilitiesEnable_Type = TNUnsigned16
_TnLldpStatusNeighborsInformationSystemCapabilitiesEnable_Object = MibTableColumn
tnLldpStatusNeighborsInformationSystemCapabilitiesEnable = _TnLldpStatusNeighborsInformationSystemCapabilitiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 2, 1, 10),
    _TnLldpStatusNeighborsInformationSystemCapabilitiesEnable_Type()
)
tnLldpStatusNeighborsInformationSystemCapabilitiesEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationSystemCapabilitiesEnable.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationTable_Object = MibTable
tnLldpStatusNeighborsMgmtInformationTable = _TnLldpStatusNeighborsMgmtInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationTable.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationEntry_Object = MibTableRow
tnLldpStatusNeighborsMgmtInformationEntry = _TnLldpStatusNeighborsMgmtInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1)
)
tnLldpStatusNeighborsMgmtInformationEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationIfIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationLldpmedIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationLldpManagement"),
)
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationEntry.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationIfIndex_Type = TNInterfaceIndex
_TnLldpStatusNeighborsMgmtInformationIfIndex_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationIfIndex = _TnLldpStatusNeighborsMgmtInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 1),
    _TnLldpStatusNeighborsMgmtInformationIfIndex_Type()
)
tnLldpStatusNeighborsMgmtInformationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationIfIndex.setStatus("current")


class _TnLldpStatusNeighborsMgmtInformationLldpmedIndex_Type(Integer32):
    """Custom type tnLldpStatusNeighborsMgmtInformationLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_TnLldpStatusNeighborsMgmtInformationLldpmedIndex_Type.__name__ = "Integer32"
_TnLldpStatusNeighborsMgmtInformationLldpmedIndex_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationLldpmedIndex = _TnLldpStatusNeighborsMgmtInformationLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 2),
    _TnLldpStatusNeighborsMgmtInformationLldpmedIndex_Type()
)
tnLldpStatusNeighborsMgmtInformationLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationLldpmedIndex.setStatus("current")


class _TnLldpStatusNeighborsMgmtInformationLldpManagement_Type(Integer32):
    """Custom type tnLldpStatusNeighborsMgmtInformationLldpManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnLldpStatusNeighborsMgmtInformationLldpManagement_Type.__name__ = "Integer32"
_TnLldpStatusNeighborsMgmtInformationLldpManagement_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationLldpManagement = _TnLldpStatusNeighborsMgmtInformationLldpManagement_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 4),
    _TnLldpStatusNeighborsMgmtInformationLldpManagement_Type()
)
tnLldpStatusNeighborsMgmtInformationLldpManagement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationLldpManagement.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype_Type = TNUnsigned8
_TnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype = _TnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 5),
    _TnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype_Type()
)
tnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype.setStatus("current")


class _TnLldpStatusNeighborsMgmtInformationSystemMgmtAddress_Type(TNDisplayString):
    """Custom type tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusNeighborsMgmtInformationSystemMgmtAddress_Type.__name__ = "TNDisplayString"
_TnLldpStatusNeighborsMgmtInformationSystemMgmtAddress_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress = _TnLldpStatusNeighborsMgmtInformationSystemMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 6),
    _TnLldpStatusNeighborsMgmtInformationSystemMgmtAddress_Type()
)
tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype_Type = Integer32
_TnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype = _TnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 7),
    _TnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype_Type()
)
tnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationSystemMgmtInterface_Type = Integer32
_TnLldpStatusNeighborsMgmtInformationSystemMgmtInterface_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationSystemMgmtInterface = _TnLldpStatusNeighborsMgmtInformationSystemMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 8),
    _TnLldpStatusNeighborsMgmtInformationSystemMgmtInterface_Type()
)
tnLldpStatusNeighborsMgmtInformationSystemMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationSystemMgmtInterface.setStatus("current")
_TnLldpStatusNeighborsMgmtInformationSystemMgmtOid_Type = ObjectIdentifier
_TnLldpStatusNeighborsMgmtInformationSystemMgmtOid_Object = MibTableColumn
tnLldpStatusNeighborsMgmtInformationSystemMgmtOid = _TnLldpStatusNeighborsMgmtInformationSystemMgmtOid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 3, 1, 9),
    _TnLldpStatusNeighborsMgmtInformationSystemMgmtOid_Type()
)
tnLldpStatusNeighborsMgmtInformationSystemMgmtOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationSystemMgmtOid.setStatus("current")
_TnLldpStatusMed_ObjectIdentity = ObjectIdentity
tnLldpStatusMed = _TnLldpStatusMed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4)
)
_TnLldpStatusMedRemoteDeviceInfoTable_Object = MibTable
tnLldpStatusMedRemoteDeviceInfoTable = _TnLldpStatusMedRemoteDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoTable.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoEntry_Object = MibTableRow
tnLldpStatusMedRemoteDeviceInfoEntry = _TnLldpStatusMedRemoteDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1)
)
tnLldpStatusMedRemoteDeviceInfoEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoIfIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoLldpmedIndex"),
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoEntry.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoIfIndex_Type = TNInterfaceIndex
_TnLldpStatusMedRemoteDeviceInfoIfIndex_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoIfIndex = _TnLldpStatusMedRemoteDeviceInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 1),
    _TnLldpStatusMedRemoteDeviceInfoIfIndex_Type()
)
tnLldpStatusMedRemoteDeviceInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoIfIndex.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoLldpmedIndex_Type(Integer32):
    """Custom type tnLldpStatusMedRemoteDeviceInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_TnLldpStatusMedRemoteDeviceInfoLldpmedIndex_Type.__name__ = "Integer32"
_TnLldpStatusMedRemoteDeviceInfoLldpmedIndex_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoLldpmedIndex = _TnLldpStatusMedRemoteDeviceInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 2),
    _TnLldpStatusMedRemoteDeviceInfoLldpmedIndex_Type()
)
tnLldpStatusMedRemoteDeviceInfoLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoLldpmedIndex.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoCapabilities_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoCapabilities_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoCapabilities = _TnLldpStatusMedRemoteDeviceInfoCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 4),
    _TnLldpStatusMedRemoteDeviceInfoCapabilities_Type()
)
tnLldpStatusMedRemoteDeviceInfoCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoCapabilities.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled = _TnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 5),
    _TnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled_Type()
)
tnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoLatitude_Type = TNInteger64
_TnLldpStatusMedRemoteDeviceInfoLatitude_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoLatitude = _TnLldpStatusMedRemoteDeviceInfoLatitude_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 6),
    _TnLldpStatusMedRemoteDeviceInfoLatitude_Type()
)
tnLldpStatusMedRemoteDeviceInfoLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoLatitude.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoLongitude_Type = TNInteger64
_TnLldpStatusMedRemoteDeviceInfoLongitude_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoLongitude = _TnLldpStatusMedRemoteDeviceInfoLongitude_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 7),
    _TnLldpStatusMedRemoteDeviceInfoLongitude_Type()
)
tnLldpStatusMedRemoteDeviceInfoLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoLongitude.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoAltitudeType_Type = TNlldpmedAltitudeType
_TnLldpStatusMedRemoteDeviceInfoAltitudeType_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoAltitudeType = _TnLldpStatusMedRemoteDeviceInfoAltitudeType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 8),
    _TnLldpStatusMedRemoteDeviceInfoAltitudeType_Type()
)
tnLldpStatusMedRemoteDeviceInfoAltitudeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoAltitudeType.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoAltitude_Type = Integer32
_TnLldpStatusMedRemoteDeviceInfoAltitude_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoAltitude = _TnLldpStatusMedRemoteDeviceInfoAltitude_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 9),
    _TnLldpStatusMedRemoteDeviceInfoAltitude_Type()
)
tnLldpStatusMedRemoteDeviceInfoAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoAltitude.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoDatum_Type = TNlldpmedDatumType
_TnLldpStatusMedRemoteDeviceInfoDatum_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoDatum = _TnLldpStatusMedRemoteDeviceInfoDatum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 10),
    _TnLldpStatusMedRemoteDeviceInfoDatum_Type()
)
tnLldpStatusMedRemoteDeviceInfoDatum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoDatum.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoElinaddr_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoElinaddr based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TnLldpStatusMedRemoteDeviceInfoElinaddr_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoElinaddr_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoElinaddr = _TnLldpStatusMedRemoteDeviceInfoElinaddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 11),
    _TnLldpStatusMedRemoteDeviceInfoElinaddr_Type()
)
tnLldpStatusMedRemoteDeviceInfoElinaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoElinaddr.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoDeviceType_Type = TNlldpmedRemoteDeviceType
_TnLldpStatusMedRemoteDeviceInfoDeviceType_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoDeviceType = _TnLldpStatusMedRemoteDeviceInfoDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 12),
    _TnLldpStatusMedRemoteDeviceInfoDeviceType_Type()
)
tnLldpStatusMedRemoteDeviceInfoDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoDeviceType.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoHwRev_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoHwRev based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoHwRev_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoHwRev_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoHwRev = _TnLldpStatusMedRemoteDeviceInfoHwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 13),
    _TnLldpStatusMedRemoteDeviceInfoHwRev_Type()
)
tnLldpStatusMedRemoteDeviceInfoHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoHwRev.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoFwRev_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoFwRev based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoFwRev_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoFwRev_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoFwRev = _TnLldpStatusMedRemoteDeviceInfoFwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 14),
    _TnLldpStatusMedRemoteDeviceInfoFwRev_Type()
)
tnLldpStatusMedRemoteDeviceInfoFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoFwRev.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoSwRev_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoSwRev based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoSwRev_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoSwRev_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoSwRev = _TnLldpStatusMedRemoteDeviceInfoSwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 15),
    _TnLldpStatusMedRemoteDeviceInfoSwRev_Type()
)
tnLldpStatusMedRemoteDeviceInfoSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoSwRev.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoSerialNo_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoSerialNo based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoSerialNo_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoSerialNo_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoSerialNo = _TnLldpStatusMedRemoteDeviceInfoSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 16),
    _TnLldpStatusMedRemoteDeviceInfoSerialNo_Type()
)
tnLldpStatusMedRemoteDeviceInfoSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoSerialNo.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoManufacturerName_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoManufacturerName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoManufacturerName_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoManufacturerName_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoManufacturerName = _TnLldpStatusMedRemoteDeviceInfoManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 17),
    _TnLldpStatusMedRemoteDeviceInfoManufacturerName_Type()
)
tnLldpStatusMedRemoteDeviceInfoManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoManufacturerName.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoModelName_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoModelName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoModelName_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoModelName_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoModelName = _TnLldpStatusMedRemoteDeviceInfoModelName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 18),
    _TnLldpStatusMedRemoteDeviceInfoModelName_Type()
)
tnLldpStatusMedRemoteDeviceInfoModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoModelName.setStatus("current")


class _TnLldpStatusMedRemoteDeviceInfoAssetId_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceInfoAssetId based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceInfoAssetId_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceInfoAssetId_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoAssetId = _TnLldpStatusMedRemoteDeviceInfoAssetId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 19),
    _TnLldpStatusMedRemoteDeviceInfoAssetId_Type()
)
tnLldpStatusMedRemoteDeviceInfoAssetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoAssetId.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoEeeRxTwSys_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoEeeRxTwSys_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoEeeRxTwSys = _TnLldpStatusMedRemoteDeviceInfoEeeRxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 20),
    _TnLldpStatusMedRemoteDeviceInfoEeeRxTwSys_Type()
)
tnLldpStatusMedRemoteDeviceInfoEeeRxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoEeeRxTwSys.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoEeeTxTwSys_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoEeeTxTwSys_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoEeeTxTwSys = _TnLldpStatusMedRemoteDeviceInfoEeeTxTwSys_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 21),
    _TnLldpStatusMedRemoteDeviceInfoEeeTxTwSys_Type()
)
tnLldpStatusMedRemoteDeviceInfoEeeTxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoEeeTxTwSys.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoEeeFbTwSys_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoEeeFbTwSys_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoEeeFbTwSys = _TnLldpStatusMedRemoteDeviceInfoEeeFbTwSys_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 22),
    _TnLldpStatusMedRemoteDeviceInfoEeeFbTwSys_Type()
)
tnLldpStatusMedRemoteDeviceInfoEeeFbTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoEeeFbTwSys.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho = _TnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 23),
    _TnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho_Type()
)
tnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho.setStatus("current")
_TnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Type = TNUnsigned16
_TnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho = _TnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 1, 1, 24),
    _TnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho_Type()
)
tnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho.setStatus("current")
_TnLldpStatusMedRemoteDeviceLocInfoTable_Object = MibTable
tnLldpStatusMedRemoteDeviceLocInfoTable = _TnLldpStatusMedRemoteDeviceLocInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoTable.setStatus("current")
_TnLldpStatusMedRemoteDeviceLocInfoEntry_Object = MibTableRow
tnLldpStatusMedRemoteDeviceLocInfoEntry = _TnLldpStatusMedRemoteDeviceLocInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1)
)
tnLldpStatusMedRemoteDeviceLocInfoEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoIfIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex"),
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoEntry.setStatus("current")
_TnLldpStatusMedRemoteDeviceLocInfoIfIndex_Type = TNInterfaceIndex
_TnLldpStatusMedRemoteDeviceLocInfoIfIndex_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoIfIndex = _TnLldpStatusMedRemoteDeviceLocInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 1),
    _TnLldpStatusMedRemoteDeviceLocInfoIfIndex_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoIfIndex.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Type(Integer32):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_TnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Type.__name__ = "Integer32"
_TnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex = _TnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 2),
    _TnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoState_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoState based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoState_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoState_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoState = _TnLldpStatusMedRemoteDeviceLocInfoState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 5),
    _TnLldpStatusMedRemoteDeviceLocInfoState_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoState.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoCounty_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoCounty based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoCounty_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoCounty_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoCounty = _TnLldpStatusMedRemoteDeviceLocInfoCounty_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 6),
    _TnLldpStatusMedRemoteDeviceLocInfoCounty_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoCounty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoCounty.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoCity_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoCity based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoCity_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoCity_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoCity = _TnLldpStatusMedRemoteDeviceLocInfoCity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 7),
    _TnLldpStatusMedRemoteDeviceLocInfoCity_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoCity.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoDistrict_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoDistrict based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoDistrict_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoDistrict_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoDistrict = _TnLldpStatusMedRemoteDeviceLocInfoDistrict_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 8),
    _TnLldpStatusMedRemoteDeviceLocInfoDistrict_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoDistrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoDistrict.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoBlock_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoBlock based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoBlock_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoBlock_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoBlock = _TnLldpStatusMedRemoteDeviceLocInfoBlock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 9),
    _TnLldpStatusMedRemoteDeviceLocInfoBlock_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoBlock.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoStreet_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoStreet based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoStreet_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoStreet_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoStreet = _TnLldpStatusMedRemoteDeviceLocInfoStreet_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 10),
    _TnLldpStatusMedRemoteDeviceLocInfoStreet_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoStreet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoStreet.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection = _TnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 11),
    _TnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix = _TnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 12),
    _TnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoStreetSuffix_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoStreetSuffix_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoStreetSuffix_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix = _TnLldpStatusMedRemoteDeviceLocInfoStreetSuffix_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 13),
    _TnLldpStatusMedRemoteDeviceLocInfoStreetSuffix_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoHouseNo_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoHouseNo based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoHouseNo_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoHouseNo_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoHouseNo = _TnLldpStatusMedRemoteDeviceLocInfoHouseNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 14),
    _TnLldpStatusMedRemoteDeviceLocInfoHouseNo_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoHouseNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoHouseNo.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix = _TnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 15),
    _TnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoLandmark_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoLandmark based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoLandmark_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoLandmark_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoLandmark = _TnLldpStatusMedRemoteDeviceLocInfoLandmark_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 16),
    _TnLldpStatusMedRemoteDeviceLocInfoLandmark_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoLandmark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoLandmark.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo = _TnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 17),
    _TnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoName_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoName_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoName_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoName = _TnLldpStatusMedRemoteDeviceLocInfoName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 18),
    _TnLldpStatusMedRemoteDeviceLocInfoName_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoName.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoZipCode_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoZipCode based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoZipCode_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoZipCode_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoZipCode = _TnLldpStatusMedRemoteDeviceLocInfoZipCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 19),
    _TnLldpStatusMedRemoteDeviceLocInfoZipCode_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoZipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoZipCode.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoBuilding_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoBuilding based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoBuilding_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoBuilding_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoBuilding = _TnLldpStatusMedRemoteDeviceLocInfoBuilding_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 20),
    _TnLldpStatusMedRemoteDeviceLocInfoBuilding_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoBuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoBuilding.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoApartment_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoApartment based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoApartment_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoApartment_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoApartment = _TnLldpStatusMedRemoteDeviceLocInfoApartment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 21),
    _TnLldpStatusMedRemoteDeviceLocInfoApartment_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoApartment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoApartment.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoFloor_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoFloor based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoFloor_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoFloor_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoFloor = _TnLldpStatusMedRemoteDeviceLocInfoFloor_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 22),
    _TnLldpStatusMedRemoteDeviceLocInfoFloor_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoFloor.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoRoomNumber_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoRoomNumber based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoRoomNumber_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoRoomNumber_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoRoomNumber = _TnLldpStatusMedRemoteDeviceLocInfoRoomNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 23),
    _TnLldpStatusMedRemoteDeviceLocInfoRoomNumber_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoRoomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoRoomNumber.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoPlaceType_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoPlaceType based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoPlaceType_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoPlaceType_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoPlaceType = _TnLldpStatusMedRemoteDeviceLocInfoPlaceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 24),
    _TnLldpStatusMedRemoteDeviceLocInfoPlaceType_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoPlaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoPlaceType.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName = _TnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 25),
    _TnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoPoBox_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoPoBox based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoPoBox_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoPoBox_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoPoBox = _TnLldpStatusMedRemoteDeviceLocInfoPoBox_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 26),
    _TnLldpStatusMedRemoteDeviceLocInfoPoBox_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoPoBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoPoBox.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoAdditionalCode_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_TnLldpStatusMedRemoteDeviceLocInfoAdditionalCode_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoAdditionalCode_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode = _TnLldpStatusMedRemoteDeviceLocInfoAdditionalCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 27),
    _TnLldpStatusMedRemoteDeviceLocInfoAdditionalCode_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode.setStatus("current")


class _TnLldpStatusMedRemoteDeviceLocInfoCountryCode_Type(TNDisplayString):
    """Custom type tnLldpStatusMedRemoteDeviceLocInfoCountryCode based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TnLldpStatusMedRemoteDeviceLocInfoCountryCode_Type.__name__ = "TNDisplayString"
_TnLldpStatusMedRemoteDeviceLocInfoCountryCode_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceLocInfoCountryCode = _TnLldpStatusMedRemoteDeviceLocInfoCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 2, 1, 28),
    _TnLldpStatusMedRemoteDeviceLocInfoCountryCode_Type()
)
tnLldpStatusMedRemoteDeviceLocInfoCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoCountryCode.setStatus("current")
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoTable_Object = MibTable
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTable = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTable.setStatus("current")
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry_Object = MibTableRow
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1)
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex"),
    (0, "TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy"),
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry.setStatus("current")
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Type = TNInterfaceIndex
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 1),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex.setStatus("current")


class _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type(Integer32):
    """Custom type tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type.__name__ = "Integer32"
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 2),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex.setStatus("current")


class _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Type(Integer32):
    """Custom type tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Type.__name__ = "Integer32"
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 3),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy.setStatus("current")
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Type = TNlldpmedRemoteNetworkPolicyApplicationType
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 5),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType.setStatus("current")
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Type = TruthValue
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 6),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy.setStatus("current")
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Type = TruthValue
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 7),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged.setStatus("current")


class _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Type(TNUnsigned16):
    """Custom type tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Type.__name__ = "TNUnsigned16"
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 8),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId.setStatus("current")


class _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Type(TNUnsigned8):
    """Custom type tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Type.__name__ = "TNUnsigned8"
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 9),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority.setStatus("current")


class _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Type(TNUnsigned8):
    """Custom type tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Type.__name__ = "TNUnsigned8"
_TnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Object = MibTableColumn
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp = _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 3, 4, 3, 1, 10),
    _TnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp_Type()
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp.setStatus("current")
_TnLldpControl_ObjectIdentity = ObjectIdentity
tnLldpControl = _TnLldpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4)
)
_TnLldpControlStatisticsClear_ObjectIdentity = ObjectIdentity
tnLldpControlStatisticsClear = _TnLldpControlStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1)
)
_TnLldpControlStatisticsClearTable_Object = MibTable
tnLldpControlStatisticsClearTable = _TnLldpControlStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearTable.setStatus("current")
_TnLldpControlStatisticsClearEntry_Object = MibTableRow
tnLldpControlStatisticsClearEntry = _TnLldpControlStatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1, 1, 1)
)
tnLldpControlStatisticsClearEntry.setIndexNames(
    (0, "TN-LLDP-MIB", "tnLldpControlStatisticsClearIfIndex"),
)
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearEntry.setStatus("current")
_TnLldpControlStatisticsClearIfIndex_Type = TNInterfaceIndex
_TnLldpControlStatisticsClearIfIndex_Object = MibTableColumn
tnLldpControlStatisticsClearIfIndex = _TnLldpControlStatisticsClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1, 1, 1, 1),
    _TnLldpControlStatisticsClearIfIndex_Type()
)
tnLldpControlStatisticsClearIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearIfIndex.setStatus("current")
_TnLldpControlStatisticsClearStatisticsClear_Type = TruthValue
_TnLldpControlStatisticsClearStatisticsClear_Object = MibTableColumn
tnLldpControlStatisticsClearStatisticsClear = _TnLldpControlStatisticsClearStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1, 1, 1, 2),
    _TnLldpControlStatisticsClearStatisticsClear_Type()
)
tnLldpControlStatisticsClearStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearStatisticsClear.setStatus("current")
_TnLldpControlStatisticsClearGlobal_ObjectIdentity = ObjectIdentity
tnLldpControlStatisticsClearGlobal = _TnLldpControlStatisticsClearGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1, 2)
)
_TnLldpControlStatisticsClearGlobalClear_Type = TNUnsigned8
_TnLldpControlStatisticsClearGlobalClear_Object = MibScalar
tnLldpControlStatisticsClearGlobalClear = _TnLldpControlStatisticsClearGlobalClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 1, 4, 1, 2, 1),
    _TnLldpControlStatisticsClearGlobalClear_Type()
)
tnLldpControlStatisticsClearGlobalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearGlobalClear.setStatus("current")
_TnLldpMibConformance_ObjectIdentity = ObjectIdentity
tnLldpMibConformance = _TnLldpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2)
)
_TnLldpMibCompliances_ObjectIdentity = ObjectIdentity
tnLldpMibCompliances = _TnLldpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 1)
)
_TnLldpMibGroups_ObjectIdentity = ObjectIdentity
tnLldpMibGroups = _TnLldpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2)
)

# Managed Objects groups

tnLldpConfigGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 1)
)
tnLldpConfigGlobalInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigGlobalReInitDelay"),
        ("TN-LLDP-MIB", "tnLldpConfigGlobalMsgTxHold"),
        ("TN-LLDP-MIB", "tnLldpConfigGlobalMsgTxInterval"),
        ("TN-LLDP-MIB", "tnLldpConfigGlobalTxDelay"))
)
if mibBuilder.loadTexts:
    tnLldpConfigGlobalInfoGroup.setStatus("current")

tnLldpConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 2)
)
tnLldpConfigInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigAdminState"),
        ("TN-LLDP-MIB", "tnLldpConfigCdpAware"),
        ("TN-LLDP-MIB", "tnLldpConfigOptionalTlvs"))
)
if mibBuilder.loadTexts:
    tnLldpConfigInfoGroup.setStatus("current")

tnLldpConfigMedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 3)
)
tnLldpConfigMedInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigMedOptionalTlvs"),
        ("TN-LLDP-MIB", "tnLldpConfigMedDeviceType"))
)
if mibBuilder.loadTexts:
    tnLldpConfigMedInfoGroup.setStatus("current")

tnLldpConfigMedPolicyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 4)
)
tnLldpConfigMedPolicyInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigMedPolicyApplicationType"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyTagged"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyVlanId"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyL2Priority"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyDscp"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyAction"))
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyInfoGroup.setStatus("current")

tnLldpConfigMedPolicyListInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 5)
)
tnLldpConfigMedPolicyListInfoGroup.setObjects(
    ("TN-LLDP-MIB", "tnLldpConfigMedPolicyListLldpmedPoliciesList")
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyListInfoGroup.setStatus("current")

tnLldpConfigMedGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 6)
)
tnLldpConfigMedGlobalInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigMedGlobalFastRepeatCount"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalLatitude"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalLongitude"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalAltitudeType"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalAltitude"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalElinAddr"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalDatum"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalCountryCode"))
)
if mibBuilder.loadTexts:
    tnLldpConfigMedGlobalInfoGroup.setStatus("current")

tnLldpConfigMedLocationInformationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 7)
)
tnLldpConfigMedLocationInformationInfoGroup.setObjects(
    ("TN-LLDP-MIB", "tnLldpConfigMedLocationInformationCivicAddress")
)
if mibBuilder.loadTexts:
    tnLldpConfigMedLocationInformationInfoGroup.setStatus("current")

tnLldpConfigMedPolicyRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 8)
)
tnLldpConfigMedPolicyRowEditorInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorLldpmedPolicy"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorApplicationType"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorTagged"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorVlanId"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorL2Priority"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorDscp"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnLldpConfigMedPolicyRowEditorInfoGroup.setStatus("current")

tnLldpStatusStatisticsGlobalCountersInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 9)
)
tnLldpStatusStatisticsGlobalCountersInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusStatisticsGlobalCountersTableInserts"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsGlobalCountersTableDeletes"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsGlobalCountersTableDrops"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsGlobalCountersTableAgeOuts"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsGlobalCountersLastChangeTime"))
)
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsGlobalCountersInfoGroup.setStatus("current")

tnLldpStatusStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 10)
)
tnLldpStatusStatisticsTableInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusStatisticsTxTotal"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsRxTotal"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsRxError"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsRxDiscarded"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsTLVsDiscarded"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsTLVsUnrecognized"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsTLVsOrgDiscarded"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsAgeOuts"))
)
if mibBuilder.loadTexts:
    tnLldpStatusStatisticsTableInfoGroup.setStatus("current")

tnLldpStatusNeighborsInformationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 11)
)
tnLldpStatusNeighborsInformationInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationChassisId"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationPortId"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationPortDescription"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationSystemName"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationSystemDescription"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationSystemCapabilities"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationSystemCapabilitiesEnable"))
)
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsInformationInfoGroup.setStatus("current")

tnLldpStatusNeighborsMgmtInformationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 12)
)
tnLldpStatusNeighborsMgmtInformationInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationSystemMgmtInterface"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationSystemMgmtOid"))
)
if mibBuilder.loadTexts:
    tnLldpStatusNeighborsMgmtInformationInfoGroup.setStatus("current")

tnLldpStatusMedRemoteDeviceInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 13)
)
tnLldpStatusMedRemoteDeviceInfoInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoCapabilities"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoLatitude"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoLongitude"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoAltitudeType"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoAltitude"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoDatum"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoElinaddr"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoDeviceType"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoHwRev"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoFwRev"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoSwRev"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoSerialNo"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoManufacturerName"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoModelName"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoAssetId"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoEeeRxTwSys"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoEeeTxTwSys"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoEeeFbTwSys"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho"))
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceInfoInfoGroup.setStatus("current")

tnLldpStatusMedRemoteDeviceLocInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 14)
)
tnLldpStatusMedRemoteDeviceLocInfoInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoState"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoCounty"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoCity"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoDistrict"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoBlock"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoStreet"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoHouseNo"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoLandmark"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoName"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoZipCode"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoBuilding"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoApartment"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoFloor"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoRoomNumber"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoPlaceType"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoPoBox"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoCountryCode"))
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceLocInfoInfoGroup.setStatus("current")

tnLldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 15)
)
tnLldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup.setObjects(
      *(("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp"))
)
if mibBuilder.loadTexts:
    tnLldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup.setStatus("current")

tnLldpControlStatisticsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 16)
)
tnLldpControlStatisticsClearTableInfoGroup.setObjects(
    ("TN-LLDP-MIB", "tnLldpControlStatisticsClearStatisticsClear")
)
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearTableInfoGroup.setStatus("current")

tnLldpControlStatisticsClearGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 2, 17)
)
tnLldpControlStatisticsClearGlobalInfoGroup.setObjects(
    ("TN-LLDP-MIB", "tnLldpControlStatisticsClearGlobalClear")
)
if mibBuilder.loadTexts:
    tnLldpControlStatisticsClearGlobalInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnLldpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 151, 2, 1, 1)
)
tnLldpMibCompliance.setObjects(
      *(("TN-LLDP-MIB", "tnLldpConfigGlobalInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigMedInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyListInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigMedGlobalInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigMedLocationInformationInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpConfigMedPolicyRowEditorInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsGlobalCountersInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusStatisticsTableInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsInformationInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusNeighborsMgmtInformationInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceInfoInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceLocInfoInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpControlStatisticsClearTableInfoGroup"),
        ("TN-LLDP-MIB", "tnLldpControlStatisticsClearGlobalInfoGroup"))
)
if mibBuilder.loadTexts:
    tnLldpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LLDP-MIB",
    **{"TNlldpAdminState": TNlldpAdminState,
       "TNlldpmedAltitudeType": TNlldpmedAltitudeType,
       "TNlldpmedCivicAddressType": TNlldpmedCivicAddressType,
       "TNlldpmedDatumType": TNlldpmedDatumType,
       "TNlldpmedDeviceType": TNlldpmedDeviceType,
       "TNlldpmedRemoteDeviceType": TNlldpmedRemoteDeviceType,
       "TNlldpmedRemoteNetworkPolicyApplicationType": TNlldpmedRemoteNetworkPolicyApplicationType,
       "tnLldpMib": tnLldpMib,
       "tnLldpMibObjects": tnLldpMibObjects,
       "tnLldpConfig": tnLldpConfig,
       "tnLldpConfigGlobal": tnLldpConfigGlobal,
       "tnLldpConfigGlobalReInitDelay": tnLldpConfigGlobalReInitDelay,
       "tnLldpConfigGlobalMsgTxHold": tnLldpConfigGlobalMsgTxHold,
       "tnLldpConfigGlobalMsgTxInterval": tnLldpConfigGlobalMsgTxInterval,
       "tnLldpConfigGlobalTxDelay": tnLldpConfigGlobalTxDelay,
       "tnLldpConfigTable": tnLldpConfigTable,
       "tnLldpConfigEntry": tnLldpConfigEntry,
       "tnLldpConfigIfIndex": tnLldpConfigIfIndex,
       "tnLldpConfigAdminState": tnLldpConfigAdminState,
       "tnLldpConfigCdpAware": tnLldpConfigCdpAware,
       "tnLldpConfigOptionalTlvs": tnLldpConfigOptionalTlvs,
       "tnLldpConfigMed": tnLldpConfigMed,
       "tnLldpConfigMedTable": tnLldpConfigMedTable,
       "tnLldpConfigMedEntry": tnLldpConfigMedEntry,
       "tnLldpConfigMedIfIndex": tnLldpConfigMedIfIndex,
       "tnLldpConfigMedOptionalTlvs": tnLldpConfigMedOptionalTlvs,
       "tnLldpConfigMedDeviceType": tnLldpConfigMedDeviceType,
       "tnLldpConfigMedPolicyTable": tnLldpConfigMedPolicyTable,
       "tnLldpConfigMedPolicyEntry": tnLldpConfigMedPolicyEntry,
       "tnLldpConfigMedPolicyLldpmedPolicy": tnLldpConfigMedPolicyLldpmedPolicy,
       "tnLldpConfigMedPolicyApplicationType": tnLldpConfigMedPolicyApplicationType,
       "tnLldpConfigMedPolicyTagged": tnLldpConfigMedPolicyTagged,
       "tnLldpConfigMedPolicyVlanId": tnLldpConfigMedPolicyVlanId,
       "tnLldpConfigMedPolicyL2Priority": tnLldpConfigMedPolicyL2Priority,
       "tnLldpConfigMedPolicyDscp": tnLldpConfigMedPolicyDscp,
       "tnLldpConfigMedPolicyAction": tnLldpConfigMedPolicyAction,
       "tnLldpConfigMedPolicyListTable": tnLldpConfigMedPolicyListTable,
       "tnLldpConfigMedPolicyListEntry": tnLldpConfigMedPolicyListEntry,
       "tnLldpConfigMedPolicyListIfIndex": tnLldpConfigMedPolicyListIfIndex,
       "tnLldpConfigMedPolicyListLldpmedPolicy": tnLldpConfigMedPolicyListLldpmedPolicy,
       "tnLldpConfigMedPolicyListLldpmedPoliciesList": tnLldpConfigMedPolicyListLldpmedPoliciesList,
       "tnLldpConfigMedGlobal": tnLldpConfigMedGlobal,
       "tnLldpConfigMedGlobalFastRepeatCount": tnLldpConfigMedGlobalFastRepeatCount,
       "tnLldpConfigMedGlobalLatitude": tnLldpConfigMedGlobalLatitude,
       "tnLldpConfigMedGlobalLongitude": tnLldpConfigMedGlobalLongitude,
       "tnLldpConfigMedGlobalAltitudeType": tnLldpConfigMedGlobalAltitudeType,
       "tnLldpConfigMedGlobalAltitude": tnLldpConfigMedGlobalAltitude,
       "tnLldpConfigMedGlobalElinAddr": tnLldpConfigMedGlobalElinAddr,
       "tnLldpConfigMedGlobalDatum": tnLldpConfigMedGlobalDatum,
       "tnLldpConfigMedGlobalCountryCode": tnLldpConfigMedGlobalCountryCode,
       "tnLldpConfigMedLocationInformationTable": tnLldpConfigMedLocationInformationTable,
       "tnLldpConfigMedLocationInformationEntry": tnLldpConfigMedLocationInformationEntry,
       "tnLldpConfigMedLocationInformationLldpmedIndex": tnLldpConfigMedLocationInformationLldpmedIndex,
       "tnLldpConfigMedLocationInformationCivicAddress": tnLldpConfigMedLocationInformationCivicAddress,
       "tnLldpConfigMedPolicyRowEditor": tnLldpConfigMedPolicyRowEditor,
       "tnLldpConfigMedPolicyRowEditorLldpmedPolicy": tnLldpConfigMedPolicyRowEditorLldpmedPolicy,
       "tnLldpConfigMedPolicyRowEditorApplicationType": tnLldpConfigMedPolicyRowEditorApplicationType,
       "tnLldpConfigMedPolicyRowEditorTagged": tnLldpConfigMedPolicyRowEditorTagged,
       "tnLldpConfigMedPolicyRowEditorVlanId": tnLldpConfigMedPolicyRowEditorVlanId,
       "tnLldpConfigMedPolicyRowEditorL2Priority": tnLldpConfigMedPolicyRowEditorL2Priority,
       "tnLldpConfigMedPolicyRowEditorDscp": tnLldpConfigMedPolicyRowEditorDscp,
       "tnLldpConfigMedPolicyRowEditorAction": tnLldpConfigMedPolicyRowEditorAction,
       "tnLldpStatus": tnLldpStatus,
       "tnLldpStatusStatistics": tnLldpStatusStatistics,
       "tnLldpStatusStatisticsGlobalCounters": tnLldpStatusStatisticsGlobalCounters,
       "tnLldpStatusStatisticsGlobalCountersTableInserts": tnLldpStatusStatisticsGlobalCountersTableInserts,
       "tnLldpStatusStatisticsGlobalCountersTableDeletes": tnLldpStatusStatisticsGlobalCountersTableDeletes,
       "tnLldpStatusStatisticsGlobalCountersTableDrops": tnLldpStatusStatisticsGlobalCountersTableDrops,
       "tnLldpStatusStatisticsGlobalCountersTableAgeOuts": tnLldpStatusStatisticsGlobalCountersTableAgeOuts,
       "tnLldpStatusStatisticsGlobalCountersLastChangeTime": tnLldpStatusStatisticsGlobalCountersLastChangeTime,
       "tnLldpStatusStatisticsTable": tnLldpStatusStatisticsTable,
       "tnLldpStatusStatisticsEntry": tnLldpStatusStatisticsEntry,
       "tnLldpStatusStatisticsIfIndex": tnLldpStatusStatisticsIfIndex,
       "tnLldpStatusStatisticsTxTotal": tnLldpStatusStatisticsTxTotal,
       "tnLldpStatusStatisticsRxTotal": tnLldpStatusStatisticsRxTotal,
       "tnLldpStatusStatisticsRxError": tnLldpStatusStatisticsRxError,
       "tnLldpStatusStatisticsRxDiscarded": tnLldpStatusStatisticsRxDiscarded,
       "tnLldpStatusStatisticsTLVsDiscarded": tnLldpStatusStatisticsTLVsDiscarded,
       "tnLldpStatusStatisticsTLVsUnrecognized": tnLldpStatusStatisticsTLVsUnrecognized,
       "tnLldpStatusStatisticsTLVsOrgDiscarded": tnLldpStatusStatisticsTLVsOrgDiscarded,
       "tnLldpStatusStatisticsAgeOuts": tnLldpStatusStatisticsAgeOuts,
       "tnLldpStatusNeighborsInformationTable": tnLldpStatusNeighborsInformationTable,
       "tnLldpStatusNeighborsInformationEntry": tnLldpStatusNeighborsInformationEntry,
       "tnLldpStatusNeighborsInformationIfIndex": tnLldpStatusNeighborsInformationIfIndex,
       "tnLldpStatusNeighborsInformationLldpmedIndex": tnLldpStatusNeighborsInformationLldpmedIndex,
       "tnLldpStatusNeighborsInformationChassisId": tnLldpStatusNeighborsInformationChassisId,
       "tnLldpStatusNeighborsInformationPortId": tnLldpStatusNeighborsInformationPortId,
       "tnLldpStatusNeighborsInformationPortDescription": tnLldpStatusNeighborsInformationPortDescription,
       "tnLldpStatusNeighborsInformationSystemName": tnLldpStatusNeighborsInformationSystemName,
       "tnLldpStatusNeighborsInformationSystemDescription": tnLldpStatusNeighborsInformationSystemDescription,
       "tnLldpStatusNeighborsInformationSystemCapabilities": tnLldpStatusNeighborsInformationSystemCapabilities,
       "tnLldpStatusNeighborsInformationSystemCapabilitiesEnable": tnLldpStatusNeighborsInformationSystemCapabilitiesEnable,
       "tnLldpStatusNeighborsMgmtInformationTable": tnLldpStatusNeighborsMgmtInformationTable,
       "tnLldpStatusNeighborsMgmtInformationEntry": tnLldpStatusNeighborsMgmtInformationEntry,
       "tnLldpStatusNeighborsMgmtInformationIfIndex": tnLldpStatusNeighborsMgmtInformationIfIndex,
       "tnLldpStatusNeighborsMgmtInformationLldpmedIndex": tnLldpStatusNeighborsMgmtInformationLldpmedIndex,
       "tnLldpStatusNeighborsMgmtInformationLldpManagement": tnLldpStatusNeighborsMgmtInformationLldpManagement,
       "tnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype": tnLldpStatusNeighborsMgmtInformationSystemMgmAddressSubtype,
       "tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress": tnLldpStatusNeighborsMgmtInformationSystemMgmtAddress,
       "tnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype": tnLldpStatusNeighborsMgmtInformationSystemMgmtInterfaceSubtype,
       "tnLldpStatusNeighborsMgmtInformationSystemMgmtInterface": tnLldpStatusNeighborsMgmtInformationSystemMgmtInterface,
       "tnLldpStatusNeighborsMgmtInformationSystemMgmtOid": tnLldpStatusNeighborsMgmtInformationSystemMgmtOid,
       "tnLldpStatusMed": tnLldpStatusMed,
       "tnLldpStatusMedRemoteDeviceInfoTable": tnLldpStatusMedRemoteDeviceInfoTable,
       "tnLldpStatusMedRemoteDeviceInfoEntry": tnLldpStatusMedRemoteDeviceInfoEntry,
       "tnLldpStatusMedRemoteDeviceInfoIfIndex": tnLldpStatusMedRemoteDeviceInfoIfIndex,
       "tnLldpStatusMedRemoteDeviceInfoLldpmedIndex": tnLldpStatusMedRemoteDeviceInfoLldpmedIndex,
       "tnLldpStatusMedRemoteDeviceInfoCapabilities": tnLldpStatusMedRemoteDeviceInfoCapabilities,
       "tnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled": tnLldpStatusMedRemoteDeviceInfoCapabilitiesEnabled,
       "tnLldpStatusMedRemoteDeviceInfoLatitude": tnLldpStatusMedRemoteDeviceInfoLatitude,
       "tnLldpStatusMedRemoteDeviceInfoLongitude": tnLldpStatusMedRemoteDeviceInfoLongitude,
       "tnLldpStatusMedRemoteDeviceInfoAltitudeType": tnLldpStatusMedRemoteDeviceInfoAltitudeType,
       "tnLldpStatusMedRemoteDeviceInfoAltitude": tnLldpStatusMedRemoteDeviceInfoAltitude,
       "tnLldpStatusMedRemoteDeviceInfoDatum": tnLldpStatusMedRemoteDeviceInfoDatum,
       "tnLldpStatusMedRemoteDeviceInfoElinaddr": tnLldpStatusMedRemoteDeviceInfoElinaddr,
       "tnLldpStatusMedRemoteDeviceInfoDeviceType": tnLldpStatusMedRemoteDeviceInfoDeviceType,
       "tnLldpStatusMedRemoteDeviceInfoHwRev": tnLldpStatusMedRemoteDeviceInfoHwRev,
       "tnLldpStatusMedRemoteDeviceInfoFwRev": tnLldpStatusMedRemoteDeviceInfoFwRev,
       "tnLldpStatusMedRemoteDeviceInfoSwRev": tnLldpStatusMedRemoteDeviceInfoSwRev,
       "tnLldpStatusMedRemoteDeviceInfoSerialNo": tnLldpStatusMedRemoteDeviceInfoSerialNo,
       "tnLldpStatusMedRemoteDeviceInfoManufacturerName": tnLldpStatusMedRemoteDeviceInfoManufacturerName,
       "tnLldpStatusMedRemoteDeviceInfoModelName": tnLldpStatusMedRemoteDeviceInfoModelName,
       "tnLldpStatusMedRemoteDeviceInfoAssetId": tnLldpStatusMedRemoteDeviceInfoAssetId,
       "tnLldpStatusMedRemoteDeviceInfoEeeRxTwSys": tnLldpStatusMedRemoteDeviceInfoEeeRxTwSys,
       "tnLldpStatusMedRemoteDeviceInfoEeeTxTwSys": tnLldpStatusMedRemoteDeviceInfoEeeTxTwSys,
       "tnLldpStatusMedRemoteDeviceInfoEeeFbTwSys": tnLldpStatusMedRemoteDeviceInfoEeeFbTwSys,
       "tnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho": tnLldpStatusMedRemoteDeviceInfoEeeTxTwSysEcho,
       "tnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho": tnLldpStatusMedRemoteDeviceInfoEeeRxTwSysEcho,
       "tnLldpStatusMedRemoteDeviceLocInfoTable": tnLldpStatusMedRemoteDeviceLocInfoTable,
       "tnLldpStatusMedRemoteDeviceLocInfoEntry": tnLldpStatusMedRemoteDeviceLocInfoEntry,
       "tnLldpStatusMedRemoteDeviceLocInfoIfIndex": tnLldpStatusMedRemoteDeviceLocInfoIfIndex,
       "tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex": tnLldpStatusMedRemoteDeviceLocInfoLldpmedIndex,
       "tnLldpStatusMedRemoteDeviceLocInfoState": tnLldpStatusMedRemoteDeviceLocInfoState,
       "tnLldpStatusMedRemoteDeviceLocInfoCounty": tnLldpStatusMedRemoteDeviceLocInfoCounty,
       "tnLldpStatusMedRemoteDeviceLocInfoCity": tnLldpStatusMedRemoteDeviceLocInfoCity,
       "tnLldpStatusMedRemoteDeviceLocInfoDistrict": tnLldpStatusMedRemoteDeviceLocInfoDistrict,
       "tnLldpStatusMedRemoteDeviceLocInfoBlock": tnLldpStatusMedRemoteDeviceLocInfoBlock,
       "tnLldpStatusMedRemoteDeviceLocInfoStreet": tnLldpStatusMedRemoteDeviceLocInfoStreet,
       "tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection": tnLldpStatusMedRemoteDeviceLocInfoLeadingStreetDirection,
       "tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix": tnLldpStatusMedRemoteDeviceLocInfoTrailingStreetSuffix,
       "tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix": tnLldpStatusMedRemoteDeviceLocInfoStreetSuffix,
       "tnLldpStatusMedRemoteDeviceLocInfoHouseNo": tnLldpStatusMedRemoteDeviceLocInfoHouseNo,
       "tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix": tnLldpStatusMedRemoteDeviceLocInfoHouseNoSuffix,
       "tnLldpStatusMedRemoteDeviceLocInfoLandmark": tnLldpStatusMedRemoteDeviceLocInfoLandmark,
       "tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo": tnLldpStatusMedRemoteDeviceLocInfoAdditionalInfo,
       "tnLldpStatusMedRemoteDeviceLocInfoName": tnLldpStatusMedRemoteDeviceLocInfoName,
       "tnLldpStatusMedRemoteDeviceLocInfoZipCode": tnLldpStatusMedRemoteDeviceLocInfoZipCode,
       "tnLldpStatusMedRemoteDeviceLocInfoBuilding": tnLldpStatusMedRemoteDeviceLocInfoBuilding,
       "tnLldpStatusMedRemoteDeviceLocInfoApartment": tnLldpStatusMedRemoteDeviceLocInfoApartment,
       "tnLldpStatusMedRemoteDeviceLocInfoFloor": tnLldpStatusMedRemoteDeviceLocInfoFloor,
       "tnLldpStatusMedRemoteDeviceLocInfoRoomNumber": tnLldpStatusMedRemoteDeviceLocInfoRoomNumber,
       "tnLldpStatusMedRemoteDeviceLocInfoPlaceType": tnLldpStatusMedRemoteDeviceLocInfoPlaceType,
       "tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName": tnLldpStatusMedRemoteDeviceLocInfoPostalCommunityName,
       "tnLldpStatusMedRemoteDeviceLocInfoPoBox": tnLldpStatusMedRemoteDeviceLocInfoPoBox,
       "tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode": tnLldpStatusMedRemoteDeviceLocInfoAdditionalCode,
       "tnLldpStatusMedRemoteDeviceLocInfoCountryCode": tnLldpStatusMedRemoteDeviceLocInfoCountryCode,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTable": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTable,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoEntry,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoIfIndex,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedIndex,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoLldpmedPolicy,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoApplicationType,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoUnknownPolicy,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoTagged,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoVlanId,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoL2Priority,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoDscp,
       "tnLldpControl": tnLldpControl,
       "tnLldpControlStatisticsClear": tnLldpControlStatisticsClear,
       "tnLldpControlStatisticsClearTable": tnLldpControlStatisticsClearTable,
       "tnLldpControlStatisticsClearEntry": tnLldpControlStatisticsClearEntry,
       "tnLldpControlStatisticsClearIfIndex": tnLldpControlStatisticsClearIfIndex,
       "tnLldpControlStatisticsClearStatisticsClear": tnLldpControlStatisticsClearStatisticsClear,
       "tnLldpControlStatisticsClearGlobal": tnLldpControlStatisticsClearGlobal,
       "tnLldpControlStatisticsClearGlobalClear": tnLldpControlStatisticsClearGlobalClear,
       "tnLldpMibConformance": tnLldpMibConformance,
       "tnLldpMibCompliances": tnLldpMibCompliances,
       "tnLldpMibCompliance": tnLldpMibCompliance,
       "tnLldpMibGroups": tnLldpMibGroups,
       "tnLldpConfigGlobalInfoGroup": tnLldpConfigGlobalInfoGroup,
       "tnLldpConfigInfoGroup": tnLldpConfigInfoGroup,
       "tnLldpConfigMedInfoGroup": tnLldpConfigMedInfoGroup,
       "tnLldpConfigMedPolicyInfoGroup": tnLldpConfigMedPolicyInfoGroup,
       "tnLldpConfigMedPolicyListInfoGroup": tnLldpConfigMedPolicyListInfoGroup,
       "tnLldpConfigMedGlobalInfoGroup": tnLldpConfigMedGlobalInfoGroup,
       "tnLldpConfigMedLocationInformationInfoGroup": tnLldpConfigMedLocationInformationInfoGroup,
       "tnLldpConfigMedPolicyRowEditorInfoGroup": tnLldpConfigMedPolicyRowEditorInfoGroup,
       "tnLldpStatusStatisticsGlobalCountersInfoGroup": tnLldpStatusStatisticsGlobalCountersInfoGroup,
       "tnLldpStatusStatisticsTableInfoGroup": tnLldpStatusStatisticsTableInfoGroup,
       "tnLldpStatusNeighborsInformationInfoGroup": tnLldpStatusNeighborsInformationInfoGroup,
       "tnLldpStatusNeighborsMgmtInformationInfoGroup": tnLldpStatusNeighborsMgmtInformationInfoGroup,
       "tnLldpStatusMedRemoteDeviceInfoInfoGroup": tnLldpStatusMedRemoteDeviceInfoInfoGroup,
       "tnLldpStatusMedRemoteDeviceLocInfoInfoGroup": tnLldpStatusMedRemoteDeviceLocInfoInfoGroup,
       "tnLldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup": tnLldpStatusMedRemoteDeviceNetworkPolicyInfoInfoGroup,
       "tnLldpControlStatisticsClearTableInfoGroup": tnLldpControlStatisticsClearTableInfoGroup,
       "tnLldpControlStatisticsClearGlobalInfoGroup": tnLldpControlStatisticsClearGlobalInfoGroup}
)
