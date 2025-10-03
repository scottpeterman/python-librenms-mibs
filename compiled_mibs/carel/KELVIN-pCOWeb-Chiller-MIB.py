# SNMP MIB module (KELVIN-pCOWeb-Chiller-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\carel\KELVIN-pCOWeb-Chiller-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:44 2025
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

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
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

kelvin_pCOWebMIB_Chiller = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1)
)
if mibBuilder.loadTexts:
    kelvin_pCOWebMIB_Chiller.setRevisions(
        ("2013-09-13 16:02",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Carel_ObjectIdentity = ObjectIdentity
carel = _Carel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839)
)
_Systm_ObjectIdentity = ObjectIdentity
systm = _Systm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 1)
)
_AgentRelease_Type = Integer32
_AgentRelease_Object = MibScalar
agentRelease = _AgentRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 1),
    _AgentRelease_Type()
)
agentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRelease.setStatus("current")
if mibBuilder.loadTexts:
    agentRelease.setUnits("N/A")
_AgentCode_Type = Integer32
_AgentCode_Object = MibScalar
agentCode = _AgentCode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2),
    _AgentCode_Type()
)
agentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCode.setStatus("current")
if mibBuilder.loadTexts:
    agentCode.setUnits("N/A")
_Instruments_ObjectIdentity = ObjectIdentity
instruments = _Instruments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2)
)
_PCOWebInfo_ObjectIdentity = ObjectIdentity
pCOWebInfo = _PCOWebInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0)
)
_PCOStatusgroup_ObjectIdentity = ObjectIdentity
pCOStatusgroup = _PCOStatusgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 10)
)
_PCOId1_Status_Type = Integer32
_PCOId1_Status_Object = MibScalar
pCOId1_Status = _PCOId1_Status_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 10, 1),
    _PCOId1_Status_Type()
)
pCOId1_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCOId1_Status.setStatus("current")
if mibBuilder.loadTexts:
    pCOId1_Status.setUnits("N/A")
_PCOErrorsNumbergroup_ObjectIdentity = ObjectIdentity
pCOErrorsNumbergroup = _PCOErrorsNumbergroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 11)
)
_PCOId1_ErrorsNumber_Type = Integer32
_PCOId1_ErrorsNumber_Object = MibScalar
pCOId1_ErrorsNumber = _PCOId1_ErrorsNumber_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 11, 1),
    _PCOId1_ErrorsNumber_Type()
)
pCOId1_ErrorsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCOId1_ErrorsNumber.setStatus("current")
if mibBuilder.loadTexts:
    pCOId1_ErrorsNumber.setUnits("N/A")
_DigitalObjects_ObjectIdentity = ObjectIdentity
digitalObjects = _DigitalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1)
)


class _Al_pa1_Type(Integer32):
    """Custom type al_pa1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_pa1_Type.__name__ = "Integer32"
_Al_pa1_Object = MibScalar
al_pa1 = _Al_pa1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Al_pa1_Type()
)
al_pa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_pa1.setStatus("current")
if mibBuilder.loadTexts:
    al_pa1.setUnits("N/A")


class _Al_pa2_Type(Integer32):
    """Custom type al_pa2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_pa2_Type.__name__ = "Integer32"
_Al_pa2_Object = MibScalar
al_pa2 = _Al_pa2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Al_pa2_Type()
)
al_pa2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_pa2.setStatus("current")
if mibBuilder.loadTexts:
    al_pa2.setUnits("N/A")


class _Al_pb1_Type(Integer32):
    """Custom type al_pb1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_pb1_Type.__name__ = "Integer32"
_Al_pb1_Object = MibScalar
al_pb1 = _Al_pb1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Al_pb1_Type()
)
al_pb1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_pb1.setStatus("current")
if mibBuilder.loadTexts:
    al_pb1.setUnits("N/A")


class _Al_pb2_Type(Integer32):
    """Custom type al_pb2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_pb2_Type.__name__ = "Integer32"
_Al_pb2_Object = MibScalar
al_pb2 = _Al_pb2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Al_pb2_Type()
)
al_pb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_pb2.setStatus("current")
if mibBuilder.loadTexts:
    al_pb2.setUnits("N/A")


class _Al_le_Type(Integer32):
    """Custom type al_le based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_le_Type.__name__ = "Integer32"
_Al_le_Object = MibScalar
al_le = _Al_le_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Al_le_Type()
)
al_le.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_le.setStatus("current")
if mibBuilder.loadTexts:
    al_le.setUnits("N/A")


class _Al_idrofrigo_fl1_Type(Integer32):
    """Custom type al_idrofrigo_fl1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idrofrigo_fl1_Type.__name__ = "Integer32"
_Al_idrofrigo_fl1_Object = MibScalar
al_idrofrigo_fl1 = _Al_idrofrigo_fl1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Al_idrofrigo_fl1_Type()
)
al_idrofrigo_fl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idrofrigo_fl1.setStatus("current")
if mibBuilder.loadTexts:
    al_idrofrigo_fl1.setUnits("N/A")


class _Static_press_alarm_Type(Integer32):
    """Custom type static_press_alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Static_press_alarm_Type.__name__ = "Integer32"
_Static_press_alarm_Object = MibScalar
static_press_alarm = _Static_press_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Static_press_alarm_Type()
)
static_press_alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    static_press_alarm.setStatus("current")
if mibBuilder.loadTexts:
    static_press_alarm.setUnits("N/A")


class _W_static_press_alarm_Type(Integer32):
    """Custom type w_static_press_alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_W_static_press_alarm_Type.__name__ = "Integer32"
_W_static_press_alarm_Object = MibScalar
w_static_press_alarm = _W_static_press_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _W_static_press_alarm_Type()
)
w_static_press_alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w_static_press_alarm.setStatus("current")
if mibBuilder.loadTexts:
    w_static_press_alarm.setUnits("N/A")


class _Flow_value_alarm_Type(Integer32):
    """Custom type flow_value_alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Flow_value_alarm_Type.__name__ = "Integer32"
_Flow_value_alarm_Object = MibScalar
flow_value_alarm = _Flow_value_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _Flow_value_alarm_Type()
)
flow_value_alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flow_value_alarm.setStatus("current")
if mibBuilder.loadTexts:
    flow_value_alarm.setUnits("N/A")


class _Al_q_comp1_Type(Integer32):
    """Custom type al_q_comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_comp1_Type.__name__ = "Integer32"
_Al_q_comp1_Object = MibScalar
al_q_comp1 = _Al_q_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _Al_q_comp1_Type()
)
al_q_comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_comp1.setStatus("current")
if mibBuilder.loadTexts:
    al_q_comp1.setUnits("N/A")


class _Al_q_comp2_Type(Integer32):
    """Custom type al_q_comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_comp2_Type.__name__ = "Integer32"
_Al_q_comp2_Object = MibScalar
al_q_comp2 = _Al_q_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Al_q_comp2_Type()
)
al_q_comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_comp2.setStatus("current")
if mibBuilder.loadTexts:
    al_q_comp2.setUnits("N/A")


class _Al_q_comp3_Type(Integer32):
    """Custom type al_q_comp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_comp3_Type.__name__ = "Integer32"
_Al_q_comp3_Object = MibScalar
al_q_comp3 = _Al_q_comp3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Al_q_comp3_Type()
)
al_q_comp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_comp3.setStatus("current")
if mibBuilder.loadTexts:
    al_q_comp3.setUnits("N/A")


class _Al_q_comp4_Type(Integer32):
    """Custom type al_q_comp4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_comp4_Type.__name__ = "Integer32"
_Al_q_comp4_Object = MibScalar
al_q_comp4 = _Al_q_comp4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _Al_q_comp4_Type()
)
al_q_comp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_comp4.setStatus("current")
if mibBuilder.loadTexts:
    al_q_comp4.setUnits("N/A")


class _Al_q_comp5_Type(Integer32):
    """Custom type al_q_comp5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_comp5_Type.__name__ = "Integer32"
_Al_q_comp5_Object = MibScalar
al_q_comp5 = _Al_q_comp5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 16),
    _Al_q_comp5_Type()
)
al_q_comp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_comp5.setStatus("current")
if mibBuilder.loadTexts:
    al_q_comp5.setUnits("N/A")


class _Al_q_comp6_Type(Integer32):
    """Custom type al_q_comp6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_comp6_Type.__name__ = "Integer32"
_Al_q_comp6_Object = MibScalar
al_q_comp6 = _Al_q_comp6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 17),
    _Al_q_comp6_Type()
)
al_q_comp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_comp6.setStatus("current")
if mibBuilder.loadTexts:
    al_q_comp6.setUnits("N/A")


class _Al_q_fan_1_Type(Integer32):
    """Custom type al_q_fan_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan_1_Type.__name__ = "Integer32"
_Al_q_fan_1_Object = MibScalar
al_q_fan_1 = _Al_q_fan_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 18),
    _Al_q_fan_1_Type()
)
al_q_fan_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan_1.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan_1.setUnits("N/A")


class _Al_q_fan_2_Type(Integer32):
    """Custom type al_q_fan_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan_2_Type.__name__ = "Integer32"
_Al_q_fan_2_Object = MibScalar
al_q_fan_2 = _Al_q_fan_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 19),
    _Al_q_fan_2_Type()
)
al_q_fan_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan_2.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan_2.setUnits("N/A")


class _Al_q_fan11_Type(Integer32):
    """Custom type al_q_fan11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan11_Type.__name__ = "Integer32"
_Al_q_fan11_Object = MibScalar
al_q_fan11 = _Al_q_fan11_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 20),
    _Al_q_fan11_Type()
)
al_q_fan11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan11.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan11.setUnits("N/A")


class _Al_q_fan12_Type(Integer32):
    """Custom type al_q_fan12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan12_Type.__name__ = "Integer32"
_Al_q_fan12_Object = MibScalar
al_q_fan12 = _Al_q_fan12_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 21),
    _Al_q_fan12_Type()
)
al_q_fan12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan12.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan12.setUnits("N/A")


class _Al_q_fan13_Type(Integer32):
    """Custom type al_q_fan13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan13_Type.__name__ = "Integer32"
_Al_q_fan13_Object = MibScalar
al_q_fan13 = _Al_q_fan13_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 22),
    _Al_q_fan13_Type()
)
al_q_fan13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan13.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan13.setUnits("N/A")


class _Al_q_fan14_Type(Integer32):
    """Custom type al_q_fan14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan14_Type.__name__ = "Integer32"
_Al_q_fan14_Object = MibScalar
al_q_fan14 = _Al_q_fan14_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _Al_q_fan14_Type()
)
al_q_fan14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan14.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan14.setUnits("N/A")


class _Al_q_fan21_Type(Integer32):
    """Custom type al_q_fan21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan21_Type.__name__ = "Integer32"
_Al_q_fan21_Object = MibScalar
al_q_fan21 = _Al_q_fan21_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _Al_q_fan21_Type()
)
al_q_fan21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan21.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan21.setUnits("N/A")


class _Al_q_fan22_Type(Integer32):
    """Custom type al_q_fan22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan22_Type.__name__ = "Integer32"
_Al_q_fan22_Object = MibScalar
al_q_fan22 = _Al_q_fan22_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 25),
    _Al_q_fan22_Type()
)
al_q_fan22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan22.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan22.setUnits("N/A")


class _Al_q_fan_23_Type(Integer32):
    """Custom type al_q_fan_23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan_23_Type.__name__ = "Integer32"
_Al_q_fan_23_Object = MibScalar
al_q_fan_23 = _Al_q_fan_23_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _Al_q_fan_23_Type()
)
al_q_fan_23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan_23.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan_23.setUnits("N/A")


class _Al_q_fan24_Type(Integer32):
    """Custom type al_q_fan24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fan24_Type.__name__ = "Integer32"
_Al_q_fan24_Object = MibScalar
al_q_fan24 = _Al_q_fan24_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _Al_q_fan24_Type()
)
al_q_fan24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fan24.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fan24.setUnits("N/A")


class _Al_idrofrigo_pump1_Type(Integer32):
    """Custom type al_idrofrigo_pump1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idrofrigo_pump1_Type.__name__ = "Integer32"
_Al_idrofrigo_pump1_Object = MibScalar
al_idrofrigo_pump1 = _Al_idrofrigo_pump1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 28),
    _Al_idrofrigo_pump1_Type()
)
al_idrofrigo_pump1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idrofrigo_pump1.setStatus("current")
if mibBuilder.loadTexts:
    al_idrofrigo_pump1.setUnits("N/A")


class _Al_idrofrigo_pump2_Type(Integer32):
    """Custom type al_idrofrigo_pump2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idrofrigo_pump2_Type.__name__ = "Integer32"
_Al_idrofrigo_pump2_Object = MibScalar
al_idrofrigo_pump2 = _Al_idrofrigo_pump2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _Al_idrofrigo_pump2_Type()
)
al_idrofrigo_pump2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idrofrigo_pump2.setStatus("current")
if mibBuilder.loadTexts:
    al_idrofrigo_pump2.setUnits("N/A")


class _Al_phase_cont_Type(Integer32):
    """Custom type al_phase_cont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_phase_cont_Type.__name__ = "Integer32"
_Al_phase_cont_Object = MibScalar
al_phase_cont = _Al_phase_cont_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _Al_phase_cont_Type()
)
al_phase_cont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_phase_cont.setStatus("current")
if mibBuilder.loadTexts:
    al_phase_cont.setUnits("N/A")


class _Al_door_sw_Type(Integer32):
    """Custom type al_door_sw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_door_sw_Type.__name__ = "Integer32"
_Al_door_sw_Object = MibScalar
al_door_sw = _Al_door_sw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 31),
    _Al_door_sw_Type()
)
al_door_sw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_door_sw.setStatus("current")
if mibBuilder.loadTexts:
    al_door_sw.setUnits("N/A")


class _Compressor_FlowRate_Type(Integer32):
    """Custom type compressor_FlowRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressor_FlowRate_Type.__name__ = "Integer32"
_Compressor_FlowRate_Object = MibScalar
compressor_FlowRate = _Compressor_FlowRate_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 32),
    _Compressor_FlowRate_Type()
)
compressor_FlowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compressor_FlowRate.setStatus("current")
if mibBuilder.loadTexts:
    compressor_FlowRate.setUnits("N/A")


class _Setpoint_inv_pumps_Type(Integer32):
    """Custom type setpoint_inv_pumps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Setpoint_inv_pumps_Type.__name__ = "Integer32"
_Setpoint_inv_pumps_Object = MibScalar
setpoint_inv_pumps = _Setpoint_inv_pumps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _Setpoint_inv_pumps_Type()
)
setpoint_inv_pumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_inv_pumps.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_inv_pumps.setUnits("N/A")


class _Enable_pumps_redundance_Type(Integer32):
    """Custom type enable_pumps_redundance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_pumps_redundance_Type.__name__ = "Integer32"
_Enable_pumps_redundance_Object = MibScalar
enable_pumps_redundance = _Enable_pumps_redundance_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _Enable_pumps_redundance_Type()
)
enable_pumps_redundance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_pumps_redundance.setStatus("current")
if mibBuilder.loadTexts:
    enable_pumps_redundance.setUnits("N/A")


class _Enable_chiller_redundance_Type(Integer32):
    """Custom type enable_chiller_redundance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_chiller_redundance_Type.__name__ = "Integer32"
_Enable_chiller_redundance_Object = MibScalar
enable_chiller_redundance = _Enable_chiller_redundance_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 35),
    _Enable_chiller_redundance_Type()
)
enable_chiller_redundance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_chiller_redundance.setStatus("current")
if mibBuilder.loadTexts:
    enable_chiller_redundance.setUnits("N/A")


class _Status_in_alarm_Type(Integer32):
    """Custom type status_in_alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Status_in_alarm_Type.__name__ = "Integer32"
_Status_in_alarm_Object = MibScalar
status_in_alarm = _Status_in_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 36),
    _Status_in_alarm_Type()
)
status_in_alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    status_in_alarm.setStatus("current")
if mibBuilder.loadTexts:
    status_in_alarm.setUnits("N/A")


class _Compressor_recovery_Type(Integer32):
    """Custom type compressor_recovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressor_recovery_Type.__name__ = "Integer32"
_Compressor_recovery_Object = MibScalar
compressor_recovery = _Compressor_recovery_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _Compressor_recovery_Type()
)
compressor_recovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compressor_recovery.setStatus("current")
if mibBuilder.loadTexts:
    compressor_recovery.setUnits("N/A")


class _Enable_thermal_redundance_Type(Integer32):
    """Custom type enable_thermal_redundance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_thermal_redundance_Type.__name__ = "Integer32"
_Enable_thermal_redundance_Object = MibScalar
enable_thermal_redundance = _Enable_thermal_redundance_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 38),
    _Enable_thermal_redundance_Type()
)
enable_thermal_redundance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_thermal_redundance.setStatus("current")
if mibBuilder.loadTexts:
    enable_thermal_redundance.setUnits("N/A")


class _Enable_multi_pumps_function_Type(Integer32):
    """Custom type enable_multi_pumps_function based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_multi_pumps_function_Type.__name__ = "Integer32"
_Enable_multi_pumps_function_Object = MibScalar
enable_multi_pumps_function = _Enable_multi_pumps_function_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _Enable_multi_pumps_function_Type()
)
enable_multi_pumps_function.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_multi_pumps_function.setStatus("current")
if mibBuilder.loadTexts:
    enable_multi_pumps_function.setUnits("N/A")


class _Enable_pumps_offline_Type(Integer32):
    """Custom type enable_pumps_offline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_pumps_offline_Type.__name__ = "Integer32"
_Enable_pumps_offline_Object = MibScalar
enable_pumps_offline = _Enable_pumps_offline_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 40),
    _Enable_pumps_offline_Type()
)
enable_pumps_offline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_pumps_offline.setStatus("current")
if mibBuilder.loadTexts:
    enable_pumps_offline.setUnits("N/A")


class _Enable_3way_valve_Type(Integer32):
    """Custom type enable_3way_valve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_3way_valve_Type.__name__ = "Integer32"
_Enable_3way_valve_Object = MibScalar
enable_3way_valve = _Enable_3way_valve_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 41),
    _Enable_3way_valve_Type()
)
enable_3way_valve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_3way_valve.setStatus("current")
if mibBuilder.loadTexts:
    enable_3way_valve.setUnits("N/A")


class _Enable_speed_up_FCM_Type(Integer32):
    """Custom type enable_speed_up_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_speed_up_FCM_Type.__name__ = "Integer32"
_Enable_speed_up_FCM_Object = MibScalar
enable_speed_up_FCM = _Enable_speed_up_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 42),
    _Enable_speed_up_FCM_Type()
)
enable_speed_up_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_speed_up_FCM.setStatus("current")
if mibBuilder.loadTexts:
    enable_speed_up_FCM.setUnits("N/A")


class _Enable_soft_start_FCM_Type(Integer32):
    """Custom type enable_soft_start_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_soft_start_FCM_Type.__name__ = "Integer32"
_Enable_soft_start_FCM_Object = MibScalar
enable_soft_start_FCM = _Enable_soft_start_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _Enable_soft_start_FCM_Type()
)
enable_soft_start_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_soft_start_FCM.setStatus("current")
if mibBuilder.loadTexts:
    enable_soft_start_FCM.setUnits("N/A")


class _Enable_freecooling_Type(Integer32):
    """Custom type enable_freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_freecooling_Type.__name__ = "Integer32"
_Enable_freecooling_Object = MibScalar
enable_freecooling = _Enable_freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _Enable_freecooling_Type()
)
enable_freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_freecooling.setStatus("current")
if mibBuilder.loadTexts:
    enable_freecooling.setUnits("N/A")


class _Enable_rot_FIFO_FC_Type(Integer32):
    """Custom type enable_rot_FIFO_FC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_rot_FIFO_FC_Type.__name__ = "Integer32"
_Enable_rot_FIFO_FC_Object = MibScalar
enable_rot_FIFO_FC = _Enable_rot_FIFO_FC_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _Enable_rot_FIFO_FC_Type()
)
enable_rot_FIFO_FC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_rot_FIFO_FC.setStatus("current")
if mibBuilder.loadTexts:
    enable_rot_FIFO_FC.setUnits("N/A")


class _Enable_HT_function_Type(Integer32):
    """Custom type enable_HT_function based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_HT_function_Type.__name__ = "Integer32"
_Enable_HT_function_Object = MibScalar
enable_HT_function = _Enable_HT_function_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _Enable_HT_function_Type()
)
enable_HT_function.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_HT_function.setStatus("current")
if mibBuilder.loadTexts:
    enable_HT_function.setUnits("N/A")


class _Enable_PID_Fc_valve_Type(Integer32):
    """Custom type enable_PID_Fc_valve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_PID_Fc_valve_Type.__name__ = "Integer32"
_Enable_PID_Fc_valve_Object = MibScalar
enable_PID_Fc_valve = _Enable_PID_Fc_valve_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _Enable_PID_Fc_valve_Type()
)
enable_PID_Fc_valve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_PID_Fc_valve.setStatus("current")
if mibBuilder.loadTexts:
    enable_PID_Fc_valve.setUnits("N/A")


class _Enable_Fc_Thermal_Exclusion_Type(Integer32):
    """Custom type enable_Fc_Thermal_Exclusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_Fc_Thermal_Exclusion_Type.__name__ = "Integer32"
_Enable_Fc_Thermal_Exclusion_Object = MibScalar
enable_Fc_Thermal_Exclusion = _Enable_Fc_Thermal_Exclusion_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _Enable_Fc_Thermal_Exclusion_Type()
)
enable_Fc_Thermal_Exclusion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_Fc_Thermal_Exclusion.setStatus("current")
if mibBuilder.loadTexts:
    enable_Fc_Thermal_Exclusion.setUnits("N/A")


class _Manual_Reset_Ext_Drycooler_Alarm_Type(Integer32):
    """Custom type manual_Reset_Ext_Drycooler_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Manual_Reset_Ext_Drycooler_Alarm_Type.__name__ = "Integer32"
_Manual_Reset_Ext_Drycooler_Alarm_Object = MibScalar
manual_Reset_Ext_Drycooler_Alarm = _Manual_Reset_Ext_Drycooler_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _Manual_Reset_Ext_Drycooler_Alarm_Type()
)
manual_Reset_Ext_Drycooler_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manual_Reset_Ext_Drycooler_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    manual_Reset_Ext_Drycooler_Alarm.setUnits("N/A")


class _Enable_static_press_Alarm_Type(Integer32):
    """Custom type enable_static_press_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_static_press_Alarm_Type.__name__ = "Integer32"
_Enable_static_press_Alarm_Object = MibScalar
enable_static_press_Alarm = _Enable_static_press_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 50),
    _Enable_static_press_Alarm_Type()
)
enable_static_press_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_static_press_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    enable_static_press_Alarm.setUnits("N/A")


class _Manual_reset_static_press_Alarm_Type(Integer32):
    """Custom type manual_reset_static_press_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Manual_reset_static_press_Alarm_Type.__name__ = "Integer32"
_Manual_reset_static_press_Alarm_Object = MibScalar
manual_reset_static_press_Alarm = _Manual_reset_static_press_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _Manual_reset_static_press_Alarm_Type()
)
manual_reset_static_press_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manual_reset_static_press_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    manual_reset_static_press_Alarm.setUnits("N/A")


class _Enable_static_press_Warning_Type(Integer32):
    """Custom type enable_static_press_Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_static_press_Warning_Type.__name__ = "Integer32"
_Enable_static_press_Warning_Object = MibScalar
enable_static_press_Warning = _Enable_static_press_Warning_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _Enable_static_press_Warning_Type()
)
enable_static_press_Warning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_static_press_Warning.setStatus("current")
if mibBuilder.loadTexts:
    enable_static_press_Warning.setUnits("N/A")


class _Manual_reset_static_press_Warning_Type(Integer32):
    """Custom type manual_reset_static_press_Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Manual_reset_static_press_Warning_Type.__name__ = "Integer32"
_Manual_reset_static_press_Warning_Object = MibScalar
manual_reset_static_press_Warning = _Manual_reset_static_press_Warning_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _Manual_reset_static_press_Warning_Type()
)
manual_reset_static_press_Warning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manual_reset_static_press_Warning.setStatus("current")
if mibBuilder.loadTexts:
    manual_reset_static_press_Warning.setUnits("N/A")


class _Enable_diff_press_Alarm_Type(Integer32):
    """Custom type enable_diff_press_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_diff_press_Alarm_Type.__name__ = "Integer32"
_Enable_diff_press_Alarm_Object = MibScalar
enable_diff_press_Alarm = _Enable_diff_press_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 54),
    _Enable_diff_press_Alarm_Type()
)
enable_diff_press_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_diff_press_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    enable_diff_press_Alarm.setUnits("N/A")


class _Manual_reset_diff_press_Alarm_Type(Integer32):
    """Custom type manual_reset_diff_press_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Manual_reset_diff_press_Alarm_Type.__name__ = "Integer32"
_Manual_reset_diff_press_Alarm_Object = MibScalar
manual_reset_diff_press_Alarm = _Manual_reset_diff_press_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _Manual_reset_diff_press_Alarm_Type()
)
manual_reset_diff_press_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manual_reset_diff_press_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    manual_reset_diff_press_Alarm.setUnits("N/A")


class _Enable_pressure_recovery_Type(Integer32):
    """Custom type enable_pressure_recovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_pressure_recovery_Type.__name__ = "Integer32"
_Enable_pressure_recovery_Object = MibScalar
enable_pressure_recovery = _Enable_pressure_recovery_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _Enable_pressure_recovery_Type()
)
enable_pressure_recovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_pressure_recovery.setStatus("current")
if mibBuilder.loadTexts:
    enable_pressure_recovery.setUnits("N/A")


class _Enable_Flow_Rate_Alarm_Type(Integer32):
    """Custom type enable_Flow_Rate_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_Flow_Rate_Alarm_Type.__name__ = "Integer32"
_Enable_Flow_Rate_Alarm_Object = MibScalar
enable_Flow_Rate_Alarm = _Enable_Flow_Rate_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 57),
    _Enable_Flow_Rate_Alarm_Type()
)
enable_Flow_Rate_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_Flow_Rate_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    enable_Flow_Rate_Alarm.setUnits("N/A")


class _Manual_reset_Flow_Rate_Alarm_Type(Integer32):
    """Custom type manual_reset_Flow_Rate_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Manual_reset_Flow_Rate_Alarm_Type.__name__ = "Integer32"
_Manual_reset_Flow_Rate_Alarm_Object = MibScalar
manual_reset_Flow_Rate_Alarm = _Manual_reset_Flow_Rate_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 58),
    _Manual_reset_Flow_Rate_Alarm_Type()
)
manual_reset_Flow_Rate_Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manual_reset_Flow_Rate_Alarm.setStatus("current")
if mibBuilder.loadTexts:
    manual_reset_Flow_Rate_Alarm.setUnits("N/A")


class _Enable_Flow_Rate_recovery_Type(Integer32):
    """Custom type enable_Flow_Rate_recovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_Flow_Rate_recovery_Type.__name__ = "Integer32"
_Enable_Flow_Rate_recovery_Object = MibScalar
enable_Flow_Rate_recovery = _Enable_Flow_Rate_recovery_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 59),
    _Enable_Flow_Rate_recovery_Type()
)
enable_Flow_Rate_recovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_Flow_Rate_recovery.setStatus("current")
if mibBuilder.loadTexts:
    enable_Flow_Rate_recovery.setUnits("N/A")


class _Enable_pCOWeb_Type(Integer32):
    """Custom type enable_pCOWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_pCOWeb_Type.__name__ = "Integer32"
_Enable_pCOWeb_Object = MibScalar
enable_pCOWeb = _Enable_pCOWeb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 60),
    _Enable_pCOWeb_Type()
)
enable_pCOWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_pCOWeb.setStatus("current")
if mibBuilder.loadTexts:
    enable_pCOWeb.setUnits("N/A")


class _Fc_single_chiller_Type(Integer32):
    """Custom type fc_single_chiller based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Fc_single_chiller_Type.__name__ = "Integer32"
_Fc_single_chiller_Object = MibScalar
fc_single_chiller = _Fc_single_chiller_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 61),
    _Fc_single_chiller_Type()
)
fc_single_chiller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc_single_chiller.setStatus("current")
if mibBuilder.loadTexts:
    fc_single_chiller.setUnits("N/A")


class _Al_idrofrigo_pump_c_1_Type(Integer32):
    """Custom type al_idrofrigo_pump_c_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idrofrigo_pump_c_1_Type.__name__ = "Integer32"
_Al_idrofrigo_pump_c_1_Object = MibScalar
al_idrofrigo_pump_c_1 = _Al_idrofrigo_pump_c_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 75),
    _Al_idrofrigo_pump_c_1_Type()
)
al_idrofrigo_pump_c_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idrofrigo_pump_c_1.setStatus("current")
if mibBuilder.loadTexts:
    al_idrofrigo_pump_c_1.setUnits("N/A")


class _Al_idrofrigo_pump_c_2_Type(Integer32):
    """Custom type al_idrofrigo_pump_c_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idrofrigo_pump_c_2_Type.__name__ = "Integer32"
_Al_idrofrigo_pump_c_2_Object = MibScalar
al_idrofrigo_pump_c_2 = _Al_idrofrigo_pump_c_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 76),
    _Al_idrofrigo_pump_c_2_Type()
)
al_idrofrigo_pump_c_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idrofrigo_pump_c_2.setStatus("current")
if mibBuilder.loadTexts:
    al_idrofrigo_pump_c_2.setUnits("N/A")


class _Al_idrofrigo_fl_C_Type(Integer32):
    """Custom type al_idrofrigo_fl_C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idrofrigo_fl_C_Type.__name__ = "Integer32"
_Al_idrofrigo_fl_C_Object = MibScalar
al_idrofrigo_fl_C = _Al_idrofrigo_fl_C_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 80),
    _Al_idrofrigo_fl_C_Type()
)
al_idrofrigo_fl_C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idrofrigo_fl_C.setStatus("current")
if mibBuilder.loadTexts:
    al_idrofrigo_fl_C.setUnits("N/A")


class _C11_on_Type(Integer32):
    """Custom type c11_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C11_on_Type.__name__ = "Integer32"
_C11_on_Object = MibScalar
c11_on = _C11_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 100),
    _C11_on_Type()
)
c11_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c11_on.setStatus("current")
if mibBuilder.loadTexts:
    c11_on.setUnits("N/A")


class _C12_on_Type(Integer32):
    """Custom type c12_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C12_on_Type.__name__ = "Integer32"
_C12_on_Object = MibScalar
c12_on = _C12_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 101),
    _C12_on_Type()
)
c12_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c12_on.setStatus("current")
if mibBuilder.loadTexts:
    c12_on.setUnits("N/A")


class _C13_on_Type(Integer32):
    """Custom type c13_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C13_on_Type.__name__ = "Integer32"
_C13_on_Object = MibScalar
c13_on = _C13_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 102),
    _C13_on_Type()
)
c13_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c13_on.setStatus("current")
if mibBuilder.loadTexts:
    c13_on.setUnits("N/A")


class _C21_on_Type(Integer32):
    """Custom type c21_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C21_on_Type.__name__ = "Integer32"
_C21_on_Object = MibScalar
c21_on = _C21_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 103),
    _C21_on_Type()
)
c21_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c21_on.setStatus("current")
if mibBuilder.loadTexts:
    c21_on.setUnits("N/A")


class _C22_on_Type(Integer32):
    """Custom type c22_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C22_on_Type.__name__ = "Integer32"
_C22_on_Object = MibScalar
c22_on = _C22_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 104),
    _C22_on_Type()
)
c22_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c22_on.setStatus("current")
if mibBuilder.loadTexts:
    c22_on.setUnits("N/A")


class _C23_on_Type(Integer32):
    """Custom type c23_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C23_on_Type.__name__ = "Integer32"
_C23_on_Object = MibScalar
c23_on = _C23_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 105),
    _C23_on_Type()
)
c23_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c23_on.setStatus("current")
if mibBuilder.loadTexts:
    c23_on.setUnits("N/A")


class _Pump1_on_Type(Integer32):
    """Custom type pump1_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pump1_on_Type.__name__ = "Integer32"
_Pump1_on_Object = MibScalar
pump1_on = _Pump1_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 106),
    _Pump1_on_Type()
)
pump1_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pump1_on.setStatus("current")
if mibBuilder.loadTexts:
    pump1_on.setUnits("N/A")


class _Pump2_on_Type(Integer32):
    """Custom type pump2_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pump2_on_Type.__name__ = "Integer32"
_Pump2_on_Object = MibScalar
pump2_on = _Pump2_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 107),
    _Pump2_on_Type()
)
pump2_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pump2_on.setStatus("current")
if mibBuilder.loadTexts:
    pump2_on.setUnits("N/A")


class _On_fan_gr1_Type(Integer32):
    """Custom type on_fan_gr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_On_fan_gr1_Type.__name__ = "Integer32"
_On_fan_gr1_Object = MibScalar
on_fan_gr1 = _On_fan_gr1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 108),
    _On_fan_gr1_Type()
)
on_fan_gr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on_fan_gr1.setStatus("current")
if mibBuilder.loadTexts:
    on_fan_gr1.setUnits("N/A")


class _On_fan_gr2_Type(Integer32):
    """Custom type on_fan_gr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_On_fan_gr2_Type.__name__ = "Integer32"
_On_fan_gr2_Object = MibScalar
on_fan_gr2 = _On_fan_gr2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 109),
    _On_fan_gr2_Type()
)
on_fan_gr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on_fan_gr2.setStatus("current")
if mibBuilder.loadTexts:
    on_fan_gr2.setUnits("N/A")


class _Fc_on_Type(Integer32):
    """Custom type fc_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Fc_on_Type.__name__ = "Integer32"
_Fc_on_Object = MibScalar
fc_on = _Fc_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 110),
    _Fc_on_Type()
)
fc_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fc_on.setStatus("current")
if mibBuilder.loadTexts:
    fc_on.setUnits("N/A")


class _En_on_off_rem_Type(Integer32):
    """Custom type en_on_off_rem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_on_off_rem_Type.__name__ = "Integer32"
_En_on_off_rem_Object = MibScalar
en_on_off_rem = _En_on_off_rem_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 130),
    _En_on_off_rem_Type()
)
en_on_off_rem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_on_off_rem.setStatus("current")
if mibBuilder.loadTexts:
    en_on_off_rem.setUnits("N/A")


class _Unit_on_Type(Integer32):
    """Custom type unit_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Unit_on_Type.__name__ = "Integer32"
_Unit_on_Object = MibScalar
unit_on = _Unit_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 131),
    _Unit_on_Type()
)
unit_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit_on.setStatus("current")
if mibBuilder.loadTexts:
    unit_on.setUnits("N/A")


class _Disch_alarm_scw_1_Type(Integer32):
    """Custom type disch_alarm_scw_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Disch_alarm_scw_1_Type.__name__ = "Integer32"
_Disch_alarm_scw_1_Object = MibScalar
disch_alarm_scw_1 = _Disch_alarm_scw_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 148),
    _Disch_alarm_scw_1_Type()
)
disch_alarm_scw_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disch_alarm_scw_1.setStatus("current")
if mibBuilder.loadTexts:
    disch_alarm_scw_1.setUnits("N/A")


class _Disch_alarm_scw_2_Type(Integer32):
    """Custom type disch_alarm_scw_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Disch_alarm_scw_2_Type.__name__ = "Integer32"
_Disch_alarm_scw_2_Object = MibScalar
disch_alarm_scw_2 = _Disch_alarm_scw_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 149),
    _Disch_alarm_scw_2_Type()
)
disch_alarm_scw_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disch_alarm_scw_2.setStatus("current")
if mibBuilder.loadTexts:
    disch_alarm_scw_2.setUnits("N/A")


class _Al_probe_inlet_Type(Integer32):
    """Custom type al_probe_inlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_probe_inlet_Type.__name__ = "Integer32"
_Al_probe_inlet_Object = MibScalar
al_probe_inlet = _Al_probe_inlet_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 150),
    _Al_probe_inlet_Type()
)
al_probe_inlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_probe_inlet.setStatus("current")
if mibBuilder.loadTexts:
    al_probe_inlet.setUnits("N/A")


class _Al_probe_amb_Type(Integer32):
    """Custom type al_probe_amb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_probe_amb_Type.__name__ = "Integer32"
_Al_probe_amb_Object = MibScalar
al_probe_amb = _Al_probe_amb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 151),
    _Al_probe_amb_Type()
)
al_probe_amb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_probe_amb.setStatus("current")
if mibBuilder.loadTexts:
    al_probe_amb.setUnits("N/A")


class _Al_frigo_fl1_Type(Integer32):
    """Custom type al_frigo_fl1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_frigo_fl1_Type.__name__ = "Integer32"
_Al_frigo_fl1_Object = MibScalar
al_frigo_fl1 = _Al_frigo_fl1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 152),
    _Al_frigo_fl1_Type()
)
al_frigo_fl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_frigo_fl1.setStatus("current")
if mibBuilder.loadTexts:
    al_frigo_fl1.setUnits("N/A")


class _Al_idro_pump1_Type(Integer32):
    """Custom type al_idro_pump1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idro_pump1_Type.__name__ = "Integer32"
_Al_idro_pump1_Object = MibScalar
al_idro_pump1 = _Al_idro_pump1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 153),
    _Al_idro_pump1_Type()
)
al_idro_pump1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idro_pump1.setStatus("current")
if mibBuilder.loadTexts:
    al_idro_pump1.setUnits("N/A")


class _Al_idro_pump2_Type(Integer32):
    """Custom type al_idro_pump2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idro_pump2_Type.__name__ = "Integer32"
_Al_idro_pump2_Object = MibScalar
al_idro_pump2 = _Al_idro_pump2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 154),
    _Al_idro_pump2_Type()
)
al_idro_pump2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idro_pump2.setStatus("current")
if mibBuilder.loadTexts:
    al_idro_pump2.setUnits("N/A")


class _Al_idro_fl1_Type(Integer32):
    """Custom type al_idro_fl1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idro_fl1_Type.__name__ = "Integer32"
_Al_idro_fl1_Object = MibScalar
al_idro_fl1 = _Al_idro_fl1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 155),
    _Al_idro_fl1_Type()
)
al_idro_fl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idro_fl1.setStatus("current")
if mibBuilder.loadTexts:
    al_idro_fl1.setUnits("N/A")


class _Al_warning_fl1_Type(Integer32):
    """Custom type al_warning_fl1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_warning_fl1_Type.__name__ = "Integer32"
_Al_warning_fl1_Object = MibScalar
al_warning_fl1 = _Al_warning_fl1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 156),
    _Al_warning_fl1_Type()
)
al_warning_fl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_warning_fl1.setStatus("current")
if mibBuilder.loadTexts:
    al_warning_fl1.setUnits("N/A")


class _Al_hi_water_temp_Type(Integer32):
    """Custom type al_hi_water_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_hi_water_temp_Type.__name__ = "Integer32"
_Al_hi_water_temp_Object = MibScalar
al_hi_water_temp = _Al_hi_water_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 157),
    _Al_hi_water_temp_Type()
)
al_hi_water_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_hi_water_temp.setStatus("current")
if mibBuilder.loadTexts:
    al_hi_water_temp.setUnits("N/A")


class _Al_lo_water_temp_Type(Integer32):
    """Custom type al_lo_water_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_lo_water_temp_Type.__name__ = "Integer32"
_Al_lo_water_temp_Object = MibScalar
al_lo_water_temp = _Al_lo_water_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 158),
    _Al_lo_water_temp_Type()
)
al_lo_water_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_lo_water_temp.setStatus("current")
if mibBuilder.loadTexts:
    al_lo_water_temp.setUnits("N/A")


class _Al_ta_probe1_Type(Integer32):
    """Custom type al_ta_probe1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_ta_probe1_Type.__name__ = "Integer32"
_Al_ta_probe1_Object = MibScalar
al_ta_probe1 = _Al_ta_probe1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 159),
    _Al_ta_probe1_Type()
)
al_ta_probe1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_ta_probe1.setStatus("current")
if mibBuilder.loadTexts:
    al_ta_probe1.setUnits("N/A")


class _Al_hi_press_Type(Integer32):
    """Custom type al_hi_press based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_hi_press_Type.__name__ = "Integer32"
_Al_hi_press_Object = MibScalar
al_hi_press = _Al_hi_press_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 160),
    _Al_hi_press_Type()
)
al_hi_press.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_hi_press.setStatus("current")
if mibBuilder.loadTexts:
    al_hi_press.setUnits("N/A")


class _Al_lo_press_Type(Integer32):
    """Custom type al_lo_press based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_lo_press_Type.__name__ = "Integer32"
_Al_lo_press_Object = MibScalar
al_lo_press = _Al_lo_press_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 161),
    _Al_lo_press_Type()
)
al_lo_press.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_lo_press.setStatus("current")
if mibBuilder.loadTexts:
    al_lo_press.setUnits("N/A")


class _Al_probe_evap_1_Type(Integer32):
    """Custom type al_probe_evap_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_probe_evap_1_Type.__name__ = "Integer32"
_Al_probe_evap_1_Object = MibScalar
al_probe_evap_1 = _Al_probe_evap_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 162),
    _Al_probe_evap_1_Type()
)
al_probe_evap_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_probe_evap_1.setStatus("current")
if mibBuilder.loadTexts:
    al_probe_evap_1.setUnits("N/A")


class _Al_probe_evap_2_Type(Integer32):
    """Custom type al_probe_evap_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_probe_evap_2_Type.__name__ = "Integer32"
_Al_probe_evap_2_Object = MibScalar
al_probe_evap_2 = _Al_probe_evap_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 163),
    _Al_probe_evap_2_Type()
)
al_probe_evap_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_probe_evap_2.setStatus("current")
if mibBuilder.loadTexts:
    al_probe_evap_2.setUnits("N/A")


class _Al_hi_press_1_Type(Integer32):
    """Custom type al_hi_press_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_hi_press_1_Type.__name__ = "Integer32"
_Al_hi_press_1_Object = MibScalar
al_hi_press_1 = _Al_hi_press_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 164),
    _Al_hi_press_1_Type()
)
al_hi_press_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_hi_press_1.setStatus("current")
if mibBuilder.loadTexts:
    al_hi_press_1.setUnits("N/A")


class _Al_hi_press_2_Type(Integer32):
    """Custom type al_hi_press_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_hi_press_2_Type.__name__ = "Integer32"
_Al_hi_press_2_Object = MibScalar
al_hi_press_2 = _Al_hi_press_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 165),
    _Al_hi_press_2_Type()
)
al_hi_press_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_hi_press_2.setStatus("current")
if mibBuilder.loadTexts:
    al_hi_press_2.setUnits("N/A")


class _Al_lo_press_1_Type(Integer32):
    """Custom type al_lo_press_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_lo_press_1_Type.__name__ = "Integer32"
_Al_lo_press_1_Object = MibScalar
al_lo_press_1 = _Al_lo_press_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 166),
    _Al_lo_press_1_Type()
)
al_lo_press_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_lo_press_1.setStatus("current")
if mibBuilder.loadTexts:
    al_lo_press_1.setUnits("N/A")


class _Al_lo_press_2_Type(Integer32):
    """Custom type al_lo_press_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_lo_press_2_Type.__name__ = "Integer32"
_Al_lo_press_2_Object = MibScalar
al_lo_press_2 = _Al_lo_press_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 167),
    _Al_lo_press_2_Type()
)
al_lo_press_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_lo_press_2.setStatus("current")
if mibBuilder.loadTexts:
    al_lo_press_2.setUnits("N/A")


class _Al_probe_tank_Type(Integer32):
    """Custom type al_probe_tank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_probe_tank_Type.__name__ = "Integer32"
_Al_probe_tank_Object = MibScalar
al_probe_tank = _Al_probe_tank_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 168),
    _Al_probe_tank_Type()
)
al_probe_tank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_probe_tank.setStatus("current")
if mibBuilder.loadTexts:
    al_probe_tank.setUnits("N/A")


class _Off_line_1_Type(Integer32):
    """Custom type off_line_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_1_Type.__name__ = "Integer32"
_Off_line_1_Object = MibScalar
off_line_1 = _Off_line_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 169),
    _Off_line_1_Type()
)
off_line_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_1.setStatus("current")
if mibBuilder.loadTexts:
    off_line_1.setUnits("N/A")


class _Off_line_2_Type(Integer32):
    """Custom type off_line_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_2_Type.__name__ = "Integer32"
_Off_line_2_Object = MibScalar
off_line_2 = _Off_line_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 170),
    _Off_line_2_Type()
)
off_line_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_2.setStatus("current")
if mibBuilder.loadTexts:
    off_line_2.setUnits("N/A")


class _Off_line_3_Type(Integer32):
    """Custom type off_line_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_3_Type.__name__ = "Integer32"
_Off_line_3_Object = MibScalar
off_line_3 = _Off_line_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 171),
    _Off_line_3_Type()
)
off_line_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_3.setStatus("current")
if mibBuilder.loadTexts:
    off_line_3.setUnits("N/A")


class _Off_line_4_Type(Integer32):
    """Custom type off_line_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_4_Type.__name__ = "Integer32"
_Off_line_4_Object = MibScalar
off_line_4 = _Off_line_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 172),
    _Off_line_4_Type()
)
off_line_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_4.setStatus("current")
if mibBuilder.loadTexts:
    off_line_4.setUnits("N/A")


class _Off_line_5_Type(Integer32):
    """Custom type off_line_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_5_Type.__name__ = "Integer32"
_Off_line_5_Object = MibScalar
off_line_5 = _Off_line_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 173),
    _Off_line_5_Type()
)
off_line_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_5.setStatus("current")
if mibBuilder.loadTexts:
    off_line_5.setUnits("N/A")


class _Off_line_6_Type(Integer32):
    """Custom type off_line_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_6_Type.__name__ = "Integer32"
_Off_line_6_Object = MibScalar
off_line_6 = _Off_line_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 174),
    _Off_line_6_Type()
)
off_line_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_6.setStatus("current")
if mibBuilder.loadTexts:
    off_line_6.setUnits("N/A")


class _Off_line_7_Type(Integer32):
    """Custom type off_line_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_7_Type.__name__ = "Integer32"
_Off_line_7_Object = MibScalar
off_line_7 = _Off_line_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 175),
    _Off_line_7_Type()
)
off_line_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_7.setStatus("current")
if mibBuilder.loadTexts:
    off_line_7.setUnits("N/A")


class _Off_line_8_Type(Integer32):
    """Custom type off_line_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Off_line_8_Type.__name__ = "Integer32"
_Off_line_8_Object = MibScalar
off_line_8 = _Off_line_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 176),
    _Off_line_8_Type()
)
off_line_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    off_line_8.setStatus("current")
if mibBuilder.loadTexts:
    off_line_8.setUnits("N/A")


class _Al_ta_probe2_Type(Integer32):
    """Custom type al_ta_probe2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_ta_probe2_Type.__name__ = "Integer32"
_Al_ta_probe2_Object = MibScalar
al_ta_probe2 = _Al_ta_probe2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 177),
    _Al_ta_probe2_Type()
)
al_ta_probe2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_ta_probe2.setStatus("current")
if mibBuilder.loadTexts:
    al_ta_probe2.setUnits("N/A")


class _Al_sms_Type(Integer32):
    """Custom type al_sms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_sms_Type.__name__ = "Integer32"
_Al_sms_Object = MibScalar
al_sms = _Al_sms_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 178),
    _Al_sms_Type()
)
al_sms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_sms.setStatus("current")
if mibBuilder.loadTexts:
    al_sms.setUnits("N/A")


class _Al_modem_Type(Integer32):
    """Custom type al_modem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_modem_Type.__name__ = "Integer32"
_Al_modem_Object = MibScalar
al_modem = _Al_modem_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 179),
    _Al_modem_Type()
)
al_modem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_modem.setStatus("current")
if mibBuilder.loadTexts:
    al_modem.setUnits("N/A")


class _Sms_coda_alarm_Type(Integer32):
    """Custom type sms_coda_alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sms_coda_alarm_Type.__name__ = "Integer32"
_Sms_coda_alarm_Object = MibScalar
sms_coda_alarm = _Sms_coda_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 180),
    _Sms_coda_alarm_Type()
)
sms_coda_alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sms_coda_alarm.setStatus("current")
if mibBuilder.loadTexts:
    sms_coda_alarm.setUnits("N/A")


class _Al_probe_fc_Type(Integer32):
    """Custom type al_probe_fc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_probe_fc_Type.__name__ = "Integer32"
_Al_probe_fc_Object = MibScalar
al_probe_fc = _Al_probe_fc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 181),
    _Al_probe_fc_Type()
)
al_probe_fc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_probe_fc.setStatus("current")
if mibBuilder.loadTexts:
    al_probe_fc.setUnits("N/A")


class _Al_maint_pw1_Type(Integer32):
    """Custom type al_maint_pw1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_maint_pw1_Type.__name__ = "Integer32"
_Al_maint_pw1_Object = MibScalar
al_maint_pw1 = _Al_maint_pw1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 182),
    _Al_maint_pw1_Type()
)
al_maint_pw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_maint_pw1.setStatus("current")
if mibBuilder.loadTexts:
    al_maint_pw1.setUnits("N/A")


class _Al_maint_pw2_Type(Integer32):
    """Custom type al_maint_pw2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_maint_pw2_Type.__name__ = "Integer32"
_Al_maint_pw2_Object = MibScalar
al_maint_pw2 = _Al_maint_pw2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 183),
    _Al_maint_pw2_Type()
)
al_maint_pw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_maint_pw2.setStatus("current")
if mibBuilder.loadTexts:
    al_maint_pw2.setUnits("N/A")


class _Al_hi_temp_rid_Type(Integer32):
    """Custom type al_hi_temp_rid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_hi_temp_rid_Type.__name__ = "Integer32"
_Al_hi_temp_rid_Object = MibScalar
al_hi_temp_rid = _Al_hi_temp_rid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 184),
    _Al_hi_temp_rid_Type()
)
al_hi_temp_rid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_hi_temp_rid.setStatus("current")
if mibBuilder.loadTexts:
    al_hi_temp_rid.setUnits("N/A")


class _Al_q_fc_sep_Type(Integer32):
    """Custom type al_q_fc_sep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_q_fc_sep_Type.__name__ = "Integer32"
_Al_q_fc_sep_Object = MibScalar
al_q_fc_sep = _Al_q_fc_sep_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 185),
    _Al_q_fc_sep_Type()
)
al_q_fc_sep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_q_fc_sep.setStatus("current")
if mibBuilder.loadTexts:
    al_q_fc_sep.setUnits("N/A")


class _Al_p_wat2_Type(Integer32):
    """Custom type al_p_wat2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_p_wat2_Type.__name__ = "Integer32"
_Al_p_wat2_Object = MibScalar
al_p_wat2 = _Al_p_wat2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 186),
    _Al_p_wat2_Type()
)
al_p_wat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_p_wat2.setStatus("current")
if mibBuilder.loadTexts:
    al_p_wat2.setUnits("N/A")


class _Al_p_wat1_Type(Integer32):
    """Custom type al_p_wat1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_p_wat1_Type.__name__ = "Integer32"
_Al_p_wat1_Object = MibScalar
al_p_wat1 = _Al_p_wat1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 187),
    _Al_p_wat1_Type()
)
al_p_wat1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_p_wat1.setStatus("current")
if mibBuilder.loadTexts:
    al_p_wat1.setUnits("N/A")


class _Al_foult_flow_p1_Type(Integer32):
    """Custom type al_foult_flow_p1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_foult_flow_p1_Type.__name__ = "Integer32"
_Al_foult_flow_p1_Object = MibScalar
al_foult_flow_p1 = _Al_foult_flow_p1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 188),
    _Al_foult_flow_p1_Type()
)
al_foult_flow_p1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_foult_flow_p1.setStatus("current")
if mibBuilder.loadTexts:
    al_foult_flow_p1.setUnits("N/A")


class _Al_foult_flow_p2_Type(Integer32):
    """Custom type al_foult_flow_p2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_foult_flow_p2_Type.__name__ = "Integer32"
_Al_foult_flow_p2_Object = MibScalar
al_foult_flow_p2 = _Al_foult_flow_p2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 189),
    _Al_foult_flow_p2_Type()
)
al_foult_flow_p2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_foult_flow_p2.setStatus("current")
if mibBuilder.loadTexts:
    al_foult_flow_p2.setUnits("N/A")


class _Al_foult_fl1_p1_Type(Integer32):
    """Custom type al_foult_fl1_p1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_foult_fl1_p1_Type.__name__ = "Integer32"
_Al_foult_fl1_p1_Object = MibScalar
al_foult_fl1_p1 = _Al_foult_fl1_p1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 190),
    _Al_foult_fl1_p1_Type()
)
al_foult_fl1_p1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_foult_fl1_p1.setStatus("current")
if mibBuilder.loadTexts:
    al_foult_fl1_p1.setUnits("N/A")


class _Al_foult_fl1_p2_Type(Integer32):
    """Custom type al_foult_fl1_p2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_foult_fl1_p2_Type.__name__ = "Integer32"
_Al_foult_fl1_p2_Object = MibScalar
al_foult_fl1_p2 = _Al_foult_fl1_p2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 191),
    _Al_foult_fl1_p2_Type()
)
al_foult_fl1_p2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_foult_fl1_p2.setStatus("current")
if mibBuilder.loadTexts:
    al_foult_fl1_p2.setUnits("N/A")


class _Al_warning_le_Type(Integer32):
    """Custom type al_warning_le based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_warning_le_Type.__name__ = "Integer32"
_Al_warning_le_Object = MibScalar
al_warning_le = _Al_warning_le_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 192),
    _Al_warning_le_Type()
)
al_warning_le.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_warning_le.setStatus("current")
if mibBuilder.loadTexts:
    al_warning_le.setUnits("N/A")


class _Al_frigo_fl_C_Type(Integer32):
    """Custom type al_frigo_fl_C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_frigo_fl_C_Type.__name__ = "Integer32"
_Al_frigo_fl_C_Object = MibScalar
al_frigo_fl_C = _Al_frigo_fl_C_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 193),
    _Al_frigo_fl_C_Type()
)
al_frigo_fl_C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_frigo_fl_C.setStatus("current")
if mibBuilder.loadTexts:
    al_frigo_fl_C.setUnits("N/A")


class _Al_idro_pump_c_1_Type(Integer32):
    """Custom type al_idro_pump_c_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idro_pump_c_1_Type.__name__ = "Integer32"
_Al_idro_pump_c_1_Object = MibScalar
al_idro_pump_c_1 = _Al_idro_pump_c_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 194),
    _Al_idro_pump_c_1_Type()
)
al_idro_pump_c_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idro_pump_c_1.setStatus("current")
if mibBuilder.loadTexts:
    al_idro_pump_c_1.setUnits("N/A")


class _Al_idro_pump_c_2_Type(Integer32):
    """Custom type al_idro_pump_c_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idro_pump_c_2_Type.__name__ = "Integer32"
_Al_idro_pump_c_2_Object = MibScalar
al_idro_pump_c_2 = _Al_idro_pump_c_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 195),
    _Al_idro_pump_c_2_Type()
)
al_idro_pump_c_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idro_pump_c_2.setStatus("current")
if mibBuilder.loadTexts:
    al_idro_pump_c_2.setUnits("N/A")


class _Al_idro_fl_C_Type(Integer32):
    """Custom type al_idro_fl_C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_idro_fl_C_Type.__name__ = "Integer32"
_Al_idro_fl_C_Object = MibScalar
al_idro_fl_C = _Al_idro_fl_C_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 196),
    _Al_idro_fl_C_Type()
)
al_idro_fl_C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_idro_fl_C.setStatus("current")
if mibBuilder.loadTexts:
    al_idro_fl_C.setUnits("N/A")


class _Al_warning_fl_C_Type(Integer32):
    """Custom type al_warning_fl_C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_warning_fl_C_Type.__name__ = "Integer32"
_Al_warning_fl_C_Object = MibScalar
al_warning_fl_C = _Al_warning_fl_C_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 197),
    _Al_warning_fl_C_Type()
)
al_warning_fl_C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_warning_fl_C.setStatus("current")
if mibBuilder.loadTexts:
    al_warning_fl_C.setUnits("N/A")


class _Al_foul_fl_C_p1_Type(Integer32):
    """Custom type al_foul_fl_C_p1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_foul_fl_C_p1_Type.__name__ = "Integer32"
_Al_foul_fl_C_p1_Object = MibScalar
al_foul_fl_C_p1 = _Al_foul_fl_C_p1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 198),
    _Al_foul_fl_C_p1_Type()
)
al_foul_fl_C_p1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_foul_fl_C_p1.setStatus("current")
if mibBuilder.loadTexts:
    al_foul_fl_C_p1.setUnits("N/A")


class _Al_foul_fl_C_p2_Type(Integer32):
    """Custom type al_foul_fl_C_p2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Al_foul_fl_C_p2_Type.__name__ = "Integer32"
_Al_foul_fl_C_p2_Object = MibScalar
al_foul_fl_C_p2 = _Al_foul_fl_C_p2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 199),
    _Al_foul_fl_C_p2_Type()
)
al_foul_fl_C_p2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    al_foul_fl_C_p2.setStatus("current")
if mibBuilder.loadTexts:
    al_foul_fl_C_p2.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Setpoint_antifreeze1_Type(Integer32):
    """Custom type setpoint_antifreeze1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_antifreeze1_Type.__name__ = "Integer32"
_Setpoint_antifreeze1_Object = MibScalar
setpoint_antifreeze1 = _Setpoint_antifreeze1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Setpoint_antifreeze1_Type()
)
setpoint_antifreeze1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_antifreeze1.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_antifreeze1.setUnits("N/A")


class _Setpoint_antifreeze2_Type(Integer32):
    """Custom type setpoint_antifreeze2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_antifreeze2_Type.__name__ = "Integer32"
_Setpoint_antifreeze2_Object = MibScalar
setpoint_antifreeze2 = _Setpoint_antifreeze2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Setpoint_antifreeze2_Type()
)
setpoint_antifreeze2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_antifreeze2.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_antifreeze2.setUnits("N/A")


class _Setpoint_Compensation_Type(Integer32):
    """Custom type setpoint_Compensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_Compensation_Type.__name__ = "Integer32"
_Setpoint_Compensation_Object = MibScalar
setpoint_Compensation = _Setpoint_Compensation_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Setpoint_Compensation_Type()
)
setpoint_Compensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_Compensation.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_Compensation.setUnits("N/A")


class _Hysteresis_Compensation_Type(Integer32):
    """Custom type hysteresis_Compensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Compensation_Type.__name__ = "Integer32"
_Hysteresis_Compensation_Object = MibScalar
hysteresis_Compensation = _Hysteresis_Compensation_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Hysteresis_Compensation_Type()
)
hysteresis_Compensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Compensation.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Compensation.setUnits("N/A")


class _Max_Compensation_Type(Integer32):
    """Custom type max_Compensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_Compensation_Type.__name__ = "Integer32"
_Max_Compensation_Object = MibScalar
max_Compensation = _Max_Compensation_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Max_Compensation_Type()
)
max_Compensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Compensation.setStatus("current")
if mibBuilder.loadTexts:
    max_Compensation.setUnits("N/A")


class _Setpoint_Differential_Type(Integer32):
    """Custom type setpoint_Differential based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_Differential_Type.__name__ = "Integer32"
_Setpoint_Differential_Object = MibScalar
setpoint_Differential = _Setpoint_Differential_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Setpoint_Differential_Type()
)
setpoint_Differential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_Differential.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_Differential.setUnits("N/A")


class _High_Limit_Type(Integer32):
    """Custom type high_Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_High_Limit_Type.__name__ = "Integer32"
_High_Limit_Object = MibScalar
high_Limit = _High_Limit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _High_Limit_Type()
)
high_Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    high_Limit.setStatus("current")
if mibBuilder.loadTexts:
    high_Limit.setUnits("N/A")


class _Low_Limit_Type(Integer32):
    """Custom type low_Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Low_Limit_Type.__name__ = "Integer32"
_Low_Limit_Object = MibScalar
low_Limit = _Low_Limit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Low_Limit_Type()
)
low_Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    low_Limit.setStatus("current")
if mibBuilder.loadTexts:
    low_Limit.setUnits("N/A")


class _Max_Setpoint_Differential_Type(Integer32):
    """Custom type max_Setpoint_Differential based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_Setpoint_Differential_Type.__name__ = "Integer32"
_Max_Setpoint_Differential_Object = MibScalar
max_Setpoint_Differential = _Max_Setpoint_Differential_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Max_Setpoint_Differential_Type()
)
max_Setpoint_Differential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Setpoint_Differential.setStatus("current")
if mibBuilder.loadTexts:
    max_Setpoint_Differential.setUnits("N/A")


class _Min_Setpoint_Differential_Type(Integer32):
    """Custom type min_Setpoint_Differential based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_Setpoint_Differential_Type.__name__ = "Integer32"
_Min_Setpoint_Differential_Object = MibScalar
min_Setpoint_Differential = _Min_Setpoint_Differential_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Min_Setpoint_Differential_Type()
)
min_Setpoint_Differential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_Setpoint_Differential.setStatus("current")
if mibBuilder.loadTexts:
    min_Setpoint_Differential.setUnits("N/A")


class _Setpoint_ASB_Inverter_pumps_Type(Integer32):
    """Custom type setpoint_ASB_Inverter_pumps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_ASB_Inverter_pumps_Type.__name__ = "Integer32"
_Setpoint_ASB_Inverter_pumps_Object = MibScalar
setpoint_ASB_Inverter_pumps = _Setpoint_ASB_Inverter_pumps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Setpoint_ASB_Inverter_pumps_Type()
)
setpoint_ASB_Inverter_pumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_ASB_Inverter_pumps.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_ASB_Inverter_pumps.setUnits("N/A")


class _Setpoint_DIFF_Inverter_pumps_Type(Integer32):
    """Custom type setpoint_DIFF_Inverter_pumps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_DIFF_Inverter_pumps_Type.__name__ = "Integer32"
_Setpoint_DIFF_Inverter_pumps_Object = MibScalar
setpoint_DIFF_Inverter_pumps = _Setpoint_DIFF_Inverter_pumps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _Setpoint_DIFF_Inverter_pumps_Type()
)
setpoint_DIFF_Inverter_pumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_DIFF_Inverter_pumps.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_DIFF_Inverter_pumps.setUnits("N/A")


class _Pressure_Out_Type(Integer32):
    """Custom type pressure_Out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Pressure_Out_Type.__name__ = "Integer32"
_Pressure_Out_Object = MibScalar
pressure_Out = _Pressure_Out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Pressure_Out_Type()
)
pressure_Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressure_Out.setStatus("current")
if mibBuilder.loadTexts:
    pressure_Out.setUnits("N/A")


class _Proportional_Band_Inverter_Pumps_PID_Type(Integer32):
    """Custom type proportional_Band_Inverter_Pumps_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Proportional_Band_Inverter_Pumps_PID_Type.__name__ = "Integer32"
_Proportional_Band_Inverter_Pumps_PID_Object = MibScalar
proportional_Band_Inverter_Pumps_PID = _Proportional_Band_Inverter_Pumps_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _Proportional_Band_Inverter_Pumps_PID_Type()
)
proportional_Band_Inverter_Pumps_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proportional_Band_Inverter_Pumps_PID.setStatus("current")
if mibBuilder.loadTexts:
    proportional_Band_Inverter_Pumps_PID.setUnits("N/A")


class _Integral_Time_Inverter_Pumps_PID_Type(Integer32):
    """Custom type integral_Time_Inverter_Pumps_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Integral_Time_Inverter_Pumps_PID_Type.__name__ = "Integer32"
_Integral_Time_Inverter_Pumps_PID_Object = MibScalar
integral_Time_Inverter_Pumps_PID = _Integral_Time_Inverter_Pumps_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 15),
    _Integral_Time_Inverter_Pumps_PID_Type()
)
integral_Time_Inverter_Pumps_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integral_Time_Inverter_Pumps_PID.setStatus("current")
if mibBuilder.loadTexts:
    integral_Time_Inverter_Pumps_PID.setUnits("N/A")


class _Derivative_Time_Inverter_Pumps_PID_Type(Integer32):
    """Custom type derivative_Time_Inverter_Pumps_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Derivative_Time_Inverter_Pumps_PID_Type.__name__ = "Integer32"
_Derivative_Time_Inverter_Pumps_PID_Object = MibScalar
derivative_Time_Inverter_Pumps_PID = _Derivative_Time_Inverter_Pumps_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 16),
    _Derivative_Time_Inverter_Pumps_PID_Type()
)
derivative_Time_Inverter_Pumps_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    derivative_Time_Inverter_Pumps_PID.setStatus("current")
if mibBuilder.loadTexts:
    derivative_Time_Inverter_Pumps_PID.setUnits("N/A")


class _Hysteresis_Thermal_redundance_Type(Integer32):
    """Custom type hysteresis_Thermal_redundance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Thermal_redundance_Type.__name__ = "Integer32"
_Hysteresis_Thermal_redundance_Object = MibScalar
hysteresis_Thermal_redundance = _Hysteresis_Thermal_redundance_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 17),
    _Hysteresis_Thermal_redundance_Type()
)
hysteresis_Thermal_redundance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Thermal_redundance.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Thermal_redundance.setUnits("N/A")


class _Min_Opening_3Way_Valve_Hydraulic_Type(Integer32):
    """Custom type min_Opening_3Way_Valve_Hydraulic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_Opening_3Way_Valve_Hydraulic_Type.__name__ = "Integer32"
_Min_Opening_3Way_Valve_Hydraulic_Object = MibScalar
min_Opening_3Way_Valve_Hydraulic = _Min_Opening_3Way_Valve_Hydraulic_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 18),
    _Min_Opening_3Way_Valve_Hydraulic_Type()
)
min_Opening_3Way_Valve_Hydraulic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_Opening_3Way_Valve_Hydraulic.setStatus("current")
if mibBuilder.loadTexts:
    min_Opening_3Way_Valve_Hydraulic.setUnits("N/A")


class _Max_Opening_3Way_Valve_Hydraulic_Type(Integer32):
    """Custom type max_Opening_3Way_Valve_Hydraulic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_Opening_3Way_Valve_Hydraulic_Type.__name__ = "Integer32"
_Max_Opening_3Way_Valve_Hydraulic_Object = MibScalar
max_Opening_3Way_Valve_Hydraulic = _Max_Opening_3Way_Valve_Hydraulic_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 19),
    _Max_Opening_3Way_Valve_Hydraulic_Type()
)
max_Opening_3Way_Valve_Hydraulic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Opening_3Way_Valve_Hydraulic.setStatus("current")
if mibBuilder.loadTexts:
    max_Opening_3Way_Valve_Hydraulic.setUnits("N/A")


class _Proportional_Band_3Way_Valve_Hydrauli_PID_Type(Integer32):
    """Custom type proportional_Band_3Way_Valve_Hydrauli_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Proportional_Band_3Way_Valve_Hydrauli_PID_Type.__name__ = "Integer32"
_Proportional_Band_3Way_Valve_Hydrauli_PID_Object = MibScalar
proportional_Band_3Way_Valve_Hydrauli_PID = _Proportional_Band_3Way_Valve_Hydrauli_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 20),
    _Proportional_Band_3Way_Valve_Hydrauli_PID_Type()
)
proportional_Band_3Way_Valve_Hydrauli_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proportional_Band_3Way_Valve_Hydrauli_PID.setStatus("current")
if mibBuilder.loadTexts:
    proportional_Band_3Way_Valve_Hydrauli_PID.setUnits("N/A")


class _Setpoint_FCM_Type(Integer32):
    """Custom type setpoint_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_FCM_Type.__name__ = "Integer32"
_Setpoint_FCM_Object = MibScalar
setpoint_FCM = _Setpoint_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 21),
    _Setpoint_FCM_Type()
)
setpoint_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_FCM.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_FCM.setUnits("N/A")


class _Hysteresis_FCM_Type(Integer32):
    """Custom type hysteresis_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_FCM_Type.__name__ = "Integer32"
_Hysteresis_FCM_Object = MibScalar
hysteresis_FCM = _Hysteresis_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 22),
    _Hysteresis_FCM_Type()
)
hysteresis_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_FCM.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_FCM.setUnits("N/A")


class _Max_Out_Speed_FCM_Type(Integer32):
    """Custom type max_Out_Speed_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_Out_Speed_FCM_Type.__name__ = "Integer32"
_Max_Out_Speed_FCM_Object = MibScalar
max_Out_Speed_FCM = _Max_Out_Speed_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 23),
    _Max_Out_Speed_FCM_Type()
)
max_Out_Speed_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Out_Speed_FCM.setStatus("current")
if mibBuilder.loadTexts:
    max_Out_Speed_FCM.setUnits("N/A")


class _Min_Out_Speed_FCM_Type(Integer32):
    """Custom type min_Out_Speed_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_Out_Speed_FCM_Type.__name__ = "Integer32"
_Min_Out_Speed_FCM_Object = MibScalar
min_Out_Speed_FCM = _Min_Out_Speed_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 24),
    _Min_Out_Speed_FCM_Type()
)
min_Out_Speed_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_Out_Speed_FCM.setStatus("current")
if mibBuilder.loadTexts:
    min_Out_Speed_FCM.setUnits("N/A")


class _Hysteresis_Cut_off_FCM_Type(Integer32):
    """Custom type hysteresis_Cut_off_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Cut_off_FCM_Type.__name__ = "Integer32"
_Hysteresis_Cut_off_FCM_Object = MibScalar
hysteresis_Cut_off_FCM = _Hysteresis_Cut_off_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 25),
    _Hysteresis_Cut_off_FCM_Type()
)
hysteresis_Cut_off_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Cut_off_FCM.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Cut_off_FCM.setUnits("N/A")


class _Max_Pressure_Alarm_FCM_Type(Integer32):
    """Custom type max_Pressure_Alarm_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_Pressure_Alarm_FCM_Type.__name__ = "Integer32"
_Max_Pressure_Alarm_FCM_Object = MibScalar
max_Pressure_Alarm_FCM = _Max_Pressure_Alarm_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 26),
    _Max_Pressure_Alarm_FCM_Type()
)
max_Pressure_Alarm_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Pressure_Alarm_FCM.setStatus("current")
if mibBuilder.loadTexts:
    max_Pressure_Alarm_FCM.setUnits("N/A")


class _Hysteresis_Max_Pressure_Alarm_FCM_Type(Integer32):
    """Custom type hysteresis_Max_Pressure_Alarm_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Max_Pressure_Alarm_FCM_Type.__name__ = "Integer32"
_Hysteresis_Max_Pressure_Alarm_FCM_Object = MibScalar
hysteresis_Max_Pressure_Alarm_FCM = _Hysteresis_Max_Pressure_Alarm_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 27),
    _Hysteresis_Max_Pressure_Alarm_FCM_Type()
)
hysteresis_Max_Pressure_Alarm_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Max_Pressure_Alarm_FCM.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Max_Pressure_Alarm_FCM.setUnits("N/A")


class _Max_Out_FCM_Type(Integer32):
    """Custom type max_Out_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_Out_FCM_Type.__name__ = "Integer32"
_Max_Out_FCM_Object = MibScalar
max_Out_FCM = _Max_Out_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 28),
    _Max_Out_FCM_Type()
)
max_Out_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Out_FCM.setStatus("current")
if mibBuilder.loadTexts:
    max_Out_FCM.setUnits("N/A")


class _Min_Pressure_Alarm_FCM_Type(Integer32):
    """Custom type min_Pressure_Alarm_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_Pressure_Alarm_FCM_Type.__name__ = "Integer32"
_Min_Pressure_Alarm_FCM_Object = MibScalar
min_Pressure_Alarm_FCM = _Min_Pressure_Alarm_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 29),
    _Min_Pressure_Alarm_FCM_Type()
)
min_Pressure_Alarm_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_Pressure_Alarm_FCM.setStatus("current")
if mibBuilder.loadTexts:
    min_Pressure_Alarm_FCM.setUnits("N/A")


class _Hysteresis_Min_Pressure_Alarm_FCM_Type(Integer32):
    """Custom type hysteresis_Min_Pressure_Alarm_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Min_Pressure_Alarm_FCM_Type.__name__ = "Integer32"
_Hysteresis_Min_Pressure_Alarm_FCM_Object = MibScalar
hysteresis_Min_Pressure_Alarm_FCM = _Hysteresis_Min_Pressure_Alarm_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 30),
    _Hysteresis_Min_Pressure_Alarm_FCM_Type()
)
hysteresis_Min_Pressure_Alarm_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Min_Pressure_Alarm_FCM.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Min_Pressure_Alarm_FCM.setUnits("N/A")


class _Min_Out_FCM_Type(Integer32):
    """Custom type min_Out_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_Out_FCM_Type.__name__ = "Integer32"
_Min_Out_FCM_Object = MibScalar
min_Out_FCM = _Min_Out_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 31),
    _Min_Out_FCM_Type()
)
min_Out_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_Out_FCM.setStatus("current")
if mibBuilder.loadTexts:
    min_Out_FCM.setUnits("N/A")


class _Delta_Freecooling_Type(Integer32):
    """Custom type delta_Freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Delta_Freecooling_Type.__name__ = "Integer32"
_Delta_Freecooling_Object = MibScalar
delta_Freecooling = _Delta_Freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 32),
    _Delta_Freecooling_Type()
)
delta_Freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delta_Freecooling.setStatus("current")
if mibBuilder.loadTexts:
    delta_Freecooling.setUnits("N/A")


class _Hysteresis_Freecooling_Type(Integer32):
    """Custom type hysteresis_Freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Freecooling_Type.__name__ = "Integer32"
_Hysteresis_Freecooling_Object = MibScalar
hysteresis_Freecooling = _Hysteresis_Freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 33),
    _Hysteresis_Freecooling_Type()
)
hysteresis_Freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Freecooling.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Freecooling.setUnits("N/A")


class _Proportional_Band_Freecooling_PID_Type(Integer32):
    """Custom type proportional_Band_Freecooling_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Proportional_Band_Freecooling_PID_Type.__name__ = "Integer32"
_Proportional_Band_Freecooling_PID_Object = MibScalar
proportional_Band_Freecooling_PID = _Proportional_Band_Freecooling_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 34),
    _Proportional_Band_Freecooling_PID_Type()
)
proportional_Band_Freecooling_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proportional_Band_Freecooling_PID.setStatus("current")
if mibBuilder.loadTexts:
    proportional_Band_Freecooling_PID.setUnits("N/A")


class _Offset_Freecooling_PID_Type(Integer32):
    """Custom type offset_Freecooling_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Offset_Freecooling_PID_Type.__name__ = "Integer32"
_Offset_Freecooling_PID_Object = MibScalar
offset_Freecooling_PID = _Offset_Freecooling_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 35),
    _Offset_Freecooling_PID_Type()
)
offset_Freecooling_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offset_Freecooling_PID.setStatus("current")
if mibBuilder.loadTexts:
    offset_Freecooling_PID.setUnits("N/A")


class _Temperature_Overlap_Freecooling_Type(Integer32):
    """Custom type temperature_Overlap_Freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Temperature_Overlap_Freecooling_Type.__name__ = "Integer32"
_Temperature_Overlap_Freecooling_Object = MibScalar
temperature_Overlap_Freecooling = _Temperature_Overlap_Freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 36),
    _Temperature_Overlap_Freecooling_Type()
)
temperature_Overlap_Freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperature_Overlap_Freecooling.setStatus("current")
if mibBuilder.loadTexts:
    temperature_Overlap_Freecooling.setUnits("N/A")


class _Min_out_freecooling_Type(Integer32):
    """Custom type min_out_freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_out_freecooling_Type.__name__ = "Integer32"
_Min_out_freecooling_Object = MibScalar
min_out_freecooling = _Min_out_freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 37),
    _Min_out_freecooling_Type()
)
min_out_freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_out_freecooling.setStatus("current")
if mibBuilder.loadTexts:
    min_out_freecooling.setUnits("N/A")


class _Neutral_zone_K_costant_Type(Integer32):
    """Custom type neutral_zone_K_costant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Neutral_zone_K_costant_Type.__name__ = "Integer32"
_Neutral_zone_K_costant_Object = MibScalar
neutral_zone_K_costant = _Neutral_zone_K_costant_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 38),
    _Neutral_zone_K_costant_Type()
)
neutral_zone_K_costant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neutral_zone_K_costant.setStatus("current")
if mibBuilder.loadTexts:
    neutral_zone_K_costant.setUnits("N/A")


class _Neutral_zone_V_variable_Type(Integer32):
    """Custom type neutral_zone_V_variable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Neutral_zone_V_variable_Type.__name__ = "Integer32"
_Neutral_zone_V_variable_Object = MibScalar
neutral_zone_V_variable = _Neutral_zone_V_variable_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 39),
    _Neutral_zone_V_variable_Type()
)
neutral_zone_V_variable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neutral_zone_V_variable.setStatus("current")
if mibBuilder.loadTexts:
    neutral_zone_V_variable.setUnits("N/A")


class _Proportional_Band_freecooling_Valve_PID_Type(Integer32):
    """Custom type proportional_Band_freecooling_Valve_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Proportional_Band_freecooling_Valve_PID_Type.__name__ = "Integer32"
_Proportional_Band_freecooling_Valve_PID_Object = MibScalar
proportional_Band_freecooling_Valve_PID = _Proportional_Band_freecooling_Valve_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 40),
    _Proportional_Band_freecooling_Valve_PID_Type()
)
proportional_Band_freecooling_Valve_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proportional_Band_freecooling_Valve_PID.setStatus("current")
if mibBuilder.loadTexts:
    proportional_Band_freecooling_Valve_PID.setUnits("N/A")


class _Offset_Freecooling_Valve_PID_Type(Integer32):
    """Custom type offset_Freecooling_Valve_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Offset_Freecooling_Valve_PID_Type.__name__ = "Integer32"
_Offset_Freecooling_Valve_PID_Object = MibScalar
offset_Freecooling_Valve_PID = _Offset_Freecooling_Valve_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 41),
    _Offset_Freecooling_Valve_PID_Type()
)
offset_Freecooling_Valve_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offset_Freecooling_Valve_PID.setStatus("current")
if mibBuilder.loadTexts:
    offset_Freecooling_Valve_PID.setUnits("N/A")


class _Temperature_A_B_Type(Integer32):
    """Custom type temperature_A_B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Temperature_A_B_Type.__name__ = "Integer32"
_Temperature_A_B_Object = MibScalar
temperature_A_B = _Temperature_A_B_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 42),
    _Temperature_A_B_Type()
)
temperature_A_B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature_A_B.setStatus("current")
if mibBuilder.loadTexts:
    temperature_A_B.setUnits("N/A")


class _Delta_Thermal_Excusion_Freecoling_Type(Integer32):
    """Custom type delta_Thermal_Excusion_Freecoling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Delta_Thermal_Excusion_Freecoling_Type.__name__ = "Integer32"
_Delta_Thermal_Excusion_Freecoling_Object = MibScalar
delta_Thermal_Excusion_Freecoling = _Delta_Thermal_Excusion_Freecoling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 43),
    _Delta_Thermal_Excusion_Freecoling_Type()
)
delta_Thermal_Excusion_Freecoling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delta_Thermal_Excusion_Freecoling.setStatus("current")
if mibBuilder.loadTexts:
    delta_Thermal_Excusion_Freecoling.setUnits("N/A")


class _Hysteresis_Thermal_Excusion_Freecoling_Type(Integer32):
    """Custom type hysteresis_Thermal_Excusion_Freecoling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Hysteresis_Thermal_Excusion_Freecoling_Type.__name__ = "Integer32"
_Hysteresis_Thermal_Excusion_Freecoling_Object = MibScalar
hysteresis_Thermal_Excusion_Freecoling = _Hysteresis_Thermal_Excusion_Freecoling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 44),
    _Hysteresis_Thermal_Excusion_Freecoling_Type()
)
hysteresis_Thermal_Excusion_Freecoling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis_Thermal_Excusion_Freecoling.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis_Thermal_Excusion_Freecoling.setUnits("N/A")


class _Alarm_Setpoint_Static_Pressure_Hydraulic_circuit_Type(Integer32):
    """Custom type alarm_Setpoint_Static_Pressure_Hydraulic_circuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Alarm_Setpoint_Static_Pressure_Hydraulic_circuit_Type.__name__ = "Integer32"
_Alarm_Setpoint_Static_Pressure_Hydraulic_circuit_Object = MibScalar
alarm_Setpoint_Static_Pressure_Hydraulic_circuit = _Alarm_Setpoint_Static_Pressure_Hydraulic_circuit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 45),
    _Alarm_Setpoint_Static_Pressure_Hydraulic_circuit_Type()
)
alarm_Setpoint_Static_Pressure_Hydraulic_circuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_Setpoint_Static_Pressure_Hydraulic_circuit.setStatus("current")
if mibBuilder.loadTexts:
    alarm_Setpoint_Static_Pressure_Hydraulic_circuit.setUnits("N/A")


class _Warnig_Setpoint_Static_Pressure_Hydraulic_circuit_Type(Integer32):
    """Custom type warnig_Setpoint_Static_Pressure_Hydraulic_circuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Warnig_Setpoint_Static_Pressure_Hydraulic_circuit_Type.__name__ = "Integer32"
_Warnig_Setpoint_Static_Pressure_Hydraulic_circuit_Object = MibScalar
warnig_Setpoint_Static_Pressure_Hydraulic_circuit = _Warnig_Setpoint_Static_Pressure_Hydraulic_circuit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 46),
    _Warnig_Setpoint_Static_Pressure_Hydraulic_circuit_Type()
)
warnig_Setpoint_Static_Pressure_Hydraulic_circuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    warnig_Setpoint_Static_Pressure_Hydraulic_circuit.setStatus("current")
if mibBuilder.loadTexts:
    warnig_Setpoint_Static_Pressure_Hydraulic_circuit.setUnits("N/A")


class _Alarm_Setpoint_Differential_Pressure_Hydraulic_circuit_Type(Integer32):
    """Custom type alarm_Setpoint_Differential_Pressure_Hydraulic_circuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Alarm_Setpoint_Differential_Pressure_Hydraulic_circuit_Type.__name__ = "Integer32"
_Alarm_Setpoint_Differential_Pressure_Hydraulic_circuit_Object = MibScalar
alarm_Setpoint_Differential_Pressure_Hydraulic_circuit = _Alarm_Setpoint_Differential_Pressure_Hydraulic_circuit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 47),
    _Alarm_Setpoint_Differential_Pressure_Hydraulic_circuit_Type()
)
alarm_Setpoint_Differential_Pressure_Hydraulic_circuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_Setpoint_Differential_Pressure_Hydraulic_circuit.setStatus("current")
if mibBuilder.loadTexts:
    alarm_Setpoint_Differential_Pressure_Hydraulic_circuit.setUnits("N/A")


class _Alarm_Setpoint_Flow_Rate_Hydraulic_circuit_Type(Integer32):
    """Custom type alarm_Setpoint_Flow_Rate_Hydraulic_circuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Alarm_Setpoint_Flow_Rate_Hydraulic_circuit_Type.__name__ = "Integer32"
_Alarm_Setpoint_Flow_Rate_Hydraulic_circuit_Object = MibScalar
alarm_Setpoint_Flow_Rate_Hydraulic_circuit = _Alarm_Setpoint_Flow_Rate_Hydraulic_circuit_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 48),
    _Alarm_Setpoint_Flow_Rate_Hydraulic_circuit_Type()
)
alarm_Setpoint_Flow_Rate_Hydraulic_circuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_Setpoint_Flow_Rate_Hydraulic_circuit.setStatus("current")
if mibBuilder.loadTexts:
    alarm_Setpoint_Flow_Rate_Hydraulic_circuit.setUnits("N/A")


class _Tempertaure_Cut_off_FCM_Type(Integer32):
    """Custom type tempertaure_Cut_off_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Tempertaure_Cut_off_FCM_Type.__name__ = "Integer32"
_Tempertaure_Cut_off_FCM_Object = MibScalar
tempertaure_Cut_off_FCM = _Tempertaure_Cut_off_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 50),
    _Tempertaure_Cut_off_FCM_Type()
)
tempertaure_Cut_off_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempertaure_Cut_off_FCM.setStatus("current")
if mibBuilder.loadTexts:
    tempertaure_Cut_off_FCM.setUnits("N/A")


class _Set_effective_Type(Integer32):
    """Custom type set_effective based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Set_effective_Type.__name__ = "Integer32"
_Set_effective_Object = MibScalar
set_effective = _Set_effective_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 59),
    _Set_effective_Type()
)
set_effective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    set_effective.setStatus("current")
if mibBuilder.loadTexts:
    set_effective.setUnits("N/A")


class _Set_fc_Type(Integer32):
    """Custom type set_fc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Set_fc_Type.__name__ = "Integer32"
_Set_fc_Object = MibScalar
set_fc = _Set_fc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 60),
    _Set_fc_Type()
)
set_fc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    set_fc.setStatus("current")
if mibBuilder.loadTexts:
    set_fc.setUnits("N/A")


class _Setpoint_a_us_Type(Integer32):
    """Custom type setpoint_a_us based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Setpoint_a_us_Type.__name__ = "Integer32"
_Setpoint_a_us_Object = MibScalar
setpoint_a_us = _Setpoint_a_us_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 61),
    _Setpoint_a_us_Type()
)
setpoint_a_us.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_a_us.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_a_us.setUnits("N/A")


class _Max_setpoint_Type(Integer32):
    """Custom type max_setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_setpoint_Type.__name__ = "Integer32"
_Max_setpoint_Object = MibScalar
max_setpoint = _Max_setpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 62),
    _Max_setpoint_Type()
)
max_setpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_setpoint.setStatus("current")
if mibBuilder.loadTexts:
    max_setpoint.setUnits("N/A")


class _Min_setpoint_Type(Integer32):
    """Custom type min_setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_setpoint_Type.__name__ = "Integer32"
_Min_setpoint_Object = MibScalar
min_setpoint = _Min_setpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 63),
    _Min_setpoint_Type()
)
min_setpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_setpoint.setStatus("current")
if mibBuilder.loadTexts:
    min_setpoint.setUnits("N/A")


class _Diff_Type(Integer32):
    """Custom type diff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Diff_Type.__name__ = "Integer32"
_Diff_Object = MibScalar
diff = _Diff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 64),
    _Diff_Type()
)
diff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diff.setStatus("current")
if mibBuilder.loadTexts:
    diff.setUnits("N/A")


class _Max_diff_Type(Integer32):
    """Custom type max_diff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Max_diff_Type.__name__ = "Integer32"
_Max_diff_Object = MibScalar
max_diff = _Max_diff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 65),
    _Max_diff_Type()
)
max_diff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_diff.setStatus("current")
if mibBuilder.loadTexts:
    max_diff.setUnits("N/A")


class _Min_diff_Type(Integer32):
    """Custom type min_diff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Min_diff_Type.__name__ = "Integer32"
_Min_diff_Object = MibScalar
min_diff = _Min_diff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 66),
    _Min_diff_Type()
)
min_diff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_diff.setStatus("current")
if mibBuilder.loadTexts:
    min_diff.setUnits("N/A")


class _Fcs_out_Type(Integer32):
    """Custom type fcs_out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Fcs_out_Type.__name__ = "Integer32"
_Fcs_out_Object = MibScalar
fcs_out = _Fcs_out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 67),
    _Fcs_out_Type()
)
fcs_out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcs_out.setStatus("current")
if mibBuilder.loadTexts:
    fcs_out.setUnits("N/A")


class _Water_temp_Type(Integer32):
    """Custom type water_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Water_temp_Type.__name__ = "Integer32"
_Water_temp_Object = MibScalar
water_temp = _Water_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 70),
    _Water_temp_Type()
)
water_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    water_temp.setStatus("current")
if mibBuilder.loadTexts:
    water_temp.setUnits("N/A")


class _Temp_inlet_Type(Integer32):
    """Custom type temp_inlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Temp_inlet_Type.__name__ = "Integer32"
_Temp_inlet_Object = MibScalar
temp_inlet = _Temp_inlet_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 71),
    _Temp_inlet_Type()
)
temp_inlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_inlet.setStatus("current")
if mibBuilder.loadTexts:
    temp_inlet.setUnits("N/A")


class _Temp_outlet_Type(Integer32):
    """Custom type temp_outlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Temp_outlet_Type.__name__ = "Integer32"
_Temp_outlet_Object = MibScalar
temp_outlet = _Temp_outlet_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 72),
    _Temp_outlet_Type()
)
temp_outlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_outlet.setStatus("current")
if mibBuilder.loadTexts:
    temp_outlet.setUnits("N/A")


class _Flow_value_Type(Integer32):
    """Custom type flow_value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_Flow_value_Type.__name__ = "Integer32"
_Flow_value_Object = MibScalar
flow_value = _Flow_value_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 73),
    _Flow_value_Type()
)
flow_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flow_value.setStatus("current")
if mibBuilder.loadTexts:
    flow_value.setUnits("N/A")


class _Amp_value_Type(Integer32):
    """Custom type amp_value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_Amp_value_Type.__name__ = "Integer32"
_Amp_value_Object = MibScalar
amp_value = _Amp_value_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 74),
    _Amp_value_Type()
)
amp_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amp_value.setStatus("current")
if mibBuilder.loadTexts:
    amp_value.setUnits("N/A")


class _Ta_probe_temp_1_Type(Integer32):
    """Custom type ta_probe_temp_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Ta_probe_temp_1_Type.__name__ = "Integer32"
_Ta_probe_temp_1_Object = MibScalar
ta_probe_temp_1 = _Ta_probe_temp_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 75),
    _Ta_probe_temp_1_Type()
)
ta_probe_temp_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ta_probe_temp_1.setStatus("current")
if mibBuilder.loadTexts:
    ta_probe_temp_1.setUnits("N/A")


class _Ta_probe_temp_2_Type(Integer32):
    """Custom type ta_probe_temp_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Ta_probe_temp_2_Type.__name__ = "Integer32"
_Ta_probe_temp_2_Object = MibScalar
ta_probe_temp_2 = _Ta_probe_temp_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 76),
    _Ta_probe_temp_2_Type()
)
ta_probe_temp_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ta_probe_temp_2.setStatus("current")
if mibBuilder.loadTexts:
    ta_probe_temp_2.setUnits("N/A")


class _Pressione1_Type(Integer32):
    """Custom type pressione1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Pressione1_Type.__name__ = "Integer32"
_Pressione1_Object = MibScalar
pressione1 = _Pressione1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 77),
    _Pressione1_Type()
)
pressione1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressione1.setStatus("current")
if mibBuilder.loadTexts:
    pressione1.setUnits("N/A")


class _Pressione2_Type(Integer32):
    """Custom type pressione2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Pressione2_Type.__name__ = "Integer32"
_Pressione2_Object = MibScalar
pressione2 = _Pressione2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 78),
    _Pressione2_Type()
)
pressione2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressione2.setStatus("current")
if mibBuilder.loadTexts:
    pressione2.setUnits("N/A")


class _Pump_sp_press_Type(Integer32):
    """Custom type pump_sp_press based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Pump_sp_press_Type.__name__ = "Integer32"
_Pump_sp_press_Object = MibScalar
pump_sp_press = _Pump_sp_press_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 79),
    _Pump_sp_press_Type()
)
pump_sp_press.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pump_sp_press.setStatus("current")
if mibBuilder.loadTexts:
    pump_sp_press.setUnits("N/A")


class _P_wat2_Type(Integer32):
    """Custom type p_wat2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_P_wat2_Type.__name__ = "Integer32"
_P_wat2_Object = MibScalar
p_wat2 = _P_wat2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 80),
    _P_wat2_Type()
)
p_wat2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p_wat2.setStatus("current")
if mibBuilder.loadTexts:
    p_wat2.setUnits("N/A")


class _Temp_amb_Type(Integer32):
    """Custom type temp_amb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Temp_amb_Type.__name__ = "Integer32"
_Temp_amb_Object = MibScalar
temp_amb = _Temp_amb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 81),
    _Temp_amb_Type()
)
temp_amb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_amb.setStatus("current")
if mibBuilder.loadTexts:
    temp_amb.setUnits("N/A")


class _Temp_fc_Type(Integer32):
    """Custom type temp_fc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Temp_fc_Type.__name__ = "Integer32"
_Temp_fc_Object = MibScalar
temp_fc = _Temp_fc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 82),
    _Temp_fc_Type()
)
temp_fc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_fc.setStatus("current")
if mibBuilder.loadTexts:
    temp_fc.setUnits("N/A")


class _Pp1_Type(Integer32):
    """Custom type pp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pp1_Type.__name__ = "Integer32"
_Pp1_Object = MibScalar
pp1 = _Pp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 90),
    _Pp1_Type()
)
pp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp1.setStatus("current")
if mibBuilder.loadTexts:
    pp1.setUnits("N/A")


class _Pp2_Type(Integer32):
    """Custom type pp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pp2_Type.__name__ = "Integer32"
_Pp2_Object = MibScalar
pp2 = _Pp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 91),
    _Pp2_Type()
)
pp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp2.setStatus("current")
if mibBuilder.loadTexts:
    pp2.setUnits("N/A")


class _Cooling_capacity_Type(Integer32):
    """Custom type cooling_capacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Cooling_capacity_Type.__name__ = "Integer32"
_Cooling_capacity_Object = MibScalar
cooling_capacity = _Cooling_capacity_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 100),
    _Cooling_capacity_Type()
)
cooling_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooling_capacity.setStatus("current")
if mibBuilder.loadTexts:
    cooling_capacity.setUnits("N/A")


class _Freecooling_capacity_Type(Integer32):
    """Custom type freecooling_capacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Freecooling_capacity_Type.__name__ = "Integer32"
_Freecooling_capacity_Object = MibScalar
freecooling_capacity = _Freecooling_capacity_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 101),
    _Freecooling_capacity_Type()
)
freecooling_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freecooling_capacity.setStatus("current")
if mibBuilder.loadTexts:
    freecooling_capacity.setUnits("N/A")


class _Total_capacity_Type(Integer32):
    """Custom type total_capacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Total_capacity_Type.__name__ = "Integer32"
_Total_capacity_Object = MibScalar
total_capacity = _Total_capacity_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 102),
    _Total_capacity_Type()
)
total_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_capacity.setStatus("current")
if mibBuilder.loadTexts:
    total_capacity.setUnits("N/A")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Ip_Address1_Type(Integer32):
    """Custom type ip_Address1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address1_Type.__name__ = "Integer32"
_Ip_Address1_Object = MibScalar
ip_Address1 = _Ip_Address1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Ip_Address1_Type()
)
ip_Address1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address1.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address1.setUnits("N/A")


class _Ip_Address2_Type(Integer32):
    """Custom type ip_Address2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address2_Type.__name__ = "Integer32"
_Ip_Address2_Object = MibScalar
ip_Address2 = _Ip_Address2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 7),
    _Ip_Address2_Type()
)
ip_Address2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address2.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address2.setUnits("N/A")


class _Ip_Address3_Type(Integer32):
    """Custom type ip_Address3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address3_Type.__name__ = "Integer32"
_Ip_Address3_Object = MibScalar
ip_Address3 = _Ip_Address3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _Ip_Address3_Type()
)
ip_Address3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address3.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address3.setUnits("N/A")


class _Ip_Address4_Type(Integer32):
    """Custom type ip_Address4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address4_Type.__name__ = "Integer32"
_Ip_Address4_Object = MibScalar
ip_Address4 = _Ip_Address4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 9),
    _Ip_Address4_Type()
)
ip_Address4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address4.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address4.setUnits("N/A")


class _NetMask_Type(Integer32):
    """Custom type netMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32),
    )


_NetMask_Type.__name__ = "Integer32"
_NetMask_Object = MibScalar
netMask = _NetMask_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _NetMask_Type()
)
netMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMask.setStatus("current")
if mibBuilder.loadTexts:
    netMask.setUnits("N/A")


class _Gateway1_Type(Integer32):
    """Custom type gateway1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gateway1_Type.__name__ = "Integer32"
_Gateway1_Object = MibScalar
gateway1 = _Gateway1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _Gateway1_Type()
)
gateway1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway1.setStatus("current")
if mibBuilder.loadTexts:
    gateway1.setUnits("N/A")


class _Gateway2_Type(Integer32):
    """Custom type gateway2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gateway2_Type.__name__ = "Integer32"
_Gateway2_Object = MibScalar
gateway2 = _Gateway2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _Gateway2_Type()
)
gateway2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway2.setStatus("current")
if mibBuilder.loadTexts:
    gateway2.setUnits("N/A")


class _Gateway3_Type(Integer32):
    """Custom type gateway3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gateway3_Type.__name__ = "Integer32"
_Gateway3_Object = MibScalar
gateway3 = _Gateway3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Gateway3_Type()
)
gateway3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway3.setStatus("current")
if mibBuilder.loadTexts:
    gateway3.setUnits("N/A")


class _Gateway4_Type(Integer32):
    """Custom type gateway4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gateway4_Type.__name__ = "Integer32"
_Gateway4_Object = MibScalar
gateway4 = _Gateway4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _Gateway4_Type()
)
gateway4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway4.setStatus("current")
if mibBuilder.loadTexts:
    gateway4.setUnits("N/A")


class _Dns1_1_Type(Integer32):
    """Custom type dns1_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns1_1_Type.__name__ = "Integer32"
_Dns1_1_Object = MibScalar
dns1_1 = _Dns1_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _Dns1_1_Type()
)
dns1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns1_1.setStatus("current")
if mibBuilder.loadTexts:
    dns1_1.setUnits("N/A")


class _Dns1_2_Type(Integer32):
    """Custom type dns1_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns1_2_Type.__name__ = "Integer32"
_Dns1_2_Object = MibScalar
dns1_2 = _Dns1_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _Dns1_2_Type()
)
dns1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns1_2.setStatus("current")
if mibBuilder.loadTexts:
    dns1_2.setUnits("N/A")


class _Dns1_3_Type(Integer32):
    """Custom type dns1_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns1_3_Type.__name__ = "Integer32"
_Dns1_3_Object = MibScalar
dns1_3 = _Dns1_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Dns1_3_Type()
)
dns1_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns1_3.setStatus("current")
if mibBuilder.loadTexts:
    dns1_3.setUnits("N/A")


class _Dns1_4_Type(Integer32):
    """Custom type dns1_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns1_4_Type.__name__ = "Integer32"
_Dns1_4_Object = MibScalar
dns1_4 = _Dns1_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Dns1_4_Type()
)
dns1_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns1_4.setStatus("current")
if mibBuilder.loadTexts:
    dns1_4.setUnits("N/A")


class _Dns2_1_Type(Integer32):
    """Custom type dns2_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns2_1_Type.__name__ = "Integer32"
_Dns2_1_Object = MibScalar
dns2_1 = _Dns2_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Dns2_1_Type()
)
dns2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns2_1.setStatus("current")
if mibBuilder.loadTexts:
    dns2_1.setUnits("N/A")


class _Dns2_2_Type(Integer32):
    """Custom type dns2_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns2_2_Type.__name__ = "Integer32"
_Dns2_2_Object = MibScalar
dns2_2 = _Dns2_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _Dns2_2_Type()
)
dns2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns2_2.setStatus("current")
if mibBuilder.loadTexts:
    dns2_2.setUnits("N/A")


class _Dns2_3_Type(Integer32):
    """Custom type dns2_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns2_3_Type.__name__ = "Integer32"
_Dns2_3_Object = MibScalar
dns2_3 = _Dns2_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _Dns2_3_Type()
)
dns2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns2_3.setStatus("current")
if mibBuilder.loadTexts:
    dns2_3.setUnits("N/A")


class _Dns2_4_Type(Integer32):
    """Custom type dns2_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dns2_4_Type.__name__ = "Integer32"
_Dns2_4_Object = MibScalar
dns2_4 = _Dns2_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _Dns2_4_Type()
)
dns2_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dns2_4.setStatus("current")
if mibBuilder.loadTexts:
    dns2_4.setUnits("N/A")


class _Ip_Address1_Out_Type(Integer32):
    """Custom type ip_Address1_Out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address1_Out_Type.__name__ = "Integer32"
_Ip_Address1_Out_Object = MibScalar
ip_Address1_Out = _Ip_Address1_Out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _Ip_Address1_Out_Type()
)
ip_Address1_Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address1_Out.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address1_Out.setUnits("N/A")


class _Ip_Address2_Out_Type(Integer32):
    """Custom type ip_Address2_Out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address2_Out_Type.__name__ = "Integer32"
_Ip_Address2_Out_Object = MibScalar
ip_Address2_Out = _Ip_Address2_Out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _Ip_Address2_Out_Type()
)
ip_Address2_Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address2_Out.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address2_Out.setUnits("N/A")


class _Ip_Address3_Out_Type(Integer32):
    """Custom type ip_Address3_Out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address3_Out_Type.__name__ = "Integer32"
_Ip_Address3_Out_Object = MibScalar
ip_Address3_Out = _Ip_Address3_Out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _Ip_Address3_Out_Type()
)
ip_Address3_Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address3_Out.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address3_Out.setUnits("N/A")


class _Ip_Address4_Out_Type(Integer32):
    """Custom type ip_Address4_Out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ip_Address4_Out_Type.__name__ = "Integer32"
_Ip_Address4_Out_Object = MibScalar
ip_Address4_Out = _Ip_Address4_Out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Ip_Address4_Out_Type()
)
ip_Address4_Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_Address4_Out.setStatus("current")
if mibBuilder.loadTexts:
    ip_Address4_Out.setUnits("N/A")


class _Starting_delay_Second_Pump_Type(Integer32):
    """Custom type starting_delay_Second_Pump based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Starting_delay_Second_Pump_Type.__name__ = "Integer32"
_Starting_delay_Second_Pump_Object = MibScalar
starting_delay_Second_Pump = _Starting_delay_Second_Pump_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Starting_delay_Second_Pump_Type()
)
starting_delay_Second_Pump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starting_delay_Second_Pump.setStatus("current")
if mibBuilder.loadTexts:
    starting_delay_Second_Pump.setUnits("N/A")


class _Starting_delay_btw_Pump_Compressor_Type(Integer32):
    """Custom type starting_delay_btw_Pump_Compressor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Starting_delay_btw_Pump_Compressor_Type.__name__ = "Integer32"
_Starting_delay_btw_Pump_Compressor_Object = MibScalar
starting_delay_btw_Pump_Compressor = _Starting_delay_btw_Pump_Compressor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 31),
    _Starting_delay_btw_Pump_Compressor_Type()
)
starting_delay_btw_Pump_Compressor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    starting_delay_btw_Pump_Compressor.setStatus("current")
if mibBuilder.loadTexts:
    starting_delay_btw_Pump_Compressor.setUnits("N/A")


class _Overlap_time_Pumps_Type(Integer32):
    """Custom type overlap_time_Pumps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Overlap_time_Pumps_Type.__name__ = "Integer32"
_Overlap_time_Pumps_Object = MibScalar
overlap_time_Pumps = _Overlap_time_Pumps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 32),
    _Overlap_time_Pumps_Type()
)
overlap_time_Pumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlap_time_Pumps.setStatus("current")
if mibBuilder.loadTexts:
    overlap_time_Pumps.setUnits("N/A")


class _Working_time_Pumps_Type(Integer32):
    """Custom type working_time_Pumps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_Working_time_Pumps_Type.__name__ = "Integer32"
_Working_time_Pumps_Object = MibScalar
working_time_Pumps = _Working_time_Pumps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 33),
    _Working_time_Pumps_Type()
)
working_time_Pumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    working_time_Pumps.setStatus("current")
if mibBuilder.loadTexts:
    working_time_Pumps.setUnits("N/A")


class _Running_time_Chillers_Type(Integer32):
    """Custom type running_time_Chillers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Running_time_Chillers_Type.__name__ = "Integer32"
_Running_time_Chillers_Object = MibScalar
running_time_Chillers = _Running_time_Chillers_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 34),
    _Running_time_Chillers_Type()
)
running_time_Chillers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    running_time_Chillers.setStatus("current")
if mibBuilder.loadTexts:
    running_time_Chillers.setUnits("N/A")


class _Overlap_time_Chillers_Type(Integer32):
    """Custom type overlap_time_Chillers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Overlap_time_Chillers_Type.__name__ = "Integer32"
_Overlap_time_Chillers_Object = MibScalar
overlap_time_Chillers = _Overlap_time_Chillers_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 35),
    _Overlap_time_Chillers_Type()
)
overlap_time_Chillers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlap_time_Chillers.setStatus("current")
if mibBuilder.loadTexts:
    overlap_time_Chillers.setUnits("N/A")


class _N_chillers_Max_Type(Integer32):
    """Custom type n_chillers_Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_N_chillers_Max_Type.__name__ = "Integer32"
_N_chillers_Max_Object = MibScalar
n_chillers_Max = _N_chillers_Max_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 36),
    _N_chillers_Max_Type()
)
n_chillers_Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_chillers_Max.setStatus("current")
if mibBuilder.loadTexts:
    n_chillers_Max.setUnits("N/A")


class _N_chillers_ON_Type(Integer32):
    """Custom type n_chillers_ON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_N_chillers_ON_Type.__name__ = "Integer32"
_N_chillers_ON_Object = MibScalar
n_chillers_ON = _N_chillers_ON_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 37),
    _N_chillers_ON_Type()
)
n_chillers_ON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_chillers_ON.setStatus("current")
if mibBuilder.loadTexts:
    n_chillers_ON.setUnits("N/A")


class _N_pumps_ON_Type(Integer32):
    """Custom type n_pumps_ON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_N_pumps_ON_Type.__name__ = "Integer32"
_N_pumps_ON_Object = MibScalar
n_pumps_ON = _N_pumps_ON_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 38),
    _N_pumps_ON_Type()
)
n_pumps_ON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_pumps_ON.setStatus("current")
if mibBuilder.loadTexts:
    n_pumps_ON.setUnits("N/A")


class _Time_Enable_Pumps_Chiller_Offline_Type(Integer32):
    """Custom type time_Enable_Pumps_Chiller_Offline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Time_Enable_Pumps_Chiller_Offline_Type.__name__ = "Integer32"
_Time_Enable_Pumps_Chiller_Offline_Object = MibScalar
time_Enable_Pumps_Chiller_Offline = _Time_Enable_Pumps_Chiller_Offline_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 39),
    _Time_Enable_Pumps_Chiller_Offline_Type()
)
time_Enable_Pumps_Chiller_Offline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Enable_Pumps_Chiller_Offline.setStatus("current")
if mibBuilder.loadTexts:
    time_Enable_Pumps_Chiller_Offline.setUnits("N/A")


class _Time_Running_Pumps_Chiller_Offline_Type(Integer32):
    """Custom type time_Running_Pumps_Chiller_Offline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Time_Running_Pumps_Chiller_Offline_Type.__name__ = "Integer32"
_Time_Running_Pumps_Chiller_Offline_Object = MibScalar
time_Running_Pumps_Chiller_Offline = _Time_Running_Pumps_Chiller_Offline_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 40),
    _Time_Running_Pumps_Chiller_Offline_Type()
)
time_Running_Pumps_Chiller_Offline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Running_Pumps_Chiller_Offline.setStatus("current")
if mibBuilder.loadTexts:
    time_Running_Pumps_Chiller_Offline.setUnits("N/A")


class _Integral_Time_3Way_Valve_Hydraulic_PID_Type(Integer32):
    """Custom type integral_Time_3Way_Valve_Hydraulic_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Integral_Time_3Way_Valve_Hydraulic_PID_Type.__name__ = "Integer32"
_Integral_Time_3Way_Valve_Hydraulic_PID_Object = MibScalar
integral_Time_3Way_Valve_Hydraulic_PID = _Integral_Time_3Way_Valve_Hydraulic_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 41),
    _Integral_Time_3Way_Valve_Hydraulic_PID_Type()
)
integral_Time_3Way_Valve_Hydraulic_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integral_Time_3Way_Valve_Hydraulic_PID.setStatus("current")
if mibBuilder.loadTexts:
    integral_Time_3Way_Valve_Hydraulic_PID.setUnits("N/A")


class _Derivative_Time_3Way_Valve_Hydraulic_PID_Type(Integer32):
    """Custom type derivative_Time_3Way_Valve_Hydraulic_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Derivative_Time_3Way_Valve_Hydraulic_PID_Type.__name__ = "Integer32"
_Derivative_Time_3Way_Valve_Hydraulic_PID_Object = MibScalar
derivative_Time_3Way_Valve_Hydraulic_PID = _Derivative_Time_3Way_Valve_Hydraulic_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 42),
    _Derivative_Time_3Way_Valve_Hydraulic_PID_Type()
)
derivative_Time_3Way_Valve_Hydraulic_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    derivative_Time_3Way_Valve_Hydraulic_PID.setStatus("current")
if mibBuilder.loadTexts:
    derivative_Time_3Way_Valve_Hydraulic_PID.setUnits("N/A")


class _Output_Address_3Way_Valve_Hydraulic_Type(Integer32):
    """Custom type output_Address_3Way_Valve_Hydraulic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Output_Address_3Way_Valve_Hydraulic_Type.__name__ = "Integer32"
_Output_Address_3Way_Valve_Hydraulic_Object = MibScalar
output_Address_3Way_Valve_Hydraulic = _Output_Address_3Way_Valve_Hydraulic_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 43),
    _Output_Address_3Way_Valve_Hydraulic_Type()
)
output_Address_3Way_Valve_Hydraulic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    output_Address_3Way_Valve_Hydraulic.setStatus("current")
if mibBuilder.loadTexts:
    output_Address_3Way_Valve_Hydraulic.setUnits("N/A")


class _Time_Speed_Up_FCM_Type(Integer32):
    """Custom type time_Speed_Up_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Time_Speed_Up_FCM_Type.__name__ = "Integer32"
_Time_Speed_Up_FCM_Object = MibScalar
time_Speed_Up_FCM = _Time_Speed_Up_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 44),
    _Time_Speed_Up_FCM_Type()
)
time_Speed_Up_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Speed_Up_FCM.setStatus("current")
if mibBuilder.loadTexts:
    time_Speed_Up_FCM.setUnits("N/A")


class _Time_Soft_Start_FCM_Type(Integer32):
    """Custom type time_Soft_Start_FCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Time_Soft_Start_FCM_Type.__name__ = "Integer32"
_Time_Soft_Start_FCM_Object = MibScalar
time_Soft_Start_FCM = _Time_Soft_Start_FCM_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 45),
    _Time_Soft_Start_FCM_Type()
)
time_Soft_Start_FCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Soft_Start_FCM.setStatus("current")
if mibBuilder.loadTexts:
    time_Soft_Start_FCM.setUnits("N/A")


class _Delay_Freecooling_Type(Integer32):
    """Custom type delay_Freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Delay_Freecooling_Type.__name__ = "Integer32"
_Delay_Freecooling_Object = MibScalar
delay_Freecooling = _Delay_Freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 47),
    _Delay_Freecooling_Type()
)
delay_Freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_Freecooling.setStatus("current")
if mibBuilder.loadTexts:
    delay_Freecooling.setUnits("N/A")


class _Integral_Time_Freeccoling_PID_Type(Integer32):
    """Custom type integral_Time_Freeccoling_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Integral_Time_Freeccoling_PID_Type.__name__ = "Integer32"
_Integral_Time_Freeccoling_PID_Object = MibScalar
integral_Time_Freeccoling_PID = _Integral_Time_Freeccoling_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 48),
    _Integral_Time_Freeccoling_PID_Type()
)
integral_Time_Freeccoling_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integral_Time_Freeccoling_PID.setStatus("current")
if mibBuilder.loadTexts:
    integral_Time_Freeccoling_PID.setUnits("N/A")


class _Derivative_Time_Freeccoling_PID_Type(Integer32):
    """Custom type derivative_Time_Freeccoling_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Derivative_Time_Freeccoling_PID_Type.__name__ = "Integer32"
_Derivative_Time_Freeccoling_PID_Object = MibScalar
derivative_Time_Freeccoling_PID = _Derivative_Time_Freeccoling_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 49),
    _Derivative_Time_Freeccoling_PID_Type()
)
derivative_Time_Freeccoling_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    derivative_Time_Freeccoling_PID.setStatus("current")
if mibBuilder.loadTexts:
    derivative_Time_Freeccoling_PID.setUnits("N/A")


class _Time_Min_On_Freecooling_Chiller_timing_Type(Integer32):
    """Custom type time_Min_On_Freecooling_Chiller_timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Time_Min_On_Freecooling_Chiller_timing_Type.__name__ = "Integer32"
_Time_Min_On_Freecooling_Chiller_timing_Object = MibScalar
time_Min_On_Freecooling_Chiller_timing = _Time_Min_On_Freecooling_Chiller_timing_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 50),
    _Time_Min_On_Freecooling_Chiller_timing_Type()
)
time_Min_On_Freecooling_Chiller_timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Min_On_Freecooling_Chiller_timing.setStatus("current")
if mibBuilder.loadTexts:
    time_Min_On_Freecooling_Chiller_timing.setUnits("N/A")


class _Time_Min_Off_Freecooling_Chiller_timing_Type(Integer32):
    """Custom type time_Min_Off_Freecooling_Chiller_timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Time_Min_Off_Freecooling_Chiller_timing_Type.__name__ = "Integer32"
_Time_Min_Off_Freecooling_Chiller_timing_Object = MibScalar
time_Min_Off_Freecooling_Chiller_timing = _Time_Min_Off_Freecooling_Chiller_timing_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 51),
    _Time_Min_Off_Freecooling_Chiller_timing_Type()
)
time_Min_Off_Freecooling_Chiller_timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Min_Off_Freecooling_Chiller_timing.setStatus("current")
if mibBuilder.loadTexts:
    time_Min_Off_Freecooling_Chiller_timing.setUnits("N/A")


class _Time_Min_Different_Freecooling_Chiller_timing_Type(Integer32):
    """Custom type time_Min_Different_Freecooling_Chiller_timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Time_Min_Different_Freecooling_Chiller_timing_Type.__name__ = "Integer32"
_Time_Min_Different_Freecooling_Chiller_timing_Object = MibScalar
time_Min_Different_Freecooling_Chiller_timing = _Time_Min_Different_Freecooling_Chiller_timing_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 52),
    _Time_Min_Different_Freecooling_Chiller_timing_Type()
)
time_Min_Different_Freecooling_Chiller_timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Min_Different_Freecooling_Chiller_timing.setStatus("current")
if mibBuilder.loadTexts:
    time_Min_Different_Freecooling_Chiller_timing.setUnits("N/A")


class _Time_Min_Same_Freecooling_Chiller_timing_Type(Integer32):
    """Custom type time_Min_Same_Freecooling_Chiller_timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Time_Min_Same_Freecooling_Chiller_timing_Type.__name__ = "Integer32"
_Time_Min_Same_Freecooling_Chiller_timing_Object = MibScalar
time_Min_Same_Freecooling_Chiller_timing = _Time_Min_Same_Freecooling_Chiller_timing_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 53),
    _Time_Min_Same_Freecooling_Chiller_timing_Type()
)
time_Min_Same_Freecooling_Chiller_timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_Min_Same_Freecooling_Chiller_timing.setStatus("current")
if mibBuilder.loadTexts:
    time_Min_Same_Freecooling_Chiller_timing.setUnits("N/A")


class _Integral_Time_Freeccoling_Valve_PID_Type(Integer32):
    """Custom type integral_Time_Freeccoling_Valve_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Integral_Time_Freeccoling_Valve_PID_Type.__name__ = "Integer32"
_Integral_Time_Freeccoling_Valve_PID_Object = MibScalar
integral_Time_Freeccoling_Valve_PID = _Integral_Time_Freeccoling_Valve_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 54),
    _Integral_Time_Freeccoling_Valve_PID_Type()
)
integral_Time_Freeccoling_Valve_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    integral_Time_Freeccoling_Valve_PID.setStatus("current")
if mibBuilder.loadTexts:
    integral_Time_Freeccoling_Valve_PID.setUnits("N/A")


class _Derivative_Time_Freeccoling_Valve_PID_Type(Integer32):
    """Custom type derivative_Time_Freeccoling_Valve_PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Derivative_Time_Freeccoling_Valve_PID_Type.__name__ = "Integer32"
_Derivative_Time_Freeccoling_Valve_PID_Object = MibScalar
derivative_Time_Freeccoling_Valve_PID = _Derivative_Time_Freeccoling_Valve_PID_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 55),
    _Derivative_Time_Freeccoling_Valve_PID_Type()
)
derivative_Time_Freeccoling_Valve_PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    derivative_Time_Freeccoling_Valve_PID.setStatus("current")
if mibBuilder.loadTexts:
    derivative_Time_Freeccoling_Valve_PID.setUnits("N/A")


class _Output_Address_Valve_Freecooling_Type(Integer32):
    """Custom type output_Address_Valve_Freecooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Output_Address_Valve_Freecooling_Type.__name__ = "Integer32"
_Output_Address_Valve_Freecooling_Object = MibScalar
output_Address_Valve_Freecooling = _Output_Address_Valve_Freecooling_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 56),
    _Output_Address_Valve_Freecooling_Type()
)
output_Address_Valve_Freecooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    output_Address_Valve_Freecooling.setStatus("current")
if mibBuilder.loadTexts:
    output_Address_Valve_Freecooling.setUnits("N/A")


class _Delay_Freecooling_Thermal_Exclusion_Type(Integer32):
    """Custom type delay_Freecooling_Thermal_Exclusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Delay_Freecooling_Thermal_Exclusion_Type.__name__ = "Integer32"
_Delay_Freecooling_Thermal_Exclusion_Object = MibScalar
delay_Freecooling_Thermal_Exclusion = _Delay_Freecooling_Thermal_Exclusion_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 57),
    _Delay_Freecooling_Thermal_Exclusion_Type()
)
delay_Freecooling_Thermal_Exclusion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_Freecooling_Thermal_Exclusion.setStatus("current")
if mibBuilder.loadTexts:
    delay_Freecooling_Thermal_Exclusion.setUnits("N/A")


class _N_of_alarm_External_Dry_Cooler_Type(Integer32):
    """Custom type n_of_alarm_External_Dry_Cooler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_N_of_alarm_External_Dry_Cooler_Type.__name__ = "Integer32"
_N_of_alarm_External_Dry_Cooler_Object = MibScalar
n_of_alarm_External_Dry_Cooler = _N_of_alarm_External_Dry_Cooler_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 58),
    _N_of_alarm_External_Dry_Cooler_Type()
)
n_of_alarm_External_Dry_Cooler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_of_alarm_External_Dry_Cooler.setStatus("current")
if mibBuilder.loadTexts:
    n_of_alarm_External_Dry_Cooler.setUnits("N/A")


class _Delay_Alarm_Static_Pressure_Type(Integer32):
    """Custom type delay_Alarm_Static_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Delay_Alarm_Static_Pressure_Type.__name__ = "Integer32"
_Delay_Alarm_Static_Pressure_Object = MibScalar
delay_Alarm_Static_Pressure = _Delay_Alarm_Static_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 59),
    _Delay_Alarm_Static_Pressure_Type()
)
delay_Alarm_Static_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_Alarm_Static_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    delay_Alarm_Static_Pressure.setUnits("N/A")


class _N_of_Alarm_Static_Pressure_Type(Integer32):
    """Custom type n_of_Alarm_Static_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N_of_Alarm_Static_Pressure_Type.__name__ = "Integer32"
_N_of_Alarm_Static_Pressure_Object = MibScalar
n_of_Alarm_Static_Pressure = _N_of_Alarm_Static_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 60),
    _N_of_Alarm_Static_Pressure_Type()
)
n_of_Alarm_Static_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_of_Alarm_Static_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    n_of_Alarm_Static_Pressure.setUnits("N/A")


class _Delay_Warning_Static_Pressure_Type(Integer32):
    """Custom type delay_Warning_Static_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Delay_Warning_Static_Pressure_Type.__name__ = "Integer32"
_Delay_Warning_Static_Pressure_Object = MibScalar
delay_Warning_Static_Pressure = _Delay_Warning_Static_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 61),
    _Delay_Warning_Static_Pressure_Type()
)
delay_Warning_Static_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_Warning_Static_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    delay_Warning_Static_Pressure.setUnits("N/A")


class _N_of_Warning_Static_Pressure_Type(Integer32):
    """Custom type n_of_Warning_Static_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N_of_Warning_Static_Pressure_Type.__name__ = "Integer32"
_N_of_Warning_Static_Pressure_Object = MibScalar
n_of_Warning_Static_Pressure = _N_of_Warning_Static_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 62),
    _N_of_Warning_Static_Pressure_Type()
)
n_of_Warning_Static_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_of_Warning_Static_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    n_of_Warning_Static_Pressure.setUnits("N/A")


class _N_of_Alarm_Differential_Pressure_Type(Integer32):
    """Custom type n_of_Alarm_Differential_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N_of_Alarm_Differential_Pressure_Type.__name__ = "Integer32"
_N_of_Alarm_Differential_Pressure_Object = MibScalar
n_of_Alarm_Differential_Pressure = _N_of_Alarm_Differential_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 63),
    _N_of_Alarm_Differential_Pressure_Type()
)
n_of_Alarm_Differential_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_of_Alarm_Differential_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    n_of_Alarm_Differential_Pressure.setUnits("N/A")


class _Priming_Time_Hydraulic_Pressure_Type(Integer32):
    """Custom type priming_Time_Hydraulic_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Priming_Time_Hydraulic_Pressure_Type.__name__ = "Integer32"
_Priming_Time_Hydraulic_Pressure_Object = MibScalar
priming_Time_Hydraulic_Pressure = _Priming_Time_Hydraulic_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 64),
    _Priming_Time_Hydraulic_Pressure_Type()
)
priming_Time_Hydraulic_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priming_Time_Hydraulic_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    priming_Time_Hydraulic_Pressure.setUnits("N/A")


class _Delay_priming_Time_Hydraulic_Pressure_Type(Integer32):
    """Custom type delay_priming_Time_Hydraulic_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Delay_priming_Time_Hydraulic_Pressure_Type.__name__ = "Integer32"
_Delay_priming_Time_Hydraulic_Pressure_Object = MibScalar
delay_priming_Time_Hydraulic_Pressure = _Delay_priming_Time_Hydraulic_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 65),
    _Delay_priming_Time_Hydraulic_Pressure_Type()
)
delay_priming_Time_Hydraulic_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_priming_Time_Hydraulic_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    delay_priming_Time_Hydraulic_Pressure.setUnits("N/A")


class _Output_Address_Alarm_Static_Pressure_Type(Integer32):
    """Custom type output_Address_Alarm_Static_Pressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_Output_Address_Alarm_Static_Pressure_Type.__name__ = "Integer32"
_Output_Address_Alarm_Static_Pressure_Object = MibScalar
output_Address_Alarm_Static_Pressure = _Output_Address_Alarm_Static_Pressure_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 66),
    _Output_Address_Alarm_Static_Pressure_Type()
)
output_Address_Alarm_Static_Pressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    output_Address_Alarm_Static_Pressure.setStatus("current")
if mibBuilder.loadTexts:
    output_Address_Alarm_Static_Pressure.setUnits("N/A")


class _N_of_Alarm_Flow_Rate_Type(Integer32):
    """Custom type n_of_Alarm_Flow_Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N_of_Alarm_Flow_Rate_Type.__name__ = "Integer32"
_N_of_Alarm_Flow_Rate_Object = MibScalar
n_of_Alarm_Flow_Rate = _N_of_Alarm_Flow_Rate_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 67),
    _N_of_Alarm_Flow_Rate_Type()
)
n_of_Alarm_Flow_Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_of_Alarm_Flow_Rate.setStatus("current")
if mibBuilder.loadTexts:
    n_of_Alarm_Flow_Rate.setUnits("N/A")


class _Priming_Time_Flow_Rate_Type(Integer32):
    """Custom type priming_Time_Flow_Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Priming_Time_Flow_Rate_Type.__name__ = "Integer32"
_Priming_Time_Flow_Rate_Object = MibScalar
priming_Time_Flow_Rate = _Priming_Time_Flow_Rate_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 68),
    _Priming_Time_Flow_Rate_Type()
)
priming_Time_Flow_Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priming_Time_Flow_Rate.setStatus("current")
if mibBuilder.loadTexts:
    priming_Time_Flow_Rate.setUnits("N/A")


class _Delay_priming_Time_Flow_Rate_Type(Integer32):
    """Custom type delay_priming_Time_Flow_Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Delay_priming_Time_Flow_Rate_Type.__name__ = "Integer32"
_Delay_priming_Time_Flow_Rate_Object = MibScalar
delay_priming_Time_Flow_Rate = _Delay_priming_Time_Flow_Rate_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 69),
    _Delay_priming_Time_Flow_Rate_Type()
)
delay_priming_Time_Flow_Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_priming_Time_Flow_Rate.setStatus("current")
if mibBuilder.loadTexts:
    delay_priming_Time_Flow_Rate.setUnits("N/A")


class _Bms_address_IDENT_Type(Integer32):
    """Custom type bms_address_IDENT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Bms_address_IDENT_Type.__name__ = "Integer32"
_Bms_address_IDENT_Object = MibScalar
bms_address_IDENT = _Bms_address_IDENT_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 70),
    _Bms_address_IDENT_Type()
)
bms_address_IDENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bms_address_IDENT.setStatus("current")
if mibBuilder.loadTexts:
    bms_address_IDENT.setUnits("N/A")


class _Chiller_name0_Type(Integer32):
    """Custom type chiller_name0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Chiller_name0_Type.__name__ = "Integer32"
_Chiller_name0_Object = MibScalar
chiller_name0 = _Chiller_name0_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 99),
    _Chiller_name0_Type()
)
chiller_name0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chiller_name0.setStatus("current")
if mibBuilder.loadTexts:
    chiller_name0.setUnits("N/A")


class _Chiller_name1_Type(Integer32):
    """Custom type chiller_name1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Chiller_name1_Type.__name__ = "Integer32"
_Chiller_name1_Object = MibScalar
chiller_name1 = _Chiller_name1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 100),
    _Chiller_name1_Type()
)
chiller_name1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chiller_name1.setStatus("current")
if mibBuilder.loadTexts:
    chiller_name1.setUnits("N/A")


class _Current_day_Type(Integer32):
    """Custom type current_day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Current_day_Type.__name__ = "Integer32"
_Current_day_Object = MibScalar
current_day = _Current_day_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 123),
    _Current_day_Type()
)
current_day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_day.setStatus("current")
if mibBuilder.loadTexts:
    current_day.setUnits("N/A")


class _Current_month_Type(Integer32):
    """Custom type current_month based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Current_month_Type.__name__ = "Integer32"
_Current_month_Object = MibScalar
current_month = _Current_month_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 124),
    _Current_month_Type()
)
current_month.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_month.setStatus("current")
if mibBuilder.loadTexts:
    current_month.setUnits("N/A")


class _Current_year_Type(Integer32):
    """Custom type current_year based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Current_year_Type.__name__ = "Integer32"
_Current_year_Object = MibScalar
current_year = _Current_year_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 125),
    _Current_year_Type()
)
current_year.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_year.setStatus("current")
if mibBuilder.loadTexts:
    current_year.setUnits("N/A")


class _Current_hour_Type(Integer32):
    """Custom type current_hour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Current_hour_Type.__name__ = "Integer32"
_Current_hour_Object = MibScalar
current_hour = _Current_hour_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 126),
    _Current_hour_Type()
)
current_hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_hour.setStatus("current")
if mibBuilder.loadTexts:
    current_hour.setUnits("N/A")


class _Current_minute_Type(Integer32):
    """Custom type current_minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Current_minute_Type.__name__ = "Integer32"
_Current_minute_Object = MibScalar
current_minute = _Current_minute_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 127),
    _Current_minute_Type()
)
current_minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_minute.setStatus("current")
if mibBuilder.loadTexts:
    current_minute.setUnits("N/A")


class _Chiller_mode_operation_Type(Integer32):
    """Custom type chiller_mode_operation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Chiller_mode_operation_Type.__name__ = "Integer32"
_Chiller_mode_operation_Object = MibScalar
chiller_mode_operation = _Chiller_mode_operation_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 150),
    _Chiller_mode_operation_Type()
)
chiller_mode_operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chiller_mode_operation.setStatus("current")
if mibBuilder.loadTexts:
    chiller_mode_operation.setUnits("N/A")
_TrapObjects_ObjectIdentity = ObjectIdentity
trapObjects = _TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100)
)

# Managed Objects groups


# Notification objects

high_pressure_switch_1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 1)
)
if mibBuilder.loadTexts:
    high_pressure_switch_1_alarm.setStatus(
        "current"
    )

high_pressure_switch_2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 2)
)
if mibBuilder.loadTexts:
    high_pressure_switch_2_alarm.setStatus(
        "current"
    )

low_pressure_switch_1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 3)
)
if mibBuilder.loadTexts:
    low_pressure_switch_1_alarm.setStatus(
        "current"
    )

low_pressure_switch_2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 4)
)
if mibBuilder.loadTexts:
    low_pressure_switch_2_alarm.setStatus(
        "current"
    )

water_level_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 6)
)
if mibBuilder.loadTexts:
    water_level_alarm.setStatus(
        "current"
    )

flow_switch_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 8)
)
if mibBuilder.loadTexts:
    flow_switch_alarm.setStatus(
        "current"
    )

water_static_pressure_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 9)
)
if mibBuilder.loadTexts:
    water_static_pressure_alarm.setStatus(
        "current"
    )

water_static_pressure_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 10)
)
if mibBuilder.loadTexts:
    water_static_pressure_warning.setStatus(
        "current"
    )

flow_rate_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 11)
)
if mibBuilder.loadTexts:
    flow_rate_alarm.setStatus(
        "current"
    )

overload_compressor1_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 12)
)
if mibBuilder.loadTexts:
    overload_compressor1_circuit1_alarm.setStatus(
        "current"
    )

overload_compressor2_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 13)
)
if mibBuilder.loadTexts:
    overload_compressor2_circuit1_alarm.setStatus(
        "current"
    )

overload_compressor3_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 14)
)
if mibBuilder.loadTexts:
    overload_compressor3_circuit1_alarm.setStatus(
        "current"
    )

overload_compressor1_circuit2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 15)
)
if mibBuilder.loadTexts:
    overload_compressor1_circuit2_alarm.setStatus(
        "current"
    )

overload_compressor2_circuit2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 16)
)
if mibBuilder.loadTexts:
    overload_compressor2_circuit2_alarm.setStatus(
        "current"
    )

overload_compressor3_circuit2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 17)
)
if mibBuilder.loadTexts:
    overload_compressor3_circuit2_alarm.setStatus(
        "current"
    )

overload_fans_circuit1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 18)
)
if mibBuilder.loadTexts:
    overload_fans_circuit1.setStatus(
        "current"
    )

overload_fans_circuit2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 19)
)
if mibBuilder.loadTexts:
    overload_fans_circuit2.setStatus(
        "current"
    )

overload_fan1_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 20)
)
if mibBuilder.loadTexts:
    overload_fan1_circuit1_alarm.setStatus(
        "current"
    )

overload_fan2_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 21)
)
if mibBuilder.loadTexts:
    overload_fan2_circuit1_alarm.setStatus(
        "current"
    )

overload_fan3_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 22)
)
if mibBuilder.loadTexts:
    overload_fan3_circuit1_alarm.setStatus(
        "current"
    )

overload_fan4_circuit1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 23)
)
if mibBuilder.loadTexts:
    overload_fan4_circuit1_alarm.setStatus(
        "current"
    )

overload_fan1_circuit_2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 24)
)
if mibBuilder.loadTexts:
    overload_fan1_circuit_2_alarm.setStatus(
        "current"
    )

overload_fan2_circuit2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 25)
)
if mibBuilder.loadTexts:
    overload_fan2_circuit2_alarm.setStatus(
        "current"
    )

overload_fan3_circuit2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 26)
)
if mibBuilder.loadTexts:
    overload_fan3_circuit2_alarm.setStatus(
        "current"
    )

overload_fan4_circuit2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 27)
)
if mibBuilder.loadTexts:
    overload_fan4_circuit2_alarm.setStatus(
        "current"
    )

overload_pump1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 28)
)
if mibBuilder.loadTexts:
    overload_pump1_alarm.setStatus(
        "current"
    )

overload_pump2_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 29)
)
if mibBuilder.loadTexts:
    overload_pump2_alarm.setStatus(
        "current"
    )

wrong_phase_rotation_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 30)
)
if mibBuilder.loadTexts:
    wrong_phase_rotation_alarm.setStatus(
        "current"
    )

back_Door_open_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 31)
)
if mibBuilder.loadTexts:
    back_Door_open_alarm.setStatus(
        "current"
    )

alarm_idrofrigo_pump_c_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 75)
)
if mibBuilder.loadTexts:
    alarm_idrofrigo_pump_c_1.setStatus(
        "current"
    )

alarm_idrofrigo_pump_c_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 76)
)
if mibBuilder.loadTexts:
    alarm_idrofrigo_pump_c_2.setStatus(
        "current"
    )

alarm_idrofrigo_fl_C = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 80)
)
if mibBuilder.loadTexts:
    alarm_idrofrigo_fl_C.setStatus(
        "current"
    )

remote_on_off = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 130)
)
if mibBuilder.loadTexts:
    remote_on_off.setStatus(
        "current"
    )

chiller_ON_OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 131)
)
if mibBuilder.loadTexts:
    chiller_ON_OFF.setStatus(
        "current"
    )

alarm_disch_scw_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 148)
)
if mibBuilder.loadTexts:
    alarm_disch_scw_1.setStatus(
        "current"
    )

alarm_disch_scw_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 149)
)
if mibBuilder.loadTexts:
    alarm_disch_scw_2.setStatus(
        "current"
    )

alarm_probe_inlet = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 150)
)
if mibBuilder.loadTexts:
    alarm_probe_inlet.setStatus(
        "current"
    )

alarm_probe_amb = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 151)
)
if mibBuilder.loadTexts:
    alarm_probe_amb.setStatus(
        "current"
    )

alarm_frigo_fl1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 152)
)
if mibBuilder.loadTexts:
    alarm_frigo_fl1.setStatus(
        "current"
    )

alarm_idro_pump1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 153)
)
if mibBuilder.loadTexts:
    alarm_idro_pump1.setStatus(
        "current"
    )

alarm_idro_pump2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 154)
)
if mibBuilder.loadTexts:
    alarm_idro_pump2.setStatus(
        "current"
    )

alarm_idro_fl1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 155)
)
if mibBuilder.loadTexts:
    alarm_idro_fl1.setStatus(
        "current"
    )

alarm_warning_fl1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 156)
)
if mibBuilder.loadTexts:
    alarm_warning_fl1.setStatus(
        "current"
    )

alarm_hi_water_temp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 157)
)
if mibBuilder.loadTexts:
    alarm_hi_water_temp.setStatus(
        "current"
    )

alarm_lo_water_temp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 158)
)
if mibBuilder.loadTexts:
    alarm_lo_water_temp.setStatus(
        "current"
    )

alarm_ta_probe1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 159)
)
if mibBuilder.loadTexts:
    alarm_ta_probe1.setStatus(
        "current"
    )

alarm_hi_press = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 160)
)
if mibBuilder.loadTexts:
    alarm_hi_press.setStatus(
        "current"
    )

alarm_lo_press = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 161)
)
if mibBuilder.loadTexts:
    alarm_lo_press.setStatus(
        "current"
    )

alarm_probe_evap_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 162)
)
if mibBuilder.loadTexts:
    alarm_probe_evap_1.setStatus(
        "current"
    )

alarm_probe_evap_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 163)
)
if mibBuilder.loadTexts:
    alarm_probe_evap_2.setStatus(
        "current"
    )

alarm_hi_press_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 164)
)
if mibBuilder.loadTexts:
    alarm_hi_press_1.setStatus(
        "current"
    )

alarm_hi_press_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 165)
)
if mibBuilder.loadTexts:
    alarm_hi_press_2.setStatus(
        "current"
    )

alarm_lo_press_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 166)
)
if mibBuilder.loadTexts:
    alarm_lo_press_1.setStatus(
        "current"
    )

alarm_lo_press_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 167)
)
if mibBuilder.loadTexts:
    alarm_lo_press_2.setStatus(
        "current"
    )

alarm_probe_tank = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 168)
)
if mibBuilder.loadTexts:
    alarm_probe_tank.setStatus(
        "current"
    )

alarm_off_line_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 169)
)
if mibBuilder.loadTexts:
    alarm_off_line_1.setStatus(
        "current"
    )

alarm_off_line_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 170)
)
if mibBuilder.loadTexts:
    alarm_off_line_2.setStatus(
        "current"
    )

alarm_off_line_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 171)
)
if mibBuilder.loadTexts:
    alarm_off_line_3.setStatus(
        "current"
    )

alarm_off_line_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 172)
)
if mibBuilder.loadTexts:
    alarm_off_line_4.setStatus(
        "current"
    )

alarm_off_line_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 173)
)
if mibBuilder.loadTexts:
    alarm_off_line_5.setStatus(
        "current"
    )

alarm_off_line_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 174)
)
if mibBuilder.loadTexts:
    alarm_off_line_6.setStatus(
        "current"
    )

alarm_off_line_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 175)
)
if mibBuilder.loadTexts:
    alarm_off_line_7.setStatus(
        "current"
    )

alarm_off_line_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 176)
)
if mibBuilder.loadTexts:
    alarm_off_line_8.setStatus(
        "current"
    )

alarm_ta_probe2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 177)
)
if mibBuilder.loadTexts:
    alarm_ta_probe2.setStatus(
        "current"
    )

alarm_sms = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 178)
)
if mibBuilder.loadTexts:
    alarm_sms.setStatus(
        "current"
    )

alarm_modem = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 179)
)
if mibBuilder.loadTexts:
    alarm_modem.setStatus(
        "current"
    )

alarm_sms_coda = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 180)
)
if mibBuilder.loadTexts:
    alarm_sms_coda.setStatus(
        "current"
    )

alarm_probe_fc = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 181)
)
if mibBuilder.loadTexts:
    alarm_probe_fc.setStatus(
        "current"
    )

alarm_maint_pw1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 182)
)
if mibBuilder.loadTexts:
    alarm_maint_pw1.setStatus(
        "current"
    )

alarm_maint_pw2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 183)
)
if mibBuilder.loadTexts:
    alarm_maint_pw2.setStatus(
        "current"
    )

alarm_hi_temp_rid = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 184)
)
if mibBuilder.loadTexts:
    alarm_hi_temp_rid.setStatus(
        "current"
    )

alarm_q_fc_sep = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 185)
)
if mibBuilder.loadTexts:
    alarm_q_fc_sep.setStatus(
        "current"
    )

alarm_p_wat2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 186)
)
if mibBuilder.loadTexts:
    alarm_p_wat2.setStatus(
        "current"
    )

alarm_p_wat1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 187)
)
if mibBuilder.loadTexts:
    alarm_p_wat1.setStatus(
        "current"
    )

alarm_foult_flow_p1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 188)
)
if mibBuilder.loadTexts:
    alarm_foult_flow_p1.setStatus(
        "current"
    )

alarm_foult_flow_p2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 189)
)
if mibBuilder.loadTexts:
    alarm_foult_flow_p2.setStatus(
        "current"
    )

alarm_foult_fl1_p1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 190)
)
if mibBuilder.loadTexts:
    alarm_foult_fl1_p1.setStatus(
        "current"
    )

alarm_foult_fl1_p2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 191)
)
if mibBuilder.loadTexts:
    alarm_foult_fl1_p2.setStatus(
        "current"
    )

alarm_warning_le = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 192)
)
if mibBuilder.loadTexts:
    alarm_warning_le.setStatus(
        "current"
    )

alarm_frigo_fl_C = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 193)
)
if mibBuilder.loadTexts:
    alarm_frigo_fl_C.setStatus(
        "current"
    )

alarm_idro_pump_c_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 194)
)
if mibBuilder.loadTexts:
    alarm_idro_pump_c_1.setStatus(
        "current"
    )

alarm_idro_pump_c_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 195)
)
if mibBuilder.loadTexts:
    alarm_idro_pump_c_2.setStatus(
        "current"
    )

alarm_idro_fl_C = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 196)
)
if mibBuilder.loadTexts:
    alarm_idro_fl_C.setStatus(
        "current"
    )

alarm_warning_fl_C = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 197)
)
if mibBuilder.loadTexts:
    alarm_warning_fl_C.setStatus(
        "current"
    )

alarm_foul_fl_C_p1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 198)
)
if mibBuilder.loadTexts:
    alarm_foul_fl_C_p1.setStatus(
        "current"
    )

alarm_foul_fl_C_p2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 100, 199)
)
if mibBuilder.loadTexts:
    alarm_foul_fl_C_p2.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KELVIN-pCOWeb-Chiller-MIB",
    **{"carel": carel,
       "systm": systm,
       "agentRelease": agentRelease,
       "agentCode": agentCode,
       "instruments": instruments,
       "pCOWebInfo": pCOWebInfo,
       "pCOStatusgroup": pCOStatusgroup,
       "pCOId1-Status": pCOId1_Status,
       "pCOErrorsNumbergroup": pCOErrorsNumbergroup,
       "pCOId1-ErrorsNumber": pCOId1_ErrorsNumber,
       "kelvin-pCOWebMIB-Chiller": kelvin_pCOWebMIB_Chiller,
       "digitalObjects": digitalObjects,
       "al-pa1": al_pa1,
       "al-pa2": al_pa2,
       "al-pb1": al_pb1,
       "al-pb2": al_pb2,
       "al-le": al_le,
       "al-idrofrigo-fl1": al_idrofrigo_fl1,
       "static-press-alarm": static_press_alarm,
       "w-static-press-alarm": w_static_press_alarm,
       "flow-value-alarm": flow_value_alarm,
       "al-q-comp1": al_q_comp1,
       "al-q-comp2": al_q_comp2,
       "al-q-comp3": al_q_comp3,
       "al-q-comp4": al_q_comp4,
       "al-q-comp5": al_q_comp5,
       "al-q-comp6": al_q_comp6,
       "al-q-fan-1": al_q_fan_1,
       "al-q-fan-2": al_q_fan_2,
       "al-q-fan11": al_q_fan11,
       "al-q-fan12": al_q_fan12,
       "al-q-fan13": al_q_fan13,
       "al-q-fan14": al_q_fan14,
       "al-q-fan21": al_q_fan21,
       "al-q-fan22": al_q_fan22,
       "al-q-fan-23": al_q_fan_23,
       "al-q-fan24": al_q_fan24,
       "al-idrofrigo-pump1": al_idrofrigo_pump1,
       "al-idrofrigo-pump2": al_idrofrigo_pump2,
       "al-phase-cont": al_phase_cont,
       "al-door-sw": al_door_sw,
       "compressor-FlowRate": compressor_FlowRate,
       "setpoint-inv-pumps": setpoint_inv_pumps,
       "enable-pumps-redundance": enable_pumps_redundance,
       "enable-chiller-redundance": enable_chiller_redundance,
       "status-in-alarm": status_in_alarm,
       "compressor-recovery": compressor_recovery,
       "enable-thermal-redundance": enable_thermal_redundance,
       "enable-multi-pumps-function": enable_multi_pumps_function,
       "enable-pumps-offline": enable_pumps_offline,
       "enable-3way-valve": enable_3way_valve,
       "enable-speed-up-FCM": enable_speed_up_FCM,
       "enable-soft-start-FCM": enable_soft_start_FCM,
       "enable-freecooling": enable_freecooling,
       "enable-rot-FIFO-FC": enable_rot_FIFO_FC,
       "enable-HT-function": enable_HT_function,
       "enable-PID-Fc-valve": enable_PID_Fc_valve,
       "enable-Fc-Thermal-Exclusion": enable_Fc_Thermal_Exclusion,
       "manual-Reset-Ext-Drycooler-Alarm": manual_Reset_Ext_Drycooler_Alarm,
       "enable-static-press-Alarm": enable_static_press_Alarm,
       "manual-reset-static-press-Alarm": manual_reset_static_press_Alarm,
       "enable-static-press-Warning": enable_static_press_Warning,
       "manual-reset-static-press-Warning": manual_reset_static_press_Warning,
       "enable-diff-press-Alarm": enable_diff_press_Alarm,
       "manual-reset-diff-press-Alarm": manual_reset_diff_press_Alarm,
       "enable-pressure-recovery": enable_pressure_recovery,
       "enable-Flow-Rate-Alarm": enable_Flow_Rate_Alarm,
       "manual-reset-Flow-Rate-Alarm": manual_reset_Flow_Rate_Alarm,
       "enable-Flow-Rate-recovery": enable_Flow_Rate_recovery,
       "enable-pCOWeb": enable_pCOWeb,
       "fc-single-chiller": fc_single_chiller,
       "al-idrofrigo-pump-c-1": al_idrofrigo_pump_c_1,
       "al-idrofrigo-pump-c-2": al_idrofrigo_pump_c_2,
       "al-idrofrigo-fl-C": al_idrofrigo_fl_C,
       "c11-on": c11_on,
       "c12-on": c12_on,
       "c13-on": c13_on,
       "c21-on": c21_on,
       "c22-on": c22_on,
       "c23-on": c23_on,
       "pump1-on": pump1_on,
       "pump2-on": pump2_on,
       "on-fan-gr1": on_fan_gr1,
       "on-fan-gr2": on_fan_gr2,
       "fc-on": fc_on,
       "en-on-off-rem": en_on_off_rem,
       "unit-on": unit_on,
       "disch-alarm-scw-1": disch_alarm_scw_1,
       "disch-alarm-scw-2": disch_alarm_scw_2,
       "al-probe-inlet": al_probe_inlet,
       "al-probe-amb": al_probe_amb,
       "al-frigo-fl1": al_frigo_fl1,
       "al-idro-pump1": al_idro_pump1,
       "al-idro-pump2": al_idro_pump2,
       "al-idro-fl1": al_idro_fl1,
       "al-warning-fl1": al_warning_fl1,
       "al-hi-water-temp": al_hi_water_temp,
       "al-lo-water-temp": al_lo_water_temp,
       "al-ta-probe1": al_ta_probe1,
       "al-hi-press": al_hi_press,
       "al-lo-press": al_lo_press,
       "al-probe-evap-1": al_probe_evap_1,
       "al-probe-evap-2": al_probe_evap_2,
       "al-hi-press-1": al_hi_press_1,
       "al-hi-press-2": al_hi_press_2,
       "al-lo-press-1": al_lo_press_1,
       "al-lo-press-2": al_lo_press_2,
       "al-probe-tank": al_probe_tank,
       "off-line-1": off_line_1,
       "off-line-2": off_line_2,
       "off-line-3": off_line_3,
       "off-line-4": off_line_4,
       "off-line-5": off_line_5,
       "off-line-6": off_line_6,
       "off-line-7": off_line_7,
       "off-line-8": off_line_8,
       "al-ta-probe2": al_ta_probe2,
       "al-sms": al_sms,
       "al-modem": al_modem,
       "sms-coda-alarm": sms_coda_alarm,
       "al-probe-fc": al_probe_fc,
       "al-maint-pw1": al_maint_pw1,
       "al-maint-pw2": al_maint_pw2,
       "al-hi-temp-rid": al_hi_temp_rid,
       "al-q-fc-sep": al_q_fc_sep,
       "al-p-wat2": al_p_wat2,
       "al-p-wat1": al_p_wat1,
       "al-foult-flow-p1": al_foult_flow_p1,
       "al-foult-flow-p2": al_foult_flow_p2,
       "al-foult-fl1-p1": al_foult_fl1_p1,
       "al-foult-fl1-p2": al_foult_fl1_p2,
       "al-warning-le": al_warning_le,
       "al-frigo-fl-C": al_frigo_fl_C,
       "al-idro-pump-c-1": al_idro_pump_c_1,
       "al-idro-pump-c-2": al_idro_pump_c_2,
       "al-idro-fl-C": al_idro_fl_C,
       "al-warning-fl-C": al_warning_fl_C,
       "al-foul-fl-C-p1": al_foul_fl_C_p1,
       "al-foul-fl-C-p2": al_foul_fl_C_p2,
       "analogObjects": analogObjects,
       "setpoint-antifreeze1": setpoint_antifreeze1,
       "setpoint-antifreeze2": setpoint_antifreeze2,
       "setpoint-Compensation": setpoint_Compensation,
       "hysteresis-Compensation": hysteresis_Compensation,
       "max-Compensation": max_Compensation,
       "setpoint-Differential": setpoint_Differential,
       "high-Limit": high_Limit,
       "low-Limit": low_Limit,
       "max-Setpoint-Differential": max_Setpoint_Differential,
       "min-Setpoint-Differential": min_Setpoint_Differential,
       "setpoint-ASB-Inverter-pumps": setpoint_ASB_Inverter_pumps,
       "setpoint-DIFF-Inverter-pumps": setpoint_DIFF_Inverter_pumps,
       "pressure-Out": pressure_Out,
       "proportional-Band-Inverter-Pumps-PID": proportional_Band_Inverter_Pumps_PID,
       "integral-Time-Inverter-Pumps-PID": integral_Time_Inverter_Pumps_PID,
       "derivative-Time-Inverter-Pumps-PID": derivative_Time_Inverter_Pumps_PID,
       "hysteresis-Thermal-redundance": hysteresis_Thermal_redundance,
       "min-Opening-3Way-Valve-Hydraulic": min_Opening_3Way_Valve_Hydraulic,
       "max-Opening-3Way-Valve-Hydraulic": max_Opening_3Way_Valve_Hydraulic,
       "proportional-Band-3Way-Valve-Hydrauli-PID": proportional_Band_3Way_Valve_Hydrauli_PID,
       "setpoint-FCM": setpoint_FCM,
       "hysteresis-FCM": hysteresis_FCM,
       "max-Out-Speed-FCM": max_Out_Speed_FCM,
       "min-Out-Speed-FCM": min_Out_Speed_FCM,
       "hysteresis-Cut-off-FCM": hysteresis_Cut_off_FCM,
       "max-Pressure-Alarm-FCM": max_Pressure_Alarm_FCM,
       "hysteresis-Max-Pressure-Alarm-FCM": hysteresis_Max_Pressure_Alarm_FCM,
       "max-Out-FCM": max_Out_FCM,
       "min-Pressure-Alarm-FCM": min_Pressure_Alarm_FCM,
       "hysteresis-Min-Pressure-Alarm-FCM": hysteresis_Min_Pressure_Alarm_FCM,
       "min-Out-FCM": min_Out_FCM,
       "delta-Freecooling": delta_Freecooling,
       "hysteresis-Freecooling": hysteresis_Freecooling,
       "proportional-Band-Freecooling-PID": proportional_Band_Freecooling_PID,
       "offset-Freecooling-PID": offset_Freecooling_PID,
       "temperature-Overlap-Freecooling": temperature_Overlap_Freecooling,
       "min-out-freecooling": min_out_freecooling,
       "neutral-zone-K-costant": neutral_zone_K_costant,
       "neutral-zone-V-variable": neutral_zone_V_variable,
       "proportional-Band-freecooling-Valve-PID": proportional_Band_freecooling_Valve_PID,
       "offset-Freecooling-Valve-PID": offset_Freecooling_Valve_PID,
       "temperature-A-B": temperature_A_B,
       "delta-Thermal-Excusion-Freecoling": delta_Thermal_Excusion_Freecoling,
       "hysteresis-Thermal-Excusion-Freecoling": hysteresis_Thermal_Excusion_Freecoling,
       "alarm-Setpoint-Static-Pressure-Hydraulic-circuit": alarm_Setpoint_Static_Pressure_Hydraulic_circuit,
       "warnig-Setpoint-Static-Pressure-Hydraulic-circuit": warnig_Setpoint_Static_Pressure_Hydraulic_circuit,
       "alarm-Setpoint-Differential-Pressure-Hydraulic-circuit": alarm_Setpoint_Differential_Pressure_Hydraulic_circuit,
       "alarm-Setpoint-Flow-Rate-Hydraulic-circuit": alarm_Setpoint_Flow_Rate_Hydraulic_circuit,
       "tempertaure-Cut-off-FCM": tempertaure_Cut_off_FCM,
       "set-effective": set_effective,
       "set-fc": set_fc,
       "setpoint-a-us": setpoint_a_us,
       "max-setpoint": max_setpoint,
       "min-setpoint": min_setpoint,
       "diff": diff,
       "max-diff": max_diff,
       "min-diff": min_diff,
       "fcs-out": fcs_out,
       "water-temp": water_temp,
       "temp-inlet": temp_inlet,
       "temp-outlet": temp_outlet,
       "flow-value": flow_value,
       "amp-value": amp_value,
       "ta-probe-temp-1": ta_probe_temp_1,
       "ta-probe-temp-2": ta_probe_temp_2,
       "pressione1": pressione1,
       "pressione2": pressione2,
       "pump-sp-press": pump_sp_press,
       "p-wat2": p_wat2,
       "temp-amb": temp_amb,
       "temp-fc": temp_fc,
       "pp1": pp1,
       "pp2": pp2,
       "cooling-capacity": cooling_capacity,
       "freecooling-capacity": freecooling_capacity,
       "total-capacity": total_capacity,
       "integerObjects": integerObjects,
       "ip-Address1": ip_Address1,
       "ip-Address2": ip_Address2,
       "ip-Address3": ip_Address3,
       "ip-Address4": ip_Address4,
       "netMask": netMask,
       "gateway1": gateway1,
       "gateway2": gateway2,
       "gateway3": gateway3,
       "gateway4": gateway4,
       "dns1-1": dns1_1,
       "dns1-2": dns1_2,
       "dns1-3": dns1_3,
       "dns1-4": dns1_4,
       "dns2-1": dns2_1,
       "dns2-2": dns2_2,
       "dns2-3": dns2_3,
       "dns2-4": dns2_4,
       "ip-Address1-Out": ip_Address1_Out,
       "ip-Address2-Out": ip_Address2_Out,
       "ip-Address3-Out": ip_Address3_Out,
       "ip-Address4-Out": ip_Address4_Out,
       "starting-delay-Second-Pump": starting_delay_Second_Pump,
       "starting-delay-btw-Pump-Compressor": starting_delay_btw_Pump_Compressor,
       "overlap-time-Pumps": overlap_time_Pumps,
       "working-time-Pumps": working_time_Pumps,
       "running-time-Chillers": running_time_Chillers,
       "overlap-time-Chillers": overlap_time_Chillers,
       "n-chillers-Max": n_chillers_Max,
       "n-chillers-ON": n_chillers_ON,
       "n-pumps-ON": n_pumps_ON,
       "time-Enable-Pumps-Chiller-Offline": time_Enable_Pumps_Chiller_Offline,
       "time-Running-Pumps-Chiller-Offline": time_Running_Pumps_Chiller_Offline,
       "integral-Time-3Way-Valve-Hydraulic-PID": integral_Time_3Way_Valve_Hydraulic_PID,
       "derivative-Time-3Way-Valve-Hydraulic-PID": derivative_Time_3Way_Valve_Hydraulic_PID,
       "output-Address-3Way-Valve-Hydraulic": output_Address_3Way_Valve_Hydraulic,
       "time-Speed-Up-FCM": time_Speed_Up_FCM,
       "time-Soft-Start-FCM": time_Soft_Start_FCM,
       "delay-Freecooling": delay_Freecooling,
       "integral-Time-Freeccoling-PID": integral_Time_Freeccoling_PID,
       "derivative-Time-Freeccoling-PID": derivative_Time_Freeccoling_PID,
       "time-Min-On-Freecooling-Chiller-timing": time_Min_On_Freecooling_Chiller_timing,
       "time-Min-Off-Freecooling-Chiller-timing": time_Min_Off_Freecooling_Chiller_timing,
       "time-Min-Different-Freecooling-Chiller-timing": time_Min_Different_Freecooling_Chiller_timing,
       "time-Min-Same-Freecooling-Chiller-timing": time_Min_Same_Freecooling_Chiller_timing,
       "integral-Time-Freeccoling-Valve-PID": integral_Time_Freeccoling_Valve_PID,
       "derivative-Time-Freeccoling-Valve-PID": derivative_Time_Freeccoling_Valve_PID,
       "output-Address-Valve-Freecooling": output_Address_Valve_Freecooling,
       "delay-Freecooling-Thermal-Exclusion": delay_Freecooling_Thermal_Exclusion,
       "n-of-alarm-External-Dry-Cooler": n_of_alarm_External_Dry_Cooler,
       "delay-Alarm-Static-Pressure": delay_Alarm_Static_Pressure,
       "n-of-Alarm-Static-Pressure": n_of_Alarm_Static_Pressure,
       "delay-Warning-Static-Pressure": delay_Warning_Static_Pressure,
       "n-of-Warning-Static-Pressure": n_of_Warning_Static_Pressure,
       "n-of-Alarm-Differential-Pressure": n_of_Alarm_Differential_Pressure,
       "priming-Time-Hydraulic-Pressure": priming_Time_Hydraulic_Pressure,
       "delay-priming-Time-Hydraulic-Pressure": delay_priming_Time_Hydraulic_Pressure,
       "output-Address-Alarm-Static-Pressure": output_Address_Alarm_Static_Pressure,
       "n-of-Alarm-Flow-Rate": n_of_Alarm_Flow_Rate,
       "priming-Time-Flow-Rate": priming_Time_Flow_Rate,
       "delay-priming-Time-Flow-Rate": delay_priming_Time_Flow_Rate,
       "bms-address-IDENT": bms_address_IDENT,
       "chiller-name0": chiller_name0,
       "chiller-name1": chiller_name1,
       "current-day": current_day,
       "current-month": current_month,
       "current-year": current_year,
       "current-hour": current_hour,
       "current-minute": current_minute,
       "chiller-mode-operation": chiller_mode_operation,
       "trapObjects": trapObjects,
       "high-pressure-switch-1-alarm": high_pressure_switch_1_alarm,
       "high-pressure-switch-2-alarm": high_pressure_switch_2_alarm,
       "low-pressure-switch-1-alarm": low_pressure_switch_1_alarm,
       "low-pressure-switch-2-alarm": low_pressure_switch_2_alarm,
       "water-level-alarm": water_level_alarm,
       "flow-switch-alarm": flow_switch_alarm,
       "water-static-pressure-alarm": water_static_pressure_alarm,
       "water-static-pressure-warning": water_static_pressure_warning,
       "flow-rate-alarm": flow_rate_alarm,
       "overload-compressor1-circuit1-alarm": overload_compressor1_circuit1_alarm,
       "overload-compressor2-circuit1-alarm": overload_compressor2_circuit1_alarm,
       "overload-compressor3-circuit1-alarm": overload_compressor3_circuit1_alarm,
       "overload-compressor1-circuit2-alarm": overload_compressor1_circuit2_alarm,
       "overload-compressor2-circuit2-alarm": overload_compressor2_circuit2_alarm,
       "overload-compressor3-circuit2-alarm": overload_compressor3_circuit2_alarm,
       "overload-fans-circuit1": overload_fans_circuit1,
       "overload-fans-circuit2": overload_fans_circuit2,
       "overload-fan1-circuit1-alarm": overload_fan1_circuit1_alarm,
       "overload-fan2-circuit1-alarm": overload_fan2_circuit1_alarm,
       "overload-fan3-circuit1-alarm": overload_fan3_circuit1_alarm,
       "overload-fan4-circuit1-alarm": overload_fan4_circuit1_alarm,
       "overload-fan1-circuit-2-alarm": overload_fan1_circuit_2_alarm,
       "overload-fan2-circuit2-alarm": overload_fan2_circuit2_alarm,
       "overload-fan3-circuit2-alarm": overload_fan3_circuit2_alarm,
       "overload-fan4-circuit2-alarm": overload_fan4_circuit2_alarm,
       "overload-pump1-alarm": overload_pump1_alarm,
       "overload-pump2-alarm": overload_pump2_alarm,
       "wrong-phase-rotation-alarm": wrong_phase_rotation_alarm,
       "back-Door-open-alarm": back_Door_open_alarm,
       "alarm-idrofrigo-pump-c-1": alarm_idrofrigo_pump_c_1,
       "alarm-idrofrigo-pump-c-2": alarm_idrofrigo_pump_c_2,
       "alarm-idrofrigo-fl-C": alarm_idrofrigo_fl_C,
       "remote-on-off": remote_on_off,
       "chiller-ON-OFF": chiller_ON_OFF,
       "alarm-disch-scw-1": alarm_disch_scw_1,
       "alarm-disch-scw-2": alarm_disch_scw_2,
       "alarm-probe-inlet": alarm_probe_inlet,
       "alarm-probe-amb": alarm_probe_amb,
       "alarm-frigo-fl1": alarm_frigo_fl1,
       "alarm-idro-pump1": alarm_idro_pump1,
       "alarm-idro-pump2": alarm_idro_pump2,
       "alarm-idro-fl1": alarm_idro_fl1,
       "alarm-warning-fl1": alarm_warning_fl1,
       "alarm-hi-water-temp": alarm_hi_water_temp,
       "alarm-lo-water-temp": alarm_lo_water_temp,
       "alarm-ta-probe1": alarm_ta_probe1,
       "alarm-hi-press": alarm_hi_press,
       "alarm-lo-press": alarm_lo_press,
       "alarm-probe-evap-1": alarm_probe_evap_1,
       "alarm-probe-evap-2": alarm_probe_evap_2,
       "alarm-hi-press-1": alarm_hi_press_1,
       "alarm-hi-press-2": alarm_hi_press_2,
       "alarm-lo-press-1": alarm_lo_press_1,
       "alarm-lo-press-2": alarm_lo_press_2,
       "alarm-probe-tank": alarm_probe_tank,
       "alarm-off-line-1": alarm_off_line_1,
       "alarm-off-line-2": alarm_off_line_2,
       "alarm-off-line-3": alarm_off_line_3,
       "alarm-off-line-4": alarm_off_line_4,
       "alarm-off-line-5": alarm_off_line_5,
       "alarm-off-line-6": alarm_off_line_6,
       "alarm-off-line-7": alarm_off_line_7,
       "alarm-off-line-8": alarm_off_line_8,
       "alarm-ta-probe2": alarm_ta_probe2,
       "alarm-sms": alarm_sms,
       "alarm-modem": alarm_modem,
       "alarm-sms-coda": alarm_sms_coda,
       "alarm-probe-fc": alarm_probe_fc,
       "alarm-maint-pw1": alarm_maint_pw1,
       "alarm-maint-pw2": alarm_maint_pw2,
       "alarm-hi-temp-rid": alarm_hi_temp_rid,
       "alarm-q-fc-sep": alarm_q_fc_sep,
       "alarm-p-wat2": alarm_p_wat2,
       "alarm-p-wat1": alarm_p_wat1,
       "alarm-foult-flow-p1": alarm_foult_flow_p1,
       "alarm-foult-flow-p2": alarm_foult_flow_p2,
       "alarm-foult-fl1-p1": alarm_foult_fl1_p1,
       "alarm-foult-fl1-p2": alarm_foult_fl1_p2,
       "alarm-warning-le": alarm_warning_le,
       "alarm-frigo-fl-C": alarm_frigo_fl_C,
       "alarm-idro-pump-c-1": alarm_idro_pump_c_1,
       "alarm-idro-pump-c-2": alarm_idro_pump_c_2,
       "alarm-idro-fl-C": alarm_idro_fl_C,
       "alarm-warning-fl-C": alarm_warning_fl_C,
       "alarm-foul-fl-C-p1": alarm_foul_fl_C_p1,
       "alarm-foul-fl-C-p2": alarm_foul_fl_C_p2}
)
