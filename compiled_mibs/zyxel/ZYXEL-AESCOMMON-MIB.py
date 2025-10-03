# SNMP MIB module (ZYXEL-AESCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-AESCOMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:50 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(aesSeriesCommon,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "aesSeriesCommon")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AesMaxNumOfProfiles_Type = Integer32
_AesMaxNumOfProfiles_Object = MibScalar
aesMaxNumOfProfiles = _AesMaxNumOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 1),
    _AesMaxNumOfProfiles_Type()
)
aesMaxNumOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesMaxNumOfProfiles.setStatus("mandatory")
_AesLineConfTable_Object = MibTable
aesLineConfTable = _AesLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2)
)
if mibBuilder.loadTexts:
    aesLineConfTable.setStatus("mandatory")
_AesLineConfEntry_Object = MibTableRow
aesLineConfEntry = _AesLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1)
)
aesLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aesLineConfEntry.setStatus("mandatory")


class _AesLineConfAdslMode_Type(Integer32):
    """Custom type aesLineConfAdslMode based on Integer32"""
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
        *(("gDotLite", 1),
          ("gDotDmt", 2),
          ("t1Dot413", 3),
          ("auto", 4),
          ("etsi", 5),
          ("adsl2", 6),
          ("adsl2Plus", 7))
    )


_AesLineConfAdslMode_Type.__name__ = "Integer32"
_AesLineConfAdslMode_Object = MibTableColumn
aesLineConfAdslMode = _AesLineConfAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 1),
    _AesLineConfAdslMode_Type()
)
aesLineConfAdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfAdslMode.setStatus("mandatory")


class _AesLineConfEncap_Type(Integer32):
    """Custom type aesLineConfEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_AesLineConfEncap_Type.__name__ = "Integer32"
_AesLineConfEncap_Object = MibTableColumn
aesLineConfEncap = _AesLineConfEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 2),
    _AesLineConfEncap_Type()
)
aesLineConfEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfEncap.setStatus("mandatory")
_AesLineConfVpi_Type = Integer32
_AesLineConfVpi_Object = MibTableColumn
aesLineConfVpi = _AesLineConfVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 3),
    _AesLineConfVpi_Type()
)
aesLineConfVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfVpi.setStatus("mandatory")
_AesLineConfVci_Type = Integer32
_AesLineConfVci_Object = MibTableColumn
aesLineConfVci = _AesLineConfVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 4),
    _AesLineConfVci_Type()
)
aesLineConfVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfVci.setStatus("mandatory")


class _AesLineConfAnnexL_Type(Integer32):
    """Custom type aesLineConfAnnexL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableNarrowMode", 1),
          ("enableWideMode", 2),
          ("disable", 3))
    )


_AesLineConfAnnexL_Type.__name__ = "Integer32"
_AesLineConfAnnexL_Object = MibTableColumn
aesLineConfAnnexL = _AesLineConfAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 5),
    _AesLineConfAnnexL_Type()
)
aesLineConfAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfAnnexL.setStatus("mandatory")


class _AesLineConfPmMode_Type(Integer32):
    """Custom type aesLineConfPmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableL2Mode", 1),
          ("enableL3Mode", 2),
          ("disable", 3))
    )


_AesLineConfPmMode_Type.__name__ = "Integer32"
_AesLineConfPmMode_Object = MibTableColumn
aesLineConfPmMode = _AesLineConfPmMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 6),
    _AesLineConfPmMode_Type()
)
aesLineConfPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfPmMode.setStatus("mandatory")


class _AesLineConfRateMode_Type(Integer32):
    """Custom type aesLineConfRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("adaptAtStartup", 2),
          ("adaptAtRuntime", 3))
    )


_AesLineConfRateMode_Type.__name__ = "Integer32"
_AesLineConfRateMode_Object = MibTableColumn
aesLineConfRateMode = _AesLineConfRateMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 7),
    _AesLineConfRateMode_Type()
)
aesLineConfRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfRateMode.setStatus("mandatory")


class _AesLineConfAnnexM_Type(Integer32):
    """Custom type aesLineConfAnnexM based on Integer32"""
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


_AesLineConfAnnexM_Type.__name__ = "Integer32"
_AesLineConfAnnexM_Object = MibTableColumn
aesLineConfAnnexM = _AesLineConfAnnexM_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 2, 1, 8),
    _AesLineConfAnnexM_Type()
)
aesLineConfAnnexM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfAnnexM.setStatus("mandatory")
_AesLineDiagnostic_ObjectIdentity = ObjectIdentity
aesLineDiagnostic = _AesLineDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3)
)
_AesAtucLineDiagLATN_Type = Integer32
_AesAtucLineDiagLATN_Object = MibScalar
aesAtucLineDiagLATN = _AesAtucLineDiagLATN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 1),
    _AesAtucLineDiagLATN_Type()
)
aesAtucLineDiagLATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagLATN.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAtucLineDiagLATN.setUnits("tenth dB")
_AesAtucLineDiagSATN_Type = Integer32
_AesAtucLineDiagSATN_Object = MibScalar
aesAtucLineDiagSATN = _AesAtucLineDiagSATN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 2),
    _AesAtucLineDiagSATN_Type()
)
aesAtucLineDiagSATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagSATN.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAtucLineDiagSATN.setUnits("tenth dB")
_AesAtucLineDiagSNRM_Type = Integer32
_AesAtucLineDiagSNRM_Object = MibScalar
aesAtucLineDiagSNRM = _AesAtucLineDiagSNRM_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 3),
    _AesAtucLineDiagSNRM_Type()
)
aesAtucLineDiagSNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagSNRM.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAtucLineDiagSNRM.setUnits("tenth dB")
_AesAtucLineDiagACTATP_Type = Integer32
_AesAtucLineDiagACTATP_Object = MibScalar
aesAtucLineDiagACTATP = _AesAtucLineDiagACTATP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 4),
    _AesAtucLineDiagACTATP_Type()
)
aesAtucLineDiagACTATP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagACTATP.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAtucLineDiagACTATP.setUnits("tenth dB")
_AesAtucLineDiagATTNDR_Type = Unsigned32
_AesAtucLineDiagATTNDR_Object = MibScalar
aesAtucLineDiagATTNDR = _AesAtucLineDiagATTNDR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 5),
    _AesAtucLineDiagATTNDR_Type()
)
aesAtucLineDiagATTNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagATTNDR.setStatus("mandatory")
_AesAturLineDiagLATN_Type = Integer32
_AesAturLineDiagLATN_Object = MibScalar
aesAturLineDiagLATN = _AesAturLineDiagLATN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 6),
    _AesAturLineDiagLATN_Type()
)
aesAturLineDiagLATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagLATN.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAturLineDiagLATN.setUnits("tenth dB")
_AesAturLineDiagSATN_Type = Integer32
_AesAturLineDiagSATN_Object = MibScalar
aesAturLineDiagSATN = _AesAturLineDiagSATN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 7),
    _AesAturLineDiagSATN_Type()
)
aesAturLineDiagSATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagSATN.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAturLineDiagSATN.setUnits("tenth dB")
_AesAturLineDiagSNRM_Type = Integer32
_AesAturLineDiagSNRM_Object = MibScalar
aesAturLineDiagSNRM = _AesAturLineDiagSNRM_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 8),
    _AesAturLineDiagSNRM_Type()
)
aesAturLineDiagSNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagSNRM.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAturLineDiagSNRM.setUnits("tenth dB")
_AesAturLineDiagACTATP_Type = Integer32
_AesAturLineDiagACTATP_Object = MibScalar
aesAturLineDiagACTATP = _AesAturLineDiagACTATP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 9),
    _AesAturLineDiagACTATP_Type()
)
aesAturLineDiagACTATP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagACTATP.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesAturLineDiagACTATP.setUnits("tenth dB")
_AesAturLineDiagATTNDR_Type = Unsigned32
_AesAturLineDiagATTNDR_Object = MibScalar
aesAturLineDiagATTNDR = _AesAturLineDiagATTNDR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 10),
    _AesAturLineDiagATTNDR_Type()
)
aesAturLineDiagATTNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagATTNDR.setStatus("mandatory")
_AesLineDiagTarget_Type = Integer32
_AesLineDiagTarget_Object = MibScalar
aesLineDiagTarget = _AesLineDiagTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 11),
    _AesLineDiagTarget_Type()
)
aesLineDiagTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineDiagTarget.setStatus("mandatory")
_AesLineDiagOps_Type = Integer32
_AesLineDiagOps_Object = MibScalar
aesLineDiagOps = _AesLineDiagOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 12),
    _AesLineDiagOps_Type()
)
aesLineDiagOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineDiagOps.setStatus("mandatory")
_AesLineDiagFailReason_Type = DisplayString
_AesLineDiagFailReason_Object = MibScalar
aesLineDiagFailReason = _AesLineDiagFailReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 3, 13),
    _AesLineDiagFailReason_Type()
)
aesLineDiagFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagFailReason.setStatus("mandatory")
_AesLineDiagPs_ObjectIdentity = ObjectIdentity
aesLineDiagPs = _AesLineDiagPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4)
)
_AesAtucNumOfSubcarriersPerPort_Type = Integer32
_AesAtucNumOfSubcarriersPerPort_Object = MibScalar
aesAtucNumOfSubcarriersPerPort = _AesAtucNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 1),
    _AesAtucNumOfSubcarriersPerPort_Type()
)
aesAtucNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucNumOfSubcarriersPerPort.setStatus("mandatory")
_AesAturNumOfSubcarriersPerPort_Type = Integer32
_AesAturNumOfSubcarriersPerPort_Object = MibScalar
aesAturNumOfSubcarriersPerPort = _AesAturNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 2),
    _AesAturNumOfSubcarriersPerPort_Type()
)
aesAturNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturNumOfSubcarriersPerPort.setStatus("mandatory")
_AesLineDiagPsCCFLirl1_Type = OctetString
_AesLineDiagPsCCFLirl1_Object = MibScalar
aesLineDiagPsCCFLirl1 = _AesLineDiagPsCCFLirl1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 3),
    _AesLineDiagPsCCFLirl1_Type()
)
aesLineDiagPsCCFLirl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLirl1.setStatus("mandatory")
_AesLineDiagPsCCFLirl2_Type = OctetString
_AesLineDiagPsCCFLirl2_Object = MibScalar
aesLineDiagPsCCFLirl2 = _AesLineDiagPsCCFLirl2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 4),
    _AesLineDiagPsCCFLirl2_Type()
)
aesLineDiagPsCCFLirl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLirl2.setStatus("mandatory")
_AesLineDiagPsCCFLiim1_Type = OctetString
_AesLineDiagPsCCFLiim1_Object = MibScalar
aesLineDiagPsCCFLiim1 = _AesLineDiagPsCCFLiim1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 5),
    _AesLineDiagPsCCFLiim1_Type()
)
aesLineDiagPsCCFLiim1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLiim1.setStatus("mandatory")
_AesLineDiagPsCCFLiim2_Type = OctetString
_AesLineDiagPsCCFLiim2_Object = MibScalar
aesLineDiagPsCCFLiim2 = _AesLineDiagPsCCFLiim2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 6),
    _AesLineDiagPsCCFLiim2_Type()
)
aesLineDiagPsCCFLiim2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLiim2.setStatus("mandatory")
_AesLineDiagPsCCFLog1_Type = OctetString
_AesLineDiagPsCCFLog1_Object = MibScalar
aesLineDiagPsCCFLog1 = _AesLineDiagPsCCFLog1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 7),
    _AesLineDiagPsCCFLog1_Type()
)
aesLineDiagPsCCFLog1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLog1.setStatus("mandatory")
_AesLineDiagPsCCFLog2_Type = OctetString
_AesLineDiagPsCCFLog2_Object = MibScalar
aesLineDiagPsCCFLog2 = _AesLineDiagPsCCFLog2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 8),
    _AesLineDiagPsCCFLog2_Type()
)
aesLineDiagPsCCFLog2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLog2.setStatus("mandatory")
_AesLineDiagPsQLN_Type = OctetString
_AesLineDiagPsQLN_Object = MibScalar
aesLineDiagPsQLN = _AesLineDiagPsQLN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 9),
    _AesLineDiagPsQLN_Type()
)
aesLineDiagPsQLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsQLN.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesLineDiagPsQLN.setUnits("tenth dB")
_AesLineDiagPsSNR_Type = OctetString
_AesLineDiagPsSNR_Object = MibScalar
aesLineDiagPsSNR = _AesLineDiagPsSNR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 4, 10),
    _AesLineDiagPsSNR_Type()
)
aesLineDiagPsSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsSNR.setStatus("mandatory")
if mibBuilder.loadTexts:
    aesLineDiagPsSNR.setUnits("tenth dB")
_AesMaxNumOfAlarmProfiles_Type = Integer32
_AesMaxNumOfAlarmProfiles_Object = MibScalar
aesMaxNumOfAlarmProfiles = _AesMaxNumOfAlarmProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 5),
    _AesMaxNumOfAlarmProfiles_Type()
)
aesMaxNumOfAlarmProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesMaxNumOfAlarmProfiles.setStatus("mandatory")
_AesBitLoadingTable_Object = MibTable
aesBitLoadingTable = _AesBitLoadingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 6)
)
if mibBuilder.loadTexts:
    aesBitLoadingTable.setStatus("mandatory")
_AesBitLoadingEntry_Object = MibTableRow
aesBitLoadingEntry = _AesBitLoadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 6, 1)
)
aesBitLoadingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aesBitLoadingEntry.setStatus("mandatory")
_AesBitLoadingBits_Type = OctetString
_AesBitLoadingBits_Object = MibTableColumn
aesBitLoadingBits = _AesBitLoadingBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 6, 1, 1),
    _AesBitLoadingBits_Type()
)
aesBitLoadingBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesBitLoadingBits.setStatus("mandatory")
_AesBitLoadingAtucNumOfCarriers_Type = Integer32
_AesBitLoadingAtucNumOfCarriers_Object = MibTableColumn
aesBitLoadingAtucNumOfCarriers = _AesBitLoadingAtucNumOfCarriers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 6, 1, 2),
    _AesBitLoadingAtucNumOfCarriers_Type()
)
aesBitLoadingAtucNumOfCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesBitLoadingAtucNumOfCarriers.setStatus("mandatory")
_AesBitLoadingAturNumOfCarriers_Type = Integer32
_AesBitLoadingAturNumOfCarriers_Object = MibTableColumn
aesBitLoadingAturNumOfCarriers = _AesBitLoadingAturNumOfCarriers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 6, 1, 3),
    _AesBitLoadingAturNumOfCarriers_Type()
)
aesBitLoadingAturNumOfCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesBitLoadingAturNumOfCarriers.setStatus("mandatory")
_AesLineStatusTable_Object = MibTable
aesLineStatusTable = _AesLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 7)
)
if mibBuilder.loadTexts:
    aesLineStatusTable.setStatus("mandatory")
_AesLineStatusEntry_Object = MibTableRow
aesLineStatusEntry = _AesLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 7, 1)
)
aesLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aesLineStatusEntry.setStatus("mandatory")


class _AesLineStatusAdslMode_Type(Integer32):
    """Custom type aesLineStatusAdslMode based on Integer32"""
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
        *(("gDotLite", 1),
          ("gDotDmt", 2),
          ("t1Dot413", 3),
          ("etsi", 4),
          ("adsl2", 5),
          ("adsl2Plus", 6))
    )


_AesLineStatusAdslMode_Type.__name__ = "Integer32"
_AesLineStatusAdslMode_Object = MibTableColumn
aesLineStatusAdslMode = _AesLineStatusAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 7, 1, 1),
    _AesLineStatusAdslMode_Type()
)
aesLineStatusAdslMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineStatusAdslMode.setStatus("mandatory")
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8, 3),
    _SeltStatus_Type()
)
seltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltStatus.setStatus("current")


class _SeltCableType_Type(Integer32):
    """Custom type seltCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("awg24", 1),
          ("awg26", 2))
    )


_SeltCableType_Type.__name__ = "Integer32"
_SeltCableType_Object = MibScalar
seltCableType = _SeltCableType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8, 5),
    _SeltLoopEstimateLengthFt_Type()
)
seltLoopEstimateLengthFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setUnits("feet")
_SeltLoopEstimateLengthMeter_Type = Integer32
_SeltLoopEstimateLengthMeter_Object = MibScalar
seltLoopEstimateLengthMeter = _SeltLoopEstimateLengthMeter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 11, 1, 8, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-AESCOMMON-MIB",
    **{"aesMaxNumOfProfiles": aesMaxNumOfProfiles,
       "aesLineConfTable": aesLineConfTable,
       "aesLineConfEntry": aesLineConfEntry,
       "aesLineConfAdslMode": aesLineConfAdslMode,
       "aesLineConfEncap": aesLineConfEncap,
       "aesLineConfVpi": aesLineConfVpi,
       "aesLineConfVci": aesLineConfVci,
       "aesLineConfAnnexL": aesLineConfAnnexL,
       "aesLineConfPmMode": aesLineConfPmMode,
       "aesLineConfRateMode": aesLineConfRateMode,
       "aesLineConfAnnexM": aesLineConfAnnexM,
       "aesLineDiagnostic": aesLineDiagnostic,
       "aesAtucLineDiagLATN": aesAtucLineDiagLATN,
       "aesAtucLineDiagSATN": aesAtucLineDiagSATN,
       "aesAtucLineDiagSNRM": aesAtucLineDiagSNRM,
       "aesAtucLineDiagACTATP": aesAtucLineDiagACTATP,
       "aesAtucLineDiagATTNDR": aesAtucLineDiagATTNDR,
       "aesAturLineDiagLATN": aesAturLineDiagLATN,
       "aesAturLineDiagSATN": aesAturLineDiagSATN,
       "aesAturLineDiagSNRM": aesAturLineDiagSNRM,
       "aesAturLineDiagACTATP": aesAturLineDiagACTATP,
       "aesAturLineDiagATTNDR": aesAturLineDiagATTNDR,
       "aesLineDiagTarget": aesLineDiagTarget,
       "aesLineDiagOps": aesLineDiagOps,
       "aesLineDiagFailReason": aesLineDiagFailReason,
       "aesLineDiagPs": aesLineDiagPs,
       "aesAtucNumOfSubcarriersPerPort": aesAtucNumOfSubcarriersPerPort,
       "aesAturNumOfSubcarriersPerPort": aesAturNumOfSubcarriersPerPort,
       "aesLineDiagPsCCFLirl1": aesLineDiagPsCCFLirl1,
       "aesLineDiagPsCCFLirl2": aesLineDiagPsCCFLirl2,
       "aesLineDiagPsCCFLiim1": aesLineDiagPsCCFLiim1,
       "aesLineDiagPsCCFLiim2": aesLineDiagPsCCFLiim2,
       "aesLineDiagPsCCFLog1": aesLineDiagPsCCFLog1,
       "aesLineDiagPsCCFLog2": aesLineDiagPsCCFLog2,
       "aesLineDiagPsQLN": aesLineDiagPsQLN,
       "aesLineDiagPsSNR": aesLineDiagPsSNR,
       "aesMaxNumOfAlarmProfiles": aesMaxNumOfAlarmProfiles,
       "aesBitLoadingTable": aesBitLoadingTable,
       "aesBitLoadingEntry": aesBitLoadingEntry,
       "aesBitLoadingBits": aesBitLoadingBits,
       "aesBitLoadingAtucNumOfCarriers": aesBitLoadingAtucNumOfCarriers,
       "aesBitLoadingAturNumOfCarriers": aesBitLoadingAturNumOfCarriers,
       "aesLineStatusTable": aesLineStatusTable,
       "aesLineStatusEntry": aesLineStatusEntry,
       "aesLineStatusAdslMode": aesLineStatusAdslMode,
       "selt": selt,
       "seltTarget": seltTarget,
       "seltOps": seltOps,
       "seltStatus": seltStatus,
       "seltCableType": seltCableType,
       "seltLoopEstimateLengthFt": seltLoopEstimateLengthFt,
       "seltLoopEstimateLengthMeter": seltLoopEstimateLengthMeter}
)
