# SNMP MIB module (CTMMIBCUSTOM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ctm\CTMMIBCUSTOM
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:36 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lastmilegear_ObjectIdentity = ObjectIdentity
lastmilegear = _Lastmilegear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25868)
)
_MibObjects_ObjectIdentity = ObjectIdentity
mibObjects = _MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25868, 1)
)
_Version_Type = OctetString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")
_Site_Type = OctetString
_Site_Object = MibScalar
site = _Site_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 2),
    _Site_Type()
)
site.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site.setStatus("mandatory")
_LastIP_Type = OctetString
_LastIP_Object = MibScalar
lastIP = _LastIP_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 3),
    _LastIP_Type()
)
lastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastIP.setStatus("mandatory")
_LastTime_Type = OctetString
_LastTime_Object = MibScalar
lastTime = _LastTime_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 4),
    _LastTime_Type()
)
lastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTime.setStatus("mandatory")
_NSats_Type = Integer32
_NSats_Object = MibScalar
nSats = _NSats_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 5),
    _NSats_Type()
)
nSats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nSats.setStatus("mandatory")
_PwrP_Type = Integer32
_PwrP_Object = MibScalar
pwrP = _PwrP_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 6),
    _PwrP_Type()
)
pwrP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrP.setStatus("mandatory")
_PwrS_Type = Integer32
_PwrS_Object = MibScalar
pwrS = _PwrS_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 7),
    _PwrS_Type()
)
pwrS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrS.setStatus("mandatory")
_CbTrip_Type = OctetString
_CbTrip_Object = MibScalar
cbTrip = _CbTrip_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 8),
    _CbTrip_Type()
)
cbTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbTrip.setStatus("mandatory")
_TempC_Type = Integer32
_TempC_Object = MibScalar
tempC = _TempC_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 9),
    _TempC_Type()
)
tempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempC.setStatus("mandatory")
_VoltsM1_Type = Integer32
_VoltsM1_Object = MibScalar
voltsM1 = _VoltsM1_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 10),
    _VoltsM1_Type()
)
voltsM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsM1.setStatus("mandatory")
_VoltsM2_Type = Integer32
_VoltsM2_Object = MibScalar
voltsM2 = _VoltsM2_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 11),
    _VoltsM2_Type()
)
voltsM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsM2.setStatus("mandatory")
_PortOnM_Type = OctetString
_PortOnM_Object = MibScalar
portOnM = _PortOnM_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 12),
    _PortOnM_Type()
)
portOnM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOnM.setStatus("mandatory")
_PortSyncM_Type = OctetString
_PortSyncM_Object = MibScalar
portSyncM = _PortSyncM_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 13),
    _PortSyncM_Type()
)
portSyncM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSyncM.setStatus("mandatory")
_PortPwrM1_Type = Integer32
_PortPwrM1_Object = MibScalar
portPwrM1 = _PortPwrM1_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 14),
    _PortPwrM1_Type()
)
portPwrM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM1.setStatus("mandatory")
_PortPwrM2_Type = Integer32
_PortPwrM2_Object = MibScalar
portPwrM2 = _PortPwrM2_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 15),
    _PortPwrM2_Type()
)
portPwrM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM2.setStatus("mandatory")
_PortPwrM3_Type = Integer32
_PortPwrM3_Object = MibScalar
portPwrM3 = _PortPwrM3_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 16),
    _PortPwrM3_Type()
)
portPwrM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM3.setStatus("mandatory")
_PortPwrM4_Type = Integer32
_PortPwrM4_Object = MibScalar
portPwrM4 = _PortPwrM4_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 17),
    _PortPwrM4_Type()
)
portPwrM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM4.setStatus("mandatory")
_PortPwrM5_Type = Integer32
_PortPwrM5_Object = MibScalar
portPwrM5 = _PortPwrM5_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 18),
    _PortPwrM5_Type()
)
portPwrM5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM5.setStatus("mandatory")
_PortPwrM6_Type = Integer32
_PortPwrM6_Object = MibScalar
portPwrM6 = _PortPwrM6_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 19),
    _PortPwrM6_Type()
)
portPwrM6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM6.setStatus("mandatory")
_PortPwrM7_Type = Integer32
_PortPwrM7_Object = MibScalar
portPwrM7 = _PortPwrM7_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 20),
    _PortPwrM7_Type()
)
portPwrM7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM7.setStatus("mandatory")
_PortPwrM8_Type = Integer32
_PortPwrM8_Object = MibScalar
portPwrM8 = _PortPwrM8_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 21),
    _PortPwrM8_Type()
)
portPwrM8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrM8.setStatus("mandatory")
_PwrSP_Type = Integer32
_PwrSP_Object = MibScalar
pwrSP = _PwrSP_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 23),
    _PwrSP_Type()
)
pwrSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSP.setStatus("mandatory")
_PwrSS_Type = Integer32
_PwrSS_Object = MibScalar
pwrSS = _PwrSS_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 24),
    _PwrSS_Type()
)
pwrSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSS.setStatus("mandatory")
_VoltsS1_Type = Integer32
_VoltsS1_Object = MibScalar
voltsS1 = _VoltsS1_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 27),
    _VoltsS1_Type()
)
voltsS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsS1.setStatus("mandatory")
_VoltsS2_Type = Integer32
_VoltsS2_Object = MibScalar
voltsS2 = _VoltsS2_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 28),
    _VoltsS2_Type()
)
voltsS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltsS2.setStatus("mandatory")
_PortOnS_Type = OctetString
_PortOnS_Object = MibScalar
portOnS = _PortOnS_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 29),
    _PortOnS_Type()
)
portOnS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOnS.setStatus("mandatory")
_PortSyncS_Type = OctetString
_PortSyncS_Object = MibScalar
portSyncS = _PortSyncS_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 30),
    _PortSyncS_Type()
)
portSyncS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSyncS.setStatus("mandatory")
_PortPwrS1_Type = Integer32
_PortPwrS1_Object = MibScalar
portPwrS1 = _PortPwrS1_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 31),
    _PortPwrS1_Type()
)
portPwrS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS1.setStatus("mandatory")
_PortPwrS2_Type = Integer32
_PortPwrS2_Object = MibScalar
portPwrS2 = _PortPwrS2_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 32),
    _PortPwrS2_Type()
)
portPwrS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS2.setStatus("mandatory")
_PortPwrS3_Type = Integer32
_PortPwrS3_Object = MibScalar
portPwrS3 = _PortPwrS3_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 33),
    _PortPwrS3_Type()
)
portPwrS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS3.setStatus("mandatory")
_PortPwrS4_Type = Integer32
_PortPwrS4_Object = MibScalar
portPwrS4 = _PortPwrS4_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 34),
    _PortPwrS4_Type()
)
portPwrS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS4.setStatus("mandatory")
_PortPwrS5_Type = Integer32
_PortPwrS5_Object = MibScalar
portPwrS5 = _PortPwrS5_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 35),
    _PortPwrS5_Type()
)
portPwrS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS5.setStatus("mandatory")
_PortPwrS6_Type = Integer32
_PortPwrS6_Object = MibScalar
portPwrS6 = _PortPwrS6_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 36),
    _PortPwrS6_Type()
)
portPwrS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS6.setStatus("mandatory")
_PortPwrS7_Type = Integer32
_PortPwrS7_Object = MibScalar
portPwrS7 = _PortPwrS7_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 37),
    _PortPwrS7_Type()
)
portPwrS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS7.setStatus("mandatory")
_PortPwrS8_Type = Integer32
_PortPwrS8_Object = MibScalar
portPwrS8 = _PortPwrS8_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 38),
    _PortPwrS8_Type()
)
portPwrS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPwrS8.setStatus("mandatory")
_ModeReqM_Type = OctetString
_ModeReqM_Object = MibScalar
modeReqM = _ModeReqM_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 39),
    _ModeReqM_Type()
)
modeReqM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeReqM.setStatus("mandatory")
_TrpCntGM1_Type = Integer32
_TrpCntGM1_Object = MibScalar
trpCntGM1 = _TrpCntGM1_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 45),
    _TrpCntGM1_Type()
)
trpCntGM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM1.setStatus("mandatory")
_TrpCntGM2_Type = Integer32
_TrpCntGM2_Object = MibScalar
trpCntGM2 = _TrpCntGM2_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 46),
    _TrpCntGM2_Type()
)
trpCntGM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM2.setStatus("mandatory")
_TrpCntGM3_Type = Integer32
_TrpCntGM3_Object = MibScalar
trpCntGM3 = _TrpCntGM3_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 47),
    _TrpCntGM3_Type()
)
trpCntGM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM3.setStatus("mandatory")
_TrpCntGM4_Type = Integer32
_TrpCntGM4_Object = MibScalar
trpCntGM4 = _TrpCntGM4_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 48),
    _TrpCntGM4_Type()
)
trpCntGM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM4.setStatus("mandatory")
_TrpCntGM5_Type = Integer32
_TrpCntGM5_Object = MibScalar
trpCntGM5 = _TrpCntGM5_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 49),
    _TrpCntGM5_Type()
)
trpCntGM5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM5.setStatus("mandatory")
_TrpCntGM6_Type = Integer32
_TrpCntGM6_Object = MibScalar
trpCntGM6 = _TrpCntGM6_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 50),
    _TrpCntGM6_Type()
)
trpCntGM6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM6.setStatus("mandatory")
_TrpCntGM7_Type = Integer32
_TrpCntGM7_Object = MibScalar
trpCntGM7 = _TrpCntGM7_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 51),
    _TrpCntGM7_Type()
)
trpCntGM7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM7.setStatus("mandatory")
_TrpCntGM8_Type = Integer32
_TrpCntGM8_Object = MibScalar
trpCntGM8 = _TrpCntGM8_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 52),
    _TrpCntGM8_Type()
)
trpCntGM8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntGM8.setStatus("mandatory")
_TrpCntBM1_Type = Integer32
_TrpCntBM1_Object = MibScalar
trpCntBM1 = _TrpCntBM1_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 53),
    _TrpCntBM1_Type()
)
trpCntBM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM1.setStatus("mandatory")
_TrpCntBM2_Type = Integer32
_TrpCntBM2_Object = MibScalar
trpCntBM2 = _TrpCntBM2_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 54),
    _TrpCntBM2_Type()
)
trpCntBM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM2.setStatus("mandatory")
_TrpCntBM3_Type = Integer32
_TrpCntBM3_Object = MibScalar
trpCntBM3 = _TrpCntBM3_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 55),
    _TrpCntBM3_Type()
)
trpCntBM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM3.setStatus("mandatory")
_TrpCntBM4_Type = Integer32
_TrpCntBM4_Object = MibScalar
trpCntBM4 = _TrpCntBM4_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 56),
    _TrpCntBM4_Type()
)
trpCntBM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM4.setStatus("mandatory")
_TrpCntBM5_Type = Integer32
_TrpCntBM5_Object = MibScalar
trpCntBM5 = _TrpCntBM5_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 57),
    _TrpCntBM5_Type()
)
trpCntBM5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM5.setStatus("mandatory")
_TrpCntBM6_Type = Integer32
_TrpCntBM6_Object = MibScalar
trpCntBM6 = _TrpCntBM6_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 58),
    _TrpCntBM6_Type()
)
trpCntBM6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM6.setStatus("mandatory")
_TrpCntBM7_Type = Integer32
_TrpCntBM7_Object = MibScalar
trpCntBM7 = _TrpCntBM7_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 59),
    _TrpCntBM7_Type()
)
trpCntBM7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM7.setStatus("mandatory")
_TrpCntBM8_Type = Integer32
_TrpCntBM8_Object = MibScalar
trpCntBM8 = _TrpCntBM8_Object(
    (1, 3, 6, 1, 4, 1, 25868, 1, 60),
    _TrpCntBM8_Type()
)
trpCntBM8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpCntBM8.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lostEthernetConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 0)
)
if mibBuilder.loadTexts:
    lostEthernetConnection.setStatus(
        ""
    )

masterPrimayPowerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 1)
)
if mibBuilder.loadTexts:
    masterPrimayPowerLost.setStatus(
        ""
    )

masterSecondaryPowerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 2)
)
if mibBuilder.loadTexts:
    masterSecondaryPowerLost.setStatus(
        ""
    )

gpsSignalLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 3)
)
if mibBuilder.loadTexts:
    gpsSignalLost.setStatus(
        ""
    )

masterTempatureError = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 4)
)
if mibBuilder.loadTexts:
    masterTempatureError.setStatus(
        ""
    )

masterCircuitBreakerTripCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 5)
)
if mibBuilder.loadTexts:
    masterCircuitBreakerTripCode.setStatus(
        ""
    )

loginFailedAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 6)
)
if mibBuilder.loadTexts:
    loginFailedAttempt.setStatus(
        ""
    )

settingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 7)
)
if mibBuilder.loadTexts:
    settingsChanged.setStatus(
        ""
    )

masterPrimaryPowerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 10)
)
if mibBuilder.loadTexts:
    masterPrimaryPowerOK.setStatus(
        ""
    )

masterSecondaryPowerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 20)
)
if mibBuilder.loadTexts:
    masterSecondaryPowerOK.setStatus(
        ""
    )

gpsSignalOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 30)
)
if mibBuilder.loadTexts:
    gpsSignalOK.setStatus(
        ""
    )

tempatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 40)
)
if mibBuilder.loadTexts:
    tempatureOK.setStatus(
        ""
    )

circuitBreakersOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 50)
)
if mibBuilder.loadTexts:
    circuitBreakersOK.setStatus(
        ""
    )

masterAutoRestartCBCompletedOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 52)
)
if mibBuilder.loadTexts:
    masterAutoRestartCBCompletedOK.setStatus(
        ""
    )

loginOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 60)
)
if mibBuilder.loadTexts:
    loginOK.setStatus(
        ""
    )

resetComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 80)
)
if mibBuilder.loadTexts:
    resetComplete.setStatus(
        ""
    )

ethernetConnectionRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 25868, 1, 0, 99)
)
if mibBuilder.loadTexts:
    ethernetConnectionRestored.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTMMIBCUSTOM",
    **{"lastmilegear": lastmilegear,
       "mibObjects": mibObjects,
       "lostEthernetConnection": lostEthernetConnection,
       "masterPrimayPowerLost": masterPrimayPowerLost,
       "masterSecondaryPowerLost": masterSecondaryPowerLost,
       "gpsSignalLost": gpsSignalLost,
       "masterTempatureError": masterTempatureError,
       "masterCircuitBreakerTripCode": masterCircuitBreakerTripCode,
       "loginFailedAttempt": loginFailedAttempt,
       "settingsChanged": settingsChanged,
       "masterPrimaryPowerOK": masterPrimaryPowerOK,
       "masterSecondaryPowerOK": masterSecondaryPowerOK,
       "gpsSignalOK": gpsSignalOK,
       "tempatureOK": tempatureOK,
       "circuitBreakersOK": circuitBreakersOK,
       "masterAutoRestartCBCompletedOK": masterAutoRestartCBCompletedOK,
       "loginOK": loginOK,
       "resetComplete": resetComplete,
       "ethernetConnectionRestored": ethernetConnectionRestored,
       "version": version,
       "site": site,
       "lastIP": lastIP,
       "lastTime": lastTime,
       "nSats": nSats,
       "pwrP": pwrP,
       "pwrS": pwrS,
       "cbTrip": cbTrip,
       "tempC": tempC,
       "voltsM1": voltsM1,
       "voltsM2": voltsM2,
       "portOnM": portOnM,
       "portSyncM": portSyncM,
       "portPwrM1": portPwrM1,
       "portPwrM2": portPwrM2,
       "portPwrM3": portPwrM3,
       "portPwrM4": portPwrM4,
       "portPwrM5": portPwrM5,
       "portPwrM6": portPwrM6,
       "portPwrM7": portPwrM7,
       "portPwrM8": portPwrM8,
       "pwrSP": pwrSP,
       "pwrSS": pwrSS,
       "voltsS1": voltsS1,
       "voltsS2": voltsS2,
       "portOnS": portOnS,
       "portSyncS": portSyncS,
       "portPwrS1": portPwrS1,
       "portPwrS2": portPwrS2,
       "portPwrS3": portPwrS3,
       "portPwrS4": portPwrS4,
       "portPwrS5": portPwrS5,
       "portPwrS6": portPwrS6,
       "portPwrS7": portPwrS7,
       "portPwrS8": portPwrS8,
       "modeReqM": modeReqM,
       "trpCntGM1": trpCntGM1,
       "trpCntGM2": trpCntGM2,
       "trpCntGM3": trpCntGM3,
       "trpCntGM4": trpCntGM4,
       "trpCntGM5": trpCntGM5,
       "trpCntGM6": trpCntGM6,
       "trpCntGM7": trpCntGM7,
       "trpCntGM8": trpCntGM8,
       "trpCntBM1": trpCntBM1,
       "trpCntBM2": trpCntBM2,
       "trpCntBM3": trpCntBM3,
       "trpCntBM4": trpCntBM4,
       "trpCntBM5": trpCntBM5,
       "trpCntBM6": trpCntBM6,
       "trpCntBM7": trpCntBM7,
       "trpCntBM8": trpCntBM8}
)
