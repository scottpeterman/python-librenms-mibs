# SNMP MIB module (CIENA-CES-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:32 2025
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

(cienaCesChassisSystemId,) = mibBuilder.importSymbols(
    "CIENA-CES-CHASSIS-MIB",
    "cienaCesChassisSystemId")

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation",
    "sysName")

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

cienaCesPortConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesPortConfigMIB.setRevisions(
        ("2018-12-18 00:00",
         "2018-11-12 00:00",
         "2018-10-09 00:00",
         "2018-06-12 00:00",
         "2017-06-07 00:00",
         "2017-05-19 00:00",
         "2017-05-08 00:00",
         "2016-10-24 00:00",
         "2015-07-03 00:00",
         "2015-06-23 00:00",
         "2015-05-15 00:00",
         "2015-05-05 00:00",
         "2015-05-01 00:00",
         "2014-07-30 00:00",
         "2014-11-28 00:00",
         "2014-04-14 00:00",
         "2014-04-11 00:00",
         "2014-04-01 00:00",
         "2013-08-22 00:00",
         "2013-08-06 00:00",
         "2013-07-31 00:00",
         "2013-07-16 00:00",
         "2013-07-15 00:00",
         "2013-03-05 00:00",
         "2012-08-01 00:00",
         "2011-06-01 00:00",
         "2010-03-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EttpDuplexPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )



class EttpAdvertisedFlowControlPolicy(TextualConvention, Integer32):
    status = "current"
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
        *(("off", 1),
          ("asym-tx", 2),
          ("sym", 3),
          ("sym-asym-rx", 4))
    )



class EttpFlowControlPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("asym-tx", 2),
          ("sym", 3),
          ("asym-rx", 5))
    )



class EttpAutoNegPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class PortPriorityTagPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leave-tag", 1),
          ("strip-tag", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesPortConfigMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesPortConfigMIBObjects = _CienaCesPortConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1)
)
_CienaCesPortConfig_ObjectIdentity = ObjectIdentity
cienaCesPortConfig = _CienaCesPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1)
)
_CienaCesLogicalPortConfigTable_Object = MibTable
cienaCesLogicalPortConfigTable = _CienaCesLogicalPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigTable.setStatus("current")
_CienaCesLogicalPortConfigEntry_Object = MibTableRow
cienaCesLogicalPortConfigEntry = _CienaCesLogicalPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1)
)
cienaCesLogicalPortConfigEntry.setIndexNames(
    (0, "CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPgId"),
)
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigEntry.setStatus("current")


class _CienaCesLogicalPortConfigPgId_Type(Unsigned32):
    """Custom type cienaCesLogicalPortConfigPgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesLogicalPortConfigPgId_Type.__name__ = "Unsigned32"
_CienaCesLogicalPortConfigPgId_Object = MibTableColumn
cienaCesLogicalPortConfigPgId = _CienaCesLogicalPortConfigPgId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 1),
    _CienaCesLogicalPortConfigPgId_Type()
)
cienaCesLogicalPortConfigPgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPgId.setStatus("current")
_CienaCesLogicalPortConfigPortAdminState_Type = CienaGlobalState
_CienaCesLogicalPortConfigPortAdminState_Object = MibTableColumn
cienaCesLogicalPortConfigPortAdminState = _CienaCesLogicalPortConfigPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 2),
    _CienaCesLogicalPortConfigPortAdminState_Type()
)
cienaCesLogicalPortConfigPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortAdminState.setStatus("current")


class _CienaCesLogicalPortConfigPortOperState_Type(Integer32):
    """Custom type cienaCesLogicalPortConfigPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("enabled", 2),
          ("disabled", 3),
          ("notAuthenticated", 4),
          ("loopbackTx", 5),
          ("loopbackRx", 6),
          ("unequipped", 7))
    )


_CienaCesLogicalPortConfigPortOperState_Type.__name__ = "Integer32"
_CienaCesLogicalPortConfigPortOperState_Object = MibTableColumn
cienaCesLogicalPortConfigPortOperState = _CienaCesLogicalPortConfigPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 3),
    _CienaCesLogicalPortConfigPortOperState_Type()
)
cienaCesLogicalPortConfigPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortOperState.setStatus("current")


class _CienaCesLogicalPortConfigPortLinkUpDownTrapState_Type(CienaGlobalState):
    """Custom type cienaCesLogicalPortConfigPortLinkUpDownTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesLogicalPortConfigPortLinkUpDownTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesLogicalPortConfigPortLinkUpDownTrapState_Object = MibTableColumn
cienaCesLogicalPortConfigPortLinkUpDownTrapState = _CienaCesLogicalPortConfigPortLinkUpDownTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 4),
    _CienaCesLogicalPortConfigPortLinkUpDownTrapState_Type()
)
cienaCesLogicalPortConfigPortLinkUpDownTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortLinkUpDownTrapState.setStatus("current")


class _CienaCesLogicalPortConfigPortAllTrapState_Type(CienaGlobalState):
    """Custom type cienaCesLogicalPortConfigPortAllTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesLogicalPortConfigPortAllTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesLogicalPortConfigPortAllTrapState_Object = MibTableColumn
cienaCesLogicalPortConfigPortAllTrapState = _CienaCesLogicalPortConfigPortAllTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 5),
    _CienaCesLogicalPortConfigPortAllTrapState_Type()
)
cienaCesLogicalPortConfigPortAllTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortAllTrapState.setStatus("current")
_CienaCesLogicalPortConfigPortPortMacAddress_Type = MacAddress
_CienaCesLogicalPortConfigPortPortMacAddress_Object = MibTableColumn
cienaCesLogicalPortConfigPortPortMacAddress = _CienaCesLogicalPortConfigPortPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 6),
    _CienaCesLogicalPortConfigPortPortMacAddress_Type()
)
cienaCesLogicalPortConfigPortPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortPortMacAddress.setStatus("current")


class _CienaCesLogicalPortConfigPortName_Type(DisplayString):
    """Custom type cienaCesLogicalPortConfigPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLogicalPortConfigPortName_Type.__name__ = "DisplayString"
_CienaCesLogicalPortConfigPortName_Object = MibTableColumn
cienaCesLogicalPortConfigPortName = _CienaCesLogicalPortConfigPortName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 7),
    _CienaCesLogicalPortConfigPortName_Type()
)
cienaCesLogicalPortConfigPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortName.setStatus("current")


class _CienaCesLogicalPortConfigPortDesc_Type(DisplayString):
    """Custom type cienaCesLogicalPortConfigPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CienaCesLogicalPortConfigPortDesc_Type.__name__ = "DisplayString"
_CienaCesLogicalPortConfigPortDesc_Object = MibTableColumn
cienaCesLogicalPortConfigPortDesc = _CienaCesLogicalPortConfigPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 8),
    _CienaCesLogicalPortConfigPortDesc_Type()
)
cienaCesLogicalPortConfigPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortDesc.setStatus("current")


class _CienaCesLogicalPortConfigPortType_Type(Integer32):
    """Custom type cienaCesLogicalPortConfigPortType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ethernet", 2),
          ("fastEthernet", 3),
          ("hundredFx", 4),
          ("gigEthernet", 5),
          ("lagPort", 6),
          ("gigHundredFx", 7),
          ("tripleSpeed", 8),
          ("tenGigEthernet", 9),
          ("vmTripleSpeedTX", 10),
          ("sonetOc3", 11),
          ("sonetOc12", 12),
          ("sonetOc48", 13),
          ("sonetOc192", 14),
          ("fortyGigEthernet", 15),
          ("hundredGigEthernet", 16),
          ("odu", 17),
          ("ethLp", 18),
          ("twoPointFiveGigEthernet", 19),
          ("odu4", 20))
    )


_CienaCesLogicalPortConfigPortType_Type.__name__ = "Integer32"
_CienaCesLogicalPortConfigPortType_Object = MibTableColumn
cienaCesLogicalPortConfigPortType = _CienaCesLogicalPortConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 9),
    _CienaCesLogicalPortConfigPortType_Type()
)
cienaCesLogicalPortConfigPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortType.setStatus("current")
_CienaCesLogicalPortConfigPortIfIndex_Type = Integer32
_CienaCesLogicalPortConfigPortIfIndex_Object = MibTableColumn
cienaCesLogicalPortConfigPortIfIndex = _CienaCesLogicalPortConfigPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 10),
    _CienaCesLogicalPortConfigPortIfIndex_Type()
)
cienaCesLogicalPortConfigPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPortIfIndex.setStatus("current")


class _CienaCesPortAdminSpeed_Type(Integer32):
    """Custom type cienaCesPortAdminSpeed based on Integer32"""
    defaultValue = 6

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tenMbps", 2),
          ("hundredMbps", 3),
          ("gig", 4),
          ("tenGig", 5),
          ("auto", 6),
          ("fortyGig", 7),
          ("hundredGig", 8),
          ("oduFlex", 9),
          ("twoPtFiveGig", 10))
    )


_CienaCesPortAdminSpeed_Type.__name__ = "Integer32"
_CienaCesPortAdminSpeed_Object = MibTableColumn
cienaCesPortAdminSpeed = _CienaCesPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 11),
    _CienaCesPortAdminSpeed_Type()
)
cienaCesPortAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortAdminSpeed.setStatus("current")


class _CienaCesPortOperSpeed_Type(Integer32):
    """Custom type cienaCesPortOperSpeed based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tenMbps", 2),
          ("hundredMbps", 3),
          ("gig", 4),
          ("tenGig", 5),
          ("fortyGig", 6),
          ("hundredGig", 7),
          ("oduFlex", 8),
          ("twoPtFiveGig", 9))
    )


_CienaCesPortOperSpeed_Type.__name__ = "Integer32"
_CienaCesPortOperSpeed_Object = MibTableColumn
cienaCesPortOperSpeed = _CienaCesPortOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 12),
    _CienaCesPortOperSpeed_Type()
)
cienaCesPortOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortOperSpeed.setStatus("current")


class _CienaCesPortMaxFrameSize_Type(Integer32):
    """Custom type cienaCesPortMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 10222),
    )


_CienaCesPortMaxFrameSize_Type.__name__ = "Integer32"
_CienaCesPortMaxFrameSize_Object = MibTableColumn
cienaCesPortMaxFrameSize = _CienaCesPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 13),
    _CienaCesPortMaxFrameSize_Type()
)
cienaCesPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortMaxFrameSize.setStatus("current")


class _CienaCesLogicalPortConfigEttpAid_Type(DisplayString):
    """Custom type cienaCesLogicalPortConfigEttpAid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLogicalPortConfigEttpAid_Type.__name__ = "DisplayString"
_CienaCesLogicalPortConfigEttpAid_Object = MibTableColumn
cienaCesLogicalPortConfigEttpAid = _CienaCesLogicalPortConfigEttpAid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 14),
    _CienaCesLogicalPortConfigEttpAid_Type()
)
cienaCesLogicalPortConfigEttpAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigEttpAid.setStatus("current")


class _CienaCesLogicalPortLastDownReason1_Type(DisplayString):
    """Custom type cienaCesLogicalPortLastDownReason1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesLogicalPortLastDownReason1_Type.__name__ = "DisplayString"
_CienaCesLogicalPortLastDownReason1_Object = MibTableColumn
cienaCesLogicalPortLastDownReason1 = _CienaCesLogicalPortLastDownReason1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 15),
    _CienaCesLogicalPortLastDownReason1_Type()
)
cienaCesLogicalPortLastDownReason1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortLastDownReason1.setStatus("current")


class _CienaCesLogicalPortLastDownReason2_Type(DisplayString):
    """Custom type cienaCesLogicalPortLastDownReason2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesLogicalPortLastDownReason2_Type.__name__ = "DisplayString"
_CienaCesLogicalPortLastDownReason2_Object = MibTableColumn
cienaCesLogicalPortLastDownReason2 = _CienaCesLogicalPortLastDownReason2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 16),
    _CienaCesLogicalPortLastDownReason2_Type()
)
cienaCesLogicalPortLastDownReason2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortLastDownReason2.setStatus("current")


class _CienaCesLogicalPortLastDownReason3_Type(DisplayString):
    """Custom type cienaCesLogicalPortLastDownReason3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesLogicalPortLastDownReason3_Type.__name__ = "DisplayString"
_CienaCesLogicalPortLastDownReason3_Object = MibTableColumn
cienaCesLogicalPortLastDownReason3 = _CienaCesLogicalPortLastDownReason3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 17),
    _CienaCesLogicalPortLastDownReason3_Type()
)
cienaCesLogicalPortLastDownReason3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortLastDownReason3.setStatus("current")


class _CienaCesLogicalPortMaskedDownReason_Type(DisplayString):
    """Custom type cienaCesLogicalPortMaskedDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLogicalPortMaskedDownReason_Type.__name__ = "DisplayString"
_CienaCesLogicalPortMaskedDownReason_Object = MibTableColumn
cienaCesLogicalPortMaskedDownReason = _CienaCesLogicalPortMaskedDownReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 18),
    _CienaCesLogicalPortMaskedDownReason_Type()
)
cienaCesLogicalPortMaskedDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortMaskedDownReason.setStatus("current")
_CienaCesLogicalPortFacilityLoopback_Type = CienaGlobalState
_CienaCesLogicalPortFacilityLoopback_Object = MibTableColumn
cienaCesLogicalPortFacilityLoopback = _CienaCesLogicalPortFacilityLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 19),
    _CienaCesLogicalPortFacilityLoopback_Type()
)
cienaCesLogicalPortFacilityLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortFacilityLoopback.setStatus("current")
_CienaCesPortIngressRcosProfileId_Type = Integer32
_CienaCesPortIngressRcosProfileId_Object = MibTableColumn
cienaCesPortIngressRcosProfileId = _CienaCesPortIngressRcosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 20),
    _CienaCesPortIngressRcosProfileId_Type()
)
cienaCesPortIngressRcosProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortIngressRcosProfileId.setStatus("current")


class _CienaCesPortIngressRcosProfileName_Type(DisplayString):
    """Custom type cienaCesPortIngressRcosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesPortIngressRcosProfileName_Type.__name__ = "DisplayString"
_CienaCesPortIngressRcosProfileName_Object = MibTableColumn
cienaCesPortIngressRcosProfileName = _CienaCesPortIngressRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 21),
    _CienaCesPortIngressRcosProfileName_Type()
)
cienaCesPortIngressRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortIngressRcosProfileName.setStatus("current")


class _CienaCesPortIngressRcosPolicy_Type(Integer32):
    """Custom type cienaCesPortIngressRcosPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("fixed", 2),
          ("dot1dToRcosTag1", 3),
          ("dot1dToRcosTag2", 4),
          ("dscpToRcos", 5),
          ("mplsToRcos", 6),
          ("dscpMplsToRcos", 7))
    )


_CienaCesPortIngressRcosPolicy_Type.__name__ = "Integer32"
_CienaCesPortIngressRcosPolicy_Object = MibTableColumn
cienaCesPortIngressRcosPolicy = _CienaCesPortIngressRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 22),
    _CienaCesPortIngressRcosPolicy_Type()
)
cienaCesPortIngressRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortIngressRcosPolicy.setStatus("current")


class _CienaCesLogicalPortConfigEttpId_Type(Unsigned32):
    """Custom type cienaCesLogicalPortConfigEttpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesLogicalPortConfigEttpId_Type.__name__ = "Unsigned32"
_CienaCesLogicalPortConfigEttpId_Object = MibTableColumn
cienaCesLogicalPortConfigEttpId = _CienaCesLogicalPortConfigEttpId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 23),
    _CienaCesLogicalPortConfigEttpId_Type()
)
cienaCesLogicalPortConfigEttpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigEttpId.setStatus("current")


class _CienaCesLogicalPortConfigEttpType_Type(Integer32):
    """Custom type cienaCesLogicalPortConfigEttpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ethernet", 2),
          ("fastEthernet", 3),
          ("hundredFx", 4),
          ("gigEthernet", 5),
          ("gigHundredFx", 7),
          ("tripleSpeed", 8),
          ("tenGigEthernet", 9),
          ("vmTripleSpeedTX", 10),
          ("sonetOc3", 11),
          ("sonetOc12", 12),
          ("sonetOc48", 13),
          ("sonetOc192", 14),
          ("fortyGigEthernet", 15),
          ("hundredGigEthernet", 16),
          ("twoPointFiveGigEthernet", 17),
          ("odu4", 18))
    )


_CienaCesLogicalPortConfigEttpType_Type.__name__ = "Integer32"
_CienaCesLogicalPortConfigEttpType_Object = MibTableColumn
cienaCesLogicalPortConfigEttpType = _CienaCesLogicalPortConfigEttpType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 24),
    _CienaCesLogicalPortConfigEttpType_Type()
)
cienaCesLogicalPortConfigEttpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigEttpType.setStatus("current")


class _CienaCesLogicalPortConfigIngMirrorPort_Type(DisplayString):
    """Custom type cienaCesLogicalPortConfigIngMirrorPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLogicalPortConfigIngMirrorPort_Type.__name__ = "DisplayString"
_CienaCesLogicalPortConfigIngMirrorPort_Object = MibTableColumn
cienaCesLogicalPortConfigIngMirrorPort = _CienaCesLogicalPortConfigIngMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 25),
    _CienaCesLogicalPortConfigIngMirrorPort_Type()
)
cienaCesLogicalPortConfigIngMirrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigIngMirrorPort.setStatus("current")


class _CienaCesLogicalPortConfigEgrMirrorPort_Type(DisplayString):
    """Custom type cienaCesLogicalPortConfigEgrMirrorPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLogicalPortConfigEgrMirrorPort_Type.__name__ = "DisplayString"
_CienaCesLogicalPortConfigEgrMirrorPort_Object = MibTableColumn
cienaCesLogicalPortConfigEgrMirrorPort = _CienaCesLogicalPortConfigEgrMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 26),
    _CienaCesLogicalPortConfigEgrMirrorPort_Type()
)
cienaCesLogicalPortConfigEgrMirrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigEgrMirrorPort.setStatus("current")


class _CienaCesLogicalPortConfigIngFloodContainer_Type(DisplayString):
    """Custom type cienaCesLogicalPortConfigIngFloodContainer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesLogicalPortConfigIngFloodContainer_Type.__name__ = "DisplayString"
_CienaCesLogicalPortConfigIngFloodContainer_Object = MibTableColumn
cienaCesLogicalPortConfigIngFloodContainer = _CienaCesLogicalPortConfigIngFloodContainer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 27),
    _CienaCesLogicalPortConfigIngFloodContainer_Type()
)
cienaCesLogicalPortConfigIngFloodContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigIngFloodContainer.setStatus("current")


class _CienaCesLogicalPortConfigPriorityTagMode_Type(PortPriorityTagPolicy):
    """Custom type cienaCesLogicalPortConfigPriorityTagMode based on PortPriorityTagPolicy"""
    defaultValue = 2


_CienaCesLogicalPortConfigPriorityTagMode_Type.__name__ = "PortPriorityTagPolicy"
_CienaCesLogicalPortConfigPriorityTagMode_Object = MibTableColumn
cienaCesLogicalPortConfigPriorityTagMode = _CienaCesLogicalPortConfigPriorityTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 28),
    _CienaCesLogicalPortConfigPriorityTagMode_Type()
)
cienaCesLogicalPortConfigPriorityTagMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigPriorityTagMode.setStatus("current")


class _CienaCesLogicalPortConfigVidTpidCount_Type(Unsigned32):
    """Custom type cienaCesLogicalPortConfigVidTpidCount based on Unsigned32"""
    defaultValue = 2


_CienaCesLogicalPortConfigVidTpidCount_Type.__name__ = "Unsigned32"
_CienaCesLogicalPortConfigVidTpidCount_Object = MibTableColumn
cienaCesLogicalPortConfigVidTpidCount = _CienaCesLogicalPortConfigVidTpidCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 29),
    _CienaCesLogicalPortConfigVidTpidCount_Type()
)
cienaCesLogicalPortConfigVidTpidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigVidTpidCount.setStatus("current")
_CienaCesPortOperationalSpeed_Type = Gauge32
_CienaCesPortOperationalSpeed_Object = MibTableColumn
cienaCesPortOperationalSpeed = _CienaCesPortOperationalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 30),
    _CienaCesPortOperationalSpeed_Type()
)
cienaCesPortOperationalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortOperationalSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortOperationalSpeed.setUnits("kbps")


class _CienaCesPortOuterTpidList_Type(DisplayString):
    """Custom type cienaCesPortOuterTpidList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesPortOuterTpidList_Type.__name__ = "DisplayString"
_CienaCesPortOuterTpidList_Object = MibTableColumn
cienaCesPortOuterTpidList = _CienaCesPortOuterTpidList_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 31),
    _CienaCesPortOuterTpidList_Type()
)
cienaCesPortOuterTpidList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortOuterTpidList.setStatus("current")


class _CienaCesPortEgressOuterTpid_Type(DisplayString):
    """Custom type cienaCesPortEgressOuterTpid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesPortEgressOuterTpid_Type.__name__ = "DisplayString"
_CienaCesPortEgressOuterTpid_Object = MibTableColumn
cienaCesPortEgressOuterTpid = _CienaCesPortEgressOuterTpid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 32),
    _CienaCesPortEgressOuterTpid_Type()
)
cienaCesPortEgressOuterTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortEgressOuterTpid.setStatus("current")


class _CienaCesPortOuterVtagTpid_Type(DisplayString):
    """Custom type cienaCesPortOuterVtagTpid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesPortOuterVtagTpid_Type.__name__ = "DisplayString"
_CienaCesPortOuterVtagTpid_Object = MibTableColumn
cienaCesPortOuterVtagTpid = _CienaCesPortOuterVtagTpid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 33),
    _CienaCesPortOuterVtagTpid_Type()
)
cienaCesPortOuterVtagTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortOuterVtagTpid.setStatus("current")
_CienaCesPortAdministrativeSpeed_Type = Unsigned32
_CienaCesPortAdministrativeSpeed_Object = MibTableColumn
cienaCesPortAdministrativeSpeed = _CienaCesPortAdministrativeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 34),
    _CienaCesPortAdministrativeSpeed_Type()
)
cienaCesPortAdministrativeSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortAdministrativeSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesPortAdministrativeSpeed.setUnits("kbps")
_CienaCesPortTerminalLoopbackState_Type = CienaGlobalState
_CienaCesPortTerminalLoopbackState_Object = MibTableColumn
cienaCesPortTerminalLoopbackState = _CienaCesPortTerminalLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 35),
    _CienaCesPortTerminalLoopbackState_Type()
)
cienaCesPortTerminalLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortTerminalLoopbackState.setStatus("current")


class _CienaCesPortLearnLimit_Type(Integer32):
    """Custom type cienaCesPortLearnLimit based on Integer32"""
    defaultValue = 64000


_CienaCesPortLearnLimit_Type.__name__ = "Integer32"
_CienaCesPortLearnLimit_Object = MibTableColumn
cienaCesPortLearnLimit = _CienaCesPortLearnLimit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 36),
    _CienaCesPortLearnLimit_Type()
)
cienaCesPortLearnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortLearnLimit.setStatus("current")


class _CienaCesLogicalPortConfigSignalDegradeDetection_Type(Integer32):
    """Custom type cienaCesLogicalPortConfigSignalDegradeDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("otn", 2),
          ("y1731SyntheticLoss", 3))
    )


_CienaCesLogicalPortConfigSignalDegradeDetection_Type.__name__ = "Integer32"
_CienaCesLogicalPortConfigSignalDegradeDetection_Object = MibTableColumn
cienaCesLogicalPortConfigSignalDegradeDetection = _CienaCesLogicalPortConfigSignalDegradeDetection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 37),
    _CienaCesLogicalPortConfigSignalDegradeDetection_Type()
)
cienaCesLogicalPortConfigSignalDegradeDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigSignalDegradeDetection.setStatus("current")


class _CienaCesLogicalPortConfigSignalDegradeState_Type(Integer32):
    """Custom type cienaCesLogicalPortConfigSignalDegradeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("degraded", 2))
    )


_CienaCesLogicalPortConfigSignalDegradeState_Type.__name__ = "Integer32"
_CienaCesLogicalPortConfigSignalDegradeState_Object = MibTableColumn
cienaCesLogicalPortConfigSignalDegradeState = _CienaCesLogicalPortConfigSignalDegradeState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 38),
    _CienaCesLogicalPortConfigSignalDegradeState_Type()
)
cienaCesLogicalPortConfigSignalDegradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortConfigSignalDegradeState.setStatus("current")


class _CienaCesPortL2CftStatus_Type(Integer32):
    """Custom type cienaCesPortL2CftStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesPortL2CftStatus_Type.__name__ = "Integer32"
_CienaCesPortL2CftStatus_Object = MibTableColumn
cienaCesPortL2CftStatus = _CienaCesPortL2CftStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 39),
    _CienaCesPortL2CftStatus_Type()
)
cienaCesPortL2CftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortL2CftStatus.setStatus("current")


class _CienaCesPortL2CftProfileId_Type(Unsigned32):
    """Custom type cienaCesPortL2CftProfileId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CienaCesPortL2CftProfileId_Type.__name__ = "Unsigned32"
_CienaCesPortL2CftProfileId_Object = MibTableColumn
cienaCesPortL2CftProfileId = _CienaCesPortL2CftProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 40),
    _CienaCesPortL2CftProfileId_Type()
)
cienaCesPortL2CftProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortL2CftProfileId.setStatus("current")


class _CienaCesPortConfigHoldOffState_Type(TruthValue):
    """Custom type cienaCesPortConfigHoldOffState based on TruthValue"""
    defaultValue = 2


_CienaCesPortConfigHoldOffState_Type.__name__ = "TruthValue"
_CienaCesPortConfigHoldOffState_Object = MibTableColumn
cienaCesPortConfigHoldOffState = _CienaCesPortConfigHoldOffState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 41),
    _CienaCesPortConfigHoldOffState_Type()
)
cienaCesPortConfigHoldOffState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortConfigHoldOffState.setStatus("current")


class _CienaCesPortConfigHoldOffTime_Type(Unsigned32):
    """Custom type cienaCesPortConfigHoldOffTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_CienaCesPortConfigHoldOffTime_Type.__name__ = "Unsigned32"
_CienaCesPortConfigHoldOffTime_Object = MibTableColumn
cienaCesPortConfigHoldOffTime = _CienaCesPortConfigHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 42),
    _CienaCesPortConfigHoldOffTime_Type()
)
cienaCesPortConfigHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortConfigHoldOffTime.setStatus("current")


class _CienaCesPortOperFecState_Type(Integer32):
    """Custom type cienaCesPortOperFecState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CienaCesPortOperFecState_Type.__name__ = "Integer32"
_CienaCesPortOperFecState_Object = MibTableColumn
cienaCesPortOperFecState = _CienaCesPortOperFecState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 1, 1, 1, 43),
    _CienaCesPortOperFecState_Type()
)
cienaCesPortOperFecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortOperFecState.setStatus("current")
_CienaCesPortPgIdMapping_ObjectIdentity = ObjectIdentity
cienaCesPortPgIdMapping = _CienaCesPortPgIdMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2)
)
_CienaCesPortPgIdMappingTable_Object = MibTable
cienaCesPortPgIdMappingTable = _CienaCesPortPgIdMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingTable.setStatus("current")
_CienaCesPortPgIdMappingEntry_Object = MibTableRow
cienaCesPortPgIdMappingEntry = _CienaCesPortPgIdMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1)
)
cienaCesPortPgIdMappingEntry.setIndexNames(
    (0, "CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingChassisIndex"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingShelfIndex"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingSlotIndex"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesPortPgidMappingPortNumber"),
)
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingEntry.setStatus("current")


class _CienaCesPortPgIdMappingChassisIndex_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingChassisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesPortPgIdMappingChassisIndex_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingChassisIndex_Object = MibTableColumn
cienaCesPortPgIdMappingChassisIndex = _CienaCesPortPgIdMappingChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 1),
    _CienaCesPortPgIdMappingChassisIndex_Type()
)
cienaCesPortPgIdMappingChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingChassisIndex.setStatus("current")


class _CienaCesPortPgIdMappingShelfIndex_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesPortPgIdMappingShelfIndex_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingShelfIndex_Object = MibTableColumn
cienaCesPortPgIdMappingShelfIndex = _CienaCesPortPgIdMappingShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 2),
    _CienaCesPortPgIdMappingShelfIndex_Type()
)
cienaCesPortPgIdMappingShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingShelfIndex.setStatus("current")


class _CienaCesPortPgIdMappingSlotIndex_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesPortPgIdMappingSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingSlotIndex_Object = MibTableColumn
cienaCesPortPgIdMappingSlotIndex = _CienaCesPortPgIdMappingSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 3),
    _CienaCesPortPgIdMappingSlotIndex_Type()
)
cienaCesPortPgIdMappingSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingSlotIndex.setStatus("current")


class _CienaCesPortPgidMappingPortNumber_Type(Unsigned32):
    """Custom type cienaCesPortPgidMappingPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortPgidMappingPortNumber_Type.__name__ = "Unsigned32"
_CienaCesPortPgidMappingPortNumber_Object = MibTableColumn
cienaCesPortPgidMappingPortNumber = _CienaCesPortPgidMappingPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 4),
    _CienaCesPortPgidMappingPortNumber_Type()
)
cienaCesPortPgidMappingPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortPgidMappingPortNumber.setStatus("current")


class _CienaCesPortPgIdMappingPgId_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingPgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortPgIdMappingPgId_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingPgId_Object = MibTableColumn
cienaCesPortPgIdMappingPgId = _CienaCesPortPgIdMappingPgId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 5),
    _CienaCesPortPgIdMappingPgId_Type()
)
cienaCesPortPgIdMappingPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingPgId.setStatus("current")


class _CienaCesPortPgIdMappingNotifChassisIndex_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingNotifChassisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesPortPgIdMappingNotifChassisIndex_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingNotifChassisIndex_Object = MibTableColumn
cienaCesPortPgIdMappingNotifChassisIndex = _CienaCesPortPgIdMappingNotifChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 6),
    _CienaCesPortPgIdMappingNotifChassisIndex_Type()
)
cienaCesPortPgIdMappingNotifChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingNotifChassisIndex.setStatus("current")


class _CienaCesPortPgIdMappingNotifShelfIndex_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingNotifShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesPortPgIdMappingNotifShelfIndex_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingNotifShelfIndex_Object = MibTableColumn
cienaCesPortPgIdMappingNotifShelfIndex = _CienaCesPortPgIdMappingNotifShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 7),
    _CienaCesPortPgIdMappingNotifShelfIndex_Type()
)
cienaCesPortPgIdMappingNotifShelfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingNotifShelfIndex.setStatus("current")


class _CienaCesPortPgIdMappingNotifSlotIndex_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingNotifSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesPortPgIdMappingNotifSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingNotifSlotIndex_Object = MibTableColumn
cienaCesPortPgIdMappingNotifSlotIndex = _CienaCesPortPgIdMappingNotifSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 8),
    _CienaCesPortPgIdMappingNotifSlotIndex_Type()
)
cienaCesPortPgIdMappingNotifSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingNotifSlotIndex.setStatus("current")


class _CienaCesPortPgIdMappingNotifPortNumber_Type(Unsigned32):
    """Custom type cienaCesPortPgIdMappingNotifPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesPortPgIdMappingNotifPortNumber_Type.__name__ = "Unsigned32"
_CienaCesPortPgIdMappingNotifPortNumber_Object = MibTableColumn
cienaCesPortPgIdMappingNotifPortNumber = _CienaCesPortPgIdMappingNotifPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 2, 1, 1, 9),
    _CienaCesPortPgIdMappingNotifPortNumber_Type()
)
cienaCesPortPgIdMappingNotifPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPortPgIdMappingNotifPortNumber.setStatus("current")
_CienaCesEttpConfig_ObjectIdentity = ObjectIdentity
cienaCesEttpConfig = _CienaCesEttpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3)
)
_CienaCesEttpConfigTable_Object = MibTable
cienaCesEttpConfigTable = _CienaCesEttpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesEttpConfigTable.setStatus("current")
_CienaCesEttpConfigEntry_Object = MibTableRow
cienaCesEttpConfigEntry = _CienaCesEttpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1)
)
cienaCesEttpConfigEntry.setIndexNames(
    (0, "CIENA-CES-PORT-MIB", "cienaCesEttpConfigEttpId"),
)
if mibBuilder.loadTexts:
    cienaCesEttpConfigEntry.setStatus("current")


class _CienaCesEttpConfigEttpId_Type(Unsigned32):
    """Custom type cienaCesEttpConfigEttpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesEttpConfigEttpId_Type.__name__ = "Unsigned32"
_CienaCesEttpConfigEttpId_Object = MibTableColumn
cienaCesEttpConfigEttpId = _CienaCesEttpConfigEttpId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 1),
    _CienaCesEttpConfigEttpId_Type()
)
cienaCesEttpConfigEttpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesEttpConfigEttpId.setStatus("current")


class _CienaCesEttpConfigOperState_Type(Integer32):
    """Custom type cienaCesEttpConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("enabled", 2),
          ("disabled", 3),
          ("notAuthenticated", 4),
          ("loopbackTx", 5),
          ("loopbackRx", 6),
          ("unequipped", 7))
    )


_CienaCesEttpConfigOperState_Type.__name__ = "Integer32"
_CienaCesEttpConfigOperState_Object = MibTableColumn
cienaCesEttpConfigOperState = _CienaCesEttpConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 2),
    _CienaCesEttpConfigOperState_Type()
)
cienaCesEttpConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigOperState.setStatus("current")


class _CienaCesEttpConfigLinkUpDownTrapState_Type(CienaGlobalState):
    """Custom type cienaCesEttpConfigLinkUpDownTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesEttpConfigLinkUpDownTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesEttpConfigLinkUpDownTrapState_Object = MibTableColumn
cienaCesEttpConfigLinkUpDownTrapState = _CienaCesEttpConfigLinkUpDownTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 3),
    _CienaCesEttpConfigLinkUpDownTrapState_Type()
)
cienaCesEttpConfigLinkUpDownTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesEttpConfigLinkUpDownTrapState.setStatus("current")


class _CienaCesEttpConfigAllTrapState_Type(CienaGlobalState):
    """Custom type cienaCesEttpConfigAllTrapState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesEttpConfigAllTrapState_Type.__name__ = "CienaGlobalState"
_CienaCesEttpConfigAllTrapState_Object = MibTableColumn
cienaCesEttpConfigAllTrapState = _CienaCesEttpConfigAllTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 4),
    _CienaCesEttpConfigAllTrapState_Type()
)
cienaCesEttpConfigAllTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesEttpConfigAllTrapState.setStatus("current")
_CienaCesEttpConfigMacAddress_Type = MacAddress
_CienaCesEttpConfigMacAddress_Object = MibTableColumn
cienaCesEttpConfigMacAddress = _CienaCesEttpConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 5),
    _CienaCesEttpConfigMacAddress_Type()
)
cienaCesEttpConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigMacAddress.setStatus("current")


class _CienaCesEttpConfigName_Type(DisplayString):
    """Custom type cienaCesEttpConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesEttpConfigName_Type.__name__ = "DisplayString"
_CienaCesEttpConfigName_Object = MibTableColumn
cienaCesEttpConfigName = _CienaCesEttpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 6),
    _CienaCesEttpConfigName_Type()
)
cienaCesEttpConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigName.setStatus("current")


class _CienaCesEttpConfigEttpType_Type(Integer32):
    """Custom type cienaCesEttpConfigEttpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ethernet", 2),
          ("fastEthernet", 3),
          ("hundredFx", 4),
          ("gigEthernet", 5),
          ("gigHundredFx", 7),
          ("tripleSpeed", 8),
          ("tenGigEthernet", 9),
          ("vmTripleSpeedTX", 10),
          ("sonetOc3", 11),
          ("sonetOc12", 12),
          ("sonetOc48", 13),
          ("sonetOc192", 14),
          ("fortyGigEthernet", 15),
          ("hundredGigEthernet", 16),
          ("twoPointFiveGigEthernet", 17),
          ("odu4", 18))
    )


_CienaCesEttpConfigEttpType_Type.__name__ = "Integer32"
_CienaCesEttpConfigEttpType_Object = MibTableColumn
cienaCesEttpConfigEttpType = _CienaCesEttpConfigEttpType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 7),
    _CienaCesEttpConfigEttpType_Type()
)
cienaCesEttpConfigEttpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigEttpType.setStatus("current")


class _CienaCesEttpConfigAdminSpeed_Type(Integer32):
    """Custom type cienaCesEttpConfigAdminSpeed based on Integer32"""
    defaultValue = 6

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tenMbps", 2),
          ("hundredMbps", 3),
          ("gig", 4),
          ("tenGig", 5),
          ("auto", 6),
          ("fortyGig", 7),
          ("hundredGig", 8),
          ("twoPtFiveGig", 10))
    )


_CienaCesEttpConfigAdminSpeed_Type.__name__ = "Integer32"
_CienaCesEttpConfigAdminSpeed_Object = MibTableColumn
cienaCesEttpConfigAdminSpeed = _CienaCesEttpConfigAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 8),
    _CienaCesEttpConfigAdminSpeed_Type()
)
cienaCesEttpConfigAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigAdminSpeed.setStatus("current")


class _CienaCesEttpConfigOperSpeed_Type(Integer32):
    """Custom type cienaCesEttpConfigOperSpeed based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tenMbps", 2),
          ("hundredMbps", 3),
          ("gig", 4),
          ("tenGig", 5),
          ("fortyGig", 6),
          ("hundredGig", 7),
          ("twoPtFiveGig", 9))
    )


_CienaCesEttpConfigOperSpeed_Type.__name__ = "Integer32"
_CienaCesEttpConfigOperSpeed_Object = MibTableColumn
cienaCesEttpConfigOperSpeed = _CienaCesEttpConfigOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 9),
    _CienaCesEttpConfigOperSpeed_Type()
)
cienaCesEttpConfigOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigOperSpeed.setStatus("current")


class _CienaCesEttpConfigEthLpPgid_Type(Unsigned32):
    """Custom type cienaCesEttpConfigEthLpPgid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesEttpConfigEthLpPgid_Type.__name__ = "Unsigned32"
_CienaCesEttpConfigEthLpPgid_Object = MibTableColumn
cienaCesEttpConfigEthLpPgid = _CienaCesEttpConfigEthLpPgid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 10),
    _CienaCesEttpConfigEthLpPgid_Type()
)
cienaCesEttpConfigEthLpPgid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigEthLpPgid.setStatus("current")


class _CienaCesEttpConfigDuplex_Type(EttpDuplexPolicy):
    """Custom type cienaCesEttpConfigDuplex based on EttpDuplexPolicy"""
    defaultValue = 2


_CienaCesEttpConfigDuplex_Type.__name__ = "EttpDuplexPolicy"
_CienaCesEttpConfigDuplex_Object = MibTableColumn
cienaCesEttpConfigDuplex = _CienaCesEttpConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 11),
    _CienaCesEttpConfigDuplex_Type()
)
cienaCesEttpConfigDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigDuplex.setStatus("current")


class _CienaCesEttpConfigFlowCntl_Type(EttpFlowControlPolicy):
    """Custom type cienaCesEttpConfigFlowCntl based on EttpFlowControlPolicy"""
    defaultValue = 1


_CienaCesEttpConfigFlowCntl_Type.__name__ = "EttpFlowControlPolicy"
_CienaCesEttpConfigFlowCntl_Object = MibTableColumn
cienaCesEttpConfigFlowCntl = _CienaCesEttpConfigFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 12),
    _CienaCesEttpConfigFlowCntl_Type()
)
cienaCesEttpConfigFlowCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigFlowCntl.setStatus("current")


class _CienaCesEttpConfigAutoNeg_Type(EttpAutoNegPolicy):
    """Custom type cienaCesEttpConfigAutoNeg based on EttpAutoNegPolicy"""
    defaultValue = 1


_CienaCesEttpConfigAutoNeg_Type.__name__ = "EttpAutoNegPolicy"
_CienaCesEttpConfigAutoNeg_Object = MibTableColumn
cienaCesEttpConfigAutoNeg = _CienaCesEttpConfigAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 13),
    _CienaCesEttpConfigAutoNeg_Type()
)
cienaCesEttpConfigAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigAutoNeg.setStatus("current")


class _CienaCesEttpConfigAdvertisedFlowCntl_Type(EttpAdvertisedFlowControlPolicy):
    """Custom type cienaCesEttpConfigAdvertisedFlowCntl based on EttpAdvertisedFlowControlPolicy"""
    defaultValue = 1


_CienaCesEttpConfigAdvertisedFlowCntl_Type.__name__ = "EttpAdvertisedFlowControlPolicy"
_CienaCesEttpConfigAdvertisedFlowCntl_Object = MibTableColumn
cienaCesEttpConfigAdvertisedFlowCntl = _CienaCesEttpConfigAdvertisedFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 14),
    _CienaCesEttpConfigAdvertisedFlowCntl_Type()
)
cienaCesEttpConfigAdvertisedFlowCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigAdvertisedFlowCntl.setStatus("current")


class _CienaCesEttpConfigIfgDecr_Type(Unsigned32):
    """Custom type cienaCesEttpConfigIfgDecr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CienaCesEttpConfigIfgDecr_Type.__name__ = "Unsigned32"
_CienaCesEttpConfigIfgDecr_Object = MibTableColumn
cienaCesEttpConfigIfgDecr = _CienaCesEttpConfigIfgDecr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 15),
    _CienaCesEttpConfigIfgDecr_Type()
)
cienaCesEttpConfigIfgDecr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigIfgDecr.setStatus("current")


class _CienaCesEttpConfigXcvrFreq_Type(Unsigned32):
    """Custom type cienaCesEttpConfigXcvrFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(191100, 196150),
    )


_CienaCesEttpConfigXcvrFreq_Type.__name__ = "Unsigned32"
_CienaCesEttpConfigXcvrFreq_Object = MibTableColumn
cienaCesEttpConfigXcvrFreq = _CienaCesEttpConfigXcvrFreq_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 3, 1, 1, 16),
    _CienaCesEttpConfigXcvrFreq_Type()
)
cienaCesEttpConfigXcvrFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesEttpConfigXcvrFreq.setStatus("current")
_CienaCesLogicalPortTpid_ObjectIdentity = ObjectIdentity
cienaCesLogicalPortTpid = _CienaCesLogicalPortTpid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 4)
)
_CienaCesLogicalPortTpidTable_Object = MibTable
cienaCesLogicalPortTpidTable = _CienaCesLogicalPortTpidTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesLogicalPortTpidTable.setStatus("current")
_CienaCesLogicalPortTpidEntry_Object = MibTableRow
cienaCesLogicalPortTpidEntry = _CienaCesLogicalPortTpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 4, 1, 1)
)
cienaCesLogicalPortTpidEntry.setIndexNames(
    (0, "CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPgId"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesLogicalPortTpidIndex"),
)
if mibBuilder.loadTexts:
    cienaCesLogicalPortTpidEntry.setStatus("current")
_CienaCesLogicalPortTpidIndex_Type = Unsigned32
_CienaCesLogicalPortTpidIndex_Object = MibTableColumn
cienaCesLogicalPortTpidIndex = _CienaCesLogicalPortTpidIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 4, 1, 1, 1),
    _CienaCesLogicalPortTpidIndex_Type()
)
cienaCesLogicalPortTpidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLogicalPortTpidIndex.setStatus("current")
_CienaCesLogicalPortInnerVidTpid_Type = Unsigned32
_CienaCesLogicalPortInnerVidTpid_Object = MibTableColumn
cienaCesLogicalPortInnerVidTpid = _CienaCesLogicalPortInnerVidTpid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 4, 1, 1, 2),
    _CienaCesLogicalPortInnerVidTpid_Type()
)
cienaCesLogicalPortInnerVidTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortInnerVidTpid.setStatus("current")
_CienaCesLogicalPortOuterVidTpid_Type = Unsigned32
_CienaCesLogicalPortOuterVidTpid_Object = MibTableColumn
cienaCesLogicalPortOuterVidTpid = _CienaCesLogicalPortOuterVidTpid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 4, 1, 1, 3),
    _CienaCesLogicalPortOuterVidTpid_Type()
)
cienaCesLogicalPortOuterVidTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLogicalPortOuterVidTpid.setStatus("current")
_CienaCesChPortPgIdMapping_ObjectIdentity = ObjectIdentity
cienaCesChPortPgIdMapping = _CienaCesChPortPgIdMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5)
)
_CienaCesChPortPgIdMappingTable_Object = MibTable
cienaCesChPortPgIdMappingTable = _CienaCesChPortPgIdMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingTable.setStatus("current")
_CienaCesChPortPgIdMappingEntry_Object = MibTableRow
cienaCesChPortPgIdMappingEntry = _CienaCesChPortPgIdMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1)
)
cienaCesChPortPgIdMappingEntry.setIndexNames(
    (0, "CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingChassisIndex"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingShelfIndex"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingSlotIndex"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingPortNumber"),
    (0, "CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingChannelNumber"),
)
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingEntry.setStatus("current")


class _CienaCesChPortPgIdMappingChassisIndex_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingChassisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChPortPgIdMappingChassisIndex_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingChassisIndex_Object = MibTableColumn
cienaCesChPortPgIdMappingChassisIndex = _CienaCesChPortPgIdMappingChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 1),
    _CienaCesChPortPgIdMappingChassisIndex_Type()
)
cienaCesChPortPgIdMappingChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingChassisIndex.setStatus("current")


class _CienaCesChPortPgIdMappingShelfIndex_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChPortPgIdMappingShelfIndex_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingShelfIndex_Object = MibTableColumn
cienaCesChPortPgIdMappingShelfIndex = _CienaCesChPortPgIdMappingShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 2),
    _CienaCesChPortPgIdMappingShelfIndex_Type()
)
cienaCesChPortPgIdMappingShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingShelfIndex.setStatus("current")


class _CienaCesChPortPgIdMappingSlotIndex_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesChPortPgIdMappingSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingSlotIndex_Object = MibTableColumn
cienaCesChPortPgIdMappingSlotIndex = _CienaCesChPortPgIdMappingSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 3),
    _CienaCesChPortPgIdMappingSlotIndex_Type()
)
cienaCesChPortPgIdMappingSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingSlotIndex.setStatus("current")


class _CienaCesChPortPgIdMappingPortNumber_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChPortPgIdMappingPortNumber_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingPortNumber_Object = MibTableColumn
cienaCesChPortPgIdMappingPortNumber = _CienaCesChPortPgIdMappingPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 4),
    _CienaCesChPortPgIdMappingPortNumber_Type()
)
cienaCesChPortPgIdMappingPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingPortNumber.setStatus("current")


class _CienaCesChPortPgIdMappingChannelNumber_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingChannelNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesChPortPgIdMappingChannelNumber_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingChannelNumber_Object = MibTableColumn
cienaCesChPortPgIdMappingChannelNumber = _CienaCesChPortPgIdMappingChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 5),
    _CienaCesChPortPgIdMappingChannelNumber_Type()
)
cienaCesChPortPgIdMappingChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingChannelNumber.setStatus("current")


class _CienaCesChPortPgIdMappingPgId_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingPgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesChPortPgIdMappingPgId_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingPgId_Object = MibTableColumn
cienaCesChPortPgIdMappingPgId = _CienaCesChPortPgIdMappingPgId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 6),
    _CienaCesChPortPgIdMappingPgId_Type()
)
cienaCesChPortPgIdMappingPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingPgId.setStatus("current")


class _CienaCesChPortPgIdMappingNotifChassisIndex_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingNotifChassisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChPortPgIdMappingNotifChassisIndex_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingNotifChassisIndex_Object = MibTableColumn
cienaCesChPortPgIdMappingNotifChassisIndex = _CienaCesChPortPgIdMappingNotifChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 7),
    _CienaCesChPortPgIdMappingNotifChassisIndex_Type()
)
cienaCesChPortPgIdMappingNotifChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingNotifChassisIndex.setStatus("current")


class _CienaCesChPortPgIdMappingNotifShelfIndex_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingNotifShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChPortPgIdMappingNotifShelfIndex_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingNotifShelfIndex_Object = MibTableColumn
cienaCesChPortPgIdMappingNotifShelfIndex = _CienaCesChPortPgIdMappingNotifShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 8),
    _CienaCesChPortPgIdMappingNotifShelfIndex_Type()
)
cienaCesChPortPgIdMappingNotifShelfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingNotifShelfIndex.setStatus("current")


class _CienaCesChPortPgIdMappingNotifSlotIndex_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingNotifSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesChPortPgIdMappingNotifSlotIndex_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingNotifSlotIndex_Object = MibTableColumn
cienaCesChPortPgIdMappingNotifSlotIndex = _CienaCesChPortPgIdMappingNotifSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 9),
    _CienaCesChPortPgIdMappingNotifSlotIndex_Type()
)
cienaCesChPortPgIdMappingNotifSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingNotifSlotIndex.setStatus("current")


class _CienaCesChPortPgIdMappingNotifPortNumber_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingNotifPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChPortPgIdMappingNotifPortNumber_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingNotifPortNumber_Object = MibTableColumn
cienaCesChPortPgIdMappingNotifPortNumber = _CienaCesChPortPgIdMappingNotifPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 10),
    _CienaCesChPortPgIdMappingNotifPortNumber_Type()
)
cienaCesChPortPgIdMappingNotifPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingNotifPortNumber.setStatus("current")


class _CienaCesChPortPgIdMappingNotifChannelNumber_Type(Unsigned32):
    """Custom type cienaCesChPortPgIdMappingNotifChannelNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesChPortPgIdMappingNotifChannelNumber_Type.__name__ = "Unsigned32"
_CienaCesChPortPgIdMappingNotifChannelNumber_Object = MibTableColumn
cienaCesChPortPgIdMappingNotifChannelNumber = _CienaCesChPortPgIdMappingNotifChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 1, 5, 1, 1, 11),
    _CienaCesChPortPgIdMappingNotifChannelNumber_Type()
)
cienaCesChPortPgIdMappingNotifChannelNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChPortPgIdMappingNotifChannelNumber.setStatus("current")
_CienaCesPortMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesPortMIBConformance = _CienaCesPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 2)
)
_CienaCesPortMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesPortMIBCompliances = _CienaCesPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 2, 1)
)
_CienaCesPortMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesPortMIBGroups = _CienaCesPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 2, 2)
)
_CienaCesPortNotificationMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesPortNotificationMIBNotificationPrefix = _CienaCesPortNotificationMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2)
)
_CienaCesPortNotificationMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesPortNotificationMIBNotifications = _CienaCesPortNotificationMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0)
)

# Managed Objects groups

portConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 2, 2, 1)
)
portConfigGroup.setObjects(
      *(("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortLinkUpDownTrapState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAllTrapState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortPortMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"))
)
if mibBuilder.loadTexts:
    portConfigGroup.setStatus("current")

portPgIdMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 2, 2, 3)
)
portPgIdMappingGroup.setObjects(
      *(("CIENA-CES-PORT-MIB", "cienaCesPortPgidMappingPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingPgId"))
)
if mibBuilder.loadTexts:
    portPgIdMappingGroup.setStatus("current")


# Notification objects

cienaCesPortNotificationPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0, 1)
)
cienaCesPortNotificationPortDown.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemId"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigEttpAid"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortLastDownReason1"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortLastDownReason2"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortLastDownReason3"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortMaskedDownReason"))
)
if mibBuilder.loadTexts:
    cienaCesPortNotificationPortDown.setStatus(
        "current"
    )

cienaCesPortNotificationPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0, 2)
)
cienaCesPortNotificationPortUp.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemId"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigEttpAid"))
)
if mibBuilder.loadTexts:
    cienaCesPortNotificationPortUp.setStatus(
        "current"
    )

cienaCesChPortNotificationPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0, 3)
)
cienaCesChPortNotificationPortUp.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifChannelNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemId"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigEttpAid"))
)
if mibBuilder.loadTexts:
    cienaCesChPortNotificationPortUp.setStatus(
        "current"
    )

cienaCesChPortNotificationPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0, 4)
)
cienaCesChPortNotificationPortDown.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifChannelNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemId"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigEttpAid"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortLastDownReason1"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortLastDownReason2"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortLastDownReason3"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortMaskedDownReason"))
)
if mibBuilder.loadTexts:
    cienaCesChPortNotificationPortDown.setStatus(
        "current"
    )

cienaCesPortNotificationPortSignalDegradeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0, 5)
)
cienaCesPortNotificationPortSignalDegradeSet.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifChannelNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemId"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigEttpAid"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigSignalDegradeDetection"))
)
if mibBuilder.loadTexts:
    cienaCesPortNotificationPortSignalDegradeSet.setStatus(
        "current"
    )

cienaCesPortNotificationPortSignalDegradeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 2, 0, 6)
)
cienaCesPortNotificationPortSignalDegradeClear.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifChassisIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifShelfIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifSlotIndex"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortPgIdMappingNotifPortNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesChPortPgIdMappingNotifChannelNumber"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortAdminState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortOperState"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortName"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortType"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigPortDesc"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemId"),
        ("CIENA-CES-PORT-MIB", "cienaCesLogicalPortConfigEttpAid"))
)
if mibBuilder.loadTexts:
    cienaCesPortNotificationPortSignalDegradeClear.setStatus(
        "current"
    )


# Notifications groups

portNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 1, 2, 2, 2)
)
portNotifGroup.setObjects(
      *(("CIENA-CES-PORT-MIB", "cienaCesPortNotificationPortDown"),
        ("CIENA-CES-PORT-MIB", "cienaCesPortNotificationPortUp"))
)
if mibBuilder.loadTexts:
    portNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-PORT-MIB",
    **{"EttpDuplexPolicy": EttpDuplexPolicy,
       "EttpAdvertisedFlowControlPolicy": EttpAdvertisedFlowControlPolicy,
       "EttpFlowControlPolicy": EttpFlowControlPolicy,
       "EttpAutoNegPolicy": EttpAutoNegPolicy,
       "PortPriorityTagPolicy": PortPriorityTagPolicy,
       "cienaCesPortConfigMIB": cienaCesPortConfigMIB,
       "cienaCesPortConfigMIBObjects": cienaCesPortConfigMIBObjects,
       "cienaCesPortConfig": cienaCesPortConfig,
       "cienaCesLogicalPortConfigTable": cienaCesLogicalPortConfigTable,
       "cienaCesLogicalPortConfigEntry": cienaCesLogicalPortConfigEntry,
       "cienaCesLogicalPortConfigPgId": cienaCesLogicalPortConfigPgId,
       "cienaCesLogicalPortConfigPortAdminState": cienaCesLogicalPortConfigPortAdminState,
       "cienaCesLogicalPortConfigPortOperState": cienaCesLogicalPortConfigPortOperState,
       "cienaCesLogicalPortConfigPortLinkUpDownTrapState": cienaCesLogicalPortConfigPortLinkUpDownTrapState,
       "cienaCesLogicalPortConfigPortAllTrapState": cienaCesLogicalPortConfigPortAllTrapState,
       "cienaCesLogicalPortConfigPortPortMacAddress": cienaCesLogicalPortConfigPortPortMacAddress,
       "cienaCesLogicalPortConfigPortName": cienaCesLogicalPortConfigPortName,
       "cienaCesLogicalPortConfigPortDesc": cienaCesLogicalPortConfigPortDesc,
       "cienaCesLogicalPortConfigPortType": cienaCesLogicalPortConfigPortType,
       "cienaCesLogicalPortConfigPortIfIndex": cienaCesLogicalPortConfigPortIfIndex,
       "cienaCesPortAdminSpeed": cienaCesPortAdminSpeed,
       "cienaCesPortOperSpeed": cienaCesPortOperSpeed,
       "cienaCesPortMaxFrameSize": cienaCesPortMaxFrameSize,
       "cienaCesLogicalPortConfigEttpAid": cienaCesLogicalPortConfigEttpAid,
       "cienaCesLogicalPortLastDownReason1": cienaCesLogicalPortLastDownReason1,
       "cienaCesLogicalPortLastDownReason2": cienaCesLogicalPortLastDownReason2,
       "cienaCesLogicalPortLastDownReason3": cienaCesLogicalPortLastDownReason3,
       "cienaCesLogicalPortMaskedDownReason": cienaCesLogicalPortMaskedDownReason,
       "cienaCesLogicalPortFacilityLoopback": cienaCesLogicalPortFacilityLoopback,
       "cienaCesPortIngressRcosProfileId": cienaCesPortIngressRcosProfileId,
       "cienaCesPortIngressRcosProfileName": cienaCesPortIngressRcosProfileName,
       "cienaCesPortIngressRcosPolicy": cienaCesPortIngressRcosPolicy,
       "cienaCesLogicalPortConfigEttpId": cienaCesLogicalPortConfigEttpId,
       "cienaCesLogicalPortConfigEttpType": cienaCesLogicalPortConfigEttpType,
       "cienaCesLogicalPortConfigIngMirrorPort": cienaCesLogicalPortConfigIngMirrorPort,
       "cienaCesLogicalPortConfigEgrMirrorPort": cienaCesLogicalPortConfigEgrMirrorPort,
       "cienaCesLogicalPortConfigIngFloodContainer": cienaCesLogicalPortConfigIngFloodContainer,
       "cienaCesLogicalPortConfigPriorityTagMode": cienaCesLogicalPortConfigPriorityTagMode,
       "cienaCesLogicalPortConfigVidTpidCount": cienaCesLogicalPortConfigVidTpidCount,
       "cienaCesPortOperationalSpeed": cienaCesPortOperationalSpeed,
       "cienaCesPortOuterTpidList": cienaCesPortOuterTpidList,
       "cienaCesPortEgressOuterTpid": cienaCesPortEgressOuterTpid,
       "cienaCesPortOuterVtagTpid": cienaCesPortOuterVtagTpid,
       "cienaCesPortAdministrativeSpeed": cienaCesPortAdministrativeSpeed,
       "cienaCesPortTerminalLoopbackState": cienaCesPortTerminalLoopbackState,
       "cienaCesPortLearnLimit": cienaCesPortLearnLimit,
       "cienaCesLogicalPortConfigSignalDegradeDetection": cienaCesLogicalPortConfigSignalDegradeDetection,
       "cienaCesLogicalPortConfigSignalDegradeState": cienaCesLogicalPortConfigSignalDegradeState,
       "cienaCesPortL2CftStatus": cienaCesPortL2CftStatus,
       "cienaCesPortL2CftProfileId": cienaCesPortL2CftProfileId,
       "cienaCesPortConfigHoldOffState": cienaCesPortConfigHoldOffState,
       "cienaCesPortConfigHoldOffTime": cienaCesPortConfigHoldOffTime,
       "cienaCesPortOperFecState": cienaCesPortOperFecState,
       "cienaCesPortPgIdMapping": cienaCesPortPgIdMapping,
       "cienaCesPortPgIdMappingTable": cienaCesPortPgIdMappingTable,
       "cienaCesPortPgIdMappingEntry": cienaCesPortPgIdMappingEntry,
       "cienaCesPortPgIdMappingChassisIndex": cienaCesPortPgIdMappingChassisIndex,
       "cienaCesPortPgIdMappingShelfIndex": cienaCesPortPgIdMappingShelfIndex,
       "cienaCesPortPgIdMappingSlotIndex": cienaCesPortPgIdMappingSlotIndex,
       "cienaCesPortPgidMappingPortNumber": cienaCesPortPgidMappingPortNumber,
       "cienaCesPortPgIdMappingPgId": cienaCesPortPgIdMappingPgId,
       "cienaCesPortPgIdMappingNotifChassisIndex": cienaCesPortPgIdMappingNotifChassisIndex,
       "cienaCesPortPgIdMappingNotifShelfIndex": cienaCesPortPgIdMappingNotifShelfIndex,
       "cienaCesPortPgIdMappingNotifSlotIndex": cienaCesPortPgIdMappingNotifSlotIndex,
       "cienaCesPortPgIdMappingNotifPortNumber": cienaCesPortPgIdMappingNotifPortNumber,
       "cienaCesEttpConfig": cienaCesEttpConfig,
       "cienaCesEttpConfigTable": cienaCesEttpConfigTable,
       "cienaCesEttpConfigEntry": cienaCesEttpConfigEntry,
       "cienaCesEttpConfigEttpId": cienaCesEttpConfigEttpId,
       "cienaCesEttpConfigOperState": cienaCesEttpConfigOperState,
       "cienaCesEttpConfigLinkUpDownTrapState": cienaCesEttpConfigLinkUpDownTrapState,
       "cienaCesEttpConfigAllTrapState": cienaCesEttpConfigAllTrapState,
       "cienaCesEttpConfigMacAddress": cienaCesEttpConfigMacAddress,
       "cienaCesEttpConfigName": cienaCesEttpConfigName,
       "cienaCesEttpConfigEttpType": cienaCesEttpConfigEttpType,
       "cienaCesEttpConfigAdminSpeed": cienaCesEttpConfigAdminSpeed,
       "cienaCesEttpConfigOperSpeed": cienaCesEttpConfigOperSpeed,
       "cienaCesEttpConfigEthLpPgid": cienaCesEttpConfigEthLpPgid,
       "cienaCesEttpConfigDuplex": cienaCesEttpConfigDuplex,
       "cienaCesEttpConfigFlowCntl": cienaCesEttpConfigFlowCntl,
       "cienaCesEttpConfigAutoNeg": cienaCesEttpConfigAutoNeg,
       "cienaCesEttpConfigAdvertisedFlowCntl": cienaCesEttpConfigAdvertisedFlowCntl,
       "cienaCesEttpConfigIfgDecr": cienaCesEttpConfigIfgDecr,
       "cienaCesEttpConfigXcvrFreq": cienaCesEttpConfigXcvrFreq,
       "cienaCesLogicalPortTpid": cienaCesLogicalPortTpid,
       "cienaCesLogicalPortTpidTable": cienaCesLogicalPortTpidTable,
       "cienaCesLogicalPortTpidEntry": cienaCesLogicalPortTpidEntry,
       "cienaCesLogicalPortTpidIndex": cienaCesLogicalPortTpidIndex,
       "cienaCesLogicalPortInnerVidTpid": cienaCesLogicalPortInnerVidTpid,
       "cienaCesLogicalPortOuterVidTpid": cienaCesLogicalPortOuterVidTpid,
       "cienaCesChPortPgIdMapping": cienaCesChPortPgIdMapping,
       "cienaCesChPortPgIdMappingTable": cienaCesChPortPgIdMappingTable,
       "cienaCesChPortPgIdMappingEntry": cienaCesChPortPgIdMappingEntry,
       "cienaCesChPortPgIdMappingChassisIndex": cienaCesChPortPgIdMappingChassisIndex,
       "cienaCesChPortPgIdMappingShelfIndex": cienaCesChPortPgIdMappingShelfIndex,
       "cienaCesChPortPgIdMappingSlotIndex": cienaCesChPortPgIdMappingSlotIndex,
       "cienaCesChPortPgIdMappingPortNumber": cienaCesChPortPgIdMappingPortNumber,
       "cienaCesChPortPgIdMappingChannelNumber": cienaCesChPortPgIdMappingChannelNumber,
       "cienaCesChPortPgIdMappingPgId": cienaCesChPortPgIdMappingPgId,
       "cienaCesChPortPgIdMappingNotifChassisIndex": cienaCesChPortPgIdMappingNotifChassisIndex,
       "cienaCesChPortPgIdMappingNotifShelfIndex": cienaCesChPortPgIdMappingNotifShelfIndex,
       "cienaCesChPortPgIdMappingNotifSlotIndex": cienaCesChPortPgIdMappingNotifSlotIndex,
       "cienaCesChPortPgIdMappingNotifPortNumber": cienaCesChPortPgIdMappingNotifPortNumber,
       "cienaCesChPortPgIdMappingNotifChannelNumber": cienaCesChPortPgIdMappingNotifChannelNumber,
       "cienaCesPortMIBConformance": cienaCesPortMIBConformance,
       "cienaCesPortMIBCompliances": cienaCesPortMIBCompliances,
       "cienaCesPortMIBGroups": cienaCesPortMIBGroups,
       "portConfigGroup": portConfigGroup,
       "portNotifGroup": portNotifGroup,
       "portPgIdMappingGroup": portPgIdMappingGroup,
       "cienaCesPortNotificationMIBNotificationPrefix": cienaCesPortNotificationMIBNotificationPrefix,
       "cienaCesPortNotificationMIBNotifications": cienaCesPortNotificationMIBNotifications,
       "cienaCesPortNotificationPortDown": cienaCesPortNotificationPortDown,
       "cienaCesPortNotificationPortUp": cienaCesPortNotificationPortUp,
       "cienaCesChPortNotificationPortUp": cienaCesChPortNotificationPortUp,
       "cienaCesChPortNotificationPortDown": cienaCesChPortNotificationPortDown,
       "cienaCesPortNotificationPortSignalDegradeSet": cienaCesPortNotificationPortSignalDegradeSet,
       "cienaCesPortNotificationPortSignalDegradeClear": cienaCesPortNotificationPortSignalDegradeClear}
)
