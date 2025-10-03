# SNMP MIB module (SLE-MPLS-TP-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-MPLS-TP-OAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:40 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMplsTpOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17)
)
if mibBuilder.loadTexts:
    sleMplsTpOam.setRevisions(
        ("2013-01-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
if mibBuilder.loadTexts:
    sleMpls.setStatus("current")
_SleMplsTpOamMeg_ObjectIdentity = ObjectIdentity
sleMplsTpOamMeg = _SleMplsTpOamMeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1)
)
_SleMplsTpOamMegInfoTable_Object = MibTable
sleMplsTpOamMegInfoTable = _SleMplsTpOamMegInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoTable.setStatus("current")
_SleMplsTpOamMegInfoEntry_Object = MibTableRow
sleMplsTpOamMegInfoEntry = _SleMplsTpOamMegInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1)
)
sleMplsTpOamMegInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-OAM-MIB", "sleMplsTpOamMegInfoIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoEntry.setStatus("current")


class _SleMplsTpOamMegInfoIndex_Type(Unsigned32):
    """Custom type sleMplsTpOamMegInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpOamMegInfoIndex_Type.__name__ = "Unsigned32"
_SleMplsTpOamMegInfoIndex_Object = MibTableColumn
sleMplsTpOamMegInfoIndex = _SleMplsTpOamMegInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1, 1),
    _SleMplsTpOamMegInfoIndex_Type()
)
sleMplsTpOamMegInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoIndex.setStatus("current")


class _SleMplsTpOamMegInfoName_Type(OctetString):
    """Custom type sleMplsTpOamMegInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleMplsTpOamMegInfoName_Type.__name__ = "OctetString"
_SleMplsTpOamMegInfoName_Object = MibTableColumn
sleMplsTpOamMegInfoName = _SleMplsTpOamMegInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1, 2),
    _SleMplsTpOamMegInfoName_Type()
)
sleMplsTpOamMegInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoName.setStatus("current")


class _SleMplsTpOamMegInfoOperatorType_Type(Integer32):
    """Custom type sleMplsTpOamMegInfoOperatorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpOamMegInfoOperatorType_Type.__name__ = "Integer32"
_SleMplsTpOamMegInfoOperatorType_Object = MibTableColumn
sleMplsTpOamMegInfoOperatorType = _SleMplsTpOamMegInfoOperatorType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1, 3),
    _SleMplsTpOamMegInfoOperatorType_Type()
)
sleMplsTpOamMegInfoOperatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoOperatorType.setStatus("current")


class _SleMplsTpOamMegInfoServiceType_Type(Integer32):
    """Custom type sleMplsTpOamMegInfoServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("vc", 2),
          ("datalink", 3))
    )


_SleMplsTpOamMegInfoServiceType_Type.__name__ = "Integer32"
_SleMplsTpOamMegInfoServiceType_Object = MibTableColumn
sleMplsTpOamMegInfoServiceType = _SleMplsTpOamMegInfoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1, 4),
    _SleMplsTpOamMegInfoServiceType_Type()
)
sleMplsTpOamMegInfoServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoServiceType.setStatus("current")


class _SleMplsTpOamMegInfoMegLevel_Type(Integer32):
    """Custom type sleMplsTpOamMegInfoMegLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsTpOamMegInfoMegLevel_Type.__name__ = "Integer32"
_SleMplsTpOamMegInfoMegLevel_Object = MibTableColumn
sleMplsTpOamMegInfoMegLevel = _SleMplsTpOamMegInfoMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1, 5),
    _SleMplsTpOamMegInfoMegLevel_Type()
)
sleMplsTpOamMegInfoMegLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoMegLevel.setStatus("current")


class _SleMplsTpOamMegInfoOperStatus_Type(Integer32):
    """Custom type sleMplsTpOamMegInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SleMplsTpOamMegInfoOperStatus_Type.__name__ = "Integer32"
_SleMplsTpOamMegInfoOperStatus_Object = MibTableColumn
sleMplsTpOamMegInfoOperStatus = _SleMplsTpOamMegInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 1, 1, 6),
    _SleMplsTpOamMegInfoOperStatus_Type()
)
sleMplsTpOamMegInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegInfoOperStatus.setStatus("current")
_SleMplsTpOamMegControl_ObjectIdentity = ObjectIdentity
sleMplsTpOamMegControl = _SleMplsTpOamMegControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2)
)


class _SleMplsTpOamMegControlRequest_Type(Integer32):
    """Custom type sleMplsTpOamMegControlRequest based on Integer32"""
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
        *(("createsleMplsTpOamMegControlEntry", 1),
          ("deletesleMplsTpOamMegControlEntry", 2),
          ("setsleMplsTpOamMegControlServiceType", 3),
          ("setsleMplsTpOamMegControlLevel", 4))
    )


_SleMplsTpOamMegControlRequest_Type.__name__ = "Integer32"
_SleMplsTpOamMegControlRequest_Object = MibScalar
sleMplsTpOamMegControlRequest = _SleMplsTpOamMegControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 1),
    _SleMplsTpOamMegControlRequest_Type()
)
sleMplsTpOamMegControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlRequest.setStatus("current")
_SleMplsTpOamMegControlStatus_Type = SleControlStatusType
_SleMplsTpOamMegControlStatus_Object = MibScalar
sleMplsTpOamMegControlStatus = _SleMplsTpOamMegControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 2),
    _SleMplsTpOamMegControlStatus_Type()
)
sleMplsTpOamMegControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlStatus.setStatus("current")
_SleMplsTpOamMegControlTimer_Type = Gauge32
_SleMplsTpOamMegControlTimer_Object = MibScalar
sleMplsTpOamMegControlTimer = _SleMplsTpOamMegControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 3),
    _SleMplsTpOamMegControlTimer_Type()
)
sleMplsTpOamMegControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlTimer.setStatus("current")
_SleMplsTpOamMegControlTimeStamp_Type = TimeTicks
_SleMplsTpOamMegControlTimeStamp_Object = MibScalar
sleMplsTpOamMegControlTimeStamp = _SleMplsTpOamMegControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 4),
    _SleMplsTpOamMegControlTimeStamp_Type()
)
sleMplsTpOamMegControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlTimeStamp.setStatus("current")
_SleMplsTpOamMegControlReqResult_Type = SleControlRequestResultType
_SleMplsTpOamMegControlReqResult_Object = MibScalar
sleMplsTpOamMegControlReqResult = _SleMplsTpOamMegControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 5),
    _SleMplsTpOamMegControlReqResult_Type()
)
sleMplsTpOamMegControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlReqResult.setStatus("current")


class _SleMplsTpOamMegControlName_Type(OctetString):
    """Custom type sleMplsTpOamMegControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleMplsTpOamMegControlName_Type.__name__ = "OctetString"
_SleMplsTpOamMegControlName_Object = MibScalar
sleMplsTpOamMegControlName = _SleMplsTpOamMegControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 6),
    _SleMplsTpOamMegControlName_Type()
)
sleMplsTpOamMegControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlName.setStatus("current")


class _SleMplsTpOamMegControlOperatorType_Type(Integer32):
    """Custom type sleMplsTpOamMegControlOperatorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpOamMegControlOperatorType_Type.__name__ = "Integer32"
_SleMplsTpOamMegControlOperatorType_Object = MibScalar
sleMplsTpOamMegControlOperatorType = _SleMplsTpOamMegControlOperatorType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 7),
    _SleMplsTpOamMegControlOperatorType_Type()
)
sleMplsTpOamMegControlOperatorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlOperatorType.setStatus("current")


class _SleMplsTpOamMegControlServiceType_Type(Integer32):
    """Custom type sleMplsTpOamMegControlServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("vc", 2),
          ("datalink", 3))
    )


_SleMplsTpOamMegControlServiceType_Type.__name__ = "Integer32"
_SleMplsTpOamMegControlServiceType_Object = MibScalar
sleMplsTpOamMegControlServiceType = _SleMplsTpOamMegControlServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 8),
    _SleMplsTpOamMegControlServiceType_Type()
)
sleMplsTpOamMegControlServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlServiceType.setStatus("current")


class _SleMplsTpOamMegControlLevel_Type(Integer32):
    """Custom type sleMplsTpOamMegControlLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsTpOamMegControlLevel_Type.__name__ = "Integer32"
_SleMplsTpOamMegControlLevel_Object = MibScalar
sleMplsTpOamMegControlLevel = _SleMplsTpOamMegControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 1, 2, 9),
    _SleMplsTpOamMegControlLevel_Type()
)
sleMplsTpOamMegControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMegControlLevel.setStatus("current")
_SleMplsTpOamMaintananceEntity_ObjectIdentity = ObjectIdentity
sleMplsTpOamMaintananceEntity = _SleMplsTpOamMaintananceEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2)
)
_SleMplsTpOamMaintanceEntityInfoTable_Object = MibTable
sleMplsTpOamMaintanceEntityInfoTable = _SleMplsTpOamMaintanceEntityInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoTable.setStatus("current")
_SleMplsTpOamMaintanceEntityInfoEntry_Object = MibTableRow
sleMplsTpOamMaintanceEntityInfoEntry = _SleMplsTpOamMaintanceEntityInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1)
)
sleMplsTpOamMaintanceEntityInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-OAM-MIB", "sleMplsTpOamMaintanceEntityInfoMeIndex"),
    (0, "SLE-MPLS-TP-OAM-MIB", "sleMplsTpOamMaintanceEntityInfoMpIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoEntry.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoMeIndex_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityInfoMeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpOamMaintanceEntityInfoMeIndex_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityInfoMeIndex_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoMeIndex = _SleMplsTpOamMaintanceEntityInfoMeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 1),
    _SleMplsTpOamMaintanceEntityInfoMeIndex_Type()
)
sleMplsTpOamMaintanceEntityInfoMeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoMeIndex.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoMpIndex_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityInfoMpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpOamMaintanceEntityInfoMpIndex_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityInfoMpIndex_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoMpIndex = _SleMplsTpOamMaintanceEntityInfoMpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 2),
    _SleMplsTpOamMaintanceEntityInfoMpIndex_Type()
)
sleMplsTpOamMaintanceEntityInfoMpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoMpIndex.setStatus("current")


class _SleMplsOamMaintenanceEntityInfoMeName_Type(SnmpAdminString):
    """Custom type sleMplsOamMaintenanceEntityInfoMeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleMplsOamMaintenanceEntityInfoMeName_Type.__name__ = "SnmpAdminString"
_SleMplsOamMaintenanceEntityInfoMeName_Object = MibTableColumn
sleMplsOamMaintenanceEntityInfoMeName = _SleMplsOamMaintenanceEntityInfoMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 3),
    _SleMplsOamMaintenanceEntityInfoMeName_Type()
)
sleMplsOamMaintenanceEntityInfoMeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsOamMaintenanceEntityInfoMeName.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoMpType_Type(Integer32):
    """Custom type sleMplsTpOamMaintanceEntityInfoMpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mep", 1),
          ("mip", 2))
    )


_SleMplsTpOamMaintanceEntityInfoMpType_Type.__name__ = "Integer32"
_SleMplsTpOamMaintanceEntityInfoMpType_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoMpType = _SleMplsTpOamMaintanceEntityInfoMpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 4),
    _SleMplsTpOamMaintanceEntityInfoMpType_Type()
)
sleMplsTpOamMaintanceEntityInfoMpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoMpType.setStatus("current")
_SleMplsOamMaintenanceEntityInfoServiceTunnelName_Type = OctetString
_SleMplsOamMaintenanceEntityInfoServiceTunnelName_Object = MibTableColumn
sleMplsOamMaintenanceEntityInfoServiceTunnelName = _SleMplsOamMaintenanceEntityInfoServiceTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 5),
    _SleMplsOamMaintenanceEntityInfoServiceTunnelName_Type()
)
sleMplsOamMaintenanceEntityInfoServiceTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsOamMaintenanceEntityInfoServiceTunnelName.setStatus("current")
_SleMplsOamMaintenanceEntityInfoServiceVcId_Type = Unsigned32
_SleMplsOamMaintenanceEntityInfoServiceVcId_Object = MibTableColumn
sleMplsOamMaintenanceEntityInfoServiceVcId = _SleMplsOamMaintenanceEntityInfoServiceVcId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 6),
    _SleMplsOamMaintenanceEntityInfoServiceVcId_Type()
)
sleMplsOamMaintenanceEntityInfoServiceVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsOamMaintenanceEntityInfoServiceVcId.setStatus("current")
_SleMplsOamMaintenanceEntityInfoServiceDatalink_Type = OctetString
_SleMplsOamMaintenanceEntityInfoServiceDatalink_Object = MibTableColumn
sleMplsOamMaintenanceEntityInfoServiceDatalink = _SleMplsOamMaintenanceEntityInfoServiceDatalink_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 7),
    _SleMplsOamMaintenanceEntityInfoServiceDatalink_Type()
)
sleMplsOamMaintenanceEntityInfoServiceDatalink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsOamMaintenanceEntityInfoServiceDatalink.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoCcInterval_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityInfoCcInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_SleMplsTpOamMaintanceEntityInfoCcInterval_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityInfoCcInterval_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoCcInterval = _SleMplsTpOamMaintanceEntityInfoCcInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 8),
    _SleMplsTpOamMaintanceEntityInfoCcInterval_Type()
)
sleMplsTpOamMaintanceEntityInfoCcInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoCcInterval.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoRemoteMpId_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityInfoRemoteMpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpOamMaintanceEntityInfoRemoteMpId_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityInfoRemoteMpId_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoRemoteMpId = _SleMplsTpOamMaintanceEntityInfoRemoteMpId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 9),
    _SleMplsTpOamMaintanceEntityInfoRemoteMpId_Type()
)
sleMplsTpOamMaintanceEntityInfoRemoteMpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoRemoteMpId.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoRemoteCc_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityInfoRemoteCc based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_SleMplsTpOamMaintanceEntityInfoRemoteCc_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityInfoRemoteCc_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoRemoteCc = _SleMplsTpOamMaintanceEntityInfoRemoteCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 10),
    _SleMplsTpOamMaintanceEntityInfoRemoteCc_Type()
)
sleMplsTpOamMaintanceEntityInfoRemoteCc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoRemoteCc.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoRemoteIcc_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityInfoRemoteIcc based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleMplsTpOamMaintanceEntityInfoRemoteIcc_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityInfoRemoteIcc_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoRemoteIcc = _SleMplsTpOamMaintanceEntityInfoRemoteIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 11),
    _SleMplsTpOamMaintanceEntityInfoRemoteIcc_Type()
)
sleMplsTpOamMaintanceEntityInfoRemoteIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoRemoteIcc.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoRemoteMeg_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityInfoRemoteMeg based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleMplsTpOamMaintanceEntityInfoRemoteMeg_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityInfoRemoteMeg_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoRemoteMeg = _SleMplsTpOamMaintanceEntityInfoRemoteMeg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 12),
    _SleMplsTpOamMaintanceEntityInfoRemoteMeg_Type()
)
sleMplsTpOamMaintanceEntityInfoRemoteMeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoRemoteMeg.setStatus("current")


class _SleMplsTpOamMaintanceEntityInfoRemoteMpdirection_Type(Integer32):
    """Custom type sleMplsTpOamMaintanceEntityInfoRemoteMpdirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reverse", 2))
    )


_SleMplsTpOamMaintanceEntityInfoRemoteMpdirection_Type.__name__ = "Integer32"
_SleMplsTpOamMaintanceEntityInfoRemoteMpdirection_Object = MibTableColumn
sleMplsTpOamMaintanceEntityInfoRemoteMpdirection = _SleMplsTpOamMaintanceEntityInfoRemoteMpdirection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 1, 1, 13),
    _SleMplsTpOamMaintanceEntityInfoRemoteMpdirection_Type()
)
sleMplsTpOamMaintanceEntityInfoRemoteMpdirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityInfoRemoteMpdirection.setStatus("current")
_SleMplsTpOamMaintanceEntityControl_ObjectIdentity = ObjectIdentity
sleMplsTpOamMaintanceEntityControl = _SleMplsTpOamMaintanceEntityControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2)
)


class _SleMplsTpOamMaintanceEntityRequest_Type(Integer32):
    """Custom type sleMplsTpOamMaintanceEntityRequest based on Integer32"""
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
        *(("createsleMplsTpOamMaintanceEntityControlEntry", 1),
          ("deletesleMplsTpOamMaintanceEntityControlEntry", 2),
          ("setsleMplsTpOamMaintanceEntityControlServiceValue", 3),
          ("setSleMplsTpOamMepControlCCInterval", 4),
          ("unsetSleMplsTpOamMepControlCCInterval", 5),
          ("setsleMplsTpOamMaintanceEntityControlRmepId", 6),
          ("unsetsleMplsTpOamMaintanceEntityControlRmepId", 7))
    )


_SleMplsTpOamMaintanceEntityRequest_Type.__name__ = "Integer32"
_SleMplsTpOamMaintanceEntityRequest_Object = MibScalar
sleMplsTpOamMaintanceEntityRequest = _SleMplsTpOamMaintanceEntityRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 1),
    _SleMplsTpOamMaintanceEntityRequest_Type()
)
sleMplsTpOamMaintanceEntityRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityRequest.setStatus("current")
_SleMplsTpOamMaintanceEntityControlStatus_Type = SleControlStatusType
_SleMplsTpOamMaintanceEntityControlStatus_Object = MibScalar
sleMplsTpOamMaintanceEntityControlStatus = _SleMplsTpOamMaintanceEntityControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 2),
    _SleMplsTpOamMaintanceEntityControlStatus_Type()
)
sleMplsTpOamMaintanceEntityControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlStatus.setStatus("current")
_SleMplsTpOamMaintanceEntityControlTimer_Type = Gauge32
_SleMplsTpOamMaintanceEntityControlTimer_Object = MibScalar
sleMplsTpOamMaintanceEntityControlTimer = _SleMplsTpOamMaintanceEntityControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 3),
    _SleMplsTpOamMaintanceEntityControlTimer_Type()
)
sleMplsTpOamMaintanceEntityControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlTimer.setStatus("current")
_SleMplsTpOamMaintanceEntityControlTimeStamp_Type = TimeTicks
_SleMplsTpOamMaintanceEntityControlTimeStamp_Object = MibScalar
sleMplsTpOamMaintanceEntityControlTimeStamp = _SleMplsTpOamMaintanceEntityControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 4),
    _SleMplsTpOamMaintanceEntityControlTimeStamp_Type()
)
sleMplsTpOamMaintanceEntityControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlTimeStamp.setStatus("current")
_SleMplsTpOamMaintanceEntityControlReqResult_Type = SleControlRequestResultType
_SleMplsTpOamMaintanceEntityControlReqResult_Object = MibScalar
sleMplsTpOamMaintanceEntityControlReqResult = _SleMplsTpOamMaintanceEntityControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 5),
    _SleMplsTpOamMaintanceEntityControlReqResult_Type()
)
sleMplsTpOamMaintanceEntityControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlReqResult.setStatus("current")
_SleMplsTpOamMaintanceEntityControlMegName_Type = OctetString
_SleMplsTpOamMaintanceEntityControlMegName_Object = MibScalar
sleMplsTpOamMaintanceEntityControlMegName = _SleMplsTpOamMaintanceEntityControlMegName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 6),
    _SleMplsTpOamMaintanceEntityControlMegName_Type()
)
sleMplsTpOamMaintanceEntityControlMegName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlMegName.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlMeName_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityControlMeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleMplsTpOamMaintanceEntityControlMeName_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityControlMeName_Object = MibScalar
sleMplsTpOamMaintanceEntityControlMeName = _SleMplsTpOamMaintanceEntityControlMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 7),
    _SleMplsTpOamMaintanceEntityControlMeName_Type()
)
sleMplsTpOamMaintanceEntityControlMeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlMeName.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlMepId_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityControlMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpOamMaintanceEntityControlMepId_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityControlMepId_Object = MibScalar
sleMplsTpOamMaintanceEntityControlMepId = _SleMplsTpOamMaintanceEntityControlMepId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 8),
    _SleMplsTpOamMaintanceEntityControlMepId_Type()
)
sleMplsTpOamMaintanceEntityControlMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlMepId.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlMpType_Type(Integer32):
    """Custom type sleMplsTpOamMaintanceEntityControlMpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mep", 1),
          ("mip", 2))
    )


_SleMplsTpOamMaintanceEntityControlMpType_Type.__name__ = "Integer32"
_SleMplsTpOamMaintanceEntityControlMpType_Object = MibScalar
sleMplsTpOamMaintanceEntityControlMpType = _SleMplsTpOamMaintanceEntityControlMpType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 9),
    _SleMplsTpOamMaintanceEntityControlMpType_Type()
)
sleMplsTpOamMaintanceEntityControlMpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlMpType.setStatus("current")
_SleMplsTpOamMaintanceEntityControlServiceValue_Type = OctetString
_SleMplsTpOamMaintanceEntityControlServiceValue_Object = MibScalar
sleMplsTpOamMaintanceEntityControlServiceValue = _SleMplsTpOamMaintanceEntityControlServiceValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 10),
    _SleMplsTpOamMaintanceEntityControlServiceValue_Type()
)
sleMplsTpOamMaintanceEntityControlServiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlServiceValue.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlCcInterval_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityControlCcInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_SleMplsTpOamMaintanceEntityControlCcInterval_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityControlCcInterval_Object = MibScalar
sleMplsTpOamMaintanceEntityControlCcInterval = _SleMplsTpOamMaintanceEntityControlCcInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 11),
    _SleMplsTpOamMaintanceEntityControlCcInterval_Type()
)
sleMplsTpOamMaintanceEntityControlCcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlCcInterval.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlRemoteMpId_Type(Unsigned32):
    """Custom type sleMplsTpOamMaintanceEntityControlRemoteMpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpOamMaintanceEntityControlRemoteMpId_Type.__name__ = "Unsigned32"
_SleMplsTpOamMaintanceEntityControlRemoteMpId_Object = MibScalar
sleMplsTpOamMaintanceEntityControlRemoteMpId = _SleMplsTpOamMaintanceEntityControlRemoteMpId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 12),
    _SleMplsTpOamMaintanceEntityControlRemoteMpId_Type()
)
sleMplsTpOamMaintanceEntityControlRemoteMpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlRemoteMpId.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlRemoteCc_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityControlRemoteCc based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_SleMplsTpOamMaintanceEntityControlRemoteCc_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityControlRemoteCc_Object = MibScalar
sleMplsTpOamMaintanceEntityControlRemoteCc = _SleMplsTpOamMaintanceEntityControlRemoteCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 13),
    _SleMplsTpOamMaintanceEntityControlRemoteCc_Type()
)
sleMplsTpOamMaintanceEntityControlRemoteCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlRemoteCc.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlRemoteIcc_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityControlRemoteIcc based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleMplsTpOamMaintanceEntityControlRemoteIcc_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityControlRemoteIcc_Object = MibScalar
sleMplsTpOamMaintanceEntityControlRemoteIcc = _SleMplsTpOamMaintanceEntityControlRemoteIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 14),
    _SleMplsTpOamMaintanceEntityControlRemoteIcc_Type()
)
sleMplsTpOamMaintanceEntityControlRemoteIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlRemoteIcc.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlRemoteMeg_Type(OctetString):
    """Custom type sleMplsTpOamMaintanceEntityControlRemoteMeg based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SleMplsTpOamMaintanceEntityControlRemoteMeg_Type.__name__ = "OctetString"
_SleMplsTpOamMaintanceEntityControlRemoteMeg_Object = MibScalar
sleMplsTpOamMaintanceEntityControlRemoteMeg = _SleMplsTpOamMaintanceEntityControlRemoteMeg_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 15),
    _SleMplsTpOamMaintanceEntityControlRemoteMeg_Type()
)
sleMplsTpOamMaintanceEntityControlRemoteMeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlRemoteMeg.setStatus("current")


class _SleMplsTpOamMaintanceEntityControlRemoteMpDirection_Type(Integer32):
    """Custom type sleMplsTpOamMaintanceEntityControlRemoteMpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fwd", 1),
          ("rev", 2))
    )


_SleMplsTpOamMaintanceEntityControlRemoteMpDirection_Type.__name__ = "Integer32"
_SleMplsTpOamMaintanceEntityControlRemoteMpDirection_Object = MibScalar
sleMplsTpOamMaintanceEntityControlRemoteMpDirection = _SleMplsTpOamMaintanceEntityControlRemoteMpDirection_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 2, 2, 16),
    _SleMplsTpOamMaintanceEntityControlRemoteMpDirection_Type()
)
sleMplsTpOamMaintanceEntityControlRemoteMpDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamMaintanceEntityControlRemoteMpDirection.setStatus("current")
_SleMplsTpOamFm_ObjectIdentity = ObjectIdentity
sleMplsTpOamFm = _SleMplsTpOamFm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3)
)
_SleMplsTpOamFmInfoTable_Object = MibTable
sleMplsTpOamFmInfoTable = _SleMplsTpOamFmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoTable.setStatus("current")
_SleMplsTpOamFmInfoEntry_Object = MibTableRow
sleMplsTpOamFmInfoEntry = _SleMplsTpOamFmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1)
)
sleMplsTpOamFmInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-OAM-MIB", "sleMplsTpOamFmInfoMegIndex"),
    (0, "SLE-MPLS-TP-OAM-MIB", "sleMplsTpOamFmInfoMeIndex"),
    (0, "SLE-MPLS-TP-OAM-MIB", "sleMplsTpOamFmInfoMpIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoEntry.setStatus("current")


class _SleMplsTpOamFmInfoMeIndex_Type(Unsigned32):
    """Custom type sleMplsTpOamFmInfoMeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpOamFmInfoMeIndex_Type.__name__ = "Unsigned32"
_SleMplsTpOamFmInfoMeIndex_Object = MibTableColumn
sleMplsTpOamFmInfoMeIndex = _SleMplsTpOamFmInfoMeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 1),
    _SleMplsTpOamFmInfoMeIndex_Type()
)
sleMplsTpOamFmInfoMeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoMeIndex.setStatus("current")


class _SleMplsTpOamFmInfoMpIndex_Type(Unsigned32):
    """Custom type sleMplsTpOamFmInfoMpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpOamFmInfoMpIndex_Type.__name__ = "Unsigned32"
_SleMplsTpOamFmInfoMpIndex_Object = MibTableColumn
sleMplsTpOamFmInfoMpIndex = _SleMplsTpOamFmInfoMpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 2),
    _SleMplsTpOamFmInfoMpIndex_Type()
)
sleMplsTpOamFmInfoMpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoMpIndex.setStatus("current")


class _SleMplsTpOamFmInfoFaultManagement_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoFaultManagement based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpOamFmInfoFaultManagement_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoFaultManagement_Object = MibTableColumn
sleMplsTpOamFmInfoFaultManagement = _SleMplsTpOamFmInfoFaultManagement_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 3),
    _SleMplsTpOamFmInfoFaultManagement_Type()
)
sleMplsTpOamFmInfoFaultManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoFaultManagement.setStatus("current")


class _SleMplsTpOamFmInfoRefreshTime_Type(Unsigned32):
    """Custom type sleMplsTpOamFmInfoRefreshTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SleMplsTpOamFmInfoRefreshTime_Type.__name__ = "Unsigned32"
_SleMplsTpOamFmInfoRefreshTime_Object = MibTableColumn
sleMplsTpOamFmInfoRefreshTime = _SleMplsTpOamFmInfoRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 4),
    _SleMplsTpOamFmInfoRefreshTime_Type()
)
sleMplsTpOamFmInfoRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoRefreshTime.setStatus("current")


class _SleMplsTpOamFmInfoLockInstruct_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLockInstruct based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpOamFmInfoLockInstruct_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLockInstruct_Object = MibTableColumn
sleMplsTpOamFmInfoLockInstruct = _SleMplsTpOamFmInfoLockInstruct_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 5),
    _SleMplsTpOamFmInfoLockInstruct_Type()
)
sleMplsTpOamFmInfoLockInstruct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLockInstruct.setStatus("current")


class _SleMplsTpOamFmInfoLockInstructRefreshTime_Type(Unsigned32):
    """Custom type sleMplsTpOamFmInfoLockInstructRefreshTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SleMplsTpOamFmInfoLockInstructRefreshTime_Type.__name__ = "Unsigned32"
_SleMplsTpOamFmInfoLockInstructRefreshTime_Object = MibTableColumn
sleMplsTpOamFmInfoLockInstructRefreshTime = _SleMplsTpOamFmInfoLockInstructRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 6),
    _SleMplsTpOamFmInfoLockInstructRefreshTime_Type()
)
sleMplsTpOamFmInfoLockInstructRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLockInstructRefreshTime.setStatus("current")


class _SleMplsTpOamFmInfoAlarmIndication_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoAlarmIndication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpOamFmInfoAlarmIndication_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoAlarmIndication_Object = MibTableColumn
sleMplsTpOamFmInfoAlarmIndication = _SleMplsTpOamFmInfoAlarmIndication_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 7),
    _SleMplsTpOamFmInfoAlarmIndication_Type()
)
sleMplsTpOamFmInfoAlarmIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoAlarmIndication.setStatus("current")


class _SleMplsTpOamFmInfoAlarmIndicationInterval_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoAlarmIndicationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneSecond", 1),
          ("sixtySeconds", 2))
    )


_SleMplsTpOamFmInfoAlarmIndicationInterval_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoAlarmIndicationInterval_Object = MibTableColumn
sleMplsTpOamFmInfoAlarmIndicationInterval = _SleMplsTpOamFmInfoAlarmIndicationInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 8),
    _SleMplsTpOamFmInfoAlarmIndicationInterval_Type()
)
sleMplsTpOamFmInfoAlarmIndicationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoAlarmIndicationInterval.setStatus("current")


class _SleMplsTpOamFmInfoAlarmIndicationLevel_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoAlarmIndicationLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsTpOamFmInfoAlarmIndicationLevel_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoAlarmIndicationLevel_Object = MibTableColumn
sleMplsTpOamFmInfoAlarmIndicationLevel = _SleMplsTpOamFmInfoAlarmIndicationLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 9),
    _SleMplsTpOamFmInfoAlarmIndicationLevel_Type()
)
sleMplsTpOamFmInfoAlarmIndicationLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoAlarmIndicationLevel.setStatus("current")


class _SleMplsTpOamFmInfoLock_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpOamFmInfoLock_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLock_Object = MibTableColumn
sleMplsTpOamFmInfoLock = _SleMplsTpOamFmInfoLock_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 10),
    _SleMplsTpOamFmInfoLock_Type()
)
sleMplsTpOamFmInfoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLock.setStatus("current")


class _SleMplsTpOamFmInfoLockInterval_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLockInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneSecond", 1),
          ("sixtySeconds", 2))
    )


_SleMplsTpOamFmInfoLockInterval_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLockInterval_Object = MibTableColumn
sleMplsTpOamFmInfoLockInterval = _SleMplsTpOamFmInfoLockInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 11),
    _SleMplsTpOamFmInfoLockInterval_Type()
)
sleMplsTpOamFmInfoLockInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLockInterval.setStatus("current")


class _SleMplsTpOamFmInfoLockLevel_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLockLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsTpOamFmInfoLockLevel_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLockLevel_Object = MibTableColumn
sleMplsTpOamFmInfoLockLevel = _SleMplsTpOamFmInfoLockLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 12),
    _SleMplsTpOamFmInfoLockLevel_Type()
)
sleMplsTpOamFmInfoLockLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLockLevel.setStatus("current")


class _SleMplsTpOamFmInfoLoopBack_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLoopBack based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpOamFmInfoLoopBack_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLoopBack_Object = MibTableColumn
sleMplsTpOamFmInfoLoopBack = _SleMplsTpOamFmInfoLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 13),
    _SleMplsTpOamFmInfoLoopBack_Type()
)
sleMplsTpOamFmInfoLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLoopBack.setStatus("current")


class _SleMplsTpOamFmInfoLoopBackStatus_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLoopBackStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SleMplsTpOamFmInfoLoopBackStatus_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLoopBackStatus_Object = MibTableColumn
sleMplsTpOamFmInfoLoopBackStatus = _SleMplsTpOamFmInfoLoopBackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 14),
    _SleMplsTpOamFmInfoLoopBackStatus_Type()
)
sleMplsTpOamFmInfoLoopBackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLoopBackStatus.setStatus("current")


class _SleMplsTpOamFmInfoLockInstructStatus_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoLockInstructStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SleMplsTpOamFmInfoLockInstructStatus_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoLockInstructStatus_Object = MibTableColumn
sleMplsTpOamFmInfoLockInstructStatus = _SleMplsTpOamFmInfoLockInstructStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 15),
    _SleMplsTpOamFmInfoLockInstructStatus_Type()
)
sleMplsTpOamFmInfoLockInstructStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoLockInstructStatus.setStatus("current")


class _SleMplsTpOamFmInfoFaultManagementStatus_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoFaultManagementStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SleMplsTpOamFmInfoFaultManagementStatus_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoFaultManagementStatus_Object = MibTableColumn
sleMplsTpOamFmInfoFaultManagementStatus = _SleMplsTpOamFmInfoFaultManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 16),
    _SleMplsTpOamFmInfoFaultManagementStatus_Type()
)
sleMplsTpOamFmInfoFaultManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoFaultManagementStatus.setStatus("current")


class _SleMplsTpOamFmInfoCcCvStatus_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoCcCvStatus based on Integer32"""
    defaultValue = 2

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


_SleMplsTpOamFmInfoCcCvStatus_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoCcCvStatus_Object = MibTableColumn
sleMplsTpOamFmInfoCcCvStatus = _SleMplsTpOamFmInfoCcCvStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 17),
    _SleMplsTpOamFmInfoCcCvStatus_Type()
)
sleMplsTpOamFmInfoCcCvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoCcCvStatus.setStatus("current")


class _SleMplsTpOamFmInfoStatus_Type(Integer32):
    """Custom type sleMplsTpOamFmInfoStatus based on Integer32"""
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
        *(("pathNotAssociated", 1),
          ("pathAssociateWithAnotherMe", 2),
          ("pathDown", 3),
          ("receivedAisFmMessage", 4),
          ("receviedLkrFmMessage", 5),
          ("bfdDetecLoc", 6),
          ("serverLayerDown", 7),
          ("invalidMe", 8))
    )


_SleMplsTpOamFmInfoStatus_Type.__name__ = "Integer32"
_SleMplsTpOamFmInfoStatus_Object = MibTableColumn
sleMplsTpOamFmInfoStatus = _SleMplsTpOamFmInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 1, 1, 18),
    _SleMplsTpOamFmInfoStatus_Type()
)
sleMplsTpOamFmInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInfoStatus.setStatus("current")
_SleMplsTpOamFmControlTable_ObjectIdentity = ObjectIdentity
sleMplsTpOamFmControlTable = _SleMplsTpOamFmControlTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2)
)


class _SleMplsTpOamFmControlRequest_Type(Integer32):
    """Custom type sleMplsTpOamFmControlRequest based on Integer32"""
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
        *(("setSleMplsTpOamFmControlInit", 1),
          ("unsetSleMplsTpOamFmControlInit", 2),
          ("setSleMplsTpOamItutAis", 3),
          ("unsetSleMplsTpOamItutAis", 4),
          ("setSleMplsTpOamItutLockInterval", 5),
          ("unsetSleMplsTpOamItutLockInterval", 6))
    )


_SleMplsTpOamFmControlRequest_Type.__name__ = "Integer32"
_SleMplsTpOamFmControlRequest_Object = MibScalar
sleMplsTpOamFmControlRequest = _SleMplsTpOamFmControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 1),
    _SleMplsTpOamFmControlRequest_Type()
)
sleMplsTpOamFmControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlRequest.setStatus("current")
_SleMplsTpOamFmControlStatus_Type = SleControlStatusType
_SleMplsTpOamFmControlStatus_Object = MibScalar
sleMplsTpOamFmControlStatus = _SleMplsTpOamFmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 2),
    _SleMplsTpOamFmControlStatus_Type()
)
sleMplsTpOamFmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlStatus.setStatus("current")
_SleMplsTpOamFmControlTimer_Type = Gauge32
_SleMplsTpOamFmControlTimer_Object = MibScalar
sleMplsTpOamFmControlTimer = _SleMplsTpOamFmControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 3),
    _SleMplsTpOamFmControlTimer_Type()
)
sleMplsTpOamFmControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlTimer.setStatus("current")
_SleMplsTpOamFmControlTimeStamp_Type = TimeTicks
_SleMplsTpOamFmControlTimeStamp_Object = MibScalar
sleMplsTpOamFmControlTimeStamp = _SleMplsTpOamFmControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 4),
    _SleMplsTpOamFmControlTimeStamp_Type()
)
sleMplsTpOamFmControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlTimeStamp.setStatus("current")
_SleMplsTpOamFmControlReqResult_Type = SleControlRequestResultType
_SleMplsTpOamFmControlReqResult_Object = MibScalar
sleMplsTpOamFmControlReqResult = _SleMplsTpOamFmControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 5),
    _SleMplsTpOamFmControlReqResult_Type()
)
sleMplsTpOamFmControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlReqResult.setStatus("current")
_SleMplsTpOamFmControlMegName_Type = OctetString
_SleMplsTpOamFmControlMegName_Object = MibScalar
sleMplsTpOamFmControlMegName = _SleMplsTpOamFmControlMegName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 6),
    _SleMplsTpOamFmControlMegName_Type()
)
sleMplsTpOamFmControlMegName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlMegName.setStatus("current")
_SleMplsTpOamFmControlMeName_Type = OctetString
_SleMplsTpOamFmControlMeName_Object = MibScalar
sleMplsTpOamFmControlMeName = _SleMplsTpOamFmControlMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 7),
    _SleMplsTpOamFmControlMeName_Type()
)
sleMplsTpOamFmControlMeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlMeName.setStatus("current")


class _SleMplsTpOamFmControlMepId_Type(Unsigned32):
    """Custom type sleMplsTpOamFmControlMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_SleMplsTpOamFmControlMepId_Type.__name__ = "Unsigned32"
_SleMplsTpOamFmControlMepId_Object = MibScalar
sleMplsTpOamFmControlMepId = _SleMplsTpOamFmControlMepId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 8),
    _SleMplsTpOamFmControlMepId_Type()
)
sleMplsTpOamFmControlMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlMepId.setStatus("current")


class _SleMplsTpOamFmInit_Type(Integer32):
    """Custom type sleMplsTpOamFmInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultMeasurment", 1),
          ("lockInstruct", 2),
          ("loopBack", 3))
    )


_SleMplsTpOamFmInit_Type.__name__ = "Integer32"
_SleMplsTpOamFmInit_Object = MibScalar
sleMplsTpOamFmInit = _SleMplsTpOamFmInit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 9),
    _SleMplsTpOamFmInit_Type()
)
sleMplsTpOamFmInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmInit.setStatus("current")


class _SleMplsTpOamFmControlRefreshTime_Type(Unsigned32):
    """Custom type sleMplsTpOamFmControlRefreshTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleMplsTpOamFmControlRefreshTime_Type.__name__ = "Unsigned32"
_SleMplsTpOamFmControlRefreshTime_Object = MibScalar
sleMplsTpOamFmControlRefreshTime = _SleMplsTpOamFmControlRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 10),
    _SleMplsTpOamFmControlRefreshTime_Type()
)
sleMplsTpOamFmControlRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlRefreshTime.setStatus("current")


class _SleMplsTpOamFmControlInterval_Type(Integer32):
    """Custom type sleMplsTpOamFmControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneOne", 1),
          ("sixtyOne", 2))
    )


_SleMplsTpOamFmControlInterval_Type.__name__ = "Integer32"
_SleMplsTpOamFmControlInterval_Object = MibScalar
sleMplsTpOamFmControlInterval = _SleMplsTpOamFmControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 11),
    _SleMplsTpOamFmControlInterval_Type()
)
sleMplsTpOamFmControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlInterval.setStatus("current")


class _SleMplsTpOamFmControlLevel_Type(Integer32):
    """Custom type sleMplsTpOamFmControlLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsTpOamFmControlLevel_Type.__name__ = "Integer32"
_SleMplsTpOamFmControlLevel_Object = MibScalar
sleMplsTpOamFmControlLevel = _SleMplsTpOamFmControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 17, 3, 2, 12),
    _SleMplsTpOamFmControlLevel_Type()
)
sleMplsTpOamFmControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpOamFmControlLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-OAM-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpOam": sleMplsTpOam,
       "sleMplsTpOamMeg": sleMplsTpOamMeg,
       "sleMplsTpOamMegInfoTable": sleMplsTpOamMegInfoTable,
       "sleMplsTpOamMegInfoEntry": sleMplsTpOamMegInfoEntry,
       "sleMplsTpOamMegInfoIndex": sleMplsTpOamMegInfoIndex,
       "sleMplsTpOamMegInfoName": sleMplsTpOamMegInfoName,
       "sleMplsTpOamMegInfoOperatorType": sleMplsTpOamMegInfoOperatorType,
       "sleMplsTpOamMegInfoServiceType": sleMplsTpOamMegInfoServiceType,
       "sleMplsTpOamMegInfoMegLevel": sleMplsTpOamMegInfoMegLevel,
       "sleMplsTpOamMegInfoOperStatus": sleMplsTpOamMegInfoOperStatus,
       "sleMplsTpOamMegControl": sleMplsTpOamMegControl,
       "sleMplsTpOamMegControlRequest": sleMplsTpOamMegControlRequest,
       "sleMplsTpOamMegControlStatus": sleMplsTpOamMegControlStatus,
       "sleMplsTpOamMegControlTimer": sleMplsTpOamMegControlTimer,
       "sleMplsTpOamMegControlTimeStamp": sleMplsTpOamMegControlTimeStamp,
       "sleMplsTpOamMegControlReqResult": sleMplsTpOamMegControlReqResult,
       "sleMplsTpOamMegControlName": sleMplsTpOamMegControlName,
       "sleMplsTpOamMegControlOperatorType": sleMplsTpOamMegControlOperatorType,
       "sleMplsTpOamMegControlServiceType": sleMplsTpOamMegControlServiceType,
       "sleMplsTpOamMegControlLevel": sleMplsTpOamMegControlLevel,
       "sleMplsTpOamMaintananceEntity": sleMplsTpOamMaintananceEntity,
       "sleMplsTpOamMaintanceEntityInfoTable": sleMplsTpOamMaintanceEntityInfoTable,
       "sleMplsTpOamMaintanceEntityInfoEntry": sleMplsTpOamMaintanceEntityInfoEntry,
       "sleMplsTpOamMaintanceEntityInfoMeIndex": sleMplsTpOamMaintanceEntityInfoMeIndex,
       "sleMplsTpOamMaintanceEntityInfoMpIndex": sleMplsTpOamMaintanceEntityInfoMpIndex,
       "sleMplsOamMaintenanceEntityInfoMeName": sleMplsOamMaintenanceEntityInfoMeName,
       "sleMplsTpOamMaintanceEntityInfoMpType": sleMplsTpOamMaintanceEntityInfoMpType,
       "sleMplsOamMaintenanceEntityInfoServiceTunnelName": sleMplsOamMaintenanceEntityInfoServiceTunnelName,
       "sleMplsOamMaintenanceEntityInfoServiceVcId": sleMplsOamMaintenanceEntityInfoServiceVcId,
       "sleMplsOamMaintenanceEntityInfoServiceDatalink": sleMplsOamMaintenanceEntityInfoServiceDatalink,
       "sleMplsTpOamMaintanceEntityInfoCcInterval": sleMplsTpOamMaintanceEntityInfoCcInterval,
       "sleMplsTpOamMaintanceEntityInfoRemoteMpId": sleMplsTpOamMaintanceEntityInfoRemoteMpId,
       "sleMplsTpOamMaintanceEntityInfoRemoteCc": sleMplsTpOamMaintanceEntityInfoRemoteCc,
       "sleMplsTpOamMaintanceEntityInfoRemoteIcc": sleMplsTpOamMaintanceEntityInfoRemoteIcc,
       "sleMplsTpOamMaintanceEntityInfoRemoteMeg": sleMplsTpOamMaintanceEntityInfoRemoteMeg,
       "sleMplsTpOamMaintanceEntityInfoRemoteMpdirection": sleMplsTpOamMaintanceEntityInfoRemoteMpdirection,
       "sleMplsTpOamMaintanceEntityControl": sleMplsTpOamMaintanceEntityControl,
       "sleMplsTpOamMaintanceEntityRequest": sleMplsTpOamMaintanceEntityRequest,
       "sleMplsTpOamMaintanceEntityControlStatus": sleMplsTpOamMaintanceEntityControlStatus,
       "sleMplsTpOamMaintanceEntityControlTimer": sleMplsTpOamMaintanceEntityControlTimer,
       "sleMplsTpOamMaintanceEntityControlTimeStamp": sleMplsTpOamMaintanceEntityControlTimeStamp,
       "sleMplsTpOamMaintanceEntityControlReqResult": sleMplsTpOamMaintanceEntityControlReqResult,
       "sleMplsTpOamMaintanceEntityControlMegName": sleMplsTpOamMaintanceEntityControlMegName,
       "sleMplsTpOamMaintanceEntityControlMeName": sleMplsTpOamMaintanceEntityControlMeName,
       "sleMplsTpOamMaintanceEntityControlMepId": sleMplsTpOamMaintanceEntityControlMepId,
       "sleMplsTpOamMaintanceEntityControlMpType": sleMplsTpOamMaintanceEntityControlMpType,
       "sleMplsTpOamMaintanceEntityControlServiceValue": sleMplsTpOamMaintanceEntityControlServiceValue,
       "sleMplsTpOamMaintanceEntityControlCcInterval": sleMplsTpOamMaintanceEntityControlCcInterval,
       "sleMplsTpOamMaintanceEntityControlRemoteMpId": sleMplsTpOamMaintanceEntityControlRemoteMpId,
       "sleMplsTpOamMaintanceEntityControlRemoteCc": sleMplsTpOamMaintanceEntityControlRemoteCc,
       "sleMplsTpOamMaintanceEntityControlRemoteIcc": sleMplsTpOamMaintanceEntityControlRemoteIcc,
       "sleMplsTpOamMaintanceEntityControlRemoteMeg": sleMplsTpOamMaintanceEntityControlRemoteMeg,
       "sleMplsTpOamMaintanceEntityControlRemoteMpDirection": sleMplsTpOamMaintanceEntityControlRemoteMpDirection,
       "sleMplsTpOamFm": sleMplsTpOamFm,
       "sleMplsTpOamFmInfoTable": sleMplsTpOamFmInfoTable,
       "sleMplsTpOamFmInfoEntry": sleMplsTpOamFmInfoEntry,
       "sleMplsTpOamFmInfoMeIndex": sleMplsTpOamFmInfoMeIndex,
       "sleMplsTpOamFmInfoMpIndex": sleMplsTpOamFmInfoMpIndex,
       "sleMplsTpOamFmInfoFaultManagement": sleMplsTpOamFmInfoFaultManagement,
       "sleMplsTpOamFmInfoRefreshTime": sleMplsTpOamFmInfoRefreshTime,
       "sleMplsTpOamFmInfoLockInstruct": sleMplsTpOamFmInfoLockInstruct,
       "sleMplsTpOamFmInfoLockInstructRefreshTime": sleMplsTpOamFmInfoLockInstructRefreshTime,
       "sleMplsTpOamFmInfoAlarmIndication": sleMplsTpOamFmInfoAlarmIndication,
       "sleMplsTpOamFmInfoAlarmIndicationInterval": sleMplsTpOamFmInfoAlarmIndicationInterval,
       "sleMplsTpOamFmInfoAlarmIndicationLevel": sleMplsTpOamFmInfoAlarmIndicationLevel,
       "sleMplsTpOamFmInfoLock": sleMplsTpOamFmInfoLock,
       "sleMplsTpOamFmInfoLockInterval": sleMplsTpOamFmInfoLockInterval,
       "sleMplsTpOamFmInfoLockLevel": sleMplsTpOamFmInfoLockLevel,
       "sleMplsTpOamFmInfoLoopBack": sleMplsTpOamFmInfoLoopBack,
       "sleMplsTpOamFmInfoLoopBackStatus": sleMplsTpOamFmInfoLoopBackStatus,
       "sleMplsTpOamFmInfoLockInstructStatus": sleMplsTpOamFmInfoLockInstructStatus,
       "sleMplsTpOamFmInfoFaultManagementStatus": sleMplsTpOamFmInfoFaultManagementStatus,
       "sleMplsTpOamFmInfoCcCvStatus": sleMplsTpOamFmInfoCcCvStatus,
       "sleMplsTpOamFmInfoStatus": sleMplsTpOamFmInfoStatus,
       "sleMplsTpOamFmControlTable": sleMplsTpOamFmControlTable,
       "sleMplsTpOamFmControlRequest": sleMplsTpOamFmControlRequest,
       "sleMplsTpOamFmControlStatus": sleMplsTpOamFmControlStatus,
       "sleMplsTpOamFmControlTimer": sleMplsTpOamFmControlTimer,
       "sleMplsTpOamFmControlTimeStamp": sleMplsTpOamFmControlTimeStamp,
       "sleMplsTpOamFmControlReqResult": sleMplsTpOamFmControlReqResult,
       "sleMplsTpOamFmControlMegName": sleMplsTpOamFmControlMegName,
       "sleMplsTpOamFmControlMeName": sleMplsTpOamFmControlMeName,
       "sleMplsTpOamFmControlMepId": sleMplsTpOamFmControlMepId,
       "sleMplsTpOamFmInit": sleMplsTpOamFmInit,
       "sleMplsTpOamFmControlRefreshTime": sleMplsTpOamFmControlRefreshTime,
       "sleMplsTpOamFmControlInterval": sleMplsTpOamFmControlInterval,
       "sleMplsTpOamFmControlLevel": sleMplsTpOamFmControlLevel}
)
