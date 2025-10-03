# SNMP MIB module (TN-MGMT-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-MGMT-TDM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:58 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnInterfaceMgmt,
 tnMgmtNotifications) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnInterfaceMgmt",
    "tnMgmtNotifications")

(CpsConnector,) = mibBuilder.importSymbols(
    "TRANSITION-TC",
    "CpsConnector")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnIfTDMTable_Object = MibTable
tnIfTDMTable = _TnIfTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tnIfTDMTable.setStatus("current")
_TnIfTDMEntry_Object = MibTableRow
tnIfTDMEntry = _TnIfTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1)
)
tnIfTDMEntry.setIndexNames(
    (0, "TN-MGMT-TDM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfTDMEntry.setStatus("current")


class _TnIfTDMAISTransmit_Type(Integer32):
    """Custom type tnIfTDMAISTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDMAISTransmit_Type.__name__ = "Integer32"
_TnIfTDMAISTransmit_Object = MibTableColumn
tnIfTDMAISTransmit = _TnIfTDMAISTransmit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 1),
    _TnIfTDMAISTransmit_Type()
)
tnIfTDMAISTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMAISTransmit.setStatus("current")


class _TnIfTDMAISFormat_Type(Integer32):
    """Custom type tnIfTDMAISFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allones", 1),
          ("blue", 2),
          ("notApplicable", 3))
    )


_TnIfTDMAISFormat_Type.__name__ = "Integer32"
_TnIfTDMAISFormat_Object = MibTableColumn
tnIfTDMAISFormat = _TnIfTDMAISFormat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 2),
    _TnIfTDMAISFormat_Type()
)
tnIfTDMAISFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMAISFormat.setStatus("current")


class _TnIfTDMAlarmIndicationSignal_Type(Integer32):
    """Custom type tnIfTDMAlarmIndicationSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_TnIfTDMAlarmIndicationSignal_Type.__name__ = "Integer32"
_TnIfTDMAlarmIndicationSignal_Object = MibTableColumn
tnIfTDMAlarmIndicationSignal = _TnIfTDMAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 3),
    _TnIfTDMAlarmIndicationSignal_Type()
)
tnIfTDMAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDMAlarmIndicationSignal.setStatus("current")


class _TnIfTDMLongHaul_Type(Integer32):
    """Custom type tnIfTDMLongHaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("notApplicable", 3))
    )


_TnIfTDMLongHaul_Type.__name__ = "Integer32"
_TnIfTDMLongHaul_Object = MibTableColumn
tnIfTDMLongHaul = _TnIfTDMLongHaul_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 4),
    _TnIfTDMLongHaul_Type()
)
tnIfTDMLongHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDMLongHaul.setStatus("current")


class _TnIfTDMType_Type(Integer32):
    """Custom type tnIfTDMType based on Integer32"""
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
          ("t1", 1),
          ("e1", 2),
          ("j1", 3),
          ("dS3", 4),
          ("e3", 5),
          ("sts-1", 6))
    )


_TnIfTDMType_Type.__name__ = "Integer32"
_TnIfTDMType_Object = MibTableColumn
tnIfTDMType = _TnIfTDMType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 5),
    _TnIfTDMType_Type()
)
tnIfTDMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDMType.setStatus("current")


class _TnIfTDMT1E1LineBuildout_Type(Integer32):
    """Custom type tnIfTDMT1E1LineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("e13-0V120ohm", 1),
          ("e12-37V75ohm", 2),
          ("t1SH-DSX-0-133ANSIT1403", 3),
          ("t1SH-DSX-133-266", 4),
          ("t1SH-DSX-266-399", 5),
          ("t1SH-DSX-399-533", 6),
          ("t1SH-DSX-533-655", 7),
          ("t1SH-DSX-6V", 8),
          ("t1LH-0dB", 9),
          ("t1LH-m7-5dB", 10),
          ("t1LH-m15dB", 11),
          ("t1LH-m22-5dB", 12))
    )


_TnIfTDMT1E1LineBuildout_Type.__name__ = "Integer32"
_TnIfTDMT1E1LineBuildout_Object = MibTableColumn
tnIfTDMT1E1LineBuildout = _TnIfTDMT1E1LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 6),
    _TnIfTDMT1E1LineBuildout_Type()
)
tnIfTDMT1E1LineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDMT1E1LineBuildout.setStatus("current")


class _TnIfTDMDS3E3LineBuildout_Type(Integer32):
    """Custom type tnIfTDMDS3E3LineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("boost", 1),
          ("normal", 2))
    )


_TnIfTDMDS3E3LineBuildout_Type.__name__ = "Integer32"
_TnIfTDMDS3E3LineBuildout_Object = MibTableColumn
tnIfTDMDS3E3LineBuildout = _TnIfTDMDS3E3LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 7),
    _TnIfTDMDS3E3LineBuildout_Type()
)
tnIfTDMDS3E3LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMDS3E3LineBuildout.setStatus("current")
_TnIfTDMConnectorType_Type = CpsConnector
_TnIfTDMConnectorType_Object = MibTableColumn
tnIfTDMConnectorType = _TnIfTDMConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 6, 1, 8),
    _TnIfTDMConnectorType_Type()
)
tnIfTDMConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDMConnectorType.setStatus("current")
_TnIfTDMExtTable_Object = MibTable
tnIfTDMExtTable = _TnIfTDMExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9)
)
if mibBuilder.loadTexts:
    tnIfTDMExtTable.setStatus("current")
_TnIfTDMExtEntry_Object = MibTableRow
tnIfTDMExtEntry = _TnIfTDMExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1)
)
tnIfTDMExtEntry.setIndexNames(
    (0, "TN-MGMT-TDM-MIB", "ifIndex"),
    (0, "TN-MGMT-TDM-MIB", "tnIfTDMExtId"),
)
if mibBuilder.loadTexts:
    tnIfTDMExtEntry.setStatus("current")


class _TnIfTDMExtId_Type(Integer32):
    """Custom type tnIfTDMExtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999999),
    )


_TnIfTDMExtId_Type.__name__ = "Integer32"
_TnIfTDMExtId_Object = MibTableColumn
tnIfTDMExtId = _TnIfTDMExtId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1, 1),
    _TnIfTDMExtId_Type()
)
tnIfTDMExtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIfTDMExtId.setStatus("current")


class _TnIfTDMExtAISTrasmit_Type(Integer32):
    """Custom type tnIfTDMExtAISTrasmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDMExtAISTrasmit_Type.__name__ = "Integer32"
_TnIfTDMExtAISTrasmit_Object = MibTableColumn
tnIfTDMExtAISTrasmit = _TnIfTDMExtAISTrasmit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1, 2),
    _TnIfTDMExtAISTrasmit_Type()
)
tnIfTDMExtAISTrasmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMExtAISTrasmit.setStatus("current")


class _TnIfTDMExtAISFormat_Type(Integer32):
    """Custom type tnIfTDMExtAISFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allones", 1),
          ("blue", 2),
          ("notApplicable", 3))
    )


_TnIfTDMExtAISFormat_Type.__name__ = "Integer32"
_TnIfTDMExtAISFormat_Object = MibTableColumn
tnIfTDMExtAISFormat = _TnIfTDMExtAISFormat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1, 3),
    _TnIfTDMExtAISFormat_Type()
)
tnIfTDMExtAISFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMExtAISFormat.setStatus("current")


class _TnIfTDMExtAlarmIndicationSingnal_Type(Integer32):
    """Custom type tnIfTDMExtAlarmIndicationSingnal based on Integer32"""
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
        *(("alarm", 1),
          ("normal", 2),
          ("yellow", 3),
          ("red", 4))
    )


_TnIfTDMExtAlarmIndicationSingnal_Type.__name__ = "Integer32"
_TnIfTDMExtAlarmIndicationSingnal_Object = MibTableColumn
tnIfTDMExtAlarmIndicationSingnal = _TnIfTDMExtAlarmIndicationSingnal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1, 4),
    _TnIfTDMExtAlarmIndicationSingnal_Type()
)
tnIfTDMExtAlarmIndicationSingnal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDMExtAlarmIndicationSingnal.setStatus("current")


class _TnIfTDMExtLoopback_Type(Integer32):
    """Custom type tnIfTDMExtLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDMExtLoopback_Type.__name__ = "Integer32"
_TnIfTDMExtLoopback_Object = MibTableColumn
tnIfTDMExtLoopback = _TnIfTDMExtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1, 5),
    _TnIfTDMExtLoopback_Type()
)
tnIfTDMExtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMExtLoopback.setStatus("current")


class _TnIfTDMExtYellowTrasmit_Type(Integer32):
    """Custom type tnIfTDMExtYellowTrasmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDMExtYellowTrasmit_Type.__name__ = "Integer32"
_TnIfTDMExtYellowTrasmit_Object = MibTableColumn
tnIfTDMExtYellowTrasmit = _TnIfTDMExtYellowTrasmit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 9, 1, 6),
    _TnIfTDMExtYellowTrasmit_Type()
)
tnIfTDMExtYellowTrasmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDMExtYellowTrasmit.setStatus("current")
_TnIfTDM2Table_Object = MibTable
tnIfTDM2Table = _TnIfTDM2Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10)
)
if mibBuilder.loadTexts:
    tnIfTDM2Table.setStatus("current")
_TnIfTDM2Entry_Object = MibTableRow
tnIfTDM2Entry = _TnIfTDM2Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1)
)
tnIfTDM2Entry.setIndexNames(
    (0, "TN-MGMT-TDM-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfTDM2Entry.setStatus("current")
_TnIfTDM2FiberLineNum_Type = Integer32
_TnIfTDM2FiberLineNum_Object = MibTableColumn
tnIfTDM2FiberLineNum = _TnIfTDM2FiberLineNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 1),
    _TnIfTDM2FiberLineNum_Type()
)
tnIfTDM2FiberLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDM2FiberLineNum.setStatus("current")


class _TnIfTDM2FiberActiveLine_Type(Integer32):
    """Custom type tnIfTDM2FiberActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_TnIfTDM2FiberActiveLine_Type.__name__ = "Integer32"
_TnIfTDM2FiberActiveLine_Object = MibTableColumn
tnIfTDM2FiberActiveLine = _TnIfTDM2FiberActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 2),
    _TnIfTDM2FiberActiveLine_Type()
)
tnIfTDM2FiberActiveLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2FiberActiveLine.setStatus("current")


class _TnIfTDM2FiberRevertive_Type(Integer32):
    """Custom type tnIfTDM2FiberRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDM2FiberRevertive_Type.__name__ = "Integer32"
_TnIfTDM2FiberRevertive_Object = MibTableColumn
tnIfTDM2FiberRevertive = _TnIfTDM2FiberRevertive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 3),
    _TnIfTDM2FiberRevertive_Type()
)
tnIfTDM2FiberRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2FiberRevertive.setStatus("current")


class _TnIfTDM2FiberPrimaryLinkStatus_Type(Integer32):
    """Custom type tnIfTDM2FiberPrimaryLinkStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_TnIfTDM2FiberPrimaryLinkStatus_Type.__name__ = "Integer32"
_TnIfTDM2FiberPrimaryLinkStatus_Object = MibTableColumn
tnIfTDM2FiberPrimaryLinkStatus = _TnIfTDM2FiberPrimaryLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 4),
    _TnIfTDM2FiberPrimaryLinkStatus_Type()
)
tnIfTDM2FiberPrimaryLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDM2FiberPrimaryLinkStatus.setStatus("current")


class _TnIfTDM2FiberSecondaryLinkStatus_Type(Integer32):
    """Custom type tnIfTDM2FiberSecondaryLinkStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_TnIfTDM2FiberSecondaryLinkStatus_Type.__name__ = "Integer32"
_TnIfTDM2FiberSecondaryLinkStatus_Object = MibTableColumn
tnIfTDM2FiberSecondaryLinkStatus = _TnIfTDM2FiberSecondaryLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 5),
    _TnIfTDM2FiberSecondaryLinkStatus_Type()
)
tnIfTDM2FiberSecondaryLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDM2FiberSecondaryLinkStatus.setStatus("current")


class _TnIfTDM2InBandLPEnable_Type(Integer32):
    """Custom type tnIfTDM2InBandLPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDM2InBandLPEnable_Type.__name__ = "Integer32"
_TnIfTDM2InBandLPEnable_Object = MibTableColumn
tnIfTDM2InBandLPEnable = _TnIfTDM2InBandLPEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 6),
    _TnIfTDM2InBandLPEnable_Type()
)
tnIfTDM2InBandLPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandLPEnable.setStatus("current")
_TnIfTDM2InBandLPStartPatten_Type = DisplayString
_TnIfTDM2InBandLPStartPatten_Object = MibTableColumn
tnIfTDM2InBandLPStartPatten = _TnIfTDM2InBandLPStartPatten_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 7),
    _TnIfTDM2InBandLPStartPatten_Type()
)
tnIfTDM2InBandLPStartPatten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandLPStartPatten.setStatus("current")
_TnIfTDM2InBandLPStopPatten_Type = DisplayString
_TnIfTDM2InBandLPStopPatten_Object = MibTableColumn
tnIfTDM2InBandLPStopPatten = _TnIfTDM2InBandLPStopPatten_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 8),
    _TnIfTDM2InBandLPStopPatten_Type()
)
tnIfTDM2InBandLPStopPatten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandLPStopPatten.setStatus("current")


class _TnIfTDM2InBandPEERLPEnable_Type(Integer32):
    """Custom type tnIfTDM2InBandPEERLPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDM2InBandPEERLPEnable_Type.__name__ = "Integer32"
_TnIfTDM2InBandPEERLPEnable_Object = MibTableColumn
tnIfTDM2InBandPEERLPEnable = _TnIfTDM2InBandPEERLPEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 9),
    _TnIfTDM2InBandPEERLPEnable_Type()
)
tnIfTDM2InBandPEERLPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandPEERLPEnable.setStatus("current")
_TnIfTDM2InBandPEERLPStartPatten_Type = DisplayString
_TnIfTDM2InBandPEERLPStartPatten_Object = MibTableColumn
tnIfTDM2InBandPEERLPStartPatten = _TnIfTDM2InBandPEERLPStartPatten_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 10),
    _TnIfTDM2InBandPEERLPStartPatten_Type()
)
tnIfTDM2InBandPEERLPStartPatten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandPEERLPStartPatten.setStatus("current")
_TnIfTDM2InBandPEERLPStopPatten_Type = DisplayString
_TnIfTDM2InBandPEERLPStopPatten_Object = MibTableColumn
tnIfTDM2InBandPEERLPStopPatten = _TnIfTDM2InBandPEERLPStopPatten_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 11),
    _TnIfTDM2InBandPEERLPStopPatten_Type()
)
tnIfTDM2InBandPEERLPStopPatten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandPEERLPStopPatten.setStatus("current")


class _TnIfTDM2InBandLPTimeoutEnable_Type(Integer32):
    """Custom type tnIfTDM2InBandLPTimeoutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDM2InBandLPTimeoutEnable_Type.__name__ = "Integer32"
_TnIfTDM2InBandLPTimeoutEnable_Object = MibTableColumn
tnIfTDM2InBandLPTimeoutEnable = _TnIfTDM2InBandLPTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 12),
    _TnIfTDM2InBandLPTimeoutEnable_Type()
)
tnIfTDM2InBandLPTimeoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandLPTimeoutEnable.setStatus("current")


class _TnIfTDM2InBandLPTimeoutCount_Type(Integer32):
    """Custom type tnIfTDM2InBandLPTimeoutCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnIfTDM2InBandLPTimeoutCount_Type.__name__ = "Integer32"
_TnIfTDM2InBandLPTimeoutCount_Object = MibTableColumn
tnIfTDM2InBandLPTimeoutCount = _TnIfTDM2InBandLPTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 13),
    _TnIfTDM2InBandLPTimeoutCount_Type()
)
tnIfTDM2InBandLPTimeoutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandLPTimeoutCount.setStatus("current")


class _TnIfTDM2InBandPEERLPTimeoutEnable_Type(Integer32):
    """Custom type tnIfTDM2InBandPEERLPTimeoutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfTDM2InBandPEERLPTimeoutEnable_Type.__name__ = "Integer32"
_TnIfTDM2InBandPEERLPTimeoutEnable_Object = MibTableColumn
tnIfTDM2InBandPEERLPTimeoutEnable = _TnIfTDM2InBandPEERLPTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 14),
    _TnIfTDM2InBandPEERLPTimeoutEnable_Type()
)
tnIfTDM2InBandPEERLPTimeoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandPEERLPTimeoutEnable.setStatus("current")


class _TnIfTDM2InBandPEERLPTimeoutCount_Type(Integer32):
    """Custom type tnIfTDM2InBandPEERLPTimeoutCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TnIfTDM2InBandPEERLPTimeoutCount_Type.__name__ = "Integer32"
_TnIfTDM2InBandPEERLPTimeoutCount_Object = MibTableColumn
tnIfTDM2InBandPEERLPTimeoutCount = _TnIfTDM2InBandPEERLPTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 10, 1, 15),
    _TnIfTDM2InBandPEERLPTimeoutCount_Type()
)
tnIfTDM2InBandPEERLPTimeoutCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDM2InBandPEERLPTimeoutCount.setStatus("current")

# Managed Objects groups


# Notification objects

tnIfTDMAlarmIndicationSignalEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 6)
)
tnIfTDMAlarmIndicationSignalEvt.setObjects(
      *(("TN-MGMT-TDM-MIB", "ifIndex"),
        ("TN-MGMT-TDM-MIB", "tnIfTDMAlarmIndicationSignal"))
)
if mibBuilder.loadTexts:
    tnIfTDMAlarmIndicationSignalEvt.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MGMT-TDM-MIB",
    **{"tnIfTDMAlarmIndicationSignalEvt": tnIfTDMAlarmIndicationSignalEvt,
       "tnIfTDMTable": tnIfTDMTable,
       "tnIfTDMEntry": tnIfTDMEntry,
       "tnIfTDMAISTransmit": tnIfTDMAISTransmit,
       "tnIfTDMAISFormat": tnIfTDMAISFormat,
       "tnIfTDMAlarmIndicationSignal": tnIfTDMAlarmIndicationSignal,
       "tnIfTDMLongHaul": tnIfTDMLongHaul,
       "tnIfTDMType": tnIfTDMType,
       "tnIfTDMT1E1LineBuildout": tnIfTDMT1E1LineBuildout,
       "tnIfTDMDS3E3LineBuildout": tnIfTDMDS3E3LineBuildout,
       "tnIfTDMConnectorType": tnIfTDMConnectorType,
       "tnIfTDMExtTable": tnIfTDMExtTable,
       "tnIfTDMExtEntry": tnIfTDMExtEntry,
       "tnIfTDMExtId": tnIfTDMExtId,
       "tnIfTDMExtAISTrasmit": tnIfTDMExtAISTrasmit,
       "tnIfTDMExtAISFormat": tnIfTDMExtAISFormat,
       "tnIfTDMExtAlarmIndicationSingnal": tnIfTDMExtAlarmIndicationSingnal,
       "tnIfTDMExtLoopback": tnIfTDMExtLoopback,
       "tnIfTDMExtYellowTrasmit": tnIfTDMExtYellowTrasmit,
       "tnIfTDM2Table": tnIfTDM2Table,
       "tnIfTDM2Entry": tnIfTDM2Entry,
       "tnIfTDM2FiberLineNum": tnIfTDM2FiberLineNum,
       "tnIfTDM2FiberActiveLine": tnIfTDM2FiberActiveLine,
       "tnIfTDM2FiberRevertive": tnIfTDM2FiberRevertive,
       "tnIfTDM2FiberPrimaryLinkStatus": tnIfTDM2FiberPrimaryLinkStatus,
       "tnIfTDM2FiberSecondaryLinkStatus": tnIfTDM2FiberSecondaryLinkStatus,
       "tnIfTDM2InBandLPEnable": tnIfTDM2InBandLPEnable,
       "tnIfTDM2InBandLPStartPatten": tnIfTDM2InBandLPStartPatten,
       "tnIfTDM2InBandLPStopPatten": tnIfTDM2InBandLPStopPatten,
       "tnIfTDM2InBandPEERLPEnable": tnIfTDM2InBandPEERLPEnable,
       "tnIfTDM2InBandPEERLPStartPatten": tnIfTDM2InBandPEERLPStartPatten,
       "tnIfTDM2InBandPEERLPStopPatten": tnIfTDM2InBandPEERLPStopPatten,
       "tnIfTDM2InBandLPTimeoutEnable": tnIfTDM2InBandLPTimeoutEnable,
       "tnIfTDM2InBandLPTimeoutCount": tnIfTDM2InBandLPTimeoutCount,
       "tnIfTDM2InBandPEERLPTimeoutEnable": tnIfTDM2InBandPEERLPTimeoutEnable,
       "tnIfTDM2InBandPEERLPTimeoutCount": tnIfTDM2InBandPEERLPTimeoutCount}
)
