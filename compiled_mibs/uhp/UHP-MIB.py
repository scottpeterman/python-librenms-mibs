# SNMP MIB module (UHP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\uhp\UHP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:43 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

uhpV32 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22)
)
if mibBuilder.loadTexts:
    uhpV32.setRevisions(
        ("2018-10-25 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Uhp_ObjectIdentity = ObjectIdentity
uhp = _Uhp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000)
)
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 1)
)


class _SaveConfig_Type(Integer32):
    """Custom type saveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nosave", 0),
          ("save0", 1),
          ("save1", 2),
          ("save2", 3),
          ("save3", 4))
    )


_SaveConfig_Type.__name__ = "Integer32"
_SaveConfig_Object = MibScalar
saveConfig = _SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 1, 1),
    _SaveConfig_Type()
)
saveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfig.setStatus("current")


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreboot", 1),
          ("reboot", 2))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 1, 2),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")
_Command_Type = DisplayString
_Command_Object = MibScalar
command = _Command_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 1, 3),
    _Command_Type()
)
command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    command.setStatus("current")
_ConfigEdit_Type = DisplayString
_ConfigEdit_Object = MibScalar
configEdit = _ConfigEdit_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 1, 4),
    _ConfigEdit_Type()
)
configEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEdit.setStatus("current")
_Profile_Type = DisplayString
_Profile_Object = MibScalar
profile = _Profile_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 1, 5),
    _Profile_Type()
)
profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profile.setStatus("current")
_Demod1_ObjectIdentity = ObjectIdentity
demod1 = _Demod1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 2)
)
_LbandSNR1_Type = Gauge32
_LbandSNR1_Object = MibScalar
lbandSNR1 = _LbandSNR1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 2, 1),
    _LbandSNR1_Type()
)
lbandSNR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbandSNR1.setStatus("current")
_LbandOffset1_Type = Integer32
_LbandOffset1_Object = MibScalar
lbandOffset1 = _LbandOffset1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 2, 2),
    _LbandOffset1_Type()
)
lbandOffset1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbandOffset1.setStatus("current")
_InLvl1_Type = Gauge32
_InLvl1_Object = MibScalar
inLvl1 = _InLvl1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 2, 3),
    _InLvl1_Type()
)
inLvl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLvl1.setStatus("current")
_InBytes1_Type = Counter32
_InBytes1_Object = MibScalar
inBytes1 = _InBytes1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 2, 4),
    _InBytes1_Type()
)
inBytes1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBytes1.setStatus("current")
_Demod2_ObjectIdentity = ObjectIdentity
demod2 = _Demod2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 3)
)
_LbandSNR2_Type = Gauge32
_LbandSNR2_Object = MibScalar
lbandSNR2 = _LbandSNR2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 3, 1),
    _LbandSNR2_Type()
)
lbandSNR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbandSNR2.setStatus("current")
_LbandOffset2_Type = Integer32
_LbandOffset2_Object = MibScalar
lbandOffset2 = _LbandOffset2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 3, 2),
    _LbandOffset2_Type()
)
lbandOffset2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbandOffset2.setStatus("current")
_InLvl2_Type = Gauge32
_InLvl2_Object = MibScalar
inLvl2 = _InLvl2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 3, 3),
    _InLvl2_Type()
)
inLvl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLvl2.setStatus("current")
_InBytes2_Type = Counter32
_InBytes2_Object = MibScalar
inBytes2 = _InBytes2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 3, 4),
    _InBytes2_Type()
)
inBytes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBytes2.setStatus("current")
_Modulator_ObjectIdentity = ObjectIdentity
modulator = _Modulator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4)
)
_PrioAll_ObjectIdentity = ObjectIdentity
prioAll = _PrioAll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1)
)
_OutBytesA_Type = Counter32
_OutBytesA_Object = MibScalar
outBytesA = _OutBytesA_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1, 1),
    _OutBytesA_Type()
)
outBytesA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesA.setStatus("current")
_OutPktsA_Type = Counter32
_OutPktsA_Object = MibScalar
outPktsA = _OutPktsA_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1, 2),
    _OutPktsA_Type()
)
outPktsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsA.setStatus("current")
_DropsA_Type = Counter32
_DropsA_Object = MibScalar
dropsA = _DropsA_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1, 3),
    _DropsA_Type()
)
dropsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsA.setStatus("current")
_QueueLenBA_Type = Counter32
_QueueLenBA_Object = MibScalar
queueLenBA = _QueueLenBA_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1, 4),
    _QueueLenBA_Type()
)
queueLenBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBA.setStatus("current")
_QueueLenPA_Type = Counter32
_QueueLenPA_Object = MibScalar
queueLenPA = _QueueLenPA_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1, 5),
    _QueueLenPA_Type()
)
queueLenPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPA.setStatus("current")
_NumStations_Type = Counter32
_NumStations_Object = MibScalar
numStations = _NumStations_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 1, 6),
    _NumStations_Type()
)
numStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numStations.setStatus("current")
_PrioP1_ObjectIdentity = ObjectIdentity
prioP1 = _PrioP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 2)
)
_OutBytesP1_Type = Counter32
_OutBytesP1_Object = MibScalar
outBytesP1 = _OutBytesP1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 2, 1),
    _OutBytesP1_Type()
)
outBytesP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP1.setStatus("current")
_OutPktsP1_Type = Counter32
_OutPktsP1_Object = MibScalar
outPktsP1 = _OutPktsP1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 2, 2),
    _OutPktsP1_Type()
)
outPktsP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP1.setStatus("current")
_DropsP1_Type = Counter32
_DropsP1_Object = MibScalar
dropsP1 = _DropsP1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 2, 3),
    _DropsP1_Type()
)
dropsP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP1.setStatus("current")
_QueueLenBP1_Type = Counter32
_QueueLenBP1_Object = MibScalar
queueLenBP1 = _QueueLenBP1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 2, 4),
    _QueueLenBP1_Type()
)
queueLenBP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP1.setStatus("current")
_QueueLenPP1_Type = Counter32
_QueueLenPP1_Object = MibScalar
queueLenPP1 = _QueueLenPP1_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 2, 5),
    _QueueLenPP1_Type()
)
queueLenPP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP1.setStatus("current")
_PrioP4_ObjectIdentity = ObjectIdentity
prioP4 = _PrioP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 3)
)
_OutBytesP4_Type = Counter32
_OutBytesP4_Object = MibScalar
outBytesP4 = _OutBytesP4_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 3, 1),
    _OutBytesP4_Type()
)
outBytesP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP4.setStatus("current")
_OutPktsP4_Type = Counter32
_OutPktsP4_Object = MibScalar
outPktsP4 = _OutPktsP4_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 3, 2),
    _OutPktsP4_Type()
)
outPktsP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP4.setStatus("current")
_DropsP4_Type = Counter32
_DropsP4_Object = MibScalar
dropsP4 = _DropsP4_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 3, 3),
    _DropsP4_Type()
)
dropsP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP4.setStatus("current")
_QueueLenBP4_Type = Counter32
_QueueLenBP4_Object = MibScalar
queueLenBP4 = _QueueLenBP4_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 3, 4),
    _QueueLenBP4_Type()
)
queueLenBP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP4.setStatus("current")
_QueueLenPP4_Type = Counter32
_QueueLenPP4_Object = MibScalar
queueLenPP4 = _QueueLenPP4_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 3, 5),
    _QueueLenPP4_Type()
)
queueLenPP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP4.setStatus("current")
_PrioP7_ObjectIdentity = ObjectIdentity
prioP7 = _PrioP7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 4)
)
_OutBytesP7_Type = Counter32
_OutBytesP7_Object = MibScalar
outBytesP7 = _OutBytesP7_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 4, 1),
    _OutBytesP7_Type()
)
outBytesP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP7.setStatus("current")
_OutPktsP7_Type = Counter32
_OutPktsP7_Object = MibScalar
outPktsP7 = _OutPktsP7_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 4, 2),
    _OutPktsP7_Type()
)
outPktsP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP7.setStatus("current")
_DropsP7_Type = Counter32
_DropsP7_Object = MibScalar
dropsP7 = _DropsP7_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 4, 3),
    _DropsP7_Type()
)
dropsP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP7.setStatus("current")
_QueueLenBP7_Type = Counter32
_QueueLenBP7_Object = MibScalar
queueLenBP7 = _QueueLenBP7_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 4, 4),
    _QueueLenBP7_Type()
)
queueLenBP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP7.setStatus("current")
_QueueLenPP7_Type = Counter32
_QueueLenPP7_Object = MibScalar
queueLenPP7 = _QueueLenPP7_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 4, 5),
    _QueueLenPP7_Type()
)
queueLenPP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP7.setStatus("current")
_PrioCtrl_ObjectIdentity = ObjectIdentity
prioCtrl = _PrioCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 5)
)
_OutBytesC_Type = Counter32
_OutBytesC_Object = MibScalar
outBytesC = _OutBytesC_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 5, 1),
    _OutBytesC_Type()
)
outBytesC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesC.setStatus("current")
_OutPktsC_Type = Counter32
_OutPktsC_Object = MibScalar
outPktsC = _OutPktsC_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 5, 2),
    _OutPktsC_Type()
)
outPktsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsC.setStatus("current")
_Level_ObjectIdentity = ObjectIdentity
level = _Level_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 6)
)
_TxLevel_Type = Gauge32
_TxLevel_Object = MibScalar
txLevel = _TxLevel_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 6, 1),
    _TxLevel_Type()
)
txLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLevel.setStatus("current")
_TxLevelDelta_Type = Integer32
_TxLevelDelta_Object = MibScalar
txLevelDelta = _TxLevelDelta_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 6, 2),
    _TxLevelDelta_Type()
)
txLevelDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLevelDelta.setStatus("current")
_TxMaxLevel_Type = Integer32
_TxMaxLevel_Object = MibScalar
txMaxLevel = _TxMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 6, 3),
    _TxMaxLevel_Type()
)
txMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMaxLevel.setStatus("current")
_PrioP2_ObjectIdentity = ObjectIdentity
prioP2 = _PrioP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 7)
)
_OutBytesP2_Type = Counter32
_OutBytesP2_Object = MibScalar
outBytesP2 = _OutBytesP2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 7, 1),
    _OutBytesP2_Type()
)
outBytesP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP2.setStatus("current")
_OutPktsP2_Type = Counter32
_OutPktsP2_Object = MibScalar
outPktsP2 = _OutPktsP2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 7, 2),
    _OutPktsP2_Type()
)
outPktsP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP2.setStatus("current")
_DropsP2_Type = Counter32
_DropsP2_Object = MibScalar
dropsP2 = _DropsP2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 7, 3),
    _DropsP2_Type()
)
dropsP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP2.setStatus("current")
_QueueLenBP2_Type = Counter32
_QueueLenBP2_Object = MibScalar
queueLenBP2 = _QueueLenBP2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 7, 4),
    _QueueLenBP2_Type()
)
queueLenBP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP2.setStatus("current")
_QueueLenPP2_Type = Counter32
_QueueLenPP2_Object = MibScalar
queueLenPP2 = _QueueLenPP2_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 7, 5),
    _QueueLenPP2_Type()
)
queueLenPP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP2.setStatus("current")
_PrioP3_ObjectIdentity = ObjectIdentity
prioP3 = _PrioP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 8)
)
_OutBytesP3_Type = Counter32
_OutBytesP3_Object = MibScalar
outBytesP3 = _OutBytesP3_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 8, 1),
    _OutBytesP3_Type()
)
outBytesP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP3.setStatus("current")
_OutPktsP3_Type = Counter32
_OutPktsP3_Object = MibScalar
outPktsP3 = _OutPktsP3_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 8, 2),
    _OutPktsP3_Type()
)
outPktsP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP3.setStatus("current")
_DropsP3_Type = Counter32
_DropsP3_Object = MibScalar
dropsP3 = _DropsP3_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 8, 3),
    _DropsP3_Type()
)
dropsP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP3.setStatus("current")
_QueueLenBP3_Type = Counter32
_QueueLenBP3_Object = MibScalar
queueLenBP3 = _QueueLenBP3_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 8, 4),
    _QueueLenBP3_Type()
)
queueLenBP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP3.setStatus("current")
_QueueLenPP3_Type = Counter32
_QueueLenPP3_Object = MibScalar
queueLenPP3 = _QueueLenPP3_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 8, 5),
    _QueueLenPP3_Type()
)
queueLenPP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP3.setStatus("current")
_PrioP5_ObjectIdentity = ObjectIdentity
prioP5 = _PrioP5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 9)
)
_OutBytesP5_Type = Counter32
_OutBytesP5_Object = MibScalar
outBytesP5 = _OutBytesP5_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 9, 1),
    _OutBytesP5_Type()
)
outBytesP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP5.setStatus("current")
_OutPktsP5_Type = Counter32
_OutPktsP5_Object = MibScalar
outPktsP5 = _OutPktsP5_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 9, 2),
    _OutPktsP5_Type()
)
outPktsP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP5.setStatus("current")
_DropsP5_Type = Counter32
_DropsP5_Object = MibScalar
dropsP5 = _DropsP5_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 9, 3),
    _DropsP5_Type()
)
dropsP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP5.setStatus("current")
_QueueLenBP5_Type = Counter32
_QueueLenBP5_Object = MibScalar
queueLenBP5 = _QueueLenBP5_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 9, 4),
    _QueueLenBP5_Type()
)
queueLenBP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP5.setStatus("current")
_QueueLenPP5_Type = Counter32
_QueueLenPP5_Object = MibScalar
queueLenPP5 = _QueueLenPP5_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 9, 5),
    _QueueLenPP5_Type()
)
queueLenPP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP5.setStatus("current")
_PrioP6_ObjectIdentity = ObjectIdentity
prioP6 = _PrioP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 10)
)
_OutBytesP6_Type = Counter32
_OutBytesP6_Object = MibScalar
outBytesP6 = _OutBytesP6_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 10, 1),
    _OutBytesP6_Type()
)
outBytesP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytesP6.setStatus("current")
_OutPktsP6_Type = Counter32
_OutPktsP6_Object = MibScalar
outPktsP6 = _OutPktsP6_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 10, 2),
    _OutPktsP6_Type()
)
outPktsP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPktsP6.setStatus("current")
_DropsP6_Type = Counter32
_DropsP6_Object = MibScalar
dropsP6 = _DropsP6_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 10, 3),
    _DropsP6_Type()
)
dropsP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropsP6.setStatus("current")
_QueueLenBP6_Type = Counter32
_QueueLenBP6_Object = MibScalar
queueLenBP6 = _QueueLenBP6_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 10, 4),
    _QueueLenBP6_Type()
)
queueLenBP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenBP6.setStatus("current")
_QueueLenPP6_Type = Counter32
_QueueLenPP6_Object = MibScalar
queueLenPP6 = _QueueLenPP6_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 4, 10, 5),
    _QueueLenPP6_Type()
)
queueLenPP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueLenPP6.setStatus("current")
_Tdma_ObjectIdentity = ObjectIdentity
tdma = _Tdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5)
)
_Tts_ObjectIdentity = ObjectIdentity
tts = _Tts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1)
)
_Tdelta_Type = Integer32
_Tdelta_Object = MibScalar
tdelta = _Tdelta_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 1),
    _Tdelta_Type()
)
tdelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdelta.setStatus("current")
_TdtConfidence_Type = Gauge32
_TdtConfidence_Object = MibScalar
tdtConfidence = _TdtConfidence_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 2),
    _TdtConfidence_Type()
)
tdtConfidence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdtConfidence.setStatus("current")
_SoftErrors_Type = Counter32
_SoftErrors_Object = MibScalar
softErrors = _SoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 3),
    _SoftErrors_Type()
)
softErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softErrors.setStatus("current")
_HardErrors_Type = Counter32
_HardErrors_Object = MibScalar
hardErrors = _HardErrors_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 4),
    _HardErrors_Type()
)
hardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardErrors.setStatus("current")
_HubTTS_Type = Gauge32
_HubTTS_Object = MibScalar
hubTTS = _HubTTS_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 5),
    _HubTTS_Type()
)
hubTTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubTTS.setStatus("current")
_HubTTSconfidence_Type = Gauge32
_HubTTSconfidence_Object = MibScalar
hubTTSconfidence = _HubTTSconfidence_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 6),
    _HubTTSconfidence_Type()
)
hubTTSconfidence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubTTSconfidence.setStatus("current")
_RemoteTTS_Type = Gauge32
_RemoteTTS_Object = MibScalar
remoteTTS = _RemoteTTS_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 1, 7),
    _RemoteTTS_Type()
)
remoteTTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTTS.setStatus("current")
_Inroute_ObjectIdentity = ObjectIdentity
inroute = _Inroute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2)
)


class _NetState_Type(Integer32):
    """Custom type netState based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("init", 1),
          ("noConfig", 2),
          ("useConfig", 3),
          ("redundant", 4),
          ("startRX", 5),
          ("cotmPointing", 6),
          ("startHubTX", 7),
          ("noRX", 8),
          ("identify", 9),
          ("getNetConfig", 10),
          ("calcDelays", 11),
          ("startTDMA", 12),
          ("startTX", 13),
          ("acquisition", 14),
          ("adjustment", 15),
          ("noStations", 16),
          ("operation", 17))
    )


_NetState_Type.__name__ = "Integer32"
_NetState_Object = MibScalar
netState = _NetState_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2, 1),
    _NetState_Type()
)
netState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netState.setStatus("current")
_FrameDelay_Type = Gauge32
_FrameDelay_Object = MibScalar
frameDelay = _FrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2, 2),
    _FrameDelay_Type()
)
frameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameDelay.setStatus("current")
_SectionBW_Type = Gauge32
_SectionBW_Object = MibScalar
sectionBW = _SectionBW_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2, 3),
    _SectionBW_Type()
)
sectionBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectionBW.setStatus("current")
_NetRequest_Type = Gauge32
_NetRequest_Object = MibScalar
netRequest = _NetRequest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2, 4),
    _NetRequest_Type()
)
netRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netRequest.setStatus("current")
_FreeSlots_Type = Gauge32
_FreeSlots_Object = MibScalar
freeSlots = _FreeSlots_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2, 5),
    _FreeSlots_Type()
)
freeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeSlots.setStatus("current")
_NetLoad_Type = Gauge32
_NetLoad_Object = MibScalar
netLoad = _NetLoad_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 2, 6),
    _NetLoad_Type()
)
netLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoad.setStatus("current")
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 3)
)


class _ServerStatus_Type(Integer32):
    """Custom type serverStatus based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("init", 1),
          ("noConfig", 2),
          ("useConfig", 3),
          ("redundant", 4),
          ("startRX", 5),
          ("cotmPointing", 6),
          ("startHubTX", 7),
          ("noRX", 8),
          ("identify", 9),
          ("getNetConfig", 10),
          ("calcDelays", 11),
          ("startTDMA", 12),
          ("startTX", 13),
          ("acquisition", 14),
          ("adjustment", 15),
          ("noStations", 16),
          ("operation", 17))
    )


_ServerStatus_Type.__name__ = "Integer32"
_ServerStatus_Object = MibScalar
serverStatus = _ServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 3, 1),
    _ServerStatus_Type()
)
serverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverStatus.setStatus("current")
_FrameDuration_Type = Gauge32
_FrameDuration_Object = MibScalar
frameDuration = _FrameDuration_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 3, 2),
    _FrameDuration_Type()
)
frameDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameDuration.setStatus("current")
_RemTable_ObjectIdentity = ObjectIdentity
remTable = _RemTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4)
)
_RxBytes_Type = Counter32
_RxBytes_Object = MibScalar
rxBytes = _RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 1),
    _RxBytes_Type()
)
rxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBytes.setStatus("current")
_P1Bytes_Type = Counter32
_P1Bytes_Object = MibScalar
p1Bytes = _P1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 2),
    _P1Bytes_Type()
)
p1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1Bytes.setStatus("current")
_P4Bytes_Type = Counter32
_P4Bytes_Object = MibScalar
p4Bytes = _P4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 3),
    _P4Bytes_Type()
)
p4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p4Bytes.setStatus("current")
_P7Bytes_Type = Counter32
_P7Bytes_Object = MibScalar
p7Bytes = _P7Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 4),
    _P7Bytes_Type()
)
p7Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p7Bytes.setStatus("current")
_CrcErrors_Type = Counter32
_CrcErrors_Object = MibScalar
crcErrors = _CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 5),
    _CrcErrors_Type()
)
crcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcErrors.setStatus("current")
_CarrierToNoise_Type = Gauge32
_CarrierToNoise_Object = MibScalar
carrierToNoise = _CarrierToNoise_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 6),
    _CarrierToNoise_Type()
)
carrierToNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierToNoise.setStatus("current")
_FreqOffset_Type = Integer32
_FreqOffset_Object = MibScalar
freqOffset = _FreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 7),
    _FreqOffset_Type()
)
freqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freqOffset.setStatus("current")
_RemRecvHub_Type = Gauge32
_RemRecvHub_Object = MibScalar
remRecvHub = _RemRecvHub_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 8),
    _RemRecvHub_Type()
)
remRecvHub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remRecvHub.setStatus("current")


class _LinkState_Type(Integer32):
    """Custom type linkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("off", 3))
    )


_LinkState_Type.__name__ = "Integer32"
_LinkState_Object = MibScalar
linkState = _LinkState_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 9),
    _LinkState_Type()
)
linkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkState.setStatus("current")
_LastHeard_Type = Gauge32
_LastHeard_Object = MibScalar
lastHeard = _LastHeard_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 10),
    _LastHeard_Type()
)
lastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastHeard.setStatus("current")
_DownTimes_Type = Gauge32
_DownTimes_Object = MibScalar
downTimes = _DownTimes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 11),
    _DownTimes_Type()
)
downTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downTimes.setStatus("current")
_TotalRequest_Type = Gauge32
_TotalRequest_Object = MibScalar
totalRequest = _TotalRequest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 12),
    _TotalRequest_Type()
)
totalRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRequest.setStatus("current")
_NrtRequest_Type = Gauge32
_NrtRequest_Object = MibScalar
nrtRequest = _NrtRequest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 13),
    _NrtRequest_Type()
)
nrtRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nrtRequest.setStatus("current")
_RtmRequest_Type = Gauge32
_RtmRequest_Object = MibScalar
rtmRequest = _RtmRequest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 14),
    _RtmRequest_Type()
)
rtmRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRequest.setStatus("current")
_CurrentFP_Type = Gauge32
_CurrentFP_Object = MibScalar
currentFP = _CurrentFP_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 15),
    _CurrentFP_Type()
)
currentFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFP.setStatus("current")
_TxLvl_Type = Gauge32
_TxLvl_Object = MibScalar
txLvl = _TxLvl_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 16),
    _TxLvl_Type()
)
txLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLvl.setStatus("current")
_Faults_Type = Gauge32
_Faults_Object = MibScalar
faults = _Faults_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 17),
    _Faults_Type()
)
faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faults.setStatus("current")
_P2Bytes_Type = Counter32
_P2Bytes_Object = MibScalar
p2Bytes = _P2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 18),
    _P2Bytes_Type()
)
p2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2Bytes.setStatus("current")
_P3Bytes_Type = Counter32
_P3Bytes_Object = MibScalar
p3Bytes = _P3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 19),
    _P3Bytes_Type()
)
p3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p3Bytes.setStatus("current")
_P5Bytes_Type = Counter32
_P5Bytes_Object = MibScalar
p5Bytes = _P5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 20),
    _P5Bytes_Type()
)
p5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p5Bytes.setStatus("current")
_P6Bytes_Type = Counter32
_P6Bytes_Object = MibScalar
p6Bytes = _P6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 4, 21),
    _P6Bytes_Type()
)
p6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p6Bytes.setStatus("current")
_Station_ObjectIdentity = ObjectIdentity
station = _Station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5)
)


class _StationState_Type(Integer32):
    """Custom type stationState based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("init", 1),
          ("noConfig", 2),
          ("useConfig", 3),
          ("redundant", 4),
          ("startRX", 5),
          ("cotmPointing", 6),
          ("startHubTX", 7),
          ("noRX", 8),
          ("identify", 9),
          ("getNetConfig", 10),
          ("calcDelays", 11),
          ("startTDMA", 12),
          ("startTX", 13),
          ("acquisition", 14),
          ("adjustment", 15),
          ("noStations", 16),
          ("operation", 17))
    )


_StationState_Type.__name__ = "Integer32"
_StationState_Object = MibScalar
stationState = _StationState_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 1),
    _StationState_Type()
)
stationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationState.setStatus("current")
_RemnrtRequest_Type = Gauge32
_RemnrtRequest_Object = MibScalar
remnrtRequest = _RemnrtRequest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 2),
    _RemnrtRequest_Type()
)
remnrtRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remnrtRequest.setStatus("current")
_RemrtRequest_Type = Gauge32
_RemrtRequest_Object = MibScalar
remrtRequest = _RemrtRequest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 3),
    _RemrtRequest_Type()
)
remrtRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remrtRequest.setStatus("current")
_FpLost_Type = Counter32
_FpLost_Object = MibScalar
fpLost = _FpLost_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 4),
    _FpLost_Type()
)
fpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLost.setStatus("current")
_LvlOffset_Type = Integer32
_LvlOffset_Object = MibScalar
lvlOffset = _LvlOffset_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 5),
    _LvlOffset_Type()
)
lvlOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvlOffset.setStatus("current")
_LvlAdjust_Type = Gauge32
_LvlAdjust_Object = MibScalar
lvlAdjust = _LvlAdjust_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 6),
    _LvlAdjust_Type()
)
lvlAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvlAdjust.setStatus("current")
_FrqOffset_Type = Integer32
_FrqOffset_Object = MibScalar
frqOffset = _FrqOffset_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 7),
    _FrqOffset_Type()
)
frqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frqOffset.setStatus("current")
_FrqAdjust_Type = Integer32
_FrqAdjust_Object = MibScalar
frqAdjust = _FrqAdjust_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 8),
    _FrqAdjust_Type()
)
frqAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frqAdjust.setStatus("current")
_TimeOffset_Type = Integer32
_TimeOffset_Object = MibScalar
timeOffset = _TimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 9),
    _TimeOffset_Type()
)
timeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOffset.setStatus("current")
_TimeAdjust_Type = Integer32
_TimeAdjust_Object = MibScalar
timeAdjust = _TimeAdjust_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 5, 5, 10),
    _TimeAdjust_Type()
)
timeAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeAdjust.setStatus("current")
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6)
)
_UnroutedPkts_Type = Counter32
_UnroutedPkts_Object = MibScalar
unroutedPkts = _UnroutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 1),
    _UnroutedPkts_Type()
)
unroutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unroutedPkts.setStatus("current")
_UnroutedSource_Type = IpAddress
_UnroutedSource_Object = MibScalar
unroutedSource = _UnroutedSource_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 2),
    _UnroutedSource_Type()
)
unroutedSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unroutedSource.setStatus("current")
_UnroutedDest_Type = IpAddress
_UnroutedDest_Object = MibScalar
unroutedDest = _UnroutedDest_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 3),
    _UnroutedDest_Type()
)
unroutedDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unroutedDest.setStatus("current")
_OutVlanBytes_Type = Counter32
_OutVlanBytes_Object = MibScalar
outVlanBytes = _OutVlanBytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 4),
    _OutVlanBytes_Type()
)
outVlanBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outVlanBytes.setStatus("current")
_InVlanBytes_Type = Counter32
_InVlanBytes_Object = MibScalar
inVlanBytes = _InVlanBytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 5),
    _InVlanBytes_Type()
)
inVlanBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inVlanBytes.setStatus("current")
_OutSvlanBytes_Type = Counter32
_OutSvlanBytes_Object = MibScalar
outSvlanBytes = _OutSvlanBytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 6),
    _OutSvlanBytes_Type()
)
outSvlanBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outSvlanBytes.setStatus("current")
_InSvlanBytes_Type = Counter32
_InSvlanBytes_Object = MibScalar
inSvlanBytes = _InSvlanBytes_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 7),
    _InSvlanBytes_Type()
)
inSvlanBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvlanBytes.setStatus("current")
_InSvlanPackets_Type = Counter32
_InSvlanPackets_Object = MibScalar
inSvlanPackets = _InSvlanPackets_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 6, 8),
    _InSvlanPackets_Type()
)
inSvlanPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSvlanPackets.setStatus("current")
_Shaper_ObjectIdentity = ObjectIdentity
shaper = _Shaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7)
)
_StreamSpeed_Type = Counter32
_StreamSpeed_Object = MibScalar
streamSpeed = _StreamSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 1),
    _StreamSpeed_Type()
)
streamSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamSpeed.setStatus("current")
_StreamP1Speed_Type = Counter32
_StreamP1Speed_Object = MibScalar
streamP1Speed = _StreamP1Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 2),
    _StreamP1Speed_Type()
)
streamP1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP1Speed.setStatus("current")
_StreamP4Speed_Type = Counter32
_StreamP4Speed_Object = MibScalar
streamP4Speed = _StreamP4Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 3),
    _StreamP4Speed_Type()
)
streamP4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP4Speed.setStatus("current")
_StreamP7Speed_Type = Counter32
_StreamP7Speed_Object = MibScalar
streamP7Speed = _StreamP7Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 4),
    _StreamP7Speed_Type()
)
streamP7Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP7Speed.setStatus("current")
_StreamDelay_Type = Gauge32
_StreamDelay_Object = MibScalar
streamDelay = _StreamDelay_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 5),
    _StreamDelay_Type()
)
streamDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamDelay.setStatus("current")
_StreamQueue_Type = Gauge32
_StreamQueue_Object = MibScalar
streamQueue = _StreamQueue_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 6),
    _StreamQueue_Type()
)
streamQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamQueue.setStatus("current")
_StreamP2Speed_Type = Counter32
_StreamP2Speed_Object = MibScalar
streamP2Speed = _StreamP2Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 7),
    _StreamP2Speed_Type()
)
streamP2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP2Speed.setStatus("current")
_StreamP3Speed_Type = Counter32
_StreamP3Speed_Object = MibScalar
streamP3Speed = _StreamP3Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 8),
    _StreamP3Speed_Type()
)
streamP3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP3Speed.setStatus("current")
_StreamP5Speed_Type = Counter32
_StreamP5Speed_Object = MibScalar
streamP5Speed = _StreamP5Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 9),
    _StreamP5Speed_Type()
)
streamP5Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP5Speed.setStatus("current")
_StreamP6Speed_Type = Counter32
_StreamP6Speed_Object = MibScalar
streamP6Speed = _StreamP6Speed_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 7, 10),
    _StreamP6Speed_Type()
)
streamP6Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamP6Speed.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8)
)
_Temperature_Type = Integer32
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8, 1),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_CpuLoad_Type = Gauge32
_CpuLoad_Object = MibScalar
cpuLoad = _CpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8, 2),
    _CpuLoad_Type()
)
cpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad.setStatus("current")
_Buffers_Type = Gauge32
_Buffers_Object = MibScalar
buffers = _Buffers_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8, 3),
    _Buffers_Type()
)
buffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buffers.setStatus("current")


class _Redundancy_Type(Integer32):
    """Custom type redundancy based on Integer32"""
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
        *(("idle", 0),
          ("backup", 1),
          ("faults", 2),
          ("trying", 3),
          ("active", 4),
          ("off", 5))
    )


_Redundancy_Type.__name__ = "Integer32"
_Redundancy_Object = MibScalar
redundancy = _Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8, 4),
    _Redundancy_Type()
)
redundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancy.setStatus("current")
_SwVersion_Type = Gauge32
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8, 5),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")
_ReleaseDate_Type = Gauge32
_ReleaseDate_Object = MibScalar
releaseDate = _ReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 8, 6),
    _ReleaseDate_Type()
)
releaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseDate.setStatus("current")
_Mobile_ObjectIdentity = ObjectIdentity
mobile = _Mobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9)
)
_Version_Type = Gauge32
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_SerialNumber_Type = Gauge32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_InputLevel_Type = Gauge32
_InputLevel_Object = MibScalar
inputLevel = _InputLevel_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 3),
    _InputLevel_Type()
)
inputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLevel.setStatus("current")
_RxState_Type = Gauge32
_RxState_Object = MibScalar
rxState = _RxState_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 4),
    _RxState_Type()
)
rxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxState.setStatus("current")
_SearchState_Type = Gauge32
_SearchState_Object = MibScalar
searchState = _SearchState_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 5),
    _SearchState_Type()
)
searchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    searchState.setStatus("current")
_TxControl_Type = Gauge32
_TxControl_Object = MibScalar
txControl = _TxControl_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 6),
    _TxControl_Type()
)
txControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txControl.setStatus("current")
_Location_Type = DisplayString
_Location_Object = MibScalar
location = _Location_Object(
    (1, 3, 6, 1, 4, 1, 8000, 22, 9, 7),
    _Location_Type()
)
location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    location.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UHP-MIB",
    **{"uhp": uhp,
       "uhpV32": uhpV32,
       "control": control,
       "saveConfig": saveConfig,
       "reboot": reboot,
       "command": command,
       "configEdit": configEdit,
       "profile": profile,
       "demod1": demod1,
       "lbandSNR1": lbandSNR1,
       "lbandOffset1": lbandOffset1,
       "inLvl1": inLvl1,
       "inBytes1": inBytes1,
       "demod2": demod2,
       "lbandSNR2": lbandSNR2,
       "lbandOffset2": lbandOffset2,
       "inLvl2": inLvl2,
       "inBytes2": inBytes2,
       "modulator": modulator,
       "prioAll": prioAll,
       "outBytesA": outBytesA,
       "outPktsA": outPktsA,
       "dropsA": dropsA,
       "queueLenBA": queueLenBA,
       "queueLenPA": queueLenPA,
       "numStations": numStations,
       "prioP1": prioP1,
       "outBytesP1": outBytesP1,
       "outPktsP1": outPktsP1,
       "dropsP1": dropsP1,
       "queueLenBP1": queueLenBP1,
       "queueLenPP1": queueLenPP1,
       "prioP4": prioP4,
       "outBytesP4": outBytesP4,
       "outPktsP4": outPktsP4,
       "dropsP4": dropsP4,
       "queueLenBP4": queueLenBP4,
       "queueLenPP4": queueLenPP4,
       "prioP7": prioP7,
       "outBytesP7": outBytesP7,
       "outPktsP7": outPktsP7,
       "dropsP7": dropsP7,
       "queueLenBP7": queueLenBP7,
       "queueLenPP7": queueLenPP7,
       "prioCtrl": prioCtrl,
       "outBytesC": outBytesC,
       "outPktsC": outPktsC,
       "level": level,
       "txLevel": txLevel,
       "txLevelDelta": txLevelDelta,
       "txMaxLevel": txMaxLevel,
       "prioP2": prioP2,
       "outBytesP2": outBytesP2,
       "outPktsP2": outPktsP2,
       "dropsP2": dropsP2,
       "queueLenBP2": queueLenBP2,
       "queueLenPP2": queueLenPP2,
       "prioP3": prioP3,
       "outBytesP3": outBytesP3,
       "outPktsP3": outPktsP3,
       "dropsP3": dropsP3,
       "queueLenBP3": queueLenBP3,
       "queueLenPP3": queueLenPP3,
       "prioP5": prioP5,
       "outBytesP5": outBytesP5,
       "outPktsP5": outPktsP5,
       "dropsP5": dropsP5,
       "queueLenBP5": queueLenBP5,
       "queueLenPP5": queueLenPP5,
       "prioP6": prioP6,
       "outBytesP6": outBytesP6,
       "outPktsP6": outPktsP6,
       "dropsP6": dropsP6,
       "queueLenBP6": queueLenBP6,
       "queueLenPP6": queueLenPP6,
       "tdma": tdma,
       "tts": tts,
       "tdelta": tdelta,
       "tdtConfidence": tdtConfidence,
       "softErrors": softErrors,
       "hardErrors": hardErrors,
       "hubTTS": hubTTS,
       "hubTTSconfidence": hubTTSconfidence,
       "remoteTTS": remoteTTS,
       "inroute": inroute,
       "netState": netState,
       "frameDelay": frameDelay,
       "sectionBW": sectionBW,
       "netRequest": netRequest,
       "freeSlots": freeSlots,
       "netLoad": netLoad,
       "server": server,
       "serverStatus": serverStatus,
       "frameDuration": frameDuration,
       "remTable": remTable,
       "rxBytes": rxBytes,
       "p1Bytes": p1Bytes,
       "p4Bytes": p4Bytes,
       "p7Bytes": p7Bytes,
       "crcErrors": crcErrors,
       "carrierToNoise": carrierToNoise,
       "freqOffset": freqOffset,
       "remRecvHub": remRecvHub,
       "linkState": linkState,
       "lastHeard": lastHeard,
       "downTimes": downTimes,
       "totalRequest": totalRequest,
       "nrtRequest": nrtRequest,
       "rtmRequest": rtmRequest,
       "currentFP": currentFP,
       "txLvl": txLvl,
       "faults": faults,
       "p2Bytes": p2Bytes,
       "p3Bytes": p3Bytes,
       "p5Bytes": p5Bytes,
       "p6Bytes": p6Bytes,
       "station": station,
       "stationState": stationState,
       "remnrtRequest": remnrtRequest,
       "remrtRequest": remrtRequest,
       "fpLost": fpLost,
       "lvlOffset": lvlOffset,
       "lvlAdjust": lvlAdjust,
       "frqOffset": frqOffset,
       "frqAdjust": frqAdjust,
       "timeOffset": timeOffset,
       "timeAdjust": timeAdjust,
       "router": router,
       "unroutedPkts": unroutedPkts,
       "unroutedSource": unroutedSource,
       "unroutedDest": unroutedDest,
       "outVlanBytes": outVlanBytes,
       "inVlanBytes": inVlanBytes,
       "outSvlanBytes": outSvlanBytes,
       "inSvlanBytes": inSvlanBytes,
       "inSvlanPackets": inSvlanPackets,
       "shaper": shaper,
       "streamSpeed": streamSpeed,
       "streamP1Speed": streamP1Speed,
       "streamP4Speed": streamP4Speed,
       "streamP7Speed": streamP7Speed,
       "streamDelay": streamDelay,
       "streamQueue": streamQueue,
       "streamP2Speed": streamP2Speed,
       "streamP3Speed": streamP3Speed,
       "streamP5Speed": streamP5Speed,
       "streamP6Speed": streamP6Speed,
       "system": system,
       "temperature": temperature,
       "cpuLoad": cpuLoad,
       "buffers": buffers,
       "redundancy": redundancy,
       "swVersion": swVersion,
       "releaseDate": releaseDate,
       "mobile": mobile,
       "version": version,
       "serialNumber": serialNumber,
       "inputLevel": inputLevel,
       "rxState": rxState,
       "searchState": searchState,
       "txControl": txControl,
       "location": location}
)
