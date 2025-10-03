# SNMP MIB module (ROSMGMT-OPTICAL-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-OPTICAL-TRANSCEIVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:06 2025
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

(rosMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "rosMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rosMgmtOpticalTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18)
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiver.setRevisions(
        ("2020-04-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableVar(TextualConvention, Integer32):
    status = "current"
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



class OpticalParameterType(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("transceiverTemperature", 1),
          ("txbiasCurrent", 2),
          ("txPower", 3),
          ("rxPower", 4),
          ("laserTemperature", 5),
          ("p5V0supplyVoltage", 6),
          ("p3V3supplyVoltage", 7),
          ("p1V8supplyVoltage", 8),
          ("n5V2supplyVoltage", 9),
          ("apdBiasVoltage", 10),
          ("p5V0supplyCurrent", 11),
          ("p3V3supplyCurrent", 12),
          ("p1V8supplyCurrent", 13),
          ("n5V2supplyCurrent", 14),
          ("tecCurrent", 15),
          ("laserWavelength", 16))
    )



class OpticalParameterValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, -1000000),
        ValueRangeConstraint(-40000, 6553600),
    )



class OpticalPMPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("twentyFourHour", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RosMgmtOpticalTransceiverNotifications_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverNotifications = _RosMgmtOpticalTransceiverNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0)
)
_RosMgmtOpticalTransceiverObjects_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverObjects = _RosMgmtOpticalTransceiverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1)
)
_RosMgmtOpticalTransceiverScalarGroup_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverScalarGroup = _RosMgmtOpticalTransceiverScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 1)
)


class _RosMgmtOpticalTransceiverNotifyEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverNotifyEnable based on EnableVar"""
    defaultValue = 2


_RosMgmtOpticalTransceiverNotifyEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverNotifyEnable_Object = MibScalar
rosMgmtOpticalTransceiverNotifyEnable = _RosMgmtOpticalTransceiverNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 1, 1),
    _RosMgmtOpticalTransceiverNotifyEnable_Type()
)
rosMgmtOpticalTransceiverNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverNotifyEnable.setStatus("current")


class _RosMgmtOpticalTransceiverDDMEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverDDMEnable based on EnableVar"""
    defaultValue = 2


_RosMgmtOpticalTransceiverDDMEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverDDMEnable_Object = MibScalar
rosMgmtOpticalTransceiverDDMEnable = _RosMgmtOpticalTransceiverDDMEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 1, 2),
    _RosMgmtOpticalTransceiverDDMEnable_Type()
)
rosMgmtOpticalTransceiverDDMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDMEnable.setStatus("current")


class _RosMgmtOpticalTransceiverCheckPwdEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverCheckPwdEnable based on EnableVar"""
    defaultValue = 2


_RosMgmtOpticalTransceiverCheckPwdEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverCheckPwdEnable_Object = MibScalar
rosMgmtOpticalTransceiverCheckPwdEnable = _RosMgmtOpticalTransceiverCheckPwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 1, 3),
    _RosMgmtOpticalTransceiverCheckPwdEnable_Type()
)
rosMgmtOpticalTransceiverCheckPwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCheckPwdEnable.setStatus("current")


class _RosMgmtOpticalTransceiverPollInterval_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_RosMgmtOpticalTransceiverPollInterval_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverPollInterval_Object = MibScalar
rosMgmtOpticalTransceiverPollInterval = _RosMgmtOpticalTransceiverPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 1, 4),
    _RosMgmtOpticalTransceiverPollInterval_Type()
)
rosMgmtOpticalTransceiverPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPollInterval.setStatus("current")


class _RosMgmtOpticalTransceiverCRCCheckEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverCRCCheckEnable based on EnableVar"""
    defaultValue = 2


_RosMgmtOpticalTransceiverCRCCheckEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverCRCCheckEnable_Object = MibScalar
rosMgmtOpticalTransceiverCRCCheckEnable = _RosMgmtOpticalTransceiverCRCCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 1, 5),
    _RosMgmtOpticalTransceiverCRCCheckEnable_Type()
)
rosMgmtOpticalTransceiverCRCCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCRCCheckEnable.setStatus("current")
_RosMgmtOpticalTransceiverCfgObjects_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverCfgObjects = _RosMgmtOpticalTransceiverCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2)
)
_RosMgmtOpticalTransceiverInfoGroup_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverInfoGroup = _RosMgmtOpticalTransceiverInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1)
)
_RosMgmtOpticalTransceiverInfoTable_Object = MibTable
rosMgmtOpticalTransceiverInfoTable = _RosMgmtOpticalTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverInfoTable.setStatus("current")
_RosMgmtOpticalTransceiverInfoEntry_Object = MibTableRow
rosMgmtOpticalTransceiverInfoEntry = _RosMgmtOpticalTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1)
)
rosMgmtOpticalTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverInfoEntry.setStatus("current")


class _RosMgmtOpticalTransceiverType_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverType based on Integer32"""
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
              14,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("gbic", 2),
          ("soldered", 3),
          ("sfp", 4),
          ("xbi", 5),
          ("xenpak", 6),
          ("xfp", 7),
          ("xff", 8),
          ("xfpe", 9),
          ("xpak", 10),
          ("x2", 11),
          ("sfpj", 12),
          ("qsfp", 14),
          ("qsfp28", 18))
    )


_RosMgmtOpticalTransceiverType_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverType_Object = MibTableColumn
rosMgmtOpticalTransceiverType = _RosMgmtOpticalTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 1),
    _RosMgmtOpticalTransceiverType_Type()
)
rosMgmtOpticalTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverType.setStatus("current")


class _RosMgmtOpticalTransceiverConnectorType_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverConnectorType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sc", 2),
          ("db9", 3),
          ("hssdc", 4),
          ("bnctnc", 5),
          ("fibercoaxialhead", 6),
          ("fiberjack", 7),
          ("lc", 8),
          ("mtrj", 9),
          ("mu", 10),
          ("sg", 11),
          ("fiberpigtail", 12),
          ("mpoparalleloptic", 13),
          ("hssdcII", 14),
          ("copper", 15),
          ("rj45", 16))
    )


_RosMgmtOpticalTransceiverConnectorType_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverConnectorType_Object = MibTableColumn
rosMgmtOpticalTransceiverConnectorType = _RosMgmtOpticalTransceiverConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 2),
    _RosMgmtOpticalTransceiverConnectorType_Type()
)
rosMgmtOpticalTransceiverConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverConnectorType.setStatus("current")
_RosMgmtOpticalTransceiverVendorName_Type = OctetString
_RosMgmtOpticalTransceiverVendorName_Object = MibTableColumn
rosMgmtOpticalTransceiverVendorName = _RosMgmtOpticalTransceiverVendorName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 3),
    _RosMgmtOpticalTransceiverVendorName_Type()
)
rosMgmtOpticalTransceiverVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverVendorName.setStatus("current")
_RosMgmtOpticalTransceiverVendorPN_Type = OctetString
_RosMgmtOpticalTransceiverVendorPN_Object = MibTableColumn
rosMgmtOpticalTransceiverVendorPN = _RosMgmtOpticalTransceiverVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 4),
    _RosMgmtOpticalTransceiverVendorPN_Type()
)
rosMgmtOpticalTransceiverVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverVendorPN.setStatus("current")
_RosMgmtOpticalTransceiverVendorSN_Type = OctetString
_RosMgmtOpticalTransceiverVendorSN_Object = MibTableColumn
rosMgmtOpticalTransceiverVendorSN = _RosMgmtOpticalTransceiverVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 5),
    _RosMgmtOpticalTransceiverVendorSN_Type()
)
rosMgmtOpticalTransceiverVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverVendorSN.setStatus("current")


class _RosMgmtOpticalTransceiverMediaType_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverMediaType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("singlemode", 1),
          ("multimodeE50", 2),
          ("multimode50", 3),
          ("multimode625", 4),
          ("copper", 5),
          ("singlemodeKm", 6),
          ("multimodeOM3", 7),
          ("multimodeOM3Qsfp", 8),
          ("multimodeOM2Qsfp", 9),
          ("multimodeOM1Qsfp", 10),
          ("multimodeOM4Qsfp", 11))
    )


_RosMgmtOpticalTransceiverMediaType_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverMediaType_Object = MibTableColumn
rosMgmtOpticalTransceiverMediaType = _RosMgmtOpticalTransceiverMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 6),
    _RosMgmtOpticalTransceiverMediaType_Type()
)
rosMgmtOpticalTransceiverMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverMediaType.setStatus("current")
_RosMgmtOpticalTransceiverTransmissionDistance_Type = Integer32
_RosMgmtOpticalTransceiverTransmissionDistance_Object = MibTableColumn
rosMgmtOpticalTransceiverTransmissionDistance = _RosMgmtOpticalTransceiverTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 7),
    _RosMgmtOpticalTransceiverTransmissionDistance_Type()
)
rosMgmtOpticalTransceiverTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTransmissionDistance.setStatus("current")
_RosMgmtOpticalTransceiverAbility_Type = Unsigned32
_RosMgmtOpticalTransceiverAbility_Object = MibTableColumn
rosMgmtOpticalTransceiverAbility = _RosMgmtOpticalTransceiverAbility_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 8),
    _RosMgmtOpticalTransceiverAbility_Type()
)
rosMgmtOpticalTransceiverAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverAbility.setStatus("current")


class _RosMgmtOpticalTransceiverDDM_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverDDM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverDDM_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverDDM_Object = MibTableColumn
rosMgmtOpticalTransceiverDDM = _RosMgmtOpticalTransceiverDDM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 9),
    _RosMgmtOpticalTransceiverDDM_Type()
)
rosMgmtOpticalTransceiverDDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDM.setStatus("current")


class _RosMgmtOpticalTransceiverCalibrationType_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverCalibrationType based on Integer32"""
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
          ("internal", 2),
          ("external", 3))
    )


_RosMgmtOpticalTransceiverCalibrationType_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverCalibrationType_Object = MibTableColumn
rosMgmtOpticalTransceiverCalibrationType = _RosMgmtOpticalTransceiverCalibrationType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 10),
    _RosMgmtOpticalTransceiverCalibrationType_Type()
)
rosMgmtOpticalTransceiverCalibrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCalibrationType.setStatus("current")


class _RosMgmtOpticalTransceiverRSSI_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverRSSI_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverRSSI_Object = MibTableColumn
rosMgmtOpticalTransceiverRSSI = _RosMgmtOpticalTransceiverRSSI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 11),
    _RosMgmtOpticalTransceiverRSSI_Type()
)
rosMgmtOpticalTransceiverRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverRSSI.setStatus("current")
_RosMgmtOpticalTransceiverVendorRev_Type = OctetString
_RosMgmtOpticalTransceiverVendorRev_Object = MibTableColumn
rosMgmtOpticalTransceiverVendorRev = _RosMgmtOpticalTransceiverVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 12),
    _RosMgmtOpticalTransceiverVendorRev_Type()
)
rosMgmtOpticalTransceiverVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverVendorRev.setStatus("current")
_RosMgmtOpticalTransceiverBRMax_Type = Integer32
_RosMgmtOpticalTransceiverBRMax_Object = MibTableColumn
rosMgmtOpticalTransceiverBRMax = _RosMgmtOpticalTransceiverBRMax_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 13),
    _RosMgmtOpticalTransceiverBRMax_Type()
)
rosMgmtOpticalTransceiverBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverBRMax.setStatus("current")
_RosMgmtOpticalTransceiverBRMin_Type = Integer32
_RosMgmtOpticalTransceiverBRMin_Object = MibTableColumn
rosMgmtOpticalTransceiverBRMin = _RosMgmtOpticalTransceiverBRMin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 14),
    _RosMgmtOpticalTransceiverBRMin_Type()
)
rosMgmtOpticalTransceiverBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverBRMin.setStatus("current")


class _RosMgmtOpticalTransceiverWavelengthContrl_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverWavelengthContrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverWavelengthContrl_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverWavelengthContrl_Object = MibTableColumn
rosMgmtOpticalTransceiverWavelengthContrl = _RosMgmtOpticalTransceiverWavelengthContrl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 15),
    _RosMgmtOpticalTransceiverWavelengthContrl_Type()
)
rosMgmtOpticalTransceiverWavelengthContrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverWavelengthContrl.setStatus("current")
_RosMgmtOpticalTransceiverWavelength_Type = Integer32
_RosMgmtOpticalTransceiverWavelength_Object = MibTableColumn
rosMgmtOpticalTransceiverWavelength = _RosMgmtOpticalTransceiverWavelength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 16),
    _RosMgmtOpticalTransceiverWavelength_Type()
)
rosMgmtOpticalTransceiverWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverWavelength.setStatus("current")
_RosMgmtOpticalTransceiverWaveTolerance_Type = Integer32
_RosMgmtOpticalTransceiverWaveTolerance_Object = MibTableColumn
rosMgmtOpticalTransceiverWaveTolerance = _RosMgmtOpticalTransceiverWaveTolerance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 17),
    _RosMgmtOpticalTransceiverWaveTolerance_Type()
)
rosMgmtOpticalTransceiverWaveTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverWaveTolerance.setStatus("current")
_RosMgmtOpticalTransceiverCompatibility_Type = OctetString
_RosMgmtOpticalTransceiverCompatibility_Object = MibTableColumn
rosMgmtOpticalTransceiverCompatibility = _RosMgmtOpticalTransceiverCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 18),
    _RosMgmtOpticalTransceiverCompatibility_Type()
)
rosMgmtOpticalTransceiverCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCompatibility.setStatus("current")


class _RosMgmtOpticalTransceiverPowerDissipation_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverPowerDissipation based on Integer32"""
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
        *(("p1W5", 1),
          ("p2W5", 2),
          ("p3W5", 3),
          ("exceed", 4))
    )


_RosMgmtOpticalTransceiverPowerDissipation_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverPowerDissipation_Object = MibTableColumn
rosMgmtOpticalTransceiverPowerDissipation = _RosMgmtOpticalTransceiverPowerDissipation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 19),
    _RosMgmtOpticalTransceiverPowerDissipation_Type()
)
rosMgmtOpticalTransceiverPowerDissipation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPowerDissipation.setStatus("current")


class _RosMgmtOpticalTransceiverCDR_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverCDR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverCDR_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverCDR_Object = MibTableColumn
rosMgmtOpticalTransceiverCDR = _RosMgmtOpticalTransceiverCDR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 20),
    _RosMgmtOpticalTransceiverCDR_Type()
)
rosMgmtOpticalTransceiverCDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCDR.setStatus("current")


class _RosMgmtOpticalTransceiverRefClock_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverRefClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("required", 1),
          ("notrequired", 2))
    )


_RosMgmtOpticalTransceiverRefClock_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverRefClock_Object = MibTableColumn
rosMgmtOpticalTransceiverRefClock = _RosMgmtOpticalTransceiverRefClock_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 21),
    _RosMgmtOpticalTransceiverRefClock_Type()
)
rosMgmtOpticalTransceiverRefClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverRefClock.setStatus("current")


class _RosMgmtOpticalTransceiverTransmitterType_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverTransmitterType based on Integer32"""
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
        *(("vcsel850nm", 1),
          ("vcsel1310nm", 2),
          ("vcsel1550nm", 3),
          ("fp1310nm", 4),
          ("dfb1310nm", 5),
          ("dfb1550nm", 6),
          ("eml1310nm", 7),
          ("eml1550nm", 8),
          ("copperothers", 9))
    )


_RosMgmtOpticalTransceiverTransmitterType_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverTransmitterType_Object = MibTableColumn
rosMgmtOpticalTransceiverTransmitterType = _RosMgmtOpticalTransceiverTransmitterType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 22),
    _RosMgmtOpticalTransceiverTransmitterType_Type()
)
rosMgmtOpticalTransceiverTransmitterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTransmitterType.setStatus("current")


class _RosMgmtOpticalTransceiverCooled_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverCooled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cooled", 1),
          ("uncooled", 2))
    )


_RosMgmtOpticalTransceiverCooled_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverCooled_Object = MibTableColumn
rosMgmtOpticalTransceiverCooled = _RosMgmtOpticalTransceiverCooled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 24),
    _RosMgmtOpticalTransceiverCooled_Type()
)
rosMgmtOpticalTransceiverCooled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCooled.setStatus("current")


class _RosMgmtOpticalTransceiverTunalbe_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverTunalbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunable", 1),
          ("untunable", 2))
    )


_RosMgmtOpticalTransceiverTunalbe_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverTunalbe_Object = MibTableColumn
rosMgmtOpticalTransceiverTunalbe = _RosMgmtOpticalTransceiverTunalbe_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 25),
    _RosMgmtOpticalTransceiverTunalbe_Type()
)
rosMgmtOpticalTransceiverTunalbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTunalbe.setStatus("current")


class _RosMgmtOpticalTransceiverDetectorType_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverDetectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pin", 1),
          ("apd", 2))
    )


_RosMgmtOpticalTransceiverDetectorType_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverDetectorType_Object = MibTableColumn
rosMgmtOpticalTransceiverDetectorType = _RosMgmtOpticalTransceiverDetectorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 26),
    _RosMgmtOpticalTransceiverDetectorType_Type()
)
rosMgmtOpticalTransceiverDetectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDetectorType.setStatus("current")


class _RosMgmtOpticalTransceiverLineLoopBack_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverLineLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverLineLoopBack_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverLineLoopBack_Object = MibTableColumn
rosMgmtOpticalTransceiverLineLoopBack = _RosMgmtOpticalTransceiverLineLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 27),
    _RosMgmtOpticalTransceiverLineLoopBack_Type()
)
rosMgmtOpticalTransceiverLineLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverLineLoopBack.setStatus("current")


class _RosMgmtOpticalTransceiverXFILoopBack_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverXFILoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverXFILoopBack_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverXFILoopBack_Object = MibTableColumn
rosMgmtOpticalTransceiverXFILoopBack = _RosMgmtOpticalTransceiverXFILoopBack_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 28),
    _RosMgmtOpticalTransceiverXFILoopBack_Type()
)
rosMgmtOpticalTransceiverXFILoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverXFILoopBack.setStatus("current")


class _RosMgmtOpticalTransceiverVps_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverVps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverVps_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverVps_Object = MibTableColumn
rosMgmtOpticalTransceiverVps = _RosMgmtOpticalTransceiverVps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 29),
    _RosMgmtOpticalTransceiverVps_Type()
)
rosMgmtOpticalTransceiverVps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverVps.setStatus("current")


class _RosMgmtOpticalTransceiverTxDis_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverTxDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverTxDis_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverTxDis_Object = MibTableColumn
rosMgmtOpticalTransceiverTxDis = _RosMgmtOpticalTransceiverTxDis_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 30),
    _RosMgmtOpticalTransceiverTxDis_Type()
)
rosMgmtOpticalTransceiverTxDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTxDis.setStatus("current")


class _RosMgmtOpticalTransceiverStandby_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverStandby_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverStandby_Object = MibTableColumn
rosMgmtOpticalTransceiverStandby = _RosMgmtOpticalTransceiverStandby_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 31),
    _RosMgmtOpticalTransceiverStandby_Type()
)
rosMgmtOpticalTransceiverStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverStandby.setStatus("current")


class _RosMgmtOpticalTransceiverInVpsLowPower_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverInVpsLowPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverInVpsLowPower_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverInVpsLowPower_Object = MibTableColumn
rosMgmtOpticalTransceiverInVpsLowPower = _RosMgmtOpticalTransceiverInVpsLowPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 32),
    _RosMgmtOpticalTransceiverInVpsLowPower_Type()
)
rosMgmtOpticalTransceiverInVpsLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverInVpsLowPower.setStatus("current")


class _RosMgmtOpticalTransceiverOutVpsLowPower_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverOutVpsLowPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverOutVpsLowPower_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverOutVpsLowPower_Object = MibTableColumn
rosMgmtOpticalTransceiverOutVpsLowPower = _RosMgmtOpticalTransceiverOutVpsLowPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 33),
    _RosMgmtOpticalTransceiverOutVpsLowPower_Type()
)
rosMgmtOpticalTransceiverOutVpsLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverOutVpsLowPower.setStatus("current")


class _RosMgmtOpticalTransceiverFEC_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverFEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverFEC_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverFEC_Object = MibTableColumn
rosMgmtOpticalTransceiverFEC = _RosMgmtOpticalTransceiverFEC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 34),
    _RosMgmtOpticalTransceiverFEC_Type()
)
rosMgmtOpticalTransceiverFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverFEC.setStatus("current")


class _RosMgmtOpticalTransceiverCMU_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverCMU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notsupport", 2))
    )


_RosMgmtOpticalTransceiverCMU_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverCMU_Object = MibTableColumn
rosMgmtOpticalTransceiverCMU = _RosMgmtOpticalTransceiverCMU_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 35),
    _RosMgmtOpticalTransceiverCMU_Type()
)
rosMgmtOpticalTransceiverCMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCMU.setStatus("current")


class _RosMgmtOpticalTransceiverBR_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              12,
              13,
              19,
              103,
              114,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("bitrate125Mbps", 1),
          ("bitrate155Mbps", 2),
          ("bitrate622Mbps", 6),
          ("bitrate1250Mbps", 12),
          ("bitrate1DOT25Gbps", 13),
          ("bitrate2DOT5Gbps", 19),
          ("bitrate10GbpsOr100Gbps1", 103),
          ("bitrate100Gbps2", 114),
          ("bitrate25Gbps", 255))
    )


_RosMgmtOpticalTransceiverBR_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverBR_Object = MibTableColumn
rosMgmtOpticalTransceiverBR = _RosMgmtOpticalTransceiverBR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 1, 1, 1, 36),
    _RosMgmtOpticalTransceiverBR_Type()
)
rosMgmtOpticalTransceiverBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverBR.setStatus("current")
_RosMgmtOpticalTransceiverDDMGroup_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverDDMGroup = _RosMgmtOpticalTransceiverDDMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2)
)
_RosMgmtOpticalTransceiverDDMTable_Object = MibTable
rosMgmtOpticalTransceiverDDMTable = _RosMgmtOpticalTransceiverDDMTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDMTable.setStatus("current")
_RosMgmtOpticalTransceiverDDMEntry_Object = MibTableRow
rosMgmtOpticalTransceiverDDMEntry = _RosMgmtOpticalTransceiverDDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1)
)
rosMgmtOpticalTransceiverDDMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterType"),
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDMEntry.setStatus("current")
_RosMgmtOpticalTransceiverParameterType_Type = OpticalParameterType
_RosMgmtOpticalTransceiverParameterType_Object = MibTableColumn
rosMgmtOpticalTransceiverParameterType = _RosMgmtOpticalTransceiverParameterType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 1),
    _RosMgmtOpticalTransceiverParameterType_Type()
)
rosMgmtOpticalTransceiverParameterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParameterType.setStatus("current")
_RosMgmtOpticalTransceiverParameterValue_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverParameterValue_Object = MibTableColumn
rosMgmtOpticalTransceiverParameterValue = _RosMgmtOpticalTransceiverParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 2),
    _RosMgmtOpticalTransceiverParameterValue_Type()
)
rosMgmtOpticalTransceiverParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParameterValue.setStatus("current")
_RosMgmtOpticalTransceiverParamHighAlarmThresh_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverParamHighAlarmThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverParamHighAlarmThresh = _RosMgmtOpticalTransceiverParamHighAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 3),
    _RosMgmtOpticalTransceiverParamHighAlarmThresh_Type()
)
rosMgmtOpticalTransceiverParamHighAlarmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamHighAlarmThresh.setStatus("current")
_RosMgmtOpticalTransceiverParamHighWarningThresh_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverParamHighWarningThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverParamHighWarningThresh = _RosMgmtOpticalTransceiverParamHighWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 4),
    _RosMgmtOpticalTransceiverParamHighWarningThresh_Type()
)
rosMgmtOpticalTransceiverParamHighWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamHighWarningThresh.setStatus("current")
_RosMgmtOpticalTransceiverParamLowAlarmThresh_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverParamLowAlarmThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverParamLowAlarmThresh = _RosMgmtOpticalTransceiverParamLowAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 5),
    _RosMgmtOpticalTransceiverParamLowAlarmThresh_Type()
)
rosMgmtOpticalTransceiverParamLowAlarmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamLowAlarmThresh.setStatus("current")
_RosMgmtOpticalTransceiverParamLowWarningThresh_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverParamLowWarningThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverParamLowWarningThresh = _RosMgmtOpticalTransceiverParamLowWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 6),
    _RosMgmtOpticalTransceiverParamLowWarningThresh_Type()
)
rosMgmtOpticalTransceiverParamLowWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamLowWarningThresh.setStatus("current")


class _RosMgmtOpticalTransceiverParamAlarmStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverParamAlarmStatus based on Integer32"""
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
        *(("normal", 1),
          ("highalarm", 2),
          ("highwarning", 3),
          ("lowalarm", 4),
          ("lowwarning", 5))
    )


_RosMgmtOpticalTransceiverParamAlarmStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverParamAlarmStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverParamAlarmStatus = _RosMgmtOpticalTransceiverParamAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 7),
    _RosMgmtOpticalTransceiverParamAlarmStatus_Type()
)
rosMgmtOpticalTransceiverParamAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamAlarmStatus.setStatus("current")
_RosMgmtOpticalTransceiverParamAlarmLastValue_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverParamAlarmLastValue_Object = MibTableColumn
rosMgmtOpticalTransceiverParamAlarmLastValue = _RosMgmtOpticalTransceiverParamAlarmLastValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 8),
    _RosMgmtOpticalTransceiverParamAlarmLastValue_Type()
)
rosMgmtOpticalTransceiverParamAlarmLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamAlarmLastValue.setStatus("current")
_RosMgmtOpticalTransceiverParamAlarmLastChange_Type = TimeTicks
_RosMgmtOpticalTransceiverParamAlarmLastChange_Object = MibTableColumn
rosMgmtOpticalTransceiverParamAlarmLastChange = _RosMgmtOpticalTransceiverParamAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 9),
    _RosMgmtOpticalTransceiverParamAlarmLastChange_Type()
)
rosMgmtOpticalTransceiverParamAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamAlarmLastChange.setStatus("current")


class _RosMgmtOpticalTransceiverDDM15MinValidIntervals_Type(Unsigned32):
    """Custom type rosMgmtOpticalTransceiverDDM15MinValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_RosMgmtOpticalTransceiverDDM15MinValidIntervals_Type.__name__ = "Unsigned32"
_RosMgmtOpticalTransceiverDDM15MinValidIntervals_Object = MibTableColumn
rosMgmtOpticalTransceiverDDM15MinValidIntervals = _RosMgmtOpticalTransceiverDDM15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 10),
    _RosMgmtOpticalTransceiverDDM15MinValidIntervals_Type()
)
rosMgmtOpticalTransceiverDDM15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDM15MinValidIntervals.setStatus("current")


class _RosMgmtOpticalTransceiverDDM24HrValidIntervals_Type(Unsigned32):
    """Custom type rosMgmtOpticalTransceiverDDM24HrValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RosMgmtOpticalTransceiverDDM24HrValidIntervals_Type.__name__ = "Unsigned32"
_RosMgmtOpticalTransceiverDDM24HrValidIntervals_Object = MibTableColumn
rosMgmtOpticalTransceiverDDM24HrValidIntervals = _RosMgmtOpticalTransceiverDDM24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 11),
    _RosMgmtOpticalTransceiverDDM24HrValidIntervals_Type()
)
rosMgmtOpticalTransceiverDDM24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDM24HrValidIntervals.setStatus("current")


class _RosMgmtOpticalTransceiverDDMValidStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverDDMValidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RosMgmtOpticalTransceiverDDMValidStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverDDMValidStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverDDMValidStatus = _RosMgmtOpticalTransceiverDDMValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 12),
    _RosMgmtOpticalTransceiverDDMValidStatus_Type()
)
rosMgmtOpticalTransceiverDDMValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDDMValidStatus.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParameterValue_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParameterValue_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParameterValue = _RosMgmtOpticalTransceiverQsfpParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 13),
    _RosMgmtOpticalTransceiverQsfpParameterValue_Type()
)
rosMgmtOpticalTransceiverQsfpParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParameterValue.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamHighAlarmThresh_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamHighAlarmThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamHighAlarmThresh = _RosMgmtOpticalTransceiverQsfpParamHighAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 14),
    _RosMgmtOpticalTransceiverQsfpParamHighAlarmThresh_Type()
)
rosMgmtOpticalTransceiverQsfpParamHighAlarmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamHighAlarmThresh.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamHighWarningThresh_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamHighWarningThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamHighWarningThresh = _RosMgmtOpticalTransceiverQsfpParamHighWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 15),
    _RosMgmtOpticalTransceiverQsfpParamHighWarningThresh_Type()
)
rosMgmtOpticalTransceiverQsfpParamHighWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamHighWarningThresh.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamLowAlarmThresh_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamLowAlarmThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamLowAlarmThresh = _RosMgmtOpticalTransceiverQsfpParamLowAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 16),
    _RosMgmtOpticalTransceiverQsfpParamLowAlarmThresh_Type()
)
rosMgmtOpticalTransceiverQsfpParamLowAlarmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamLowAlarmThresh.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamLowWarningThresh_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamLowWarningThresh_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamLowWarningThresh = _RosMgmtOpticalTransceiverQsfpParamLowWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 17),
    _RosMgmtOpticalTransceiverQsfpParamLowWarningThresh_Type()
)
rosMgmtOpticalTransceiverQsfpParamLowWarningThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamLowWarningThresh.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamAlarmStatus_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamAlarmStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamAlarmStatus = _RosMgmtOpticalTransceiverQsfpParamAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 18),
    _RosMgmtOpticalTransceiverQsfpParamAlarmStatus_Type()
)
rosMgmtOpticalTransceiverQsfpParamAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamAlarmStatus.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamAlarmLastValue_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamAlarmLastValue_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamAlarmLastValue = _RosMgmtOpticalTransceiverQsfpParamAlarmLastValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 19),
    _RosMgmtOpticalTransceiverQsfpParamAlarmLastValue_Type()
)
rosMgmtOpticalTransceiverQsfpParamAlarmLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamAlarmLastValue.setStatus("current")
_RosMgmtOpticalTransceiverQsfpParamAlarmLastChange_Type = OctetString
_RosMgmtOpticalTransceiverQsfpParamAlarmLastChange_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpParamAlarmLastChange = _RosMgmtOpticalTransceiverQsfpParamAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 20),
    _RosMgmtOpticalTransceiverQsfpParamAlarmLastChange_Type()
)
rosMgmtOpticalTransceiverQsfpParamAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpParamAlarmLastChange.setStatus("current")
_RosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals_Type = OctetString
_RosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals = _RosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 21),
    _RosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals_Type()
)
rosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals.setStatus("current")
_RosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals_Type = OctetString
_RosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals = _RosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 22),
    _RosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals_Type()
)
rosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals.setStatus("current")
_RosMgmtOpticalTransceiverQsfpDDMValidStatus_Type = OctetString
_RosMgmtOpticalTransceiverQsfpDDMValidStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpDDMValidStatus = _RosMgmtOpticalTransceiverQsfpDDMValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 2, 1, 1, 23),
    _RosMgmtOpticalTransceiverQsfpDDMValidStatus_Type()
)
rosMgmtOpticalTransceiverQsfpDDMValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpDDMValidStatus.setStatus("current")
_RosMgmtOpticalTransceiverPMGroup_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverPMGroup = _RosMgmtOpticalTransceiverPMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3)
)
_RosMgmtOpticalTransceiverPMCurrentTable_Object = MibTable
rosMgmtOpticalTransceiverPMCurrentTable = _RosMgmtOpticalTransceiverPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentTable.setStatus("current")
_RosMgmtOpticalTransceiverPMCurrentEntry_Object = MibTableRow
rosMgmtOpticalTransceiverPMCurrentEntry = _RosMgmtOpticalTransceiverPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1)
)
rosMgmtOpticalTransceiverPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverPMCurrentPeriod"),
    (0, "ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverPMCurrentParamType"),
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentEntry.setStatus("current")
_RosMgmtOpticalTransceiverPMCurrentPeriod_Type = OpticalPMPeriod
_RosMgmtOpticalTransceiverPMCurrentPeriod_Object = MibTableColumn
rosMgmtOpticalTransceiverPMCurrentPeriod = _RosMgmtOpticalTransceiverPMCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 1),
    _RosMgmtOpticalTransceiverPMCurrentPeriod_Type()
)
rosMgmtOpticalTransceiverPMCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentPeriod.setStatus("current")
_RosMgmtOpticalTransceiverPMCurrentParamType_Type = OpticalParameterType
_RosMgmtOpticalTransceiverPMCurrentParamType_Object = MibTableColumn
rosMgmtOpticalTransceiverPMCurrentParamType = _RosMgmtOpticalTransceiverPMCurrentParamType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 2),
    _RosMgmtOpticalTransceiverPMCurrentParamType_Type()
)
rosMgmtOpticalTransceiverPMCurrentParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentParamType.setStatus("current")
_RosMgmtOpticalTransceiverPMCurrentMaxParam_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverPMCurrentMaxParam_Object = MibTableColumn
rosMgmtOpticalTransceiverPMCurrentMaxParam = _RosMgmtOpticalTransceiverPMCurrentMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 3),
    _RosMgmtOpticalTransceiverPMCurrentMaxParam_Type()
)
rosMgmtOpticalTransceiverPMCurrentMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentMaxParam.setStatus("current")
_RosMgmtOpticalTransceiverPMCurrentMinParam_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverPMCurrentMinParam_Object = MibTableColumn
rosMgmtOpticalTransceiverPMCurrentMinParam = _RosMgmtOpticalTransceiverPMCurrentMinParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 4),
    _RosMgmtOpticalTransceiverPMCurrentMinParam_Type()
)
rosMgmtOpticalTransceiverPMCurrentMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentMinParam.setStatus("current")
_RosMgmtOpticalTransceiverPMCurrentMeanParam_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverPMCurrentMeanParam_Object = MibTableColumn
rosMgmtOpticalTransceiverPMCurrentMeanParam = _RosMgmtOpticalTransceiverPMCurrentMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 5),
    _RosMgmtOpticalTransceiverPMCurrentMeanParam_Type()
)
rosMgmtOpticalTransceiverPMCurrentMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMCurrentMeanParam.setStatus("current")
_RosMgmtOpticalTransceiverQsfpPMCurrentMaxParam_Type = OctetString
_RosMgmtOpticalTransceiverQsfpPMCurrentMaxParam_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpPMCurrentMaxParam = _RosMgmtOpticalTransceiverQsfpPMCurrentMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 6),
    _RosMgmtOpticalTransceiverQsfpPMCurrentMaxParam_Type()
)
rosMgmtOpticalTransceiverQsfpPMCurrentMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpPMCurrentMaxParam.setStatus("current")
_RosMgmtOpticalTransceiverQsfpPMCurrentMinParam_Type = OctetString
_RosMgmtOpticalTransceiverQsfpPMCurrentMinParam_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpPMCurrentMinParam = _RosMgmtOpticalTransceiverQsfpPMCurrentMinParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 7),
    _RosMgmtOpticalTransceiverQsfpPMCurrentMinParam_Type()
)
rosMgmtOpticalTransceiverQsfpPMCurrentMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpPMCurrentMinParam.setStatus("current")
_RosMgmtOpticalTransceiverQsfpPMCurrentMeanParam_Type = OctetString
_RosMgmtOpticalTransceiverQsfpPMCurrentMeanParam_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpPMCurrentMeanParam = _RosMgmtOpticalTransceiverQsfpPMCurrentMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 1, 1, 8),
    _RosMgmtOpticalTransceiverQsfpPMCurrentMeanParam_Type()
)
rosMgmtOpticalTransceiverQsfpPMCurrentMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpPMCurrentMeanParam.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalTable_Object = MibTable
rosMgmtOpticalTransceiverPMIntervalTable = _RosMgmtOpticalTransceiverPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalTable.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalEntry_Object = MibTableRow
rosMgmtOpticalTransceiverPMIntervalEntry = _RosMgmtOpticalTransceiverPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1)
)
rosMgmtOpticalTransceiverPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverPMIntervalPeriod"),
    (0, "ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverPMIntervalNumber"),
    (0, "ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverPMIntervalParamType"),
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalEntry.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalPeriod_Type = OpticalPMPeriod
_RosMgmtOpticalTransceiverPMIntervalPeriod_Object = MibTableColumn
rosMgmtOpticalTransceiverPMIntervalPeriod = _RosMgmtOpticalTransceiverPMIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 1),
    _RosMgmtOpticalTransceiverPMIntervalPeriod_Type()
)
rosMgmtOpticalTransceiverPMIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalPeriod.setStatus("current")


class _RosMgmtOpticalTransceiverPMIntervalNumber_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RosMgmtOpticalTransceiverPMIntervalNumber_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverPMIntervalNumber_Object = MibTableColumn
rosMgmtOpticalTransceiverPMIntervalNumber = _RosMgmtOpticalTransceiverPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 2),
    _RosMgmtOpticalTransceiverPMIntervalNumber_Type()
)
rosMgmtOpticalTransceiverPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalNumber.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalParamType_Type = OpticalParameterType
_RosMgmtOpticalTransceiverPMIntervalParamType_Object = MibTableColumn
rosMgmtOpticalTransceiverPMIntervalParamType = _RosMgmtOpticalTransceiverPMIntervalParamType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 3),
    _RosMgmtOpticalTransceiverPMIntervalParamType_Type()
)
rosMgmtOpticalTransceiverPMIntervalParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalParamType.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalMaxParam_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverPMIntervalMaxParam_Object = MibTableColumn
rosMgmtOpticalTransceiverPMIntervalMaxParam = _RosMgmtOpticalTransceiverPMIntervalMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 4),
    _RosMgmtOpticalTransceiverPMIntervalMaxParam_Type()
)
rosMgmtOpticalTransceiverPMIntervalMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalMaxParam.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalMinParam_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverPMIntervalMinParam_Object = MibTableColumn
rosMgmtOpticalTransceiverPMIntervalMinParam = _RosMgmtOpticalTransceiverPMIntervalMinParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 5),
    _RosMgmtOpticalTransceiverPMIntervalMinParam_Type()
)
rosMgmtOpticalTransceiverPMIntervalMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalMinParam.setStatus("current")
_RosMgmtOpticalTransceiverPMIntervalMeanParam_Type = OpticalParameterValue
_RosMgmtOpticalTransceiverPMIntervalMeanParam_Object = MibTableColumn
rosMgmtOpticalTransceiverPMIntervalMeanParam = _RosMgmtOpticalTransceiverPMIntervalMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 6),
    _RosMgmtOpticalTransceiverPMIntervalMeanParam_Type()
)
rosMgmtOpticalTransceiverPMIntervalMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPMIntervalMeanParam.setStatus("current")
_RosMgmtOpticalTransceiverQsfpPMIntervalMaxParam_Type = OctetString
_RosMgmtOpticalTransceiverQsfpPMIntervalMaxParam_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpPMIntervalMaxParam = _RosMgmtOpticalTransceiverQsfpPMIntervalMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 7),
    _RosMgmtOpticalTransceiverQsfpPMIntervalMaxParam_Type()
)
rosMgmtOpticalTransceiverQsfpPMIntervalMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpPMIntervalMaxParam.setStatus("current")
_RosMgmtOpticalTransceiverQsfpPMIntervalMinParam_Type = OctetString
_RosMgmtOpticalTransceiverQsfpPMIntervalMinParam_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpPMIntervalMinParam = _RosMgmtOpticalTransceiverQsfpPMIntervalMinParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 8),
    _RosMgmtOpticalTransceiverQsfpPMIntervalMinParam_Type()
)
rosMgmtOpticalTransceiverQsfpPMIntervalMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpPMIntervalMinParam.setStatus("current")
_RosMgmtOpticalTransceiverQsfpPMIntervalMeanParam_Type = OctetString
_RosMgmtOpticalTransceiverQsfpPMIntervalMeanParam_Object = MibTableColumn
rosMgmtOpticalTransceiverQsfpPMIntervalMeanParam = _RosMgmtOpticalTransceiverQsfpPMIntervalMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 3, 2, 1, 9),
    _RosMgmtOpticalTransceiverQsfpPMIntervalMeanParam_Type()
)
rosMgmtOpticalTransceiverQsfpPMIntervalMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverQsfpPMIntervalMeanParam.setStatus("current")
_RosMgmtOpticalTransceiverStatusGroup_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverStatusGroup = _RosMgmtOpticalTransceiverStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4)
)
_RosMgmtOpticalTransceiverCurrentStatusTable_Object = MibTable
rosMgmtOpticalTransceiverCurrentStatusTable = _RosMgmtOpticalTransceiverCurrentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCurrentStatusTable.setStatus("current")
_RosMgmtOpticalTransceiverCurrentStatusEntry_Object = MibTableRow
rosMgmtOpticalTransceiverCurrentStatusEntry = _RosMgmtOpticalTransceiverCurrentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1)
)
rosMgmtOpticalTransceiverCurrentStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverCurrentStatusEntry.setStatus("current")


class _RosMgmtOpticalTransceiverHwInfoAbsStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverHwInfoAbsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_RosMgmtOpticalTransceiverHwInfoAbsStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverHwInfoAbsStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverHwInfoAbsStatus = _RosMgmtOpticalTransceiverHwInfoAbsStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 1),
    _RosMgmtOpticalTransceiverHwInfoAbsStatus_Type()
)
rosMgmtOpticalTransceiverHwInfoAbsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverHwInfoAbsStatus.setStatus("current")


class _RosMgmtOpticalTransceiverHwInfoNRStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverHwInfoNRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("notready", 2))
    )


_RosMgmtOpticalTransceiverHwInfoNRStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverHwInfoNRStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverHwInfoNRStatus = _RosMgmtOpticalTransceiverHwInfoNRStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 2),
    _RosMgmtOpticalTransceiverHwInfoNRStatus_Type()
)
rosMgmtOpticalTransceiverHwInfoNRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverHwInfoNRStatus.setStatus("current")


class _RosMgmtOpticalTransceiverHwInfoRxLosStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverHwInfoRxLosStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RosMgmtOpticalTransceiverHwInfoRxLosStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverHwInfoRxLosStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverHwInfoRxLosStatus = _RosMgmtOpticalTransceiverHwInfoRxLosStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 3),
    _RosMgmtOpticalTransceiverHwInfoRxLosStatus_Type()
)
rosMgmtOpticalTransceiverHwInfoRxLosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverHwInfoRxLosStatus.setStatus("current")


class _RosMgmtOpticalTransceiverHwInfoStandby_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverHwInfoStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("standby", 2))
    )


_RosMgmtOpticalTransceiverHwInfoStandby_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverHwInfoStandby_Object = MibTableColumn
rosMgmtOpticalTransceiverHwInfoStandby = _RosMgmtOpticalTransceiverHwInfoStandby_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 4),
    _RosMgmtOpticalTransceiverHwInfoStandby_Type()
)
rosMgmtOpticalTransceiverHwInfoStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverHwInfoStandby.setStatus("current")


class _RosMgmtOpticalTransceiverHwInfoLaser_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverHwInfoLaser based on Integer32"""
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


_RosMgmtOpticalTransceiverHwInfoLaser_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverHwInfoLaser_Object = MibTableColumn
rosMgmtOpticalTransceiverHwInfoLaser = _RosMgmtOpticalTransceiverHwInfoLaser_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 5),
    _RosMgmtOpticalTransceiverHwInfoLaser_Type()
)
rosMgmtOpticalTransceiverHwInfoLaser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverHwInfoLaser.setStatus("current")
_RosMgmtOpticalTransceiverWaveLengthError_Type = Integer32
_RosMgmtOpticalTransceiverWaveLengthError_Object = MibTableColumn
rosMgmtOpticalTransceiverWaveLengthError = _RosMgmtOpticalTransceiverWaveLengthError_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 6),
    _RosMgmtOpticalTransceiverWaveLengthError_Type()
)
rosMgmtOpticalTransceiverWaveLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverWaveLengthError.setStatus("current")


class _RosMgmtOpticalTransceiverUserWaveLength_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverUserWaveLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276800),
    )


_RosMgmtOpticalTransceiverUserWaveLength_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverUserWaveLength_Object = MibTableColumn
rosMgmtOpticalTransceiverUserWaveLength = _RosMgmtOpticalTransceiverUserWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 7),
    _RosMgmtOpticalTransceiverUserWaveLength_Type()
)
rosMgmtOpticalTransceiverUserWaveLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverUserWaveLength.setStatus("current")


class _RosMgmtOpticalTransceiverUserDataRate_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverUserDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9500, 12500),
    )


_RosMgmtOpticalTransceiverUserDataRate_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverUserDataRate_Object = MibTableColumn
rosMgmtOpticalTransceiverUserDataRate = _RosMgmtOpticalTransceiverUserDataRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 8),
    _RosMgmtOpticalTransceiverUserDataRate_Type()
)
rosMgmtOpticalTransceiverUserDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverUserDataRate.setStatus("current")


class _RosMgmtOpticalTransceiverUserLineLoopBack_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverUserLineLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("lineLoopback", 2))
    )


_RosMgmtOpticalTransceiverUserLineLoopBack_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverUserLineLoopBack_Object = MibTableColumn
rosMgmtOpticalTransceiverUserLineLoopBack = _RosMgmtOpticalTransceiverUserLineLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 9),
    _RosMgmtOpticalTransceiverUserLineLoopBack_Type()
)
rosMgmtOpticalTransceiverUserLineLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverUserLineLoopBack.setStatus("current")


class _RosMgmtOpticalTransceiverUserXFILoopBack_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverUserXFILoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("xfiLoopback", 2))
    )


_RosMgmtOpticalTransceiverUserXFILoopBack_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverUserXFILoopBack_Object = MibTableColumn
rosMgmtOpticalTransceiverUserXFILoopBack = _RosMgmtOpticalTransceiverUserXFILoopBack_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 10),
    _RosMgmtOpticalTransceiverUserXFILoopBack_Type()
)
rosMgmtOpticalTransceiverUserXFILoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverUserXFILoopBack.setStatus("current")


class _RosMgmtOpticalTransceiverPortNotifyEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverPortNotifyEnable based on EnableVar"""
    defaultValue = 1


_RosMgmtOpticalTransceiverPortNotifyEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverPortNotifyEnable_Object = MibTableColumn
rosMgmtOpticalTransceiverPortNotifyEnable = _RosMgmtOpticalTransceiverPortNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 11),
    _RosMgmtOpticalTransceiverPortNotifyEnable_Type()
)
rosMgmtOpticalTransceiverPortNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPortNotifyEnable.setStatus("current")


class _RosMgmtOpticalTransceiverPortDDMEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverPortDDMEnable based on EnableVar"""
    defaultValue = 1


_RosMgmtOpticalTransceiverPortDDMEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverPortDDMEnable_Object = MibTableColumn
rosMgmtOpticalTransceiverPortDDMEnable = _RosMgmtOpticalTransceiverPortDDMEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 12),
    _RosMgmtOpticalTransceiverPortDDMEnable_Type()
)
rosMgmtOpticalTransceiverPortDDMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPortDDMEnable.setStatus("current")


class _RosMgmtOpticalTransceiverPortCheckPwdEnable_Type(EnableVar):
    """Custom type rosMgmtOpticalTransceiverPortCheckPwdEnable based on EnableVar"""
    defaultValue = 1


_RosMgmtOpticalTransceiverPortCheckPwdEnable_Type.__name__ = "EnableVar"
_RosMgmtOpticalTransceiverPortCheckPwdEnable_Object = MibTableColumn
rosMgmtOpticalTransceiverPortCheckPwdEnable = _RosMgmtOpticalTransceiverPortCheckPwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 13),
    _RosMgmtOpticalTransceiverPortCheckPwdEnable_Type()
)
rosMgmtOpticalTransceiverPortCheckPwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPortCheckPwdEnable.setStatus("current")
_RosMgmtOpticalTransceiverTxFaultCount_Type = Integer32
_RosMgmtOpticalTransceiverTxFaultCount_Object = MibTableColumn
rosMgmtOpticalTransceiverTxFaultCount = _RosMgmtOpticalTransceiverTxFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 14),
    _RosMgmtOpticalTransceiverTxFaultCount_Type()
)
rosMgmtOpticalTransceiverTxFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTxFaultCount.setStatus("current")
_RosMgmtOpticalTransceiverTxFaultCountClear_Type = TruthValue
_RosMgmtOpticalTransceiverTxFaultCountClear_Object = MibTableColumn
rosMgmtOpticalTransceiverTxFaultCountClear = _RosMgmtOpticalTransceiverTxFaultCountClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 15),
    _RosMgmtOpticalTransceiverTxFaultCountClear_Type()
)
rosMgmtOpticalTransceiverTxFaultCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTxFaultCountClear.setStatus("current")


class _RosMgmtOpticalTransceiverSpecificationCheckStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverSpecificationCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("accord", 1),
          ("notaccord", 2))
    )


_RosMgmtOpticalTransceiverSpecificationCheckStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverSpecificationCheckStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverSpecificationCheckStatus = _RosMgmtOpticalTransceiverSpecificationCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 16),
    _RosMgmtOpticalTransceiverSpecificationCheckStatus_Type()
)
rosMgmtOpticalTransceiverSpecificationCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverSpecificationCheckStatus.setStatus("current")


class _RosMgmtOpticalTransceiverTxFaultStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverTxFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("txfault", 2))
    )


_RosMgmtOpticalTransceiverTxFaultStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverTxFaultStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverTxFaultStatus = _RosMgmtOpticalTransceiverTxFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 17),
    _RosMgmtOpticalTransceiverTxFaultStatus_Type()
)
rosMgmtOpticalTransceiverTxFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTxFaultStatus.setStatus("current")
_RosMgmtOpticalTransceiverPortCRCCheckEnable_Type = EnableVar
_RosMgmtOpticalTransceiverPortCRCCheckEnable_Object = MibTableColumn
rosMgmtOpticalTransceiverPortCRCCheckEnable = _RosMgmtOpticalTransceiverPortCRCCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 18),
    _RosMgmtOpticalTransceiverPortCRCCheckEnable_Type()
)
rosMgmtOpticalTransceiverPortCRCCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPortCRCCheckEnable.setStatus("current")


class _RosMgmtOpticalTransceiverBaseCRCCheckStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverBaseCRCCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pass", 1),
          ("notpass", 2))
    )


_RosMgmtOpticalTransceiverBaseCRCCheckStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverBaseCRCCheckStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverBaseCRCCheckStatus = _RosMgmtOpticalTransceiverBaseCRCCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 19),
    _RosMgmtOpticalTransceiverBaseCRCCheckStatus_Type()
)
rosMgmtOpticalTransceiverBaseCRCCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverBaseCRCCheckStatus.setStatus("current")


class _RosMgmtOpticalTransceiverStaticDdmCRCCheckStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverStaticDdmCRCCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pass", 1),
          ("notpass", 2))
    )


_RosMgmtOpticalTransceiverStaticDdmCRCCheckStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverStaticDdmCRCCheckStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverStaticDdmCRCCheckStatus = _RosMgmtOpticalTransceiverStaticDdmCRCCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 20),
    _RosMgmtOpticalTransceiverStaticDdmCRCCheckStatus_Type()
)
rosMgmtOpticalTransceiverStaticDdmCRCCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverStaticDdmCRCCheckStatus.setStatus("current")


class _RosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus_Type(Integer32):
    """Custom type rosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pass", 1),
          ("notpass", 2))
    )


_RosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus_Type.__name__ = "Integer32"
_RosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus_Object = MibTableColumn
rosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus = _RosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 1, 2, 4, 1, 1, 21),
    _RosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus_Type()
)
rosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus.setStatus("current")
_RosMgmtOpticalTransceiverConformance_ObjectIdentity = ObjectIdentity
rosMgmtOpticalTransceiverConformance = _RosMgmtOpticalTransceiverConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 2)
)

# Managed Objects groups


# Notification objects

rosMgmtOpticalTransceiverAbsentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 1)
)
rosMgmtOpticalTransceiverAbsentTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverHwInfoAbsStatus"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverSpecificationCheckStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverAbsentTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverPresentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 2)
)
rosMgmtOpticalTransceiverPresentTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverHwInfoAbsStatus"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverSpecificationCheckStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverPresentTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverNRAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 3)
)
rosMgmtOpticalTransceiverNRAlarmTrap.setObjects(
    ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverHwInfoNRStatus")
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverNRAlarmTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverNRNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 4)
)
rosMgmtOpticalTransceiverNRNormalTrap.setObjects(
    ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverHwInfoNRStatus")
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverNRNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverRxLosAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 5)
)
rosMgmtOpticalTransceiverRxLosAlarmTrap.setObjects(
    ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverHwInfoRxLosStatus")
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverRxLosAlarmTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverRxLosNormaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 6)
)
rosMgmtOpticalTransceiverRxLosNormaTrap.setObjects(
    ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverHwInfoRxLosStatus")
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverRxLosNormaTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 7)
)
rosMgmtOpticalTransceiverParamAlarmTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamAlarmTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamAlarmNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 8)
)
rosMgmtOpticalTransceiverParamAlarmNormalTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamAlarmNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 9)
)
rosMgmtOpticalTransceiverParamWarningTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamWarningTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamWarningNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 10)
)
rosMgmtOpticalTransceiverParamWarningNormalTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamWarningNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverLaserBackLightAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 11)
)
rosMgmtOpticalTransceiverLaserBackLightAlarmTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverLaserBackLightAlarmTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverLaserBackLightAlarmNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 12)
)
rosMgmtOpticalTransceiverLaserBackLightAlarmNormalTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverLaserBackLightAlarmNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverLaserLifeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 13)
)
rosMgmtOpticalTransceiverLaserLifeAlarmTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverLaserLifeAlarmTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverLaserLifeAlarmNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 14)
)
rosMgmtOpticalTransceiverLaserLifeAlarmNormalTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverLaserLifeAlarmNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamLowAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 15)
)
rosMgmtOpticalTransceiverParamLowAlarmTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamLowAlarmTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamLowAlarmNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 16)
)
rosMgmtOpticalTransceiverParamLowAlarmNormalTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamLowAlarmNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamLowWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 17)
)
rosMgmtOpticalTransceiverParamLowWarningTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamLowWarningTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverParamLowWarningNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 18)
)
rosMgmtOpticalTransceiverParamLowWarningNormalTrap.setObjects(
      *(("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParameterValue"),
        ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverParamAlarmStatus"))
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverParamLowWarningNormalTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverTxFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 19)
)
rosMgmtOpticalTransceiverTxFaultTrap.setObjects(
    ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverTxFaultStatus")
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTxFaultTrap.setStatus(
        "current"
    )

rosMgmtOpticalTransceiverTxNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 18, 0, 20)
)
rosMgmtOpticalTransceiverTxNormalTrap.setObjects(
    ("ROSMGMT-OPTICAL-TRANSCEIVER-MIB", "rosMgmtOpticalTransceiverTxFaultStatus")
)
if mibBuilder.loadTexts:
    rosMgmtOpticalTransceiverTxNormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-OPTICAL-TRANSCEIVER-MIB",
    **{"EnableVar": EnableVar,
       "OpticalParameterType": OpticalParameterType,
       "OpticalParameterValue": OpticalParameterValue,
       "OpticalPMPeriod": OpticalPMPeriod,
       "rosMgmtOpticalTransceiver": rosMgmtOpticalTransceiver,
       "rosMgmtOpticalTransceiverNotifications": rosMgmtOpticalTransceiverNotifications,
       "rosMgmtOpticalTransceiverAbsentTrap": rosMgmtOpticalTransceiverAbsentTrap,
       "rosMgmtOpticalTransceiverPresentTrap": rosMgmtOpticalTransceiverPresentTrap,
       "rosMgmtOpticalTransceiverNRAlarmTrap": rosMgmtOpticalTransceiverNRAlarmTrap,
       "rosMgmtOpticalTransceiverNRNormalTrap": rosMgmtOpticalTransceiverNRNormalTrap,
       "rosMgmtOpticalTransceiverRxLosAlarmTrap": rosMgmtOpticalTransceiverRxLosAlarmTrap,
       "rosMgmtOpticalTransceiverRxLosNormaTrap": rosMgmtOpticalTransceiverRxLosNormaTrap,
       "rosMgmtOpticalTransceiverParamAlarmTrap": rosMgmtOpticalTransceiverParamAlarmTrap,
       "rosMgmtOpticalTransceiverParamAlarmNormalTrap": rosMgmtOpticalTransceiverParamAlarmNormalTrap,
       "rosMgmtOpticalTransceiverParamWarningTrap": rosMgmtOpticalTransceiverParamWarningTrap,
       "rosMgmtOpticalTransceiverParamWarningNormalTrap": rosMgmtOpticalTransceiverParamWarningNormalTrap,
       "rosMgmtOpticalTransceiverLaserBackLightAlarmTrap": rosMgmtOpticalTransceiverLaserBackLightAlarmTrap,
       "rosMgmtOpticalTransceiverLaserBackLightAlarmNormalTrap": rosMgmtOpticalTransceiverLaserBackLightAlarmNormalTrap,
       "rosMgmtOpticalTransceiverLaserLifeAlarmTrap": rosMgmtOpticalTransceiverLaserLifeAlarmTrap,
       "rosMgmtOpticalTransceiverLaserLifeAlarmNormalTrap": rosMgmtOpticalTransceiverLaserLifeAlarmNormalTrap,
       "rosMgmtOpticalTransceiverParamLowAlarmTrap": rosMgmtOpticalTransceiverParamLowAlarmTrap,
       "rosMgmtOpticalTransceiverParamLowAlarmNormalTrap": rosMgmtOpticalTransceiverParamLowAlarmNormalTrap,
       "rosMgmtOpticalTransceiverParamLowWarningTrap": rosMgmtOpticalTransceiverParamLowWarningTrap,
       "rosMgmtOpticalTransceiverParamLowWarningNormalTrap": rosMgmtOpticalTransceiverParamLowWarningNormalTrap,
       "rosMgmtOpticalTransceiverTxFaultTrap": rosMgmtOpticalTransceiverTxFaultTrap,
       "rosMgmtOpticalTransceiverTxNormalTrap": rosMgmtOpticalTransceiverTxNormalTrap,
       "rosMgmtOpticalTransceiverObjects": rosMgmtOpticalTransceiverObjects,
       "rosMgmtOpticalTransceiverScalarGroup": rosMgmtOpticalTransceiverScalarGroup,
       "rosMgmtOpticalTransceiverNotifyEnable": rosMgmtOpticalTransceiverNotifyEnable,
       "rosMgmtOpticalTransceiverDDMEnable": rosMgmtOpticalTransceiverDDMEnable,
       "rosMgmtOpticalTransceiverCheckPwdEnable": rosMgmtOpticalTransceiverCheckPwdEnable,
       "rosMgmtOpticalTransceiverPollInterval": rosMgmtOpticalTransceiverPollInterval,
       "rosMgmtOpticalTransceiverCRCCheckEnable": rosMgmtOpticalTransceiverCRCCheckEnable,
       "rosMgmtOpticalTransceiverCfgObjects": rosMgmtOpticalTransceiverCfgObjects,
       "rosMgmtOpticalTransceiverInfoGroup": rosMgmtOpticalTransceiverInfoGroup,
       "rosMgmtOpticalTransceiverInfoTable": rosMgmtOpticalTransceiverInfoTable,
       "rosMgmtOpticalTransceiverInfoEntry": rosMgmtOpticalTransceiverInfoEntry,
       "rosMgmtOpticalTransceiverType": rosMgmtOpticalTransceiverType,
       "rosMgmtOpticalTransceiverConnectorType": rosMgmtOpticalTransceiverConnectorType,
       "rosMgmtOpticalTransceiverVendorName": rosMgmtOpticalTransceiverVendorName,
       "rosMgmtOpticalTransceiverVendorPN": rosMgmtOpticalTransceiverVendorPN,
       "rosMgmtOpticalTransceiverVendorSN": rosMgmtOpticalTransceiverVendorSN,
       "rosMgmtOpticalTransceiverMediaType": rosMgmtOpticalTransceiverMediaType,
       "rosMgmtOpticalTransceiverTransmissionDistance": rosMgmtOpticalTransceiverTransmissionDistance,
       "rosMgmtOpticalTransceiverAbility": rosMgmtOpticalTransceiverAbility,
       "rosMgmtOpticalTransceiverDDM": rosMgmtOpticalTransceiverDDM,
       "rosMgmtOpticalTransceiverCalibrationType": rosMgmtOpticalTransceiverCalibrationType,
       "rosMgmtOpticalTransceiverRSSI": rosMgmtOpticalTransceiverRSSI,
       "rosMgmtOpticalTransceiverVendorRev": rosMgmtOpticalTransceiverVendorRev,
       "rosMgmtOpticalTransceiverBRMax": rosMgmtOpticalTransceiverBRMax,
       "rosMgmtOpticalTransceiverBRMin": rosMgmtOpticalTransceiverBRMin,
       "rosMgmtOpticalTransceiverWavelengthContrl": rosMgmtOpticalTransceiverWavelengthContrl,
       "rosMgmtOpticalTransceiverWavelength": rosMgmtOpticalTransceiverWavelength,
       "rosMgmtOpticalTransceiverWaveTolerance": rosMgmtOpticalTransceiverWaveTolerance,
       "rosMgmtOpticalTransceiverCompatibility": rosMgmtOpticalTransceiverCompatibility,
       "rosMgmtOpticalTransceiverPowerDissipation": rosMgmtOpticalTransceiverPowerDissipation,
       "rosMgmtOpticalTransceiverCDR": rosMgmtOpticalTransceiverCDR,
       "rosMgmtOpticalTransceiverRefClock": rosMgmtOpticalTransceiverRefClock,
       "rosMgmtOpticalTransceiverTransmitterType": rosMgmtOpticalTransceiverTransmitterType,
       "rosMgmtOpticalTransceiverCooled": rosMgmtOpticalTransceiverCooled,
       "rosMgmtOpticalTransceiverTunalbe": rosMgmtOpticalTransceiverTunalbe,
       "rosMgmtOpticalTransceiverDetectorType": rosMgmtOpticalTransceiverDetectorType,
       "rosMgmtOpticalTransceiverLineLoopBack": rosMgmtOpticalTransceiverLineLoopBack,
       "rosMgmtOpticalTransceiverXFILoopBack": rosMgmtOpticalTransceiverXFILoopBack,
       "rosMgmtOpticalTransceiverVps": rosMgmtOpticalTransceiverVps,
       "rosMgmtOpticalTransceiverTxDis": rosMgmtOpticalTransceiverTxDis,
       "rosMgmtOpticalTransceiverStandby": rosMgmtOpticalTransceiverStandby,
       "rosMgmtOpticalTransceiverInVpsLowPower": rosMgmtOpticalTransceiverInVpsLowPower,
       "rosMgmtOpticalTransceiverOutVpsLowPower": rosMgmtOpticalTransceiverOutVpsLowPower,
       "rosMgmtOpticalTransceiverFEC": rosMgmtOpticalTransceiverFEC,
       "rosMgmtOpticalTransceiverCMU": rosMgmtOpticalTransceiverCMU,
       "rosMgmtOpticalTransceiverBR": rosMgmtOpticalTransceiverBR,
       "rosMgmtOpticalTransceiverDDMGroup": rosMgmtOpticalTransceiverDDMGroup,
       "rosMgmtOpticalTransceiverDDMTable": rosMgmtOpticalTransceiverDDMTable,
       "rosMgmtOpticalTransceiverDDMEntry": rosMgmtOpticalTransceiverDDMEntry,
       "rosMgmtOpticalTransceiverParameterType": rosMgmtOpticalTransceiverParameterType,
       "rosMgmtOpticalTransceiverParameterValue": rosMgmtOpticalTransceiverParameterValue,
       "rosMgmtOpticalTransceiverParamHighAlarmThresh": rosMgmtOpticalTransceiverParamHighAlarmThresh,
       "rosMgmtOpticalTransceiverParamHighWarningThresh": rosMgmtOpticalTransceiverParamHighWarningThresh,
       "rosMgmtOpticalTransceiverParamLowAlarmThresh": rosMgmtOpticalTransceiverParamLowAlarmThresh,
       "rosMgmtOpticalTransceiverParamLowWarningThresh": rosMgmtOpticalTransceiverParamLowWarningThresh,
       "rosMgmtOpticalTransceiverParamAlarmStatus": rosMgmtOpticalTransceiverParamAlarmStatus,
       "rosMgmtOpticalTransceiverParamAlarmLastValue": rosMgmtOpticalTransceiverParamAlarmLastValue,
       "rosMgmtOpticalTransceiverParamAlarmLastChange": rosMgmtOpticalTransceiverParamAlarmLastChange,
       "rosMgmtOpticalTransceiverDDM15MinValidIntervals": rosMgmtOpticalTransceiverDDM15MinValidIntervals,
       "rosMgmtOpticalTransceiverDDM24HrValidIntervals": rosMgmtOpticalTransceiverDDM24HrValidIntervals,
       "rosMgmtOpticalTransceiverDDMValidStatus": rosMgmtOpticalTransceiverDDMValidStatus,
       "rosMgmtOpticalTransceiverQsfpParameterValue": rosMgmtOpticalTransceiverQsfpParameterValue,
       "rosMgmtOpticalTransceiverQsfpParamHighAlarmThresh": rosMgmtOpticalTransceiverQsfpParamHighAlarmThresh,
       "rosMgmtOpticalTransceiverQsfpParamHighWarningThresh": rosMgmtOpticalTransceiverQsfpParamHighWarningThresh,
       "rosMgmtOpticalTransceiverQsfpParamLowAlarmThresh": rosMgmtOpticalTransceiverQsfpParamLowAlarmThresh,
       "rosMgmtOpticalTransceiverQsfpParamLowWarningThresh": rosMgmtOpticalTransceiverQsfpParamLowWarningThresh,
       "rosMgmtOpticalTransceiverQsfpParamAlarmStatus": rosMgmtOpticalTransceiverQsfpParamAlarmStatus,
       "rosMgmtOpticalTransceiverQsfpParamAlarmLastValue": rosMgmtOpticalTransceiverQsfpParamAlarmLastValue,
       "rosMgmtOpticalTransceiverQsfpParamAlarmLastChange": rosMgmtOpticalTransceiverQsfpParamAlarmLastChange,
       "rosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals": rosMgmtOpticalTransceiverQsfpDDM15MinValidIntervals,
       "rosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals": rosMgmtOpticalTransceiverQsfpDDM24HrValidIntervals,
       "rosMgmtOpticalTransceiverQsfpDDMValidStatus": rosMgmtOpticalTransceiverQsfpDDMValidStatus,
       "rosMgmtOpticalTransceiverPMGroup": rosMgmtOpticalTransceiverPMGroup,
       "rosMgmtOpticalTransceiverPMCurrentTable": rosMgmtOpticalTransceiverPMCurrentTable,
       "rosMgmtOpticalTransceiverPMCurrentEntry": rosMgmtOpticalTransceiverPMCurrentEntry,
       "rosMgmtOpticalTransceiverPMCurrentPeriod": rosMgmtOpticalTransceiverPMCurrentPeriod,
       "rosMgmtOpticalTransceiverPMCurrentParamType": rosMgmtOpticalTransceiverPMCurrentParamType,
       "rosMgmtOpticalTransceiverPMCurrentMaxParam": rosMgmtOpticalTransceiverPMCurrentMaxParam,
       "rosMgmtOpticalTransceiverPMCurrentMinParam": rosMgmtOpticalTransceiverPMCurrentMinParam,
       "rosMgmtOpticalTransceiverPMCurrentMeanParam": rosMgmtOpticalTransceiverPMCurrentMeanParam,
       "rosMgmtOpticalTransceiverQsfpPMCurrentMaxParam": rosMgmtOpticalTransceiverQsfpPMCurrentMaxParam,
       "rosMgmtOpticalTransceiverQsfpPMCurrentMinParam": rosMgmtOpticalTransceiverQsfpPMCurrentMinParam,
       "rosMgmtOpticalTransceiverQsfpPMCurrentMeanParam": rosMgmtOpticalTransceiverQsfpPMCurrentMeanParam,
       "rosMgmtOpticalTransceiverPMIntervalTable": rosMgmtOpticalTransceiverPMIntervalTable,
       "rosMgmtOpticalTransceiverPMIntervalEntry": rosMgmtOpticalTransceiverPMIntervalEntry,
       "rosMgmtOpticalTransceiverPMIntervalPeriod": rosMgmtOpticalTransceiverPMIntervalPeriod,
       "rosMgmtOpticalTransceiverPMIntervalNumber": rosMgmtOpticalTransceiverPMIntervalNumber,
       "rosMgmtOpticalTransceiverPMIntervalParamType": rosMgmtOpticalTransceiverPMIntervalParamType,
       "rosMgmtOpticalTransceiverPMIntervalMaxParam": rosMgmtOpticalTransceiverPMIntervalMaxParam,
       "rosMgmtOpticalTransceiverPMIntervalMinParam": rosMgmtOpticalTransceiverPMIntervalMinParam,
       "rosMgmtOpticalTransceiverPMIntervalMeanParam": rosMgmtOpticalTransceiverPMIntervalMeanParam,
       "rosMgmtOpticalTransceiverQsfpPMIntervalMaxParam": rosMgmtOpticalTransceiverQsfpPMIntervalMaxParam,
       "rosMgmtOpticalTransceiverQsfpPMIntervalMinParam": rosMgmtOpticalTransceiverQsfpPMIntervalMinParam,
       "rosMgmtOpticalTransceiverQsfpPMIntervalMeanParam": rosMgmtOpticalTransceiverQsfpPMIntervalMeanParam,
       "rosMgmtOpticalTransceiverStatusGroup": rosMgmtOpticalTransceiverStatusGroup,
       "rosMgmtOpticalTransceiverCurrentStatusTable": rosMgmtOpticalTransceiverCurrentStatusTable,
       "rosMgmtOpticalTransceiverCurrentStatusEntry": rosMgmtOpticalTransceiverCurrentStatusEntry,
       "rosMgmtOpticalTransceiverHwInfoAbsStatus": rosMgmtOpticalTransceiverHwInfoAbsStatus,
       "rosMgmtOpticalTransceiverHwInfoNRStatus": rosMgmtOpticalTransceiverHwInfoNRStatus,
       "rosMgmtOpticalTransceiverHwInfoRxLosStatus": rosMgmtOpticalTransceiverHwInfoRxLosStatus,
       "rosMgmtOpticalTransceiverHwInfoStandby": rosMgmtOpticalTransceiverHwInfoStandby,
       "rosMgmtOpticalTransceiverHwInfoLaser": rosMgmtOpticalTransceiverHwInfoLaser,
       "rosMgmtOpticalTransceiverWaveLengthError": rosMgmtOpticalTransceiverWaveLengthError,
       "rosMgmtOpticalTransceiverUserWaveLength": rosMgmtOpticalTransceiverUserWaveLength,
       "rosMgmtOpticalTransceiverUserDataRate": rosMgmtOpticalTransceiverUserDataRate,
       "rosMgmtOpticalTransceiverUserLineLoopBack": rosMgmtOpticalTransceiverUserLineLoopBack,
       "rosMgmtOpticalTransceiverUserXFILoopBack": rosMgmtOpticalTransceiverUserXFILoopBack,
       "rosMgmtOpticalTransceiverPortNotifyEnable": rosMgmtOpticalTransceiverPortNotifyEnable,
       "rosMgmtOpticalTransceiverPortDDMEnable": rosMgmtOpticalTransceiverPortDDMEnable,
       "rosMgmtOpticalTransceiverPortCheckPwdEnable": rosMgmtOpticalTransceiverPortCheckPwdEnable,
       "rosMgmtOpticalTransceiverTxFaultCount": rosMgmtOpticalTransceiverTxFaultCount,
       "rosMgmtOpticalTransceiverTxFaultCountClear": rosMgmtOpticalTransceiverTxFaultCountClear,
       "rosMgmtOpticalTransceiverSpecificationCheckStatus": rosMgmtOpticalTransceiverSpecificationCheckStatus,
       "rosMgmtOpticalTransceiverTxFaultStatus": rosMgmtOpticalTransceiverTxFaultStatus,
       "rosMgmtOpticalTransceiverPortCRCCheckEnable": rosMgmtOpticalTransceiverPortCRCCheckEnable,
       "rosMgmtOpticalTransceiverBaseCRCCheckStatus": rosMgmtOpticalTransceiverBaseCRCCheckStatus,
       "rosMgmtOpticalTransceiverStaticDdmCRCCheckStatus": rosMgmtOpticalTransceiverStaticDdmCRCCheckStatus,
       "rosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus": rosMgmtOpticalTransceiverDynamicDdmCRCCheckStatus,
       "rosMgmtOpticalTransceiverConformance": rosMgmtOpticalTransceiverConformance}
)
