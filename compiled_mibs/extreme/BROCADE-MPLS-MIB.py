# SNMP MIB module (BROCADE-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\BROCADE-MPLS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:14 2025
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(MplsTunnelAffinity,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsTunnelAffinity")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

brocadeMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10)
)
if mibBuilder.loadTexts:
    brocadeMplsMIB.setRevisions(
        ("2018-05-29 12:00",
         "2016-09-28 00:00",
         "2013-05-29 00:00",
         "2010-06-02 00:00",
         "2008-02-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClassOfService(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )



# MIB Managed Objects in the order of their OIDs

_BcsiMplsNotifications_ObjectIdentity = ObjectIdentity
bcsiMplsNotifications = _BcsiMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 0)
)
_BcsiMplsObjects_ObjectIdentity = ObjectIdentity
bcsiMplsObjects = _BcsiMplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1)
)
_BcsiMplsInfo_ObjectIdentity = ObjectIdentity
bcsiMplsInfo = _BcsiMplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1)
)
_BcsiMplsVersion_Type = Unsigned32
_BcsiMplsVersion_Object = MibScalar
bcsiMplsVersion = _BcsiMplsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 1),
    _BcsiMplsVersion_Type()
)
bcsiMplsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsVersion.setStatus("current")
_BcsiMplsAdminGroupTable_Object = MibTable
bcsiMplsAdminGroupTable = _BcsiMplsAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    bcsiMplsAdminGroupTable.setStatus("current")
_BcsiMplsAdminGroupEntry_Object = MibTableRow
bcsiMplsAdminGroupEntry = _BcsiMplsAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 2, 1)
)
bcsiMplsAdminGroupEntry.setIndexNames(
    (0, "BROCADE-MPLS-MIB", "bcsiMplsAdminGroupId"),
)
if mibBuilder.loadTexts:
    bcsiMplsAdminGroupEntry.setStatus("current")


class _BcsiMplsAdminGroupId_Type(Unsigned32):
    """Custom type bcsiMplsAdminGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BcsiMplsAdminGroupId_Type.__name__ = "Unsigned32"
_BcsiMplsAdminGroupId_Object = MibTableColumn
bcsiMplsAdminGroupId = _BcsiMplsAdminGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 2, 1, 1),
    _BcsiMplsAdminGroupId_Type()
)
bcsiMplsAdminGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiMplsAdminGroupId.setStatus("current")


class _BcsiMplsAdminGroupName_Type(DisplayString):
    """Custom type bcsiMplsAdminGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BcsiMplsAdminGroupName_Type.__name__ = "DisplayString"
_BcsiMplsAdminGroupName_Object = MibTableColumn
bcsiMplsAdminGroupName = _BcsiMplsAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 2, 1, 2),
    _BcsiMplsAdminGroupName_Type()
)
bcsiMplsAdminGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcsiMplsAdminGroupName.setStatus("current")
_BcsiMplsAdminGroupRowStatus_Type = RowStatus
_BcsiMplsAdminGroupRowStatus_Object = MibTableColumn
bcsiMplsAdminGroupRowStatus = _BcsiMplsAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 2, 1, 3),
    _BcsiMplsAdminGroupRowStatus_Type()
)
bcsiMplsAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcsiMplsAdminGroupRowStatus.setStatus("current")
_BcsiMplsInterfaceTable_Object = MibTable
bcsiMplsInterfaceTable = _BcsiMplsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    bcsiMplsInterfaceTable.setStatus("current")
_BcsiMplsInterfaceEntry_Object = MibTableRow
bcsiMplsInterfaceEntry = _BcsiMplsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 3, 1)
)
bcsiMplsInterfaceEntry.setIndexNames(
    (0, "BROCADE-MPLS-MIB", "bcsiMplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    bcsiMplsInterfaceEntry.setStatus("current")
_BcsiMplsInterfaceIndex_Type = Unsigned32
_BcsiMplsInterfaceIndex_Object = MibTableColumn
bcsiMplsInterfaceIndex = _BcsiMplsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 3, 1, 1),
    _BcsiMplsInterfaceIndex_Type()
)
bcsiMplsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiMplsInterfaceIndex.setStatus("current")
_BcsiMplsInterfaceAdminGroup_Type = MplsTunnelAffinity
_BcsiMplsInterfaceAdminGroup_Object = MibTableColumn
bcsiMplsInterfaceAdminGroup = _BcsiMplsInterfaceAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 3, 1, 2),
    _BcsiMplsInterfaceAdminGroup_Type()
)
bcsiMplsInterfaceAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcsiMplsInterfaceAdminGroup.setStatus("current")
_BcsiMplsInterfaceRowStatus_Type = RowStatus
_BcsiMplsInterfaceRowStatus_Object = MibTableColumn
bcsiMplsInterfaceRowStatus = _BcsiMplsInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 1, 3, 1, 3),
    _BcsiMplsInterfaceRowStatus_Type()
)
bcsiMplsInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bcsiMplsInterfaceRowStatus.setStatus("current")
_BcsiMplsLspInfo_ObjectIdentity = ObjectIdentity
bcsiMplsLspInfo = _BcsiMplsLspInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2)
)
_BcsiMplsConfiguredLsps_Type = Unsigned32
_BcsiMplsConfiguredLsps_Object = MibScalar
bcsiMplsConfiguredLsps = _BcsiMplsConfiguredLsps_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 1),
    _BcsiMplsConfiguredLsps_Type()
)
bcsiMplsConfiguredLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsConfiguredLsps.setStatus("deprecated")
_BcsiMplsActiveLsps_Type = Unsigned32
_BcsiMplsActiveLsps_Object = MibScalar
bcsiMplsActiveLsps = _BcsiMplsActiveLsps_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 2),
    _BcsiMplsActiveLsps_Type()
)
bcsiMplsActiveLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsActiveLsps.setStatus("deprecated")
_BcsiMplsLspTable_Object = MibTable
bcsiMplsLspTable = _BcsiMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    bcsiMplsLspTable.setStatus("current")
_BcsiMplsLspEntry_Object = MibTableRow
bcsiMplsLspEntry = _BcsiMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1)
)
bcsiMplsLspEntry.setIndexNames(
    (0, "BROCADE-MPLS-MIB", "bcsiMplsLspSignalingProto"),
    (0, "BROCADE-MPLS-MIB", "bcsiMplsLspIndex"),
)
if mibBuilder.loadTexts:
    bcsiMplsLspEntry.setStatus("current")


class _BcsiMplsLspSignalingProto_Type(Integer32):
    """Custom type bcsiMplsLspSignalingProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldp", 1),
          ("rsvp", 2))
    )


_BcsiMplsLspSignalingProto_Type.__name__ = "Integer32"
_BcsiMplsLspSignalingProto_Object = MibTableColumn
bcsiMplsLspSignalingProto = _BcsiMplsLspSignalingProto_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 1),
    _BcsiMplsLspSignalingProto_Type()
)
bcsiMplsLspSignalingProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiMplsLspSignalingProto.setStatus("current")
_BcsiMplsLspIndex_Type = Unsigned32
_BcsiMplsLspIndex_Object = MibTableColumn
bcsiMplsLspIndex = _BcsiMplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 2),
    _BcsiMplsLspIndex_Type()
)
bcsiMplsLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsiMplsLspIndex.setStatus("current")


class _BcsiMplsLspName_Type(DisplayString):
    """Custom type bcsiMplsLspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BcsiMplsLspName_Type.__name__ = "DisplayString"
_BcsiMplsLspName_Object = MibTableColumn
bcsiMplsLspName = _BcsiMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 3),
    _BcsiMplsLspName_Type()
)
bcsiMplsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspName.setStatus("current")


class _BcsiMplsLspState_Type(Integer32):
    """Custom type bcsiMplsLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("up", 2),
          ("down", 3))
    )


_BcsiMplsLspState_Type.__name__ = "Integer32"
_BcsiMplsLspState_Object = MibTableColumn
bcsiMplsLspState = _BcsiMplsLspState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 4),
    _BcsiMplsLspState_Type()
)
bcsiMplsLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspState.setStatus("current")
_BcsiMplsLspPackets_Type = Counter64
_BcsiMplsLspPackets_Object = MibTableColumn
bcsiMplsLspPackets = _BcsiMplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 5),
    _BcsiMplsLspPackets_Type()
)
bcsiMplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPackets.setStatus("current")
_BcsiMplsLspAge_Type = TimeStamp
_BcsiMplsLspAge_Object = MibTableColumn
bcsiMplsLspAge = _BcsiMplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 6),
    _BcsiMplsLspAge_Type()
)
bcsiMplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspAge.setStatus("current")
_BcsiMplsLspTimeUp_Type = TimeStamp
_BcsiMplsLspTimeUp_Object = MibTableColumn
bcsiMplsLspTimeUp = _BcsiMplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 7),
    _BcsiMplsLspTimeUp_Type()
)
bcsiMplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspTimeUp.setStatus("current")
_BcsiMplsLspPrimaryTimeUp_Type = TimeStamp
_BcsiMplsLspPrimaryTimeUp_Object = MibTableColumn
bcsiMplsLspPrimaryTimeUp = _BcsiMplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 8),
    _BcsiMplsLspPrimaryTimeUp_Type()
)
bcsiMplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPrimaryTimeUp.setStatus("current")
_BcsiMplsLspTransitions_Type = Counter32
_BcsiMplsLspTransitions_Object = MibTableColumn
bcsiMplsLspTransitions = _BcsiMplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 9),
    _BcsiMplsLspTransitions_Type()
)
bcsiMplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspTransitions.setStatus("current")
_BcsiMplsLspLastTransition_Type = TimeStamp
_BcsiMplsLspLastTransition_Object = MibTableColumn
bcsiMplsLspLastTransition = _BcsiMplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 10),
    _BcsiMplsLspLastTransition_Type()
)
bcsiMplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspLastTransition.setStatus("current")
_BcsiMplsLspFrom_Type = IpAddress
_BcsiMplsLspFrom_Object = MibTableColumn
bcsiMplsLspFrom = _BcsiMplsLspFrom_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 11),
    _BcsiMplsLspFrom_Type()
)
bcsiMplsLspFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrom.setStatus("current")
_BcsiMplsLspTo_Type = IpAddress
_BcsiMplsLspTo_Object = MibTableColumn
bcsiMplsLspTo = _BcsiMplsLspTo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 12),
    _BcsiMplsLspTo_Type()
)
bcsiMplsLspTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspTo.setStatus("current")


class _BcsiMplsLspPathName_Type(DisplayString):
    """Custom type bcsiMplsLspPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BcsiMplsLspPathName_Type.__name__ = "DisplayString"
_BcsiMplsLspPathName_Object = MibTableColumn
bcsiMplsLspPathName = _BcsiMplsLspPathName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 13),
    _BcsiMplsLspPathName_Type()
)
bcsiMplsLspPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPathName.setStatus("current")


class _BcsiMplsLspPathType_Type(Integer32):
    """Custom type bcsiMplsLspPathType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("standby", 3),
          ("secondary", 4))
    )


_BcsiMplsLspPathType_Type.__name__ = "Integer32"
_BcsiMplsLspPathType_Object = MibTableColumn
bcsiMplsLspPathType = _BcsiMplsLspPathType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 14),
    _BcsiMplsLspPathType_Type()
)
bcsiMplsLspPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPathType.setStatus("current")
_BcsiMplsLspAdaptive_Type = TruthValue
_BcsiMplsLspAdaptive_Object = MibTableColumn
bcsiMplsLspAdaptive = _BcsiMplsLspAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 15),
    _BcsiMplsLspAdaptive_Type()
)
bcsiMplsLspAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspAdaptive.setStatus("current")
_BcsiMplsLspBfdSessionId_Type = Unsigned32
_BcsiMplsLspBfdSessionId_Object = MibTableColumn
bcsiMplsLspBfdSessionId = _BcsiMplsLspBfdSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 16),
    _BcsiMplsLspBfdSessionId_Type()
)
bcsiMplsLspBfdSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspBfdSessionId.setStatus("current")


class _BcsiMplsLspReoptimizeTimer_Type(Unsigned32):
    """Custom type bcsiMplsLspReoptimizeTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 65535),
    )


_BcsiMplsLspReoptimizeTimer_Type.__name__ = "Unsigned32"
_BcsiMplsLspReoptimizeTimer_Object = MibTableColumn
bcsiMplsLspReoptimizeTimer = _BcsiMplsLspReoptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 17),
    _BcsiMplsLspReoptimizeTimer_Type()
)
bcsiMplsLspReoptimizeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspReoptimizeTimer.setStatus("current")
_BcsiMplsLspCoS_Type = ClassOfService
_BcsiMplsLspCoS_Object = MibTableColumn
bcsiMplsLspCoS = _BcsiMplsLspCoS_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 18),
    _BcsiMplsLspCoS_Type()
)
bcsiMplsLspCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspCoS.setStatus("current")


class _BcsiMplsLspHopLimit_Type(Unsigned32):
    """Custom type bcsiMplsLspHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcsiMplsLspHopLimit_Type.__name__ = "Unsigned32"
_BcsiMplsLspHopLimit_Object = MibTableColumn
bcsiMplsLspHopLimit = _BcsiMplsLspHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 19),
    _BcsiMplsLspHopLimit_Type()
)
bcsiMplsLspHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspHopLimit.setStatus("current")


class _BcsiMplsLspCspf_Type(Integer32):
    """Custom type bcsiMplsLspCspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_BcsiMplsLspCspf_Type.__name__ = "Integer32"
_BcsiMplsLspCspf_Object = MibTableColumn
bcsiMplsLspCspf = _BcsiMplsLspCspf_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 20),
    _BcsiMplsLspCspf_Type()
)
bcsiMplsLspCspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspCspf.setStatus("current")


class _BcsiMplsLspCspfTieBreaker_Type(Integer32):
    """Custom type bcsiMplsLspCspfTieBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("random", 1),
          ("leastFill", 2),
          ("mostFill", 3))
    )


_BcsiMplsLspCspfTieBreaker_Type.__name__ = "Integer32"
_BcsiMplsLspCspfTieBreaker_Object = MibTableColumn
bcsiMplsLspCspfTieBreaker = _BcsiMplsLspCspfTieBreaker_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 21),
    _BcsiMplsLspCspfTieBreaker_Type()
)
bcsiMplsLspCspfTieBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspCspfTieBreaker.setStatus("current")


class _BcsiMplsLspFrrMode_Type(Integer32):
    """Custom type bcsiMplsLspFrrMode based on Integer32"""
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
          ("detour", 2),
          ("facility", 3))
    )


_BcsiMplsLspFrrMode_Type.__name__ = "Integer32"
_BcsiMplsLspFrrMode_Object = MibTableColumn
bcsiMplsLspFrrMode = _BcsiMplsLspFrrMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 22),
    _BcsiMplsLspFrrMode_Type()
)
bcsiMplsLspFrrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrMode.setStatus("current")


class _BcsiMplsLspFrrSetupPriority_Type(Unsigned32):
    """Custom type bcsiMplsLspFrrSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BcsiMplsLspFrrSetupPriority_Type.__name__ = "Unsigned32"
_BcsiMplsLspFrrSetupPriority_Object = MibTableColumn
bcsiMplsLspFrrSetupPriority = _BcsiMplsLspFrrSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 23),
    _BcsiMplsLspFrrSetupPriority_Type()
)
bcsiMplsLspFrrSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrSetupPriority.setStatus("current")


class _BcsiMplsLspFrrHoldingPriority_Type(Unsigned32):
    """Custom type bcsiMplsLspFrrHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BcsiMplsLspFrrHoldingPriority_Type.__name__ = "Unsigned32"
_BcsiMplsLspFrrHoldingPriority_Object = MibTableColumn
bcsiMplsLspFrrHoldingPriority = _BcsiMplsLspFrrHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 24),
    _BcsiMplsLspFrrHoldingPriority_Type()
)
bcsiMplsLspFrrHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrHoldingPriority.setStatus("current")


class _BcsiMplsLspFrrHopLimit_Type(Unsigned32):
    """Custom type bcsiMplsLspFrrHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcsiMplsLspFrrHopLimit_Type.__name__ = "Unsigned32"
_BcsiMplsLspFrrHopLimit_Object = MibTableColumn
bcsiMplsLspFrrHopLimit = _BcsiMplsLspFrrHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 25),
    _BcsiMplsLspFrrHopLimit_Type()
)
bcsiMplsLspFrrHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrHopLimit.setStatus("current")


class _BcsiMplsLspFrrBandwidth_Type(Unsigned32):
    """Custom type bcsiMplsLspFrrBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BcsiMplsLspFrrBandwidth_Type.__name__ = "Unsigned32"
_BcsiMplsLspFrrBandwidth_Object = MibTableColumn
bcsiMplsLspFrrBandwidth = _BcsiMplsLspFrrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 26),
    _BcsiMplsLspFrrBandwidth_Type()
)
bcsiMplsLspFrrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrBandwidth.setStatus("current")
_BcsiMplsLspFrrAdmGrpIncludeAny_Type = MplsTunnelAffinity
_BcsiMplsLspFrrAdmGrpIncludeAny_Object = MibTableColumn
bcsiMplsLspFrrAdmGrpIncludeAny = _BcsiMplsLspFrrAdmGrpIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 27),
    _BcsiMplsLspFrrAdmGrpIncludeAny_Type()
)
bcsiMplsLspFrrAdmGrpIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrAdmGrpIncludeAny.setStatus("current")
_BcsiMplsLspFrrAdmGrpIncludeAll_Type = MplsTunnelAffinity
_BcsiMplsLspFrrAdmGrpIncludeAll_Object = MibTableColumn
bcsiMplsLspFrrAdmGrpIncludeAll = _BcsiMplsLspFrrAdmGrpIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 28),
    _BcsiMplsLspFrrAdmGrpIncludeAll_Type()
)
bcsiMplsLspFrrAdmGrpIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrAdmGrpIncludeAll.setStatus("current")
_BcsiMplsLspFrrAdmGrpExcludeAny_Type = MplsTunnelAffinity
_BcsiMplsLspFrrAdmGrpExcludeAny_Object = MibTableColumn
bcsiMplsLspFrrAdmGrpExcludeAny = _BcsiMplsLspFrrAdmGrpExcludeAny_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 29),
    _BcsiMplsLspFrrAdmGrpExcludeAny_Type()
)
bcsiMplsLspFrrAdmGrpExcludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspFrrAdmGrpExcludeAny.setStatus("current")


class _BcsiMplsLspPathSelectMode_Type(Integer32):
    """Custom type bcsiMplsLspPathSelectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("unconditional", 3))
    )


_BcsiMplsLspPathSelectMode_Type.__name__ = "Integer32"
_BcsiMplsLspPathSelectMode_Object = MibTableColumn
bcsiMplsLspPathSelectMode = _BcsiMplsLspPathSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 30),
    _BcsiMplsLspPathSelectMode_Type()
)
bcsiMplsLspPathSelectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPathSelectMode.setStatus("current")


class _BcsiMplsLspPathSelectPathname_Type(DisplayString):
    """Custom type bcsiMplsLspPathSelectPathname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BcsiMplsLspPathSelectPathname_Type.__name__ = "DisplayString"
_BcsiMplsLspPathSelectPathname_Object = MibTableColumn
bcsiMplsLspPathSelectPathname = _BcsiMplsLspPathSelectPathname_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 31),
    _BcsiMplsLspPathSelectPathname_Type()
)
bcsiMplsLspPathSelectPathname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPathSelectPathname.setStatus("current")


class _BcsiMplsLspPathSelectRevertTimer_Type(Unsigned32):
    """Custom type bcsiMplsLspPathSelectRevertTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BcsiMplsLspPathSelectRevertTimer_Type.__name__ = "Unsigned32"
_BcsiMplsLspPathSelectRevertTimer_Object = MibTableColumn
bcsiMplsLspPathSelectRevertTimer = _BcsiMplsLspPathSelectRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 32),
    _BcsiMplsLspPathSelectRevertTimer_Type()
)
bcsiMplsLspPathSelectRevertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspPathSelectRevertTimer.setStatus("current")
_BcsiMplsLspShortcutOspfAllowed_Type = TruthValue
_BcsiMplsLspShortcutOspfAllowed_Object = MibTableColumn
bcsiMplsLspShortcutOspfAllowed = _BcsiMplsLspShortcutOspfAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 33),
    _BcsiMplsLspShortcutOspfAllowed_Type()
)
bcsiMplsLspShortcutOspfAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspShortcutOspfAllowed.setStatus("current")
_BcsiMplsLspShortcutIsisAllowed_Type = TruthValue
_BcsiMplsLspShortcutIsisAllowed_Object = MibTableColumn
bcsiMplsLspShortcutIsisAllowed = _BcsiMplsLspShortcutIsisAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 34),
    _BcsiMplsLspShortcutIsisAllowed_Type()
)
bcsiMplsLspShortcutIsisAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspShortcutIsisAllowed.setStatus("current")


class _BcsiMplsLspShortcutIsisLevel_Type(Integer32):
    """Custom type bcsiMplsLspShortcutIsisLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1and2", 3))
    )


_BcsiMplsLspShortcutIsisLevel_Type.__name__ = "Integer32"
_BcsiMplsLspShortcutIsisLevel_Object = MibTableColumn
bcsiMplsLspShortcutIsisLevel = _BcsiMplsLspShortcutIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 35),
    _BcsiMplsLspShortcutIsisLevel_Type()
)
bcsiMplsLspShortcutIsisLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspShortcutIsisLevel.setStatus("current")
_BcsiMplsLspShortcutIsisAnnounce_Type = TruthValue
_BcsiMplsLspShortcutIsisAnnounce_Object = MibTableColumn
bcsiMplsLspShortcutIsisAnnounce = _BcsiMplsLspShortcutIsisAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 36),
    _BcsiMplsLspShortcutIsisAnnounce_Type()
)
bcsiMplsLspShortcutIsisAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspShortcutIsisAnnounce.setStatus("current")


class _BcsiMplsLspShortcutIsisAnnounceMetric_Type(Integer32):
    """Custom type bcsiMplsLspShortcutIsisAnnounceMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_BcsiMplsLspShortcutIsisAnnounceMetric_Type.__name__ = "Integer32"
_BcsiMplsLspShortcutIsisAnnounceMetric_Object = MibTableColumn
bcsiMplsLspShortcutIsisAnnounceMetric = _BcsiMplsLspShortcutIsisAnnounceMetric_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 37),
    _BcsiMplsLspShortcutIsisAnnounceMetric_Type()
)
bcsiMplsLspShortcutIsisAnnounceMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspShortcutIsisAnnounceMetric.setStatus("current")


class _BcsiMplsLspShortcutIsisRelativeMetric_Type(Integer32):
    """Custom type bcsiMplsLspShortcutIsisRelativeMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16777215, 16777215),
    )


_BcsiMplsLspShortcutIsisRelativeMetric_Type.__name__ = "Integer32"
_BcsiMplsLspShortcutIsisRelativeMetric_Object = MibTableColumn
bcsiMplsLspShortcutIsisRelativeMetric = _BcsiMplsLspShortcutIsisRelativeMetric_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 2, 3, 1, 38),
    _BcsiMplsLspShortcutIsisRelativeMetric_Type()
)
bcsiMplsLspShortcutIsisRelativeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsiMplsLspShortcutIsisRelativeMetric.setStatus("current")
_BcsiMplsVllInfo_ObjectIdentity = ObjectIdentity
bcsiMplsVllInfo = _BcsiMplsVllInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 3)
)
_BcsiMplsVplsInfo_ObjectIdentity = ObjectIdentity
bcsiMplsVplsInfo = _BcsiMplsVplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 1, 4)
)
_BcsiMplsConformance_ObjectIdentity = ObjectIdentity
bcsiMplsConformance = _BcsiMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 2)
)

# Managed Objects groups


# Notification objects

bcsiMplsLspUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 0, 1)
)
bcsiMplsLspUpNotification.setObjects(
      *(("BROCADE-MPLS-MIB", "bcsiMplsLspName"),
        ("BROCADE-MPLS-MIB", "bcsiMplsLspPathName"))
)
if mibBuilder.loadTexts:
    bcsiMplsLspUpNotification.setStatus(
        "current"
    )

bcsiMplsLspDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 0, 2)
)
bcsiMplsLspDownNotification.setObjects(
      *(("BROCADE-MPLS-MIB", "bcsiMplsLspName"),
        ("BROCADE-MPLS-MIB", "bcsiMplsLspPathName"))
)
if mibBuilder.loadTexts:
    bcsiMplsLspDownNotification.setStatus(
        "current"
    )

bcsiMplsLspChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 10, 0, 3)
)
bcsiMplsLspChangeNotification.setObjects(
      *(("BROCADE-MPLS-MIB", "bcsiMplsLspName"),
        ("BROCADE-MPLS-MIB", "bcsiMplsLspPathName"))
)
if mibBuilder.loadTexts:
    bcsiMplsLspChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-MPLS-MIB",
    **{"ClassOfService": ClassOfService,
       "brocadeMplsMIB": brocadeMplsMIB,
       "bcsiMplsNotifications": bcsiMplsNotifications,
       "bcsiMplsLspUpNotification": bcsiMplsLspUpNotification,
       "bcsiMplsLspDownNotification": bcsiMplsLspDownNotification,
       "bcsiMplsLspChangeNotification": bcsiMplsLspChangeNotification,
       "bcsiMplsObjects": bcsiMplsObjects,
       "bcsiMplsInfo": bcsiMplsInfo,
       "bcsiMplsVersion": bcsiMplsVersion,
       "bcsiMplsAdminGroupTable": bcsiMplsAdminGroupTable,
       "bcsiMplsAdminGroupEntry": bcsiMplsAdminGroupEntry,
       "bcsiMplsAdminGroupId": bcsiMplsAdminGroupId,
       "bcsiMplsAdminGroupName": bcsiMplsAdminGroupName,
       "bcsiMplsAdminGroupRowStatus": bcsiMplsAdminGroupRowStatus,
       "bcsiMplsInterfaceTable": bcsiMplsInterfaceTable,
       "bcsiMplsInterfaceEntry": bcsiMplsInterfaceEntry,
       "bcsiMplsInterfaceIndex": bcsiMplsInterfaceIndex,
       "bcsiMplsInterfaceAdminGroup": bcsiMplsInterfaceAdminGroup,
       "bcsiMplsInterfaceRowStatus": bcsiMplsInterfaceRowStatus,
       "bcsiMplsLspInfo": bcsiMplsLspInfo,
       "bcsiMplsConfiguredLsps": bcsiMplsConfiguredLsps,
       "bcsiMplsActiveLsps": bcsiMplsActiveLsps,
       "bcsiMplsLspTable": bcsiMplsLspTable,
       "bcsiMplsLspEntry": bcsiMplsLspEntry,
       "bcsiMplsLspSignalingProto": bcsiMplsLspSignalingProto,
       "bcsiMplsLspIndex": bcsiMplsLspIndex,
       "bcsiMplsLspName": bcsiMplsLspName,
       "bcsiMplsLspState": bcsiMplsLspState,
       "bcsiMplsLspPackets": bcsiMplsLspPackets,
       "bcsiMplsLspAge": bcsiMplsLspAge,
       "bcsiMplsLspTimeUp": bcsiMplsLspTimeUp,
       "bcsiMplsLspPrimaryTimeUp": bcsiMplsLspPrimaryTimeUp,
       "bcsiMplsLspTransitions": bcsiMplsLspTransitions,
       "bcsiMplsLspLastTransition": bcsiMplsLspLastTransition,
       "bcsiMplsLspFrom": bcsiMplsLspFrom,
       "bcsiMplsLspTo": bcsiMplsLspTo,
       "bcsiMplsLspPathName": bcsiMplsLspPathName,
       "bcsiMplsLspPathType": bcsiMplsLspPathType,
       "bcsiMplsLspAdaptive": bcsiMplsLspAdaptive,
       "bcsiMplsLspBfdSessionId": bcsiMplsLspBfdSessionId,
       "bcsiMplsLspReoptimizeTimer": bcsiMplsLspReoptimizeTimer,
       "bcsiMplsLspCoS": bcsiMplsLspCoS,
       "bcsiMplsLspHopLimit": bcsiMplsLspHopLimit,
       "bcsiMplsLspCspf": bcsiMplsLspCspf,
       "bcsiMplsLspCspfTieBreaker": bcsiMplsLspCspfTieBreaker,
       "bcsiMplsLspFrrMode": bcsiMplsLspFrrMode,
       "bcsiMplsLspFrrSetupPriority": bcsiMplsLspFrrSetupPriority,
       "bcsiMplsLspFrrHoldingPriority": bcsiMplsLspFrrHoldingPriority,
       "bcsiMplsLspFrrHopLimit": bcsiMplsLspFrrHopLimit,
       "bcsiMplsLspFrrBandwidth": bcsiMplsLspFrrBandwidth,
       "bcsiMplsLspFrrAdmGrpIncludeAny": bcsiMplsLspFrrAdmGrpIncludeAny,
       "bcsiMplsLspFrrAdmGrpIncludeAll": bcsiMplsLspFrrAdmGrpIncludeAll,
       "bcsiMplsLspFrrAdmGrpExcludeAny": bcsiMplsLspFrrAdmGrpExcludeAny,
       "bcsiMplsLspPathSelectMode": bcsiMplsLspPathSelectMode,
       "bcsiMplsLspPathSelectPathname": bcsiMplsLspPathSelectPathname,
       "bcsiMplsLspPathSelectRevertTimer": bcsiMplsLspPathSelectRevertTimer,
       "bcsiMplsLspShortcutOspfAllowed": bcsiMplsLspShortcutOspfAllowed,
       "bcsiMplsLspShortcutIsisAllowed": bcsiMplsLspShortcutIsisAllowed,
       "bcsiMplsLspShortcutIsisLevel": bcsiMplsLspShortcutIsisLevel,
       "bcsiMplsLspShortcutIsisAnnounce": bcsiMplsLspShortcutIsisAnnounce,
       "bcsiMplsLspShortcutIsisAnnounceMetric": bcsiMplsLspShortcutIsisAnnounceMetric,
       "bcsiMplsLspShortcutIsisRelativeMetric": bcsiMplsLspShortcutIsisRelativeMetric,
       "bcsiMplsVllInfo": bcsiMplsVllInfo,
       "bcsiMplsVplsInfo": bcsiMplsVplsInfo,
       "bcsiMplsConformance": bcsiMplsConformance}
)
