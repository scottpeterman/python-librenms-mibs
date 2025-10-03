# SNMP MIB module (DB7001-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\deva\DB7001-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:24 2025
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

devabroadcast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35833)
)
if mibBuilder.loadTexts:
    devabroadcast.setRevisions(
        ("2022-01-04 11:00",
         "2022-01-04 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Fr8p8(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class Fr1p15(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class Ix10(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class Ix1000(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



# MIB Managed Objects in the order of their OIDs

_Db7001_ObjectIdentity = ObjectIdentity
db7001 = _Db7001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37)
)
if mibBuilder.loadTexts:
    db7001.setStatus("current")
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 1)
)


class _Fwrev_Type(DisplayString):
    """Custom type fwrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Fwrev_Type.__name__ = "DisplayString"
_Fwrev_Object = MibScalar
fwrev = _Fwrev_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 1, 1),
    _Fwrev_Type()
)
fwrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwrev.setStatus("current")


class _Sernum_Type(DisplayString):
    """Custom type sernum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Sernum_Type.__name__ = "DisplayString"
_Sernum_Object = MibScalar
sernum = _Sernum_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 1, 2),
    _Sernum_Type()
)
sernum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sernum.setStatus("current")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2)
)
_Tuner_ObjectIdentity = ObjectIdentity
tuner = _Tuner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1)
)
_MainStation_ObjectIdentity = ObjectIdentity
mainStation = _MainStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 1)
)


class _Freq_Type(Integer32):
    """Custom type freq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87100, 107900),
    )


_Freq_Type.__name__ = "Integer32"
_Freq_Object = MibScalar
freq = _Freq_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 1, 1),
    _Freq_Type()
)
freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freq.setStatus("current")


class _Att_Type(Integer32):
    """Custom type att based on Integer32"""
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
        *(("attAuto", 0),
          ("attOFF", 1),
          ("att10dB", 2),
          ("att20dB", 3),
          ("att30dB", 4))
    )


_Att_Type.__name__ = "Integer32"
_Att_Object = MibScalar
att = _Att_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 1, 2),
    _Att_Type()
)
att.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    att.setStatus("current")


class _Piproten_Type(Integer32):
    """Custom type piproten based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Piproten_Type.__name__ = "Integer32"
_Piproten_Object = MibScalar
piproten = _Piproten_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 1, 3),
    _Piproten_Type()
)
piproten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piproten.setStatus("current")


class _Piprot_Type(Integer32):
    """Custom type piprot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Piprot_Type.__name__ = "Integer32"
_Piprot_Object = MibScalar
piprot = _Piprot_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 1, 4),
    _Piprot_Type()
)
piprot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piprot.setStatus("current")
_BackupStation_ObjectIdentity = ObjectIdentity
backupStation = _BackupStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 2)
)


class _Altsfreq_Type(Integer32):
    """Custom type altsfreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87100, 107900),
    )


_Altsfreq_Type.__name__ = "Integer32"
_Altsfreq_Object = MibScalar
altsfreq = _Altsfreq_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 2, 1),
    _Altsfreq_Type()
)
altsfreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altsfreq.setStatus("current")


class _Altsatt_Type(Integer32):
    """Custom type altsatt based on Integer32"""
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
        *(("attAuto", 0),
          ("attOFF", 1),
          ("att10dB", 2),
          ("att20dB", 3),
          ("att30dB", 4))
    )


_Altsatt_Type.__name__ = "Integer32"
_Altsatt_Object = MibScalar
altsatt = _Altsatt_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 2, 2),
    _Altsatt_Type()
)
altsatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altsatt.setStatus("current")


class _Altspiproten_Type(Integer32):
    """Custom type altspiproten based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Altspiproten_Type.__name__ = "Integer32"
_Altspiproten_Object = MibScalar
altspiproten = _Altspiproten_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 2, 3),
    _Altspiproten_Type()
)
altspiproten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altspiproten.setStatus("current")


class _Altspiprot_Type(Integer32):
    """Custom type altspiprot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Altspiprot_Type.__name__ = "Integer32"
_Altspiprot_Object = MibScalar
altspiprot = _Altspiprot_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 2, 4),
    _Altspiprot_Type()
)
altspiprot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altspiprot.setStatus("current")


class _Freqstep_Type(Integer32):
    """Custom type freqstep based on Integer32"""
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
        *(("freqstep10kHz", 0),
          ("freqstep20kHz", 1),
          ("freqstep50kHz", 2),
          ("freqstep100kHz", 3),
          ("freqstep200kHz", 4))
    )


_Freqstep_Type.__name__ = "Integer32"
_Freqstep_Object = MibScalar
freqstep = _Freqstep_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 3),
    _Freqstep_Type()
)
freqstep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    freqstep.setStatus("current")


class _Deemph_Type(Integer32):
    """Custom type deemph based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deemphFLAT", 0),
          ("deemph50uS", 1),
          ("deemph75uS", 2))
    )


_Deemph_Type.__name__ = "Integer32"
_Deemph_Object = MibScalar
deemph = _Deemph_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 4),
    _Deemph_Type()
)
deemph.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deemph.setStatus("current")


class _Rdsmode_Type(Integer32):
    """Custom type rdsmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rdsmodeRDS", 0),
          ("rdsmodeRBDS", 1))
    )


_Rdsmode_Type.__name__ = "Integer32"
_Rdsmode_Object = MibScalar
rdsmode = _Rdsmode_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 5),
    _Rdsmode_Type()
)
rdsmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsmode.setStatus("current")


class _Ifbw_Type(Integer32):
    """Custom type ifbw based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("ifbw27kHz", 0),
          ("ifbw36kHz", 1),
          ("ifbw45kHz", 2),
          ("ifbw53kHz", 3),
          ("ifbw62kHz", 4),
          ("ifbw71kHz", 5),
          ("ifbw79kHz", 6),
          ("ifbw88kHz", 7),
          ("ifbw97kHz", 8),
          ("ifbw105kHz", 9),
          ("ifbw114kHz", 10),
          ("ifbw123kHz", 11),
          ("ifbw131kHz", 12),
          ("ifbw140kHz", 13),
          ("ifbw149kHz", 14),
          ("ifbw157kHz", 15),
          ("ifbwAuto", 16))
    )


_Ifbw_Type.__name__ = "Integer32"
_Ifbw_Object = MibScalar
ifbw = _Ifbw_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 6),
    _Ifbw_Type()
)
ifbw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifbw.setStatus("current")


class _Stblend_Type(Integer32):
    """Custom type stblend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("altAuto", 0),
          ("altOff", 1))
    )


_Stblend_Type.__name__ = "Integer32"
_Stblend_Object = MibScalar
stblend = _Stblend_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 7),
    _Stblend_Type()
)
stblend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stblend.setStatus("current")


class _Hicut_Type(Integer32):
    """Custom type hicut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("altAuto", 0),
          ("altOff", 1))
    )


_Hicut_Type.__name__ = "Integer32"
_Hicut_Object = MibScalar
hicut = _Hicut_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 8),
    _Hicut_Type()
)
hicut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hicut.setStatus("current")


class _Hiblend_Type(Integer32):
    """Custom type hiblend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("altAuto", 0),
          ("altOff", 1))
    )


_Hiblend_Type.__name__ = "Integer32"
_Hiblend_Object = MibScalar
hiblend = _Hiblend_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 9),
    _Hiblend_Type()
)
hiblend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiblend.setStatus("current")


class _Smute_Type(Integer32):
    """Custom type smute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("altAuto", 0),
          ("altOff", 1))
    )


_Smute_Type.__name__ = "Integer32"
_Smute_Object = MibScalar
smute = _Smute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 10),
    _Smute_Type()
)
smute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smute.setStatus("current")


class _Audiocut_Type(Integer32):
    """Custom type audiocut based on Integer32"""
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
        *(("audiocut5kHz", 0),
          ("audiocut10kHz", 1),
          ("audiocut15kHz", 2),
          ("audiocutOff", 3))
    )


_Audiocut_Type.__name__ = "Integer32"
_Audiocut_Object = MibScalar
audiocut = _Audiocut_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 11),
    _Audiocut_Type()
)
audiocut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audiocut.setStatus("current")
_AverageAndPeak_ObjectIdentity = ObjectIdentity
averageAndPeak = _AverageAndPeak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 12)
)


class _Avratck_Type(Integer32):
    """Custom type avratck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Avratck_Type.__name__ = "Integer32"
_Avratck_Object = MibScalar
avratck = _Avratck_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 12, 1),
    _Avratck_Type()
)
avratck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avratck.setStatus("current")


class _Avrrel_Type(Integer32):
    """Custom type avrrel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_Avrrel_Type.__name__ = "Integer32"
_Avrrel_Object = MibScalar
avrrel = _Avrrel_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 12, 2),
    _Avrrel_Type()
)
avrrel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avrrel.setStatus("current")


class _Peakhold_Type(Integer32):
    """Custom type peakhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 5000),
    )


_Peakhold_Type.__name__ = "Integer32"
_Peakhold_Object = MibScalar
peakhold = _Peakhold_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 1, 12, 3),
    _Peakhold_Type()
)
peakhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakhold.setStatus("current")
_MpxGenerator_ObjectIdentity = ObjectIdentity
mpxGenerator = _MpxGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2)
)


class _Mpxsrc_Type(Integer32):
    """Custom type mpxsrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mpxsrcRAWMPX", 0),
          ("mpxsrcStereoGen", 1),
          ("mpxsrcTestTone400Hz", 2))
    )


_Mpxsrc_Type.__name__ = "Integer32"
_Mpxsrc_Object = MibScalar
mpxsrc = _Mpxsrc_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 1),
    _Mpxsrc_Type()
)
mpxsrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxsrc.setStatus("current")


class _Stmode_Type(Integer32):
    """Custom type stmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("altMono", 8),
          ("altStereo", 9))
    )


_Stmode_Type.__name__ = "Integer32"
_Stmode_Object = MibScalar
stmode = _Stmode_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 2),
    _Stmode_Type()
)
stmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stmode.setStatus("current")


class _Preemph_Type(Integer32):
    """Custom type preemph based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deemphFLAT", 0),
          ("deemph50uS", 1),
          ("deemph75uS", 2))
    )


_Preemph_Type.__name__ = "Integer32"
_Preemph_Object = MibScalar
preemph = _Preemph_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 3),
    _Preemph_Type()
)
preemph.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemph.setStatus("current")


class _Injaudio_Type(Fr8p8):
    """Custom type injaudio based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3072, 768),
    )


_Injaudio_Type.__name__ = "Fr8p8"
_Injaudio_Object = MibScalar
injaudio = _Injaudio_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 4),
    _Injaudio_Type()
)
injaudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    injaudio.setStatus("current")


class _Injpilot_Type(Fr8p8):
    """Custom type injpilot based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560),
    )


_Injpilot_Type.__name__ = "Fr8p8"
_Injpilot_Object = MibScalar
injpilot = _Injpilot_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 5),
    _Injpilot_Type()
)
injpilot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    injpilot.setStatus("current")


class _Injrds_Type(Fr8p8):
    """Custom type injrds based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560),
    )


_Injrds_Type.__name__ = "Fr8p8"
_Injrds_Object = MibScalar
injrds = _Injrds_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 6),
    _Injrds_Type()
)
injrds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    injrds.setStatus("current")


class _Phpilot_Type(Fr8p8):
    """Custom type phpilot based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2560, 2560),
    )


_Phpilot_Type.__name__ = "Fr8p8"
_Phpilot_Object = MibScalar
phpilot = _Phpilot_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 7),
    _Phpilot_Type()
)
phpilot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phpilot.setStatus("current")


class _Mpxlimen_Type(Integer32):
    """Custom type mpxlimen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Mpxlimen_Type.__name__ = "Integer32"
_Mpxlimen_Object = MibScalar
mpxlimen = _Mpxlimen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 8),
    _Mpxlimen_Type()
)
mpxlimen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxlimen.setStatus("current")


class _Mpxlimth_Type(Integer32):
    """Custom type mpxlimth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280, 2560),
    )


_Mpxlimth_Type.__name__ = "Integer32"
_Mpxlimth_Object = MibScalar
mpxlimth = _Mpxlimth_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 2, 9),
    _Mpxlimth_Type()
)
mpxlimth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpxlimth.setStatus("current")
_RdsEncoder_ObjectIdentity = ObjectIdentity
rdsEncoder = _RdsEncoder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3)
)


class _Rdssrc_Type(Integer32):
    """Custom type rdssrc based on Integer32"""
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
        *(("rdssrcOriginal", 0),
          ("rdssrcLocalFallback", 1),
          ("rdssrcLocal", 2),
          ("rdssrcReplace", 3))
    )


_Rdssrc_Type.__name__ = "Integer32"
_Rdssrc_Object = MibScalar
rdssrc = _Rdssrc_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 1),
    _Rdssrc_Type()
)
rdssrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdssrc.setStatus("current")


class _Rdspi_Type(Integer32):
    """Custom type rdspi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rdspi_Type.__name__ = "Integer32"
_Rdspi_Object = MibScalar
rdspi = _Rdspi_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 2),
    _Rdspi_Type()
)
rdspi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdspi.setStatus("current")


class _Rdsps_Type(DisplayString):
    """Custom type rdsps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Rdsps_Type.__name__ = "DisplayString"
_Rdsps_Object = MibScalar
rdsps = _Rdsps_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 3),
    _Rdsps_Type()
)
rdsps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsps.setStatus("current")


class _Rdsrt_Type(DisplayString):
    """Custom type rdsrt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 67),
    )


_Rdsrt_Type.__name__ = "DisplayString"
_Rdsrt_Object = MibScalar
rdsrt = _Rdsrt_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 4),
    _Rdsrt_Type()
)
rdsrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsrt.setStatus("current")


class _Rdspty_Type(Integer32):
    """Custom type rdspty based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("rdsptyNone", 0),
          ("rdsptyNews", 1),
          ("rdsptyCurrentAffairs", 2),
          ("rdsptyInfo", 3),
          ("rdsptySport", 4),
          ("rdsptyEducation", 5),
          ("rdsptyDrama", 6),
          ("rdsptyCultures", 7),
          ("rdsptyScience", 8),
          ("rdsptyVariedSpeech", 9),
          ("rdsptyPopMusic", 10),
          ("rdsptyRockMusic", 11),
          ("rdsptyEasyListening", 12),
          ("rdsptyLightClassicsM", 13),
          ("rdsptySeriousClassics", 14),
          ("rdsptyOtherMusic", 15),
          ("rdsptyWeather", 16),
          ("rdsptyFinance", 17),
          ("rdsptyChildrensProgs", 18),
          ("rdsptySocialAffairs", 19),
          ("rdsptyReligion", 20),
          ("rdsptyPhoneIn", 21),
          ("rdsptyTravelTouring", 22),
          ("rdsptyLeisureHobby", 23),
          ("rdsptyJazzMusic", 24),
          ("rdsptyCountryMusic", 25),
          ("rdsptyNationalMusic", 26),
          ("rdsptyOldiesMusic", 27),
          ("rdsptyFolkMusic", 28),
          ("rdsptyDocumentary", 29),
          ("rdsptyAlarmTest", 30),
          ("rdsptyAlarmAlarm", 31))
    )


_Rdspty_Type.__name__ = "Integer32"
_Rdspty_Object = MibScalar
rdspty = _Rdspty_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 5),
    _Rdspty_Type()
)
rdspty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdspty.setStatus("current")


class _Rdsms_Type(Integer32):
    """Custom type rdsms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("altSpeech", 10),
          ("altMusic", 11))
    )


_Rdsms_Type.__name__ = "Integer32"
_Rdsms_Object = MibScalar
rdsms = _Rdsms_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 6),
    _Rdsms_Type()
)
rdsms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsms.setStatus("current")


class _Rdstp_Type(Integer32):
    """Custom type rdstp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_Rdstp_Type.__name__ = "Integer32"
_Rdstp_Object = MibScalar
rdstp = _Rdstp_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 7),
    _Rdstp_Type()
)
rdstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdstp.setStatus("current")


class _Rdsta_Type(Integer32):
    """Custom type rdsta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_Rdsta_Type.__name__ = "Integer32"
_Rdsta_Object = MibScalar
rdsta = _Rdsta_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 8),
    _Rdsta_Type()
)
rdsta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsta.setStatus("current")
_DiFlags_ObjectIdentity = ObjectIdentity
diFlags = _DiFlags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 9)
)


class _Rdsdi0_Type(Integer32):
    """Custom type rdsdi0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_Rdsdi0_Type.__name__ = "Integer32"
_Rdsdi0_Object = MibScalar
rdsdi0 = _Rdsdi0_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 9, 1),
    _Rdsdi0_Type()
)
rdsdi0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsdi0.setStatus("current")


class _Rdsdi1_Type(Integer32):
    """Custom type rdsdi1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_Rdsdi1_Type.__name__ = "Integer32"
_Rdsdi1_Object = MibScalar
rdsdi1 = _Rdsdi1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 9, 2),
    _Rdsdi1_Type()
)
rdsdi1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsdi1.setStatus("current")


class _Rdsdi2_Type(Integer32):
    """Custom type rdsdi2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_Rdsdi2_Type.__name__ = "Integer32"
_Rdsdi2_Object = MibScalar
rdsdi2 = _Rdsdi2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 9, 3),
    _Rdsdi2_Type()
)
rdsdi2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsdi2.setStatus("current")


class _Rdsdi3_Type(Integer32):
    """Custom type rdsdi3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_Rdsdi3_Type.__name__ = "Integer32"
_Rdsdi3_Object = MibScalar
rdsdi3 = _Rdsdi3_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 9, 4),
    _Rdsdi3_Type()
)
rdsdi3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsdi3.setStatus("current")
_AfList_ObjectIdentity = ObjectIdentity
afList = _AfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10)
)


class _Rdsafcount_Type(Integer32):
    """Custom type rdsafcount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_Rdsafcount_Type.__name__ = "Integer32"
_Rdsafcount_Object = MibScalar
rdsafcount = _Rdsafcount_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 1),
    _Rdsafcount_Type()
)
rdsafcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsafcount.setStatus("current")


class _Rdsaf1_Type(Integer32):
    """Custom type rdsaf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf1_Type.__name__ = "Integer32"
_Rdsaf1_Object = MibScalar
rdsaf1 = _Rdsaf1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 2),
    _Rdsaf1_Type()
)
rdsaf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf1.setStatus("current")


class _Rdsaf2_Type(Integer32):
    """Custom type rdsaf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf2_Type.__name__ = "Integer32"
_Rdsaf2_Object = MibScalar
rdsaf2 = _Rdsaf2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 3),
    _Rdsaf2_Type()
)
rdsaf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf2.setStatus("current")


class _Rdsaf3_Type(Integer32):
    """Custom type rdsaf3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf3_Type.__name__ = "Integer32"
_Rdsaf3_Object = MibScalar
rdsaf3 = _Rdsaf3_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 4),
    _Rdsaf3_Type()
)
rdsaf3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf3.setStatus("current")


class _Rdsaf4_Type(Integer32):
    """Custom type rdsaf4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf4_Type.__name__ = "Integer32"
_Rdsaf4_Object = MibScalar
rdsaf4 = _Rdsaf4_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 5),
    _Rdsaf4_Type()
)
rdsaf4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf4.setStatus("current")


class _Rdsaf5_Type(Integer32):
    """Custom type rdsaf5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf5_Type.__name__ = "Integer32"
_Rdsaf5_Object = MibScalar
rdsaf5 = _Rdsaf5_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 6),
    _Rdsaf5_Type()
)
rdsaf5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf5.setStatus("current")


class _Rdsaf6_Type(Integer32):
    """Custom type rdsaf6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf6_Type.__name__ = "Integer32"
_Rdsaf6_Object = MibScalar
rdsaf6 = _Rdsaf6_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 7),
    _Rdsaf6_Type()
)
rdsaf6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf6.setStatus("current")


class _Rdsaf7_Type(Integer32):
    """Custom type rdsaf7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf7_Type.__name__ = "Integer32"
_Rdsaf7_Object = MibScalar
rdsaf7 = _Rdsaf7_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 8),
    _Rdsaf7_Type()
)
rdsaf7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf7.setStatus("current")


class _Rdsaf8_Type(Integer32):
    """Custom type rdsaf8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf8_Type.__name__ = "Integer32"
_Rdsaf8_Object = MibScalar
rdsaf8 = _Rdsaf8_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 9),
    _Rdsaf8_Type()
)
rdsaf8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf8.setStatus("current")


class _Rdsaf9_Type(Integer32):
    """Custom type rdsaf9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf9_Type.__name__ = "Integer32"
_Rdsaf9_Object = MibScalar
rdsaf9 = _Rdsaf9_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 10),
    _Rdsaf9_Type()
)
rdsaf9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf9.setStatus("current")


class _Rdsaf10_Type(Integer32):
    """Custom type rdsaf10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf10_Type.__name__ = "Integer32"
_Rdsaf10_Object = MibScalar
rdsaf10 = _Rdsaf10_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 11),
    _Rdsaf10_Type()
)
rdsaf10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf10.setStatus("current")


class _Rdsaf11_Type(Integer32):
    """Custom type rdsaf11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf11_Type.__name__ = "Integer32"
_Rdsaf11_Object = MibScalar
rdsaf11 = _Rdsaf11_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 12),
    _Rdsaf11_Type()
)
rdsaf11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf11.setStatus("current")


class _Rdsaf12_Type(Integer32):
    """Custom type rdsaf12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf12_Type.__name__ = "Integer32"
_Rdsaf12_Object = MibScalar
rdsaf12 = _Rdsaf12_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 13),
    _Rdsaf12_Type()
)
rdsaf12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf12.setStatus("current")


class _Rdsaf13_Type(Integer32):
    """Custom type rdsaf13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf13_Type.__name__ = "Integer32"
_Rdsaf13_Object = MibScalar
rdsaf13 = _Rdsaf13_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 14),
    _Rdsaf13_Type()
)
rdsaf13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf13.setStatus("current")


class _Rdsaf14_Type(Integer32):
    """Custom type rdsaf14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf14_Type.__name__ = "Integer32"
_Rdsaf14_Object = MibScalar
rdsaf14 = _Rdsaf14_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 15),
    _Rdsaf14_Type()
)
rdsaf14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf14.setStatus("current")


class _Rdsaf15_Type(Integer32):
    """Custom type rdsaf15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf15_Type.__name__ = "Integer32"
_Rdsaf15_Object = MibScalar
rdsaf15 = _Rdsaf15_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 16),
    _Rdsaf15_Type()
)
rdsaf15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf15.setStatus("current")


class _Rdsaf16_Type(Integer32):
    """Custom type rdsaf16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf16_Type.__name__ = "Integer32"
_Rdsaf16_Object = MibScalar
rdsaf16 = _Rdsaf16_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 17),
    _Rdsaf16_Type()
)
rdsaf16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf16.setStatus("current")


class _Rdsaf17_Type(Integer32):
    """Custom type rdsaf17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf17_Type.__name__ = "Integer32"
_Rdsaf17_Object = MibScalar
rdsaf17 = _Rdsaf17_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 18),
    _Rdsaf17_Type()
)
rdsaf17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf17.setStatus("current")


class _Rdsaf18_Type(Integer32):
    """Custom type rdsaf18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf18_Type.__name__ = "Integer32"
_Rdsaf18_Object = MibScalar
rdsaf18 = _Rdsaf18_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 19),
    _Rdsaf18_Type()
)
rdsaf18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf18.setStatus("current")


class _Rdsaf19_Type(Integer32):
    """Custom type rdsaf19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf19_Type.__name__ = "Integer32"
_Rdsaf19_Object = MibScalar
rdsaf19 = _Rdsaf19_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 20),
    _Rdsaf19_Type()
)
rdsaf19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf19.setStatus("current")


class _Rdsaf20_Type(Integer32):
    """Custom type rdsaf20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf20_Type.__name__ = "Integer32"
_Rdsaf20_Object = MibScalar
rdsaf20 = _Rdsaf20_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 21),
    _Rdsaf20_Type()
)
rdsaf20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf20.setStatus("current")


class _Rdsaf21_Type(Integer32):
    """Custom type rdsaf21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf21_Type.__name__ = "Integer32"
_Rdsaf21_Object = MibScalar
rdsaf21 = _Rdsaf21_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 22),
    _Rdsaf21_Type()
)
rdsaf21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf21.setStatus("current")


class _Rdsaf22_Type(Integer32):
    """Custom type rdsaf22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf22_Type.__name__ = "Integer32"
_Rdsaf22_Object = MibScalar
rdsaf22 = _Rdsaf22_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 23),
    _Rdsaf22_Type()
)
rdsaf22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf22.setStatus("current")


class _Rdsaf23_Type(Integer32):
    """Custom type rdsaf23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf23_Type.__name__ = "Integer32"
_Rdsaf23_Object = MibScalar
rdsaf23 = _Rdsaf23_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 24),
    _Rdsaf23_Type()
)
rdsaf23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf23.setStatus("current")


class _Rdsaf24_Type(Integer32):
    """Custom type rdsaf24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf24_Type.__name__ = "Integer32"
_Rdsaf24_Object = MibScalar
rdsaf24 = _Rdsaf24_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 25),
    _Rdsaf24_Type()
)
rdsaf24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf24.setStatus("current")


class _Rdsaf25_Type(Integer32):
    """Custom type rdsaf25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87600, 107900),
    )


_Rdsaf25_Type.__name__ = "Integer32"
_Rdsaf25_Object = MibScalar
rdsaf25 = _Rdsaf25_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 10, 26),
    _Rdsaf25_Type()
)
rdsaf25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsaf25.setStatus("current")


class _Rdsreplpi_Type(Integer32):
    """Custom type rdsreplpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplpi_Type.__name__ = "Integer32"
_Rdsreplpi_Object = MibScalar
rdsreplpi = _Rdsreplpi_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 11),
    _Rdsreplpi_Type()
)
rdsreplpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplpi.setStatus("current")


class _Rdsreplps_Type(Integer32):
    """Custom type rdsreplps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplps_Type.__name__ = "Integer32"
_Rdsreplps_Object = MibScalar
rdsreplps = _Rdsreplps_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 12),
    _Rdsreplps_Type()
)
rdsreplps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplps.setStatus("current")


class _Rdsreplrt_Type(Integer32):
    """Custom type rdsreplrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplrt_Type.__name__ = "Integer32"
_Rdsreplrt_Object = MibScalar
rdsreplrt = _Rdsreplrt_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 13),
    _Rdsreplrt_Type()
)
rdsreplrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplrt.setStatus("current")


class _Rdsreplpty_Type(Integer32):
    """Custom type rdsreplpty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplpty_Type.__name__ = "Integer32"
_Rdsreplpty_Object = MibScalar
rdsreplpty = _Rdsreplpty_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 14),
    _Rdsreplpty_Type()
)
rdsreplpty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplpty.setStatus("current")


class _Rdsreplms_Type(Integer32):
    """Custom type rdsreplms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplms_Type.__name__ = "Integer32"
_Rdsreplms_Object = MibScalar
rdsreplms = _Rdsreplms_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 15),
    _Rdsreplms_Type()
)
rdsreplms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplms.setStatus("current")


class _Rdsrepltp_Type(Integer32):
    """Custom type rdsrepltp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsrepltp_Type.__name__ = "Integer32"
_Rdsrepltp_Object = MibScalar
rdsrepltp = _Rdsrepltp_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 16),
    _Rdsrepltp_Type()
)
rdsrepltp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsrepltp.setStatus("current")


class _Rdsreplta_Type(Integer32):
    """Custom type rdsreplta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplta_Type.__name__ = "Integer32"
_Rdsreplta_Object = MibScalar
rdsreplta = _Rdsreplta_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 17),
    _Rdsreplta_Type()
)
rdsreplta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplta.setStatus("current")


class _Rdsrepldi_Type(Integer32):
    """Custom type rdsrepldi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsrepldi_Type.__name__ = "Integer32"
_Rdsrepldi_Object = MibScalar
rdsrepldi = _Rdsrepldi_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 18),
    _Rdsrepldi_Type()
)
rdsrepldi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsrepldi.setStatus("current")


class _Rdsreplaf_Type(Integer32):
    """Custom type rdsreplaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Rdsreplaf_Type.__name__ = "Integer32"
_Rdsreplaf_Object = MibScalar
rdsreplaf = _Rdsreplaf_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 3, 19),
    _Rdsreplaf_Type()
)
rdsreplaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdsreplaf.setStatus("current")
_Communication_ObjectIdentity = ObjectIdentity
communication = _Communication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4)
)
_GeneralSetup_ObjectIdentity = ObjectIdentity
generalSetup = _GeneralSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1)
)


class _Ethen_Type(Integer32):
    """Custom type ethen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Ethen_Type.__name__ = "Integer32"
_Ethen_Object = MibScalar
ethen = _Ethen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 1),
    _Ethen_Type()
)
ethen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethen.setStatus("current")


class _Snmpen_Type(Integer32):
    """Custom type snmpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Snmpen_Type.__name__ = "Integer32"
_Snmpen_Object = MibScalar
snmpen = _Snmpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 2),
    _Snmpen_Type()
)
snmpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpen.setStatus("current")


class _Appen_Type(Integer32):
    """Custom type appen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Appen_Type.__name__ = "Integer32"
_Appen_Object = MibScalar
appen = _Appen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 3),
    _Appen_Type()
)
appen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appen.setStatus("current")


class _Httpen_Type(Integer32):
    """Custom type httpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Httpen_Type.__name__ = "Integer32"
_Httpen_Object = MibScalar
httpen = _Httpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 4),
    _Httpen_Type()
)
httpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpen.setStatus("current")


class _Ftpen_Type(Integer32):
    """Custom type ftpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Ftpen_Type.__name__ = "Integer32"
_Ftpen_Object = MibScalar
ftpen = _Ftpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 5),
    _Ftpen_Type()
)
ftpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpen.setStatus("current")


class _Emailen_Type(Integer32):
    """Custom type emailen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("smtpconnDEVAAccount", 2),
          ("smtpconnSMTPAccount", 3),
          ("smtpconnDisabled", 4))
    )


_Emailen_Type.__name__ = "Integer32"
_Emailen_Object = MibScalar
emailen = _Emailen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 6),
    _Emailen_Type()
)
emailen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailen.setStatus("current")


class _Sntpen_Type(Integer32):
    """Custom type sntpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Sntpen_Type.__name__ = "Integer32"
_Sntpen_Object = MibScalar
sntpen = _Sntpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 7),
    _Sntpen_Type()
)
sntpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpen.setStatus("current")


class _Streamen_Type(Integer32):
    """Custom type streamen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Streamen_Type.__name__ = "Integer32"
_Streamen_Object = MibScalar
streamen = _Streamen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 8),
    _Streamen_Type()
)
streamen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamen.setStatus("current")


class _Syslogen_Type(Integer32):
    """Custom type syslogen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Syslogen_Type.__name__ = "Integer32"
_Syslogen_Object = MibScalar
syslogen = _Syslogen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 9),
    _Syslogen_Type()
)
syslogen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogen.setStatus("current")


class _Uecpsrven_Type(Integer32):
    """Custom type uecpsrven based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Uecpsrven_Type.__name__ = "Integer32"
_Uecpsrven_Object = MibScalar
uecpsrven = _Uecpsrven_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 10),
    _Uecpsrven_Type()
)
uecpsrven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uecpsrven.setStatus("current")


class _Uecprelen_Type(Integer32):
    """Custom type uecprelen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Uecprelen_Type.__name__ = "Integer32"
_Uecprelen_Object = MibScalar
uecprelen = _Uecprelen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 11),
    _Uecprelen_Type()
)
uecprelen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uecprelen.setStatus("current")


class _Usben_Type(Integer32):
    """Custom type usben based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Usben_Type.__name__ = "Integer32"
_Usben_Object = MibScalar
usben = _Usben_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 12),
    _Usben_Type()
)
usben.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usben.setStatus("current")


class _Upnpen_Type(Integer32):
    """Custom type upnpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Upnpen_Type.__name__ = "Integer32"
_Upnpen_Object = MibScalar
upnpen = _Upnpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 1, 13),
    _Upnpen_Type()
)
upnpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpen.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2)
)


class _Dhcpen_Type(Integer32):
    """Custom type dhcpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Dhcpen_Type.__name__ = "Integer32"
_Dhcpen_Object = MibScalar
dhcpen = _Dhcpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2, 1),
    _Dhcpen_Type()
)
dhcpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpen.setStatus("current")
_Ip_Type = IpAddress
_Ip_Object = MibScalar
ip = _Ip_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2, 2),
    _Ip_Type()
)
ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip.setStatus("current")
_Netmask_Type = IpAddress
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2, 3),
    _Netmask_Type()
)
netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_Gwip_Type = IpAddress
_Gwip_Object = MibScalar
gwip = _Gwip_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2, 4),
    _Gwip_Type()
)
gwip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwip.setStatus("current")
_Dns1ip_Type = IpAddress
_Dns1ip_Object = MibScalar
dns1ip = _Dns1ip_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2, 5),
    _Dns1ip_Type()
)
dns1ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns1ip.setStatus("current")
_Dns2ip_Type = IpAddress
_Dns2ip_Object = MibScalar
dns2ip = _Dns2ip_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 2, 6),
    _Dns2ip_Type()
)
dns2ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns2ip.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3)
)
_Snmpmip_Type = IpAddress
_Snmpmip_Object = MibScalar
snmpmip = _Snmpmip_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 1),
    _Snmpmip_Type()
)
snmpmip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpmip.setStatus("current")


class _Snmpmport_Type(Integer32):
    """Custom type snmpmport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Snmpmport_Type.__name__ = "Integer32"
_Snmpmport_Object = MibScalar
snmpmport = _Snmpmport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 2),
    _Snmpmport_Type()
)
snmpmport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpmport.setStatus("current")


class _Snmpaport_Type(Integer32):
    """Custom type snmpaport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Snmpaport_Type.__name__ = "Integer32"
_Snmpaport_Object = MibScalar
snmpaport = _Snmpaport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 3),
    _Snmpaport_Type()
)
snmpaport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpaport.setStatus("current")


class _Snmpaid_Type(Integer32):
    """Custom type snmpaid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Snmpaid_Type.__name__ = "Integer32"
_Snmpaid_Object = MibScalar
snmpaid = _Snmpaid_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 4),
    _Snmpaid_Type()
)
snmpaid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpaid.setStatus("current")


class _Snmprcomm_Type(DisplayString):
    """Custom type snmprcomm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Snmprcomm_Type.__name__ = "DisplayString"
_Snmprcomm_Object = MibScalar
snmprcomm = _Snmprcomm_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 5),
    _Snmprcomm_Type()
)
snmprcomm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmprcomm.setStatus("current")


class _Snmpwcomm_Type(DisplayString):
    """Custom type snmpwcomm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Snmpwcomm_Type.__name__ = "DisplayString"
_Snmpwcomm_Object = MibScalar
snmpwcomm = _Snmpwcomm_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 6),
    _Snmpwcomm_Type()
)
snmpwcomm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpwcomm.setStatus("current")


class _Snmptout_Type(Integer32):
    """Custom type snmptout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_Snmptout_Type.__name__ = "Integer32"
_Snmptout_Object = MibScalar
snmptout = _Snmptout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 3, 7),
    _Snmptout_Type()
)
snmptout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmptout.setStatus("current")
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 4)
)


class _Appport_Type(Integer32):
    """Custom type appport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Appport_Type.__name__ = "Integer32"
_Appport_Object = MibScalar
appport = _Appport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 4, 1),
    _Appport_Type()
)
appport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appport.setStatus("current")


class _Apptout_Type(Integer32):
    """Custom type apptout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_Apptout_Type.__name__ = "Integer32"
_Apptout_Object = MibScalar
apptout = _Apptout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 4, 2),
    _Apptout_Type()
)
apptout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apptout.setStatus("current")
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 5)
)


class _Httpport_Type(Integer32):
    """Custom type httpport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Httpport_Type.__name__ = "Integer32"
_Httpport_Object = MibScalar
httpport = _Httpport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 5, 1),
    _Httpport_Type()
)
httpport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpport.setStatus("current")


class _Httptout_Type(Integer32):
    """Custom type httptout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Httptout_Type.__name__ = "Integer32"
_Httptout_Object = MibScalar
httptout = _Httptout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 5, 2),
    _Httptout_Type()
)
httptout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httptout.setStatus("current")
_Ftp_ObjectIdentity = ObjectIdentity
ftp = _Ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 6)
)


class _Ftpdport_Type(Integer32):
    """Custom type ftpdport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ftpdport_Type.__name__ = "Integer32"
_Ftpdport_Object = MibScalar
ftpdport = _Ftpdport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 6, 1),
    _Ftpdport_Type()
)
ftpdport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpdport.setStatus("current")


class _Ftpcport_Type(Integer32):
    """Custom type ftpcport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ftpcport_Type.__name__ = "Integer32"
_Ftpcport_Object = MibScalar
ftpcport = _Ftpcport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 6, 2),
    _Ftpcport_Type()
)
ftpcport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpcport.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 7)
)


class _Sntpsrv_Type(DisplayString):
    """Custom type sntpsrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Sntpsrv_Type.__name__ = "DisplayString"
_Sntpsrv_Object = MibScalar
sntpsrv = _Sntpsrv_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 7, 1),
    _Sntpsrv_Type()
)
sntpsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpsrv.setStatus("current")


class _Sntpport_Type(Integer32):
    """Custom type sntpport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sntpport_Type.__name__ = "Integer32"
_Sntpport_Object = MibScalar
sntpport = _Sntpport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 7, 2),
    _Sntpport_Type()
)
sntpport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpport.setStatus("current")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8)
)


class _Smtpsrv_Type(DisplayString):
    """Custom type smtpsrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Smtpsrv_Type.__name__ = "DisplayString"
_Smtpsrv_Object = MibScalar
smtpsrv = _Smtpsrv_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 1),
    _Smtpsrv_Type()
)
smtpsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpsrv.setStatus("current")


class _Smtpport_Type(Integer32):
    """Custom type smtpport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Smtpport_Type.__name__ = "Integer32"
_Smtpport_Object = MibScalar
smtpport = _Smtpport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 2),
    _Smtpport_Type()
)
smtpport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpport.setStatus("current")


class _Email1_Type(DisplayString):
    """Custom type email1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Email1_Type.__name__ = "DisplayString"
_Email1_Object = MibScalar
email1 = _Email1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 3),
    _Email1_Type()
)
email1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    email1.setStatus("current")


class _Email2_Type(DisplayString):
    """Custom type email2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Email2_Type.__name__ = "DisplayString"
_Email2_Object = MibScalar
email2 = _Email2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 4),
    _Email2_Type()
)
email2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    email2.setStatus("current")


class _Smtpsender_Type(DisplayString):
    """Custom type smtpsender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Smtpsender_Type.__name__ = "DisplayString"
_Smtpsender_Object = MibScalar
smtpsender = _Smtpsender_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 5),
    _Smtpsender_Type()
)
smtpsender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpsender.setStatus("current")


class _Smtpuname_Type(DisplayString):
    """Custom type smtpuname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Smtpuname_Type.__name__ = "DisplayString"
_Smtpuname_Object = MibScalar
smtpuname = _Smtpuname_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 6),
    _Smtpuname_Type()
)
smtpuname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpuname.setStatus("current")


class _Smtpupass_Type(DisplayString):
    """Custom type smtpupass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Smtpupass_Type.__name__ = "DisplayString"
_Smtpupass_Object = MibScalar
smtpupass = _Smtpupass_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 7),
    _Smtpupass_Type()
)
smtpupass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpupass.setStatus("current")


class _Smtphostname_Type(DisplayString):
    """Custom type smtphostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Smtphostname_Type.__name__ = "DisplayString"
_Smtphostname_Object = MibScalar
smtphostname = _Smtphostname_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 8),
    _Smtphostname_Type()
)
smtphostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtphostname.setStatus("current")


class _Smtpconntype_Type(Integer32):
    """Custom type smtpconntype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("smtpconnRegular", 0),
          ("smtpconnEncrypted", 1))
    )


_Smtpconntype_Type.__name__ = "Integer32"
_Smtpconntype_Object = MibScalar
smtpconntype = _Smtpconntype_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 8, 9),
    _Smtpconntype_Type()
)
smtpconntype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpconntype.setStatus("current")
_Streamer_ObjectIdentity = ObjectIdentity
streamer = _Streamer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 9)
)


class _Strmport_Type(Integer32):
    """Custom type strmport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Strmport_Type.__name__ = "Integer32"
_Strmport_Object = MibScalar
strmport = _Strmport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 9, 1),
    _Strmport_Type()
)
strmport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strmport.setStatus("current")


class _Strmbps_Type(Integer32):
    """Custom type strmbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 256),
    )


_Strmbps_Type.__name__ = "Integer32"
_Strmbps_Object = MibScalar
strmbps = _Strmbps_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 9, 2),
    _Strmbps_Type()
)
strmbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strmbps.setStatus("current")
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 10)
)


class _Slogsrv_Type(DisplayString):
    """Custom type slogsrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Slogsrv_Type.__name__ = "DisplayString"
_Slogsrv_Object = MibScalar
slogsrv = _Slogsrv_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 10, 1),
    _Slogsrv_Type()
)
slogsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slogsrv.setStatus("current")


class _Slogport_Type(Integer32):
    """Custom type slogport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Slogport_Type.__name__ = "Integer32"
_Slogport_Object = MibScalar
slogport = _Slogport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 10, 2),
    _Slogport_Type()
)
slogport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slogport.setStatus("current")
_UecpTpcServer_ObjectIdentity = ObjectIdentity
uecpTpcServer = _UecpTpcServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 11)
)


class _Uecpsrvport_Type(Integer32):
    """Custom type uecpsrvport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Uecpsrvport_Type.__name__ = "Integer32"
_Uecpsrvport_Object = MibScalar
uecpsrvport = _Uecpsrvport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 11, 1),
    _Uecpsrvport_Type()
)
uecpsrvport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uecpsrvport.setStatus("current")
_UecpUdpRelay_ObjectIdentity = ObjectIdentity
uecpUdpRelay = _UecpUdpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 12)
)


class _Uecprelsrv_Type(DisplayString):
    """Custom type uecprelsrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Uecprelsrv_Type.__name__ = "DisplayString"
_Uecprelsrv_Object = MibScalar
uecprelsrv = _Uecprelsrv_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 12, 1),
    _Uecprelsrv_Type()
)
uecprelsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uecprelsrv.setStatus("current")


class _Uecprelport_Type(Integer32):
    """Custom type uecprelport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Uecprelport_Type.__name__ = "Integer32"
_Uecprelport_Object = MibScalar
uecprelport = _Uecprelport_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 12, 2),
    _Uecprelport_Type()
)
uecprelport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uecprelport.setStatus("current")
_GsmModem_ObjectIdentity = ObjectIdentity
gsmModem = _GsmModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13)
)


class _Mdmtype_Type(Integer32):
    """Custom type mdmtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("mdmGeneric", 0)
    )


_Mdmtype_Type.__name__ = "Integer32"
_Mdmtype_Object = MibScalar
mdmtype = _Mdmtype_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 1),
    _Mdmtype_Type()
)
mdmtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmtype.setStatus("current")


class _Mdmbrate_Type(Integer32):
    """Custom type mdmbrate based on Integer32"""
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
        *(("gsmbrate4800bps", 0),
          ("gsmbrate9600bps", 1),
          ("gsmbrate19200bps", 2),
          ("gsmbrate38400bps", 3),
          ("gsmbrate57600bps", 4))
    )


_Mdmbrate_Type.__name__ = "Integer32"
_Mdmbrate_Object = MibScalar
mdmbrate = _Mdmbrate_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 2),
    _Mdmbrate_Type()
)
mdmbrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmbrate.setStatus("current")


class _Mdmnum1_Type(DisplayString):
    """Custom type mdmnum1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Mdmnum1_Type.__name__ = "DisplayString"
_Mdmnum1_Object = MibScalar
mdmnum1 = _Mdmnum1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 3),
    _Mdmnum1_Type()
)
mdmnum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmnum1.setStatus("current")


class _Mdmnum2_Type(DisplayString):
    """Custom type mdmnum2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Mdmnum2_Type.__name__ = "DisplayString"
_Mdmnum2_Object = MibScalar
mdmnum2 = _Mdmnum2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 4),
    _Mdmnum2_Type()
)
mdmnum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmnum2.setStatus("current")


class _Mdmnum3_Type(DisplayString):
    """Custom type mdmnum3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Mdmnum3_Type.__name__ = "DisplayString"
_Mdmnum3_Object = MibScalar
mdmnum3 = _Mdmnum3_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 5),
    _Mdmnum3_Type()
)
mdmnum3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmnum3.setStatus("current")


class _Mdmnum4_Type(DisplayString):
    """Custom type mdmnum4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Mdmnum4_Type.__name__ = "DisplayString"
_Mdmnum4_Object = MibScalar
mdmnum4 = _Mdmnum4_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 6),
    _Mdmnum4_Type()
)
mdmnum4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmnum4.setStatus("current")


class _Mdmnum5_Type(DisplayString):
    """Custom type mdmnum5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Mdmnum5_Type.__name__ = "DisplayString"
_Mdmnum5_Object = MibScalar
mdmnum5 = _Mdmnum5_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 4, 13, 7),
    _Mdmnum5_Type()
)
mdmnum5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmnum5.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5)
)
_Panel_ObjectIdentity = ObjectIdentity
panel = _Panel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 1)
)


class _Locken_Type(Integer32):
    """Custom type locken based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Locken_Type.__name__ = "Integer32"
_Locken_Object = MibScalar
locken = _Locken_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 1, 1),
    _Locken_Type()
)
locken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locken.setStatus("current")


class _Lockcode_Type(Integer32):
    """Custom type lockcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Lockcode_Type.__name__ = "Integer32"
_Lockcode_Object = MibScalar
lockcode = _Lockcode_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 1, 2),
    _Lockcode_Type()
)
lockcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lockcode.setStatus("current")


class _Locktout_Type(Integer32):
    """Custom type locktout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Locktout_Type.__name__ = "Integer32"
_Locktout_Object = MibScalar
locktout = _Locktout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 1, 3),
    _Locktout_Type()
)
locktout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locktout.setStatus("current")
_RemoteAccess_ObjectIdentity = ObjectIdentity
remoteAccess = _RemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 2)
)


class _Accaname_Type(DisplayString):
    """Custom type accaname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Accaname_Type.__name__ = "DisplayString"
_Accaname_Object = MibScalar
accaname = _Accaname_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 2, 1),
    _Accaname_Type()
)
accaname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accaname.setStatus("current")


class _Accapass_Type(DisplayString):
    """Custom type accapass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Accapass_Type.__name__ = "DisplayString"
_Accapass_Object = MibScalar
accapass = _Accapass_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 2, 2),
    _Accapass_Type()
)
accapass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accapass.setStatus("current")


class _Accuname_Type(DisplayString):
    """Custom type accuname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Accuname_Type.__name__ = "DisplayString"
_Accuname_Object = MibScalar
accuname = _Accuname_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 2, 3),
    _Accuname_Type()
)
accuname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accuname.setStatus("current")


class _Accupass_Type(DisplayString):
    """Custom type accupass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Accupass_Type.__name__ = "DisplayString"
_Accupass_Object = MibScalar
accupass = _Accupass_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 5, 2, 4),
    _Accupass_Type()
)
accupass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accupass.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6)
)
_AlarmEvents_ObjectIdentity = ObjectIdentity
alarmEvents = _AlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 1)
)


class _Alsmtpen_Type(Integer32):
    """Custom type alsmtpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alsmtpen_Type.__name__ = "Integer32"
_Alsmtpen_Object = MibScalar
alsmtpen = _Alsmtpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 1, 1),
    _Alsmtpen_Type()
)
alsmtpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alsmtpen.setStatus("current")


class _Alsmsen_Type(Integer32):
    """Custom type alsmsen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alsmsen_Type.__name__ = "Integer32"
_Alsmsen_Object = MibScalar
alsmsen = _Alsmsen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 1, 2),
    _Alsmsen_Type()
)
alsmsen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alsmsen.setStatus("current")


class _Alsnmpen_Type(Integer32):
    """Custom type alsnmpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alsnmpen_Type.__name__ = "Integer32"
_Alsnmpen_Object = MibScalar
alsnmpen = _Alsnmpen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 1, 3),
    _Alsnmpen_Type()
)
alsnmpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alsnmpen.setStatus("current")


class _Algpoen_Type(Integer32):
    """Custom type algpoen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Algpoen_Type.__name__ = "Integer32"
_Algpoen_Object = MibScalar
algpoen = _Algpoen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 1, 4),
    _Algpoen_Type()
)
algpoen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    algpoen.setStatus("current")


class _AlarmRfMin_Type(Fr8p8):
    """Custom type alarmRfMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5120, 28160),
    )


_AlarmRfMin_Type.__name__ = "Fr8p8"
_AlarmRfMin_Object = MibScalar
alarmRfMin = _AlarmRfMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 3),
    _AlarmRfMin_Type()
)
alarmRfMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRfMin.setStatus("current")


class _AlarmRfMax_Type(Fr8p8):
    """Custom type alarmRfMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5120, 28160),
    )


_AlarmRfMax_Type.__name__ = "Fr8p8"
_AlarmRfMax_Object = MibScalar
alarmRfMax = _AlarmRfMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 4),
    _AlarmRfMax_Type()
)
alarmRfMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRfMax.setStatus("current")


class _AlarmRfTrigger_Type(Integer32):
    """Custom type alarmRfTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmRfTrigger_Type.__name__ = "Integer32"
_AlarmRfTrigger_Object = MibScalar
alarmRfTrigger = _AlarmRfTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 5),
    _AlarmRfTrigger_Type()
)
alarmRfTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRfTrigger.setStatus("current")


class _AlarmRfRelease_Type(Integer32):
    """Custom type alarmRfRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmRfRelease_Type.__name__ = "Integer32"
_AlarmRfRelease_Object = MibScalar
alarmRfRelease = _AlarmRfRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 6),
    _AlarmRfRelease_Type()
)
alarmRfRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRfRelease.setStatus("current")


class _AlarmRfEvents_Type(Integer32):
    """Custom type alarmRfEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmRfEvents_Type.__name__ = "Integer32"
_AlarmRfEvents_Object = MibScalar
alarmRfEvents = _AlarmRfEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 7),
    _AlarmRfEvents_Type()
)
alarmRfEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRfEvents.setStatus("current")


class _AlarmMpxMin_Type(Fr8p8):
    """Custom type alarmMpxMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AlarmMpxMin_Type.__name__ = "Fr8p8"
_AlarmMpxMin_Object = MibScalar
alarmMpxMin = _AlarmMpxMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 8),
    _AlarmMpxMin_Type()
)
alarmMpxMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMpxMin.setStatus("current")


class _AlarmMpxMax_Type(Fr8p8):
    """Custom type alarmMpxMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AlarmMpxMax_Type.__name__ = "Fr8p8"
_AlarmMpxMax_Object = MibScalar
alarmMpxMax = _AlarmMpxMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 9),
    _AlarmMpxMax_Type()
)
alarmMpxMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMpxMax.setStatus("current")


class _AlarmMpxTrigger_Type(Integer32):
    """Custom type alarmMpxTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmMpxTrigger_Type.__name__ = "Integer32"
_AlarmMpxTrigger_Object = MibScalar
alarmMpxTrigger = _AlarmMpxTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 10),
    _AlarmMpxTrigger_Type()
)
alarmMpxTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMpxTrigger.setStatus("current")


class _AlarmMpxRelease_Type(Integer32):
    """Custom type alarmMpxRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmMpxRelease_Type.__name__ = "Integer32"
_AlarmMpxRelease_Object = MibScalar
alarmMpxRelease = _AlarmMpxRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 11),
    _AlarmMpxRelease_Type()
)
alarmMpxRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMpxRelease.setStatus("current")


class _AlarmMpxEvents_Type(Integer32):
    """Custom type alarmMpxEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmMpxEvents_Type.__name__ = "Integer32"
_AlarmMpxEvents_Object = MibScalar
alarmMpxEvents = _AlarmMpxEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 12),
    _AlarmMpxEvents_Type()
)
alarmMpxEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMpxEvents.setStatus("current")


class _AlarmPilotMin_Type(Fr8p8):
    """Custom type alarmPilotMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_AlarmPilotMin_Type.__name__ = "Fr8p8"
_AlarmPilotMin_Object = MibScalar
alarmPilotMin = _AlarmPilotMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 13),
    _AlarmPilotMin_Type()
)
alarmPilotMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPilotMin.setStatus("current")


class _AlarmPilotMax_Type(Fr8p8):
    """Custom type alarmPilotMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_AlarmPilotMax_Type.__name__ = "Fr8p8"
_AlarmPilotMax_Object = MibScalar
alarmPilotMax = _AlarmPilotMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 14),
    _AlarmPilotMax_Type()
)
alarmPilotMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPilotMax.setStatus("current")


class _AlarmPilotTrigger_Type(Integer32):
    """Custom type alarmPilotTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmPilotTrigger_Type.__name__ = "Integer32"
_AlarmPilotTrigger_Object = MibScalar
alarmPilotTrigger = _AlarmPilotTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 15),
    _AlarmPilotTrigger_Type()
)
alarmPilotTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPilotTrigger.setStatus("current")


class _AlarmPilotRelease_Type(Integer32):
    """Custom type alarmPilotRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmPilotRelease_Type.__name__ = "Integer32"
_AlarmPilotRelease_Object = MibScalar
alarmPilotRelease = _AlarmPilotRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 16),
    _AlarmPilotRelease_Type()
)
alarmPilotRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPilotRelease.setStatus("current")


class _AlarmPilotEvents_Type(Integer32):
    """Custom type alarmPilotEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmPilotEvents_Type.__name__ = "Integer32"
_AlarmPilotEvents_Object = MibScalar
alarmPilotEvents = _AlarmPilotEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 17),
    _AlarmPilotEvents_Type()
)
alarmPilotEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPilotEvents.setStatus("current")


class _AlarmRdsMin_Type(Fr8p8):
    """Custom type alarmRdsMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_AlarmRdsMin_Type.__name__ = "Fr8p8"
_AlarmRdsMin_Object = MibScalar
alarmRdsMin = _AlarmRdsMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 18),
    _AlarmRdsMin_Type()
)
alarmRdsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRdsMin.setStatus("current")


class _AlarmRdsMax_Type(Fr8p8):
    """Custom type alarmRdsMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_AlarmRdsMax_Type.__name__ = "Fr8p8"
_AlarmRdsMax_Object = MibScalar
alarmRdsMax = _AlarmRdsMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 19),
    _AlarmRdsMax_Type()
)
alarmRdsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRdsMax.setStatus("current")


class _AlarmRdsTrigger_Type(Integer32):
    """Custom type alarmRdsTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmRdsTrigger_Type.__name__ = "Integer32"
_AlarmRdsTrigger_Object = MibScalar
alarmRdsTrigger = _AlarmRdsTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 20),
    _AlarmRdsTrigger_Type()
)
alarmRdsTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRdsTrigger.setStatus("current")


class _AlarmRdsRelease_Type(Integer32):
    """Custom type alarmRdsRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmRdsRelease_Type.__name__ = "Integer32"
_AlarmRdsRelease_Object = MibScalar
alarmRdsRelease = _AlarmRdsRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 21),
    _AlarmRdsRelease_Type()
)
alarmRdsRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRdsRelease.setStatus("current")


class _AlarmRdsEvents_Type(Integer32):
    """Custom type alarmRdsEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmRdsEvents_Type.__name__ = "Integer32"
_AlarmRdsEvents_Object = MibScalar
alarmRdsEvents = _AlarmRdsEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 22),
    _AlarmRdsEvents_Type()
)
alarmRdsEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRdsEvents.setStatus("current")


class _AlarmLeftMin_Type(Fr8p8):
    """Custom type alarmLeftMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12800, 1280),
    )


_AlarmLeftMin_Type.__name__ = "Fr8p8"
_AlarmLeftMin_Object = MibScalar
alarmLeftMin = _AlarmLeftMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 23),
    _AlarmLeftMin_Type()
)
alarmLeftMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLeftMin.setStatus("current")


class _AlarmLeftMax_Type(Fr8p8):
    """Custom type alarmLeftMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12800, 1280),
    )


_AlarmLeftMax_Type.__name__ = "Fr8p8"
_AlarmLeftMax_Object = MibScalar
alarmLeftMax = _AlarmLeftMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 24),
    _AlarmLeftMax_Type()
)
alarmLeftMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLeftMax.setStatus("current")


class _AlarmLeftTrigger_Type(Integer32):
    """Custom type alarmLeftTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmLeftTrigger_Type.__name__ = "Integer32"
_AlarmLeftTrigger_Object = MibScalar
alarmLeftTrigger = _AlarmLeftTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 25),
    _AlarmLeftTrigger_Type()
)
alarmLeftTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLeftTrigger.setStatus("current")


class _AlarmLeftRelease_Type(Integer32):
    """Custom type alarmLeftRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmLeftRelease_Type.__name__ = "Integer32"
_AlarmLeftRelease_Object = MibScalar
alarmLeftRelease = _AlarmLeftRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 26),
    _AlarmLeftRelease_Type()
)
alarmLeftRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLeftRelease.setStatus("current")


class _AlarmLeftEvents_Type(Integer32):
    """Custom type alarmLeftEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmLeftEvents_Type.__name__ = "Integer32"
_AlarmLeftEvents_Object = MibScalar
alarmLeftEvents = _AlarmLeftEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 27),
    _AlarmLeftEvents_Type()
)
alarmLeftEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLeftEvents.setStatus("current")


class _AlarmRightMin_Type(Fr8p8):
    """Custom type alarmRightMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12800, 1280),
    )


_AlarmRightMin_Type.__name__ = "Fr8p8"
_AlarmRightMin_Object = MibScalar
alarmRightMin = _AlarmRightMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 28),
    _AlarmRightMin_Type()
)
alarmRightMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRightMin.setStatus("current")


class _AlarmRightMax_Type(Fr8p8):
    """Custom type alarmRightMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12800, 1280),
    )


_AlarmRightMax_Type.__name__ = "Fr8p8"
_AlarmRightMax_Object = MibScalar
alarmRightMax = _AlarmRightMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 29),
    _AlarmRightMax_Type()
)
alarmRightMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRightMax.setStatus("current")


class _AlarmRightTrigger_Type(Integer32):
    """Custom type alarmRightTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmRightTrigger_Type.__name__ = "Integer32"
_AlarmRightTrigger_Object = MibScalar
alarmRightTrigger = _AlarmRightTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 30),
    _AlarmRightTrigger_Type()
)
alarmRightTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRightTrigger.setStatus("current")


class _AlarmRightRelease_Type(Integer32):
    """Custom type alarmRightRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmRightRelease_Type.__name__ = "Integer32"
_AlarmRightRelease_Object = MibScalar
alarmRightRelease = _AlarmRightRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 31),
    _AlarmRightRelease_Type()
)
alarmRightRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRightRelease.setStatus("current")


class _AlarmRightEvents_Type(Integer32):
    """Custom type alarmRightEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmRightEvents_Type.__name__ = "Integer32"
_AlarmRightEvents_Object = MibScalar
alarmRightEvents = _AlarmRightEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 32),
    _AlarmRightEvents_Type()
)
alarmRightEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRightEvents.setStatus("current")


class _AlarmTempMin_Type(Fr8p8):
    """Custom type alarmTempMin based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_AlarmTempMin_Type.__name__ = "Fr8p8"
_AlarmTempMin_Object = MibScalar
alarmTempMin = _AlarmTempMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 33),
    _AlarmTempMin_Type()
)
alarmTempMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTempMin.setStatus("current")


class _AlarmTempMax_Type(Fr8p8):
    """Custom type alarmTempMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_AlarmTempMax_Type.__name__ = "Fr8p8"
_AlarmTempMax_Object = MibScalar
alarmTempMax = _AlarmTempMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 34),
    _AlarmTempMax_Type()
)
alarmTempMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTempMax.setStatus("current")


class _AlarmTempTrigger_Type(Integer32):
    """Custom type alarmTempTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmTempTrigger_Type.__name__ = "Integer32"
_AlarmTempTrigger_Object = MibScalar
alarmTempTrigger = _AlarmTempTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 35),
    _AlarmTempTrigger_Type()
)
alarmTempTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTempTrigger.setStatus("current")


class _AlarmTempRelease_Type(Integer32):
    """Custom type alarmTempRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmTempRelease_Type.__name__ = "Integer32"
_AlarmTempRelease_Object = MibScalar
alarmTempRelease = _AlarmTempRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 36),
    _AlarmTempRelease_Type()
)
alarmTempRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTempRelease.setStatus("current")


class _AlarmTempEvents_Type(Integer32):
    """Custom type alarmTempEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmTempEvents_Type.__name__ = "Integer32"
_AlarmTempEvents_Object = MibScalar
alarmTempEvents = _AlarmTempEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 37),
    _AlarmTempEvents_Type()
)
alarmTempEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTempEvents.setStatus("current")


class _AlarmFanMin_Type(Integer32):
    """Custom type alarmFanMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_AlarmFanMin_Type.__name__ = "Integer32"
_AlarmFanMin_Object = MibScalar
alarmFanMin = _AlarmFanMin_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 38),
    _AlarmFanMin_Type()
)
alarmFanMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFanMin.setStatus("current")


class _AlarmFanMax_Type(Integer32):
    """Custom type alarmFanMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_AlarmFanMax_Type.__name__ = "Integer32"
_AlarmFanMax_Object = MibScalar
alarmFanMax = _AlarmFanMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 39),
    _AlarmFanMax_Type()
)
alarmFanMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFanMax.setStatus("current")


class _AlarmFanTrigger_Type(Integer32):
    """Custom type alarmFanTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmFanTrigger_Type.__name__ = "Integer32"
_AlarmFanTrigger_Object = MibScalar
alarmFanTrigger = _AlarmFanTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 40),
    _AlarmFanTrigger_Type()
)
alarmFanTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFanTrigger.setStatus("current")


class _AlarmFanRelease_Type(Integer32):
    """Custom type alarmFanRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AlarmFanRelease_Type.__name__ = "Integer32"
_AlarmFanRelease_Object = MibScalar
alarmFanRelease = _AlarmFanRelease_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 41),
    _AlarmFanRelease_Type()
)
alarmFanRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFanRelease.setStatus("current")


class _AlarmFanEvents_Type(Integer32):
    """Custom type alarmFanEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmFanEvents_Type.__name__ = "Integer32"
_AlarmFanEvents_Object = MibScalar
alarmFanEvents = _AlarmFanEvents_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 6, 42),
    _AlarmFanEvents_Type()
)
alarmFanEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFanEvents.setStatus("current")
_ActiveAlarmAction_ObjectIdentity = ObjectIdentity
activeAlarmAction = _ActiveAlarmAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7)
)
_RfAlarm_ObjectIdentity = ObjectIdentity
rfAlarm = _RfAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 1)
)


class _Alrmrfaudmute_Type(Integer32):
    """Custom type alrmrfaudmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmrfaudmute_Type.__name__ = "Integer32"
_Alrmrfaudmute_Object = MibScalar
alrmrfaudmute = _Alrmrfaudmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 1, 1),
    _Alrmrfaudmute_Type()
)
alrmrfaudmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmrfaudmute.setStatus("current")


class _Alrmrfmpxmute_Type(Integer32):
    """Custom type alrmrfmpxmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmrfmpxmute_Type.__name__ = "Integer32"
_Alrmrfmpxmute_Object = MibScalar
alrmrfmpxmute = _Alrmrfmpxmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 1, 2),
    _Alrmrfmpxmute_Type()
)
alrmrfmpxmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmrfmpxmute.setStatus("current")


class _Alrmrfswitch_Type(Integer32):
    """Custom type alrmrfswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmrfswitch_Type.__name__ = "Integer32"
_Alrmrfswitch_Object = MibScalar
alrmrfswitch = _Alrmrfswitch_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 1, 3),
    _Alrmrfswitch_Type()
)
alrmrfswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmrfswitch.setStatus("current")
_MpxAlarm_ObjectIdentity = ObjectIdentity
mpxAlarm = _MpxAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 2)
)


class _Alrmmpxaudmute_Type(Integer32):
    """Custom type alrmmpxaudmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmmpxaudmute_Type.__name__ = "Integer32"
_Alrmmpxaudmute_Object = MibScalar
alrmmpxaudmute = _Alrmmpxaudmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 2, 1),
    _Alrmmpxaudmute_Type()
)
alrmmpxaudmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmmpxaudmute.setStatus("current")


class _Alrmmpxmpxmute_Type(Integer32):
    """Custom type alrmmpxmpxmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmmpxmpxmute_Type.__name__ = "Integer32"
_Alrmmpxmpxmute_Object = MibScalar
alrmmpxmpxmute = _Alrmmpxmpxmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 2, 2),
    _Alrmmpxmpxmute_Type()
)
alrmmpxmpxmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmmpxmpxmute.setStatus("current")


class _Alrmmpxswitch_Type(Integer32):
    """Custom type alrmmpxswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmmpxswitch_Type.__name__ = "Integer32"
_Alrmmpxswitch_Object = MibScalar
alrmmpxswitch = _Alrmmpxswitch_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 2, 3),
    _Alrmmpxswitch_Type()
)
alrmmpxswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmmpxswitch.setStatus("current")
_AudioAlarm_ObjectIdentity = ObjectIdentity
audioAlarm = _AudioAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 3)
)


class _Alrmaudaudmute_Type(Integer32):
    """Custom type alrmaudaudmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmaudaudmute_Type.__name__ = "Integer32"
_Alrmaudaudmute_Object = MibScalar
alrmaudaudmute = _Alrmaudaudmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 3, 1),
    _Alrmaudaudmute_Type()
)
alrmaudaudmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmaudaudmute.setStatus("current")


class _Alrmaudmpxmute_Type(Integer32):
    """Custom type alrmaudmpxmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmaudmpxmute_Type.__name__ = "Integer32"
_Alrmaudmpxmute_Object = MibScalar
alrmaudmpxmute = _Alrmaudmpxmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 3, 2),
    _Alrmaudmpxmute_Type()
)
alrmaudmpxmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmaudmpxmute.setStatus("current")


class _Alrmaudswitch_Type(Integer32):
    """Custom type alrmaudswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmaudswitch_Type.__name__ = "Integer32"
_Alrmaudswitch_Object = MibScalar
alrmaudswitch = _Alrmaudswitch_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 3, 3),
    _Alrmaudswitch_Type()
)
alrmaudswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmaudswitch.setStatus("current")
_PilotAlarm_ObjectIdentity = ObjectIdentity
pilotAlarm = _PilotAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 4)
)


class _Alrmpltaudmute_Type(Integer32):
    """Custom type alrmpltaudmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmpltaudmute_Type.__name__ = "Integer32"
_Alrmpltaudmute_Object = MibScalar
alrmpltaudmute = _Alrmpltaudmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 4, 1),
    _Alrmpltaudmute_Type()
)
alrmpltaudmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmpltaudmute.setStatus("current")


class _Alrmpltmpxmute_Type(Integer32):
    """Custom type alrmpltmpxmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmpltmpxmute_Type.__name__ = "Integer32"
_Alrmpltmpxmute_Object = MibScalar
alrmpltmpxmute = _Alrmpltmpxmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 4, 2),
    _Alrmpltmpxmute_Type()
)
alrmpltmpxmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmpltmpxmute.setStatus("current")


class _Alrmpltswitch_Type(Integer32):
    """Custom type alrmpltswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmpltswitch_Type.__name__ = "Integer32"
_Alrmpltswitch_Object = MibScalar
alrmpltswitch = _Alrmpltswitch_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 4, 3),
    _Alrmpltswitch_Type()
)
alrmpltswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmpltswitch.setStatus("current")
_PiProtection_ObjectIdentity = ObjectIdentity
piProtection = _PiProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 5)
)


class _Alrmpiaudmute_Type(Integer32):
    """Custom type alrmpiaudmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmpiaudmute_Type.__name__ = "Integer32"
_Alrmpiaudmute_Object = MibScalar
alrmpiaudmute = _Alrmpiaudmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 5, 1),
    _Alrmpiaudmute_Type()
)
alrmpiaudmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmpiaudmute.setStatus("current")


class _Alrmpimpxmute_Type(Integer32):
    """Custom type alrmpimpxmute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmpimpxmute_Type.__name__ = "Integer32"
_Alrmpimpxmute_Object = MibScalar
alrmpimpxmute = _Alrmpimpxmute_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 5, 2),
    _Alrmpimpxmute_Type()
)
alrmpimpxmute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmpimpxmute.setStatus("current")


class _Alrmpiswitch_Type(Integer32):
    """Custom type alrmpiswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Alrmpiswitch_Type.__name__ = "Integer32"
_Alrmpiswitch_Object = MibScalar
alrmpiswitch = _Alrmpiswitch_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 7, 5, 3),
    _Alrmpiswitch_Type()
)
alrmpiswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrmpiswitch.setStatus("current")
_GpOutputs_ObjectIdentity = ObjectIdentity
gpOutputs = _GpOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8)
)


class _Gpofunc1_Type(Integer32):
    """Custom type gpofunc1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc1_Type.__name__ = "Integer32"
_Gpofunc1_Object = MibScalar
gpofunc1 = _Gpofunc1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 1),
    _Gpofunc1_Type()
)
gpofunc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc1.setStatus("current")


class _Gpotype1_Type(Integer32):
    """Custom type gpotype1 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype1_Type.__name__ = "Integer32"
_Gpotype1_Object = MibScalar
gpotype1 = _Gpotype1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 2),
    _Gpotype1_Type()
)
gpotype1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype1.setStatus("current")


class _Gpotout1_Type(Integer32):
    """Custom type gpotout1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout1_Type.__name__ = "Integer32"
_Gpotout1_Object = MibScalar
gpotout1 = _Gpotout1_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 3),
    _Gpotout1_Type()
)
gpotout1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout1.setStatus("current")


class _Gpofunc2_Type(Integer32):
    """Custom type gpofunc2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc2_Type.__name__ = "Integer32"
_Gpofunc2_Object = MibScalar
gpofunc2 = _Gpofunc2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 4),
    _Gpofunc2_Type()
)
gpofunc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc2.setStatus("current")


class _Gpotype2_Type(Integer32):
    """Custom type gpotype2 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype2_Type.__name__ = "Integer32"
_Gpotype2_Object = MibScalar
gpotype2 = _Gpotype2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 5),
    _Gpotype2_Type()
)
gpotype2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype2.setStatus("current")


class _Gpotout2_Type(Integer32):
    """Custom type gpotout2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout2_Type.__name__ = "Integer32"
_Gpotout2_Object = MibScalar
gpotout2 = _Gpotout2_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 6),
    _Gpotout2_Type()
)
gpotout2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout2.setStatus("current")


class _Gpofunc3_Type(Integer32):
    """Custom type gpofunc3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc3_Type.__name__ = "Integer32"
_Gpofunc3_Object = MibScalar
gpofunc3 = _Gpofunc3_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 7),
    _Gpofunc3_Type()
)
gpofunc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc3.setStatus("current")


class _Gpotype3_Type(Integer32):
    """Custom type gpotype3 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype3_Type.__name__ = "Integer32"
_Gpotype3_Object = MibScalar
gpotype3 = _Gpotype3_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 8),
    _Gpotype3_Type()
)
gpotype3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype3.setStatus("current")


class _Gpotout3_Type(Integer32):
    """Custom type gpotout3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout3_Type.__name__ = "Integer32"
_Gpotout3_Object = MibScalar
gpotout3 = _Gpotout3_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 9),
    _Gpotout3_Type()
)
gpotout3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout3.setStatus("current")


class _Gpofunc4_Type(Integer32):
    """Custom type gpofunc4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc4_Type.__name__ = "Integer32"
_Gpofunc4_Object = MibScalar
gpofunc4 = _Gpofunc4_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 10),
    _Gpofunc4_Type()
)
gpofunc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc4.setStatus("current")


class _Gpotype4_Type(Integer32):
    """Custom type gpotype4 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype4_Type.__name__ = "Integer32"
_Gpotype4_Object = MibScalar
gpotype4 = _Gpotype4_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 11),
    _Gpotype4_Type()
)
gpotype4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype4.setStatus("current")


class _Gpotout4_Type(Integer32):
    """Custom type gpotout4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout4_Type.__name__ = "Integer32"
_Gpotout4_Object = MibScalar
gpotout4 = _Gpotout4_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 12),
    _Gpotout4_Type()
)
gpotout4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout4.setStatus("current")


class _Gpofunc5_Type(Integer32):
    """Custom type gpofunc5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc5_Type.__name__ = "Integer32"
_Gpofunc5_Object = MibScalar
gpofunc5 = _Gpofunc5_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 13),
    _Gpofunc5_Type()
)
gpofunc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc5.setStatus("current")


class _Gpotype5_Type(Integer32):
    """Custom type gpotype5 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype5_Type.__name__ = "Integer32"
_Gpotype5_Object = MibScalar
gpotype5 = _Gpotype5_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 14),
    _Gpotype5_Type()
)
gpotype5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype5.setStatus("current")


class _Gpotout5_Type(Integer32):
    """Custom type gpotout5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout5_Type.__name__ = "Integer32"
_Gpotout5_Object = MibScalar
gpotout5 = _Gpotout5_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 15),
    _Gpotout5_Type()
)
gpotout5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout5.setStatus("current")


class _Gpofunc6_Type(Integer32):
    """Custom type gpofunc6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc6_Type.__name__ = "Integer32"
_Gpofunc6_Object = MibScalar
gpofunc6 = _Gpofunc6_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 16),
    _Gpofunc6_Type()
)
gpofunc6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc6.setStatus("current")


class _Gpotype6_Type(Integer32):
    """Custom type gpotype6 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype6_Type.__name__ = "Integer32"
_Gpotype6_Object = MibScalar
gpotype6 = _Gpotype6_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 17),
    _Gpotype6_Type()
)
gpotype6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype6.setStatus("current")


class _Gpotout6_Type(Integer32):
    """Custom type gpotout6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout6_Type.__name__ = "Integer32"
_Gpotout6_Object = MibScalar
gpotout6 = _Gpotout6_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 18),
    _Gpotout6_Type()
)
gpotout6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout6.setStatus("current")


class _Gpofunc7_Type(Integer32):
    """Custom type gpofunc7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("gpoAlarmGPOutput", 8),
          ("gpoRDSLock", 9),
          ("gpoTAFlag", 10),
          ("gpoTPFlag", 11))
    )


_Gpofunc7_Type.__name__ = "Integer32"
_Gpofunc7_Object = MibScalar
gpofunc7 = _Gpofunc7_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 19),
    _Gpofunc7_Type()
)
gpofunc7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpofunc7.setStatus("current")


class _Gpotype7_Type(Integer32):
    """Custom type gpotype7 based on Integer32"""
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
        *(("gpoLevelHigh", 0),
          ("gpoLevelLow", 1),
          ("gpoPulseHigh", 2),
          ("gpoPulseLow", 3))
    )


_Gpotype7_Type.__name__ = "Integer32"
_Gpotype7_Object = MibScalar
gpotype7 = _Gpotype7_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 20),
    _Gpotype7_Type()
)
gpotype7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotype7.setStatus("current")


class _Gpotout7_Type(Integer32):
    """Custom type gpotout7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gpotout7_Type.__name__ = "Integer32"
_Gpotout7_Object = MibScalar
gpotout7 = _Gpotout7_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 8, 21),
    _Gpotout7_Type()
)
gpotout7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpotout7.setStatus("current")
_AudioMpxOutputs_ObjectIdentity = ObjectIdentity
audioMpxOutputs = _AudioMpxOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 9)
)


class _Volph_Type(Integer32):
    """Custom type volph based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 0),
    )


_Volph_Type.__name__ = "Integer32"
_Volph_Object = MibScalar
volph = _Volph_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 9, 1),
    _Volph_Type()
)
volph.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    volph.setStatus("current")


class _Volaudio_Type(Integer32):
    """Custom type volaudio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 60),
    )


_Volaudio_Type.__name__ = "Integer32"
_Volaudio_Object = MibScalar
volaudio = _Volaudio_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 9, 2),
    _Volaudio_Type()
)
volaudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    volaudio.setStatus("current")


class _Volmpx_Type(Integer32):
    """Custom type volmpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 120),
    )


_Volmpx_Type.__name__ = "Integer32"
_Volmpx_Object = MibScalar
volmpx = _Volmpx_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 9, 3),
    _Volmpx_Type()
)
volmpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    volmpx.setStatus("current")


class _Volgsm_Type(Integer32):
    """Custom type volgsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 0),
    )


_Volgsm_Type.__name__ = "Integer32"
_Volgsm_Object = MibScalar
volgsm = _Volgsm_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 9, 4),
    _Volgsm_Type()
)
volgsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    volgsm.setStatus("current")


class _Digout_Type(Integer32):
    """Custom type digout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("altEnable", 3),
          ("altDisable", 4))
    )


_Digout_Type.__name__ = "Integer32"
_Digout_Object = MibScalar
digout = _Digout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 9, 5),
    _Digout_Type()
)
digout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digout.setStatus("current")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10)
)


class _Alias_Type(DisplayString):
    """Custom type alias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Alias_Type.__name__ = "DisplayString"
_Alias_Object = MibScalar
alias = _Alias_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 1),
    _Alias_Type()
)
alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alias.setStatus("current")


class _Region_Type(Integer32):
    """Custom type region based on Integer32"""
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
        *(("regEurope", 0),
          ("regJapan", 1),
          ("regUSA", 2),
          ("regOIRT", 3))
    )


_Region_Type.__name__ = "Integer32"
_Region_Object = MibScalar
region = _Region_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 2),
    _Region_Type()
)
region.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    region.setStatus("current")
_DateTime_ObjectIdentity = ObjectIdentity
dateTime = _DateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 3)
)
_Date_Type = Integer32
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 3, 1),
    _Date_Type()
)
date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date.setStatus("current")


class _Time_Type(Integer32):
    """Custom type time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_Time_Type.__name__ = "Integer32"
_Time_Object = MibScalar
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 3, 2),
    _Time_Type()
)
time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time.setStatus("current")


class _Tzone_Type(Integer32):
    """Custom type tzone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_Tzone_Type.__name__ = "Integer32"
_Tzone_Object = MibScalar
tzone = _Tzone_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 3, 3),
    _Tzone_Type()
)
tzone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tzone.setStatus("current")


class _Dsten_Type(Integer32):
    """Custom type dsten based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dstNotused", 0),
          ("dstEUDSTChange", 1),
          ("dstUSADSTChange", 2))
    )


_Dsten_Type.__name__ = "Integer32"
_Dsten_Object = MibScalar
dsten = _Dsten_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 3, 4),
    _Dsten_Type()
)
dsten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsten.setStatus("current")
_FrontPanel_ObjectIdentity = ObjectIdentity
frontPanel = _FrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 4)
)


class _Dispcontr_Type(Integer32):
    """Custom type dispcontr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dispcontr_Type.__name__ = "Integer32"
_Dispcontr_Object = MibScalar
dispcontr = _Dispcontr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 4, 1),
    _Dispcontr_Type()
)
dispcontr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dispcontr.setStatus("current")


class _Ledbright_Type(Integer32):
    """Custom type ledbright based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ledbright_Type.__name__ = "Integer32"
_Ledbright_Object = MibScalar
ledbright = _Ledbright_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 4, 2),
    _Ledbright_Type()
)
ledbright.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledbright.setStatus("current")


class _Scrsaver_Type(Integer32):
    """Custom type scrsaver based on Integer32"""
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
        *(("logDisable", 0),
          ("log1min", 1),
          ("log2min", 2),
          ("log5min", 3),
          ("log10min", 4))
    )


_Scrsaver_Type.__name__ = "Integer32"
_Scrsaver_Object = MibScalar
scrsaver = _Scrsaver_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 4, 3),
    _Scrsaver_Type()
)
scrsaver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrsaver.setStatus("current")


class _Paneltout_Type(Integer32):
    """Custom type paneltout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_Paneltout_Type.__name__ = "Integer32"
_Paneltout_Object = MibScalar
paneltout = _Paneltout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 4, 4),
    _Paneltout_Type()
)
paneltout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paneltout.setStatus("current")
_Loss_ObjectIdentity = ObjectIdentity
loss = _Loss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 5)
)


class _Audiolossth_Type(Integer32):
    """Custom type audiolossth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_Audiolossth_Type.__name__ = "Integer32"
_Audiolossth_Object = MibScalar
audiolossth = _Audiolossth_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 5, 1),
    _Audiolossth_Type()
)
audiolossth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audiolossth.setStatus("current")


class _Audiolosstout_Type(Integer32):
    """Custom type audiolosstout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Audiolosstout_Type.__name__ = "Integer32"
_Audiolosstout_Object = MibScalar
audiolosstout = _Audiolosstout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 5, 2),
    _Audiolosstout_Type()
)
audiolosstout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audiolosstout.setStatus("current")


class _Mpathth_Type(Integer32):
    """Custom type mpathth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Mpathth_Type.__name__ = "Integer32"
_Mpathth_Object = MibScalar
mpathth = _Mpathth_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 5, 3),
    _Mpathth_Type()
)
mpathth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpathth.setStatus("current")


class _Mpathtout_Type(Integer32):
    """Custom type mpathtout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Mpathtout_Type.__name__ = "Integer32"
_Mpathtout_Object = MibScalar
mpathtout = _Mpathtout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 5, 4),
    _Mpathtout_Type()
)
mpathtout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpathtout.setStatus("current")


class _Rdstout_Type(Integer32):
    """Custom type rdstout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Rdstout_Type.__name__ = "Integer32"
_Rdstout_Object = MibScalar
rdstout = _Rdstout_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 5, 5),
    _Rdstout_Type()
)
rdstout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdstout.setStatus("current")


class _Homescreen_Type(Integer32):
    """Custom type homescreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Homescreen_Type.__name__ = "Integer32"
_Homescreen_Object = MibScalar
homescreen = _Homescreen_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 6),
    _Homescreen_Type()
)
homescreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    homescreen.setStatus("current")


class _Fanctrl_Type(Integer32):
    """Custom type fanctrl based on Integer32"""
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
        *(("fanAuto", 0),
          ("fan25perc", 1),
          ("fan50perc", 2),
          ("fan75perc", 3),
          ("fan100perc", 4))
    )


_Fanctrl_Type.__name__ = "Integer32"
_Fanctrl_Object = MibScalar
fanctrl = _Fanctrl_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 7),
    _Fanctrl_Type()
)
fanctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanctrl.setStatus("current")


class _Slogmage_Type(Integer32):
    """Custom type slogmage based on Integer32"""
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
        *(("slogInfinite", 0),
          ("slog5days", 1),
          ("slog10days", 2),
          ("slog15days", 3),
          ("slog20days", 4),
          ("slog25days", 5),
          ("slog30days", 6))
    )


_Slogmage_Type.__name__ = "Integer32"
_Slogmage_Object = MibScalar
slogmage = _Slogmage_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 2, 10, 8),
    _Slogmage_Type()
)
slogmage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slogmage.setStatus("current")
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3)
)


class _MntrFreq_Type(Integer32):
    """Custom type mntrFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(87100, 107900),
    )


_MntrFreq_Type.__name__ = "Integer32"
_MntrFreq_Object = MibScalar
mntrFreq = _MntrFreq_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 1),
    _MntrFreq_Type()
)
mntrFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrFreq.setStatus("current")


class _MntrRflvlValue_Type(Fr8p8):
    """Custom type mntrRflvlValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28160),
    )


_MntrRflvlValue_Type.__name__ = "Fr8p8"
_MntrRflvlValue_Object = MibScalar
mntrRflvlValue = _MntrRflvlValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 2),
    _MntrRflvlValue_Type()
)
mntrRflvlValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRflvlValue.setStatus("current")


class _MntrRflvlValueAvr_Type(Fr8p8):
    """Custom type mntrRflvlValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28160),
    )


_MntrRflvlValueAvr_Type.__name__ = "Fr8p8"
_MntrRflvlValueAvr_Object = MibScalar
mntrRflvlValueAvr = _MntrRflvlValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 3),
    _MntrRflvlValueAvr_Type()
)
mntrRflvlValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRflvlValueAvr.setStatus("current")


class _MntrRflvlPeakMax_Type(Fr8p8):
    """Custom type mntrRflvlPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28160),
    )


_MntrRflvlPeakMax_Type.__name__ = "Fr8p8"
_MntrRflvlPeakMax_Object = MibScalar
mntrRflvlPeakMax = _MntrRflvlPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 4),
    _MntrRflvlPeakMax_Type()
)
mntrRflvlPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRflvlPeakMax.setStatus("current")


class _MntrMpathValue_Type(Fr8p8):
    """Custom type mntrMpathValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
    )


_MntrMpathValue_Type.__name__ = "Fr8p8"
_MntrMpathValue_Object = MibScalar
mntrMpathValue = _MntrMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 5),
    _MntrMpathValue_Type()
)
mntrMpathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrMpathValue.setStatus("current")


class _MntrMpathValueAvr_Type(Fr8p8):
    """Custom type mntrMpathValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
    )


_MntrMpathValueAvr_Type.__name__ = "Fr8p8"
_MntrMpathValueAvr_Object = MibScalar
mntrMpathValueAvr = _MntrMpathValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 6),
    _MntrMpathValueAvr_Type()
)
mntrMpathValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrMpathValueAvr.setStatus("current")


class _MntrMpathPeakMax_Type(Fr8p8):
    """Custom type mntrMpathPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
    )


_MntrMpathPeakMax_Type.__name__ = "Fr8p8"
_MntrMpathPeakMax_Object = MibScalar
mntrMpathPeakMax = _MntrMpathPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 7),
    _MntrMpathPeakMax_Type()
)
mntrMpathPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrMpathPeakMax.setStatus("current")


class _MntrMpxtValue_Type(Fr8p8):
    """Custom type mntrMpxtValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MntrMpxtValue_Type.__name__ = "Fr8p8"
_MntrMpxtValue_Object = MibScalar
mntrMpxtValue = _MntrMpxtValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 8),
    _MntrMpxtValue_Type()
)
mntrMpxtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrMpxtValue.setStatus("current")


class _MntrMpxtValueAvr_Type(Fr8p8):
    """Custom type mntrMpxtValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MntrMpxtValueAvr_Type.__name__ = "Fr8p8"
_MntrMpxtValueAvr_Object = MibScalar
mntrMpxtValueAvr = _MntrMpxtValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 9),
    _MntrMpxtValueAvr_Type()
)
mntrMpxtValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrMpxtValueAvr.setStatus("current")


class _MntrMpxtPeakMax_Type(Fr8p8):
    """Custom type mntrMpxtPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MntrMpxtPeakMax_Type.__name__ = "Fr8p8"
_MntrMpxtPeakMax_Object = MibScalar
mntrMpxtPeakMax = _MntrMpxtPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 10),
    _MntrMpxtPeakMax_Type()
)
mntrMpxtPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrMpxtPeakMax.setStatus("current")


class _MntrPilotValue_Type(Fr8p8):
    """Custom type mntrPilotValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_MntrPilotValue_Type.__name__ = "Fr8p8"
_MntrPilotValue_Object = MibScalar
mntrPilotValue = _MntrPilotValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 14),
    _MntrPilotValue_Type()
)
mntrPilotValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrPilotValue.setStatus("current")


class _MntrPilotValueAvr_Type(Fr8p8):
    """Custom type mntrPilotValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_MntrPilotValueAvr_Type.__name__ = "Fr8p8"
_MntrPilotValueAvr_Object = MibScalar
mntrPilotValueAvr = _MntrPilotValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 15),
    _MntrPilotValueAvr_Type()
)
mntrPilotValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrPilotValueAvr.setStatus("current")


class _MntrPilotPeakMax_Type(Fr8p8):
    """Custom type mntrPilotPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_MntrPilotPeakMax_Type.__name__ = "Fr8p8"
_MntrPilotPeakMax_Object = MibScalar
mntrPilotPeakMax = _MntrPilotPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 16),
    _MntrPilotPeakMax_Type()
)
mntrPilotPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrPilotPeakMax.setStatus("current")


class _MntrRdsValue_Type(Fr8p8):
    """Custom type mntrRdsValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_MntrRdsValue_Type.__name__ = "Fr8p8"
_MntrRdsValue_Object = MibScalar
mntrRdsValue = _MntrRdsValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 17),
    _MntrRdsValue_Type()
)
mntrRdsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsValue.setStatus("current")


class _MntrRdsValueAvr_Type(Fr8p8):
    """Custom type mntrRdsValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_MntrRdsValueAvr_Type.__name__ = "Fr8p8"
_MntrRdsValueAvr_Object = MibScalar
mntrRdsValueAvr = _MntrRdsValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 18),
    _MntrRdsValueAvr_Type()
)
mntrRdsValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsValueAvr.setStatus("current")


class _MntrRdsPeakMax_Type(Fr8p8):
    """Custom type mntrRdsPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3840),
    )


_MntrRdsPeakMax_Type.__name__ = "Fr8p8"
_MntrRdsPeakMax_Object = MibScalar
mntrRdsPeakMax = _MntrRdsPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 19),
    _MntrRdsPeakMax_Type()
)
mntrRdsPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsPeakMax.setStatus("current")


class _MntrLeftValue_Type(Fr8p8):
    """Custom type mntrLeftValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15360, 1280),
    )


_MntrLeftValue_Type.__name__ = "Fr8p8"
_MntrLeftValue_Object = MibScalar
mntrLeftValue = _MntrLeftValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 20),
    _MntrLeftValue_Type()
)
mntrLeftValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrLeftValue.setStatus("current")


class _MntrLeftValueAvr_Type(Fr8p8):
    """Custom type mntrLeftValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15360, 1280),
    )


_MntrLeftValueAvr_Type.__name__ = "Fr8p8"
_MntrLeftValueAvr_Object = MibScalar
mntrLeftValueAvr = _MntrLeftValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 21),
    _MntrLeftValueAvr_Type()
)
mntrLeftValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrLeftValueAvr.setStatus("current")


class _MntrLeftPeakMax_Type(Fr8p8):
    """Custom type mntrLeftPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15360, 1280),
    )


_MntrLeftPeakMax_Type.__name__ = "Fr8p8"
_MntrLeftPeakMax_Object = MibScalar
mntrLeftPeakMax = _MntrLeftPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 22),
    _MntrLeftPeakMax_Type()
)
mntrLeftPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrLeftPeakMax.setStatus("current")


class _MntrRightValue_Type(Fr8p8):
    """Custom type mntrRightValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15360, 1280),
    )


_MntrRightValue_Type.__name__ = "Fr8p8"
_MntrRightValue_Object = MibScalar
mntrRightValue = _MntrRightValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 23),
    _MntrRightValue_Type()
)
mntrRightValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRightValue.setStatus("current")


class _MntrRightValueAvr_Type(Fr8p8):
    """Custom type mntrRightValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15360, 1280),
    )


_MntrRightValueAvr_Type.__name__ = "Fr8p8"
_MntrRightValueAvr_Object = MibScalar
mntrRightValueAvr = _MntrRightValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 24),
    _MntrRightValueAvr_Type()
)
mntrRightValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRightValueAvr.setStatus("current")


class _MntrRightPeakMax_Type(Fr8p8):
    """Custom type mntrRightPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15360, 1280),
    )


_MntrRightPeakMax_Type.__name__ = "Fr8p8"
_MntrRightPeakMax_Object = MibScalar
mntrRightPeakMax = _MntrRightPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 25),
    _MntrRightPeakMax_Type()
)
mntrRightPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRightPeakMax.setStatus("current")


class _MntrRdsgroupValue_Type(Integer32):
    """Custom type mntrRdsgroupValue based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("grp0A", 0),
          ("grp1A", 1),
          ("grp2A", 2),
          ("grp3A", 3),
          ("grp4A", 4),
          ("grp5A", 5),
          ("grp6A", 6),
          ("grp7A", 7),
          ("grp8A", 8),
          ("grp9A", 9),
          ("grp10A", 10),
          ("grp11A", 11),
          ("grp12A", 12),
          ("grp13A", 13),
          ("grp14A", 14),
          ("grp15A", 15),
          ("grp0B", 16),
          ("grp1B", 17),
          ("grp2B", 18),
          ("grp3B", 19),
          ("grp4B", 20),
          ("grp5B", 21),
          ("grp6B", 22),
          ("grp7B", 23),
          ("grp8B", 24),
          ("grp9B", 25),
          ("grp10B", 26),
          ("grp11B", 27),
          ("grp12B", 28),
          ("grp13B", 29),
          ("grp14B", 30),
          ("grp15B", 31))
    )


_MntrRdsgroupValue_Type.__name__ = "Integer32"
_MntrRdsgroupValue_Object = MibScalar
mntrRdsgroupValue = _MntrRdsgroupValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 26),
    _MntrRdsgroupValue_Type()
)
mntrRdsgroupValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsgroupValue.setStatus("current")


class _MntrRdsLock_Type(Integer32):
    """Custom type mntrRdsLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_MntrRdsLock_Type.__name__ = "Integer32"
_MntrRdsLock_Object = MibScalar
mntrRdsLock = _MntrRdsLock_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 27),
    _MntrRdsLock_Type()
)
mntrRdsLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsLock.setStatus("current")


class _MntrRdsPi_Type(DisplayString):
    """Custom type mntrRdsPi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MntrRdsPi_Type.__name__ = "DisplayString"
_MntrRdsPi_Object = MibScalar
mntrRdsPi = _MntrRdsPi_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 28),
    _MntrRdsPi_Type()
)
mntrRdsPi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsPi.setStatus("current")


class _MntrRdsPs_Type(DisplayString):
    """Custom type mntrRdsPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MntrRdsPs_Type.__name__ = "DisplayString"
_MntrRdsPs_Object = MibScalar
mntrRdsPs = _MntrRdsPs_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 29),
    _MntrRdsPs_Type()
)
mntrRdsPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsPs.setStatus("current")


class _MntrRdsRt_Type(DisplayString):
    """Custom type mntrRdsRt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_MntrRdsRt_Type.__name__ = "DisplayString"
_MntrRdsRt_Object = MibScalar
mntrRdsRt = _MntrRdsRt_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 30),
    _MntrRdsRt_Type()
)
mntrRdsRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsRt.setStatus("current")


class _MntrRdsTa_Type(Integer32):
    """Custom type mntrRdsTa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_MntrRdsTa_Type.__name__ = "Integer32"
_MntrRdsTa_Object = MibScalar
mntrRdsTa = _MntrRdsTa_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 31),
    _MntrRdsTa_Type()
)
mntrRdsTa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsTa.setStatus("current")


class _MntrRdsTp_Type(Integer32):
    """Custom type mntrRdsTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("altOff", 1),
          ("altOn", 2))
    )


_MntrRdsTp_Type.__name__ = "Integer32"
_MntrRdsTp_Object = MibScalar
mntrRdsTp = _MntrRdsTp_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 32),
    _MntrRdsTp_Type()
)
mntrRdsTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsTp.setStatus("current")


class _MntrRdsMusicspeech_Type(Integer32):
    """Custom type mntrRdsMusicspeech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("altSpeech", 10),
          ("altMusic", 11))
    )


_MntrRdsMusicspeech_Type.__name__ = "Integer32"
_MntrRdsMusicspeech_Object = MibScalar
mntrRdsMusicspeech = _MntrRdsMusicspeech_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 33),
    _MntrRdsMusicspeech_Type()
)
mntrRdsMusicspeech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsMusicspeech.setStatus("current")


class _MntrRdsPty_Type(Integer32):
    """Custom type mntrRdsPty based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("rdsptyNone", 0),
          ("rdsptyNews", 1),
          ("rdsptyCurrentAffairs", 2),
          ("rdsptyInfo", 3),
          ("rdsptySport", 4),
          ("rdsptyEducation", 5),
          ("rdsptyDrama", 6),
          ("rdsptyCultures", 7),
          ("rdsptyScience", 8),
          ("rdsptyVariedSpeech", 9),
          ("rdsptyPopMusic", 10),
          ("rdsptyRockMusic", 11),
          ("rdsptyEasyListening", 12),
          ("rdsptyLightClassicsM", 13),
          ("rdsptySeriousClassics", 14),
          ("rdsptyOtherMusic", 15),
          ("rdsptyWeather", 16),
          ("rdsptyFinance", 17),
          ("rdsptyChildrensProgs", 18),
          ("rdsptySocialAffairs", 19),
          ("rdsptyReligion", 20),
          ("rdsptyPhoneIn", 21),
          ("rdsptyTravelTouring", 22),
          ("rdsptyLeisureHobby", 23),
          ("rdsptyJazzMusic", 24),
          ("rdsptyCountryMusic", 25),
          ("rdsptyNationalMusic", 26),
          ("rdsptyOldiesMusic", 27),
          ("rdsptyFolkMusic", 28),
          ("rdsptyDocumentary", 29),
          ("rdsptyAlarmTest", 30),
          ("rdsptyAlarmAlarm", 31))
    )


_MntrRdsPty_Type.__name__ = "Integer32"
_MntrRdsPty_Object = MibScalar
mntrRdsPty = _MntrRdsPty_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 34),
    _MntrRdsPty_Type()
)
mntrRdsPty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsPty.setStatus("current")


class _MntrRdsBer_Type(Fr1p15):
    """Custom type mntrRdsBer based on Fr1p15"""
    subtypeSpec = Fr1p15.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MntrRdsBer_Type.__name__ = "Fr1p15"
_MntrRdsBer_Object = MibScalar
mntrRdsBer = _MntrRdsBer_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 35),
    _MntrRdsBer_Type()
)
mntrRdsBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsBer.setStatus("current")
_MntrRdsTotalBits_Type = Counter32
_MntrRdsTotalBits_Object = MibScalar
mntrRdsTotalBits = _MntrRdsTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 36),
    _MntrRdsTotalBits_Type()
)
mntrRdsTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsTotalBits.setStatus("current")
_MntrRdsErrorBits_Type = Counter32
_MntrRdsErrorBits_Object = MibScalar
mntrRdsErrorBits = _MntrRdsErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 37),
    _MntrRdsErrorBits_Type()
)
mntrRdsErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrRdsErrorBits.setStatus("current")


class _MntrAudioStereo_Type(Integer32):
    """Custom type mntrAudioStereo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("altMono", 8),
          ("altStereo", 9))
    )


_MntrAudioStereo_Type.__name__ = "Integer32"
_MntrAudioStereo_Object = MibScalar
mntrAudioStereo = _MntrAudioStereo_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 38),
    _MntrAudioStereo_Type()
)
mntrAudioStereo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrAudioStereo.setStatus("current")


class _MntrTempcValue_Type(Fr8p8):
    """Custom type mntrTempcValue based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
    )


_MntrTempcValue_Type.__name__ = "Fr8p8"
_MntrTempcValue_Object = MibScalar
mntrTempcValue = _MntrTempcValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 39),
    _MntrTempcValue_Type()
)
mntrTempcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrTempcValue.setStatus("current")


class _MntrTempcValueAvr_Type(Fr8p8):
    """Custom type mntrTempcValueAvr based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
    )


_MntrTempcValueAvr_Type.__name__ = "Fr8p8"
_MntrTempcValueAvr_Object = MibScalar
mntrTempcValueAvr = _MntrTempcValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 40),
    _MntrTempcValueAvr_Type()
)
mntrTempcValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrTempcValueAvr.setStatus("current")


class _MntrTempcPeakMax_Type(Fr8p8):
    """Custom type mntrTempcPeakMax based on Fr8p8"""
    subtypeSpec = Fr8p8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
    )


_MntrTempcPeakMax_Type.__name__ = "Fr8p8"
_MntrTempcPeakMax_Object = MibScalar
mntrTempcPeakMax = _MntrTempcPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 41),
    _MntrTempcPeakMax_Type()
)
mntrTempcPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrTempcPeakMax.setStatus("current")


class _MntrFanrpmValue_Type(Integer32):
    """Custom type mntrFanrpmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MntrFanrpmValue_Type.__name__ = "Integer32"
_MntrFanrpmValue_Object = MibScalar
mntrFanrpmValue = _MntrFanrpmValue_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 42),
    _MntrFanrpmValue_Type()
)
mntrFanrpmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrFanrpmValue.setStatus("current")


class _MntrFanrpmValueAvr_Type(Integer32):
    """Custom type mntrFanrpmValueAvr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MntrFanrpmValueAvr_Type.__name__ = "Integer32"
_MntrFanrpmValueAvr_Object = MibScalar
mntrFanrpmValueAvr = _MntrFanrpmValueAvr_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 43),
    _MntrFanrpmValueAvr_Type()
)
mntrFanrpmValueAvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrFanrpmValueAvr.setStatus("current")


class _MntrFanrpmPeakMax_Type(Integer32):
    """Custom type mntrFanrpmPeakMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MntrFanrpmPeakMax_Type.__name__ = "Integer32"
_MntrFanrpmPeakMax_Object = MibScalar
mntrFanrpmPeakMax = _MntrFanrpmPeakMax_Object(
    (1, 3, 6, 1, 4, 1, 35833, 37, 3, 44),
    _MntrFanrpmPeakMax_Type()
)
mntrFanrpmPeakMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mntrFanrpmPeakMax.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254)
)
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0)
)

# Managed Objects groups


# Notification objects

notifTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 1)
)
notifTest.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifTest.setStatus(
        "current"
    )

notifRflvlOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 2)
)
notifRflvlOk.setObjects(
      *(("DB7001-MIB", "mntrRflvlValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRflvlOk.setStatus(
        "current"
    )

notifRflvlLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 3)
)
notifRflvlLow.setObjects(
      *(("DB7001-MIB", "mntrRflvlValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRflvlLow.setStatus(
        "current"
    )

notifRflvlHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 4)
)
notifRflvlHigh.setObjects(
      *(("DB7001-MIB", "mntrRflvlValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRflvlHigh.setStatus(
        "current"
    )

notifMpxtOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 5)
)
notifMpxtOk.setObjects(
      *(("DB7001-MIB", "mntrMpxtValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifMpxtOk.setStatus(
        "current"
    )

notifMpxtLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 6)
)
notifMpxtLow.setObjects(
      *(("DB7001-MIB", "mntrMpxtValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifMpxtLow.setStatus(
        "current"
    )

notifMpxtHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 7)
)
notifMpxtHigh.setObjects(
      *(("DB7001-MIB", "mntrMpxtValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifMpxtHigh.setStatus(
        "current"
    )

notifPilotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 8)
)
notifPilotOk.setObjects(
      *(("DB7001-MIB", "mntrPilotValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifPilotOk.setStatus(
        "current"
    )

notifPilotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 9)
)
notifPilotLow.setObjects(
      *(("DB7001-MIB", "mntrPilotValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifPilotLow.setStatus(
        "current"
    )

notifPilotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 10)
)
notifPilotHigh.setObjects(
      *(("DB7001-MIB", "mntrPilotValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifPilotHigh.setStatus(
        "current"
    )

notifRdsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 11)
)
notifRdsOk.setObjects(
      *(("DB7001-MIB", "mntrRdsValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRdsOk.setStatus(
        "current"
    )

notifRdsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 12)
)
notifRdsLow.setObjects(
      *(("DB7001-MIB", "mntrRdsValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRdsLow.setStatus(
        "current"
    )

notifRdsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 13)
)
notifRdsHigh.setObjects(
      *(("DB7001-MIB", "mntrRdsValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRdsHigh.setStatus(
        "current"
    )

notifLeftOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 14)
)
notifLeftOk.setObjects(
      *(("DB7001-MIB", "mntrLeftValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifLeftOk.setStatus(
        "current"
    )

notifLeftLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 15)
)
notifLeftLow.setObjects(
      *(("DB7001-MIB", "mntrLeftValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifLeftLow.setStatus(
        "current"
    )

notifLeftHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 16)
)
notifLeftHigh.setObjects(
      *(("DB7001-MIB", "mntrLeftValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifLeftHigh.setStatus(
        "current"
    )

notifRightOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 17)
)
notifRightOk.setObjects(
      *(("DB7001-MIB", "mntrRightValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRightOk.setStatus(
        "current"
    )

notifRightLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 18)
)
notifRightLow.setObjects(
      *(("DB7001-MIB", "mntrRightValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRightLow.setStatus(
        "current"
    )

notifRightHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 19)
)
notifRightHigh.setObjects(
      *(("DB7001-MIB", "mntrRightValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifRightHigh.setStatus(
        "current"
    )

notifTempcOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 20)
)
notifTempcOk.setObjects(
      *(("DB7001-MIB", "mntrTempcValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifTempcOk.setStatus(
        "current"
    )

notifTempcLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 21)
)
notifTempcLow.setObjects(
      *(("DB7001-MIB", "mntrTempcValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifTempcLow.setStatus(
        "current"
    )

notifTempcHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 22)
)
notifTempcHigh.setObjects(
      *(("DB7001-MIB", "mntrTempcValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifTempcHigh.setStatus(
        "current"
    )

notifFanrpmOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 23)
)
notifFanrpmOk.setObjects(
      *(("DB7001-MIB", "mntrFanrpmValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifFanrpmOk.setStatus(
        "current"
    )

notifFanrpmLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 24)
)
notifFanrpmLow.setObjects(
      *(("DB7001-MIB", "mntrFanrpmValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifFanrpmLow.setStatus(
        "current"
    )

notifFanrpmHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 25)
)
notifFanrpmHigh.setObjects(
      *(("DB7001-MIB", "mntrFanrpmValue"),
        ("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifFanrpmHigh.setStatus(
        "current"
    )

notifAudiomuteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 26)
)
notifAudiomuteActive.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifAudiomuteActive.setStatus(
        "current"
    )

notifAudiomuteInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 27)
)
notifAudiomuteInactive.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifAudiomuteInactive.setStatus(
        "current"
    )

notifMpxmuteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 28)
)
notifMpxmuteActive.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifMpxmuteActive.setStatus(
        "current"
    )

notifMpxmuteInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 29)
)
notifMpxmuteInactive.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifMpxmuteInactive.setStatus(
        "current"
    )

notifPiprotectionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 30)
)
notifPiprotectionActive.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifPiprotectionActive.setStatus(
        "current"
    )

notifPiprotectionInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 31)
)
notifPiprotectionInactive.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifPiprotectionInactive.setStatus(
        "current"
    )

notifSwitchMainstation = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 32)
)
notifSwitchMainstation.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifSwitchMainstation.setStatus(
        "current"
    )

notifSwitchBackupstation = NotificationType(
    (1, 3, 6, 1, 4, 1, 35833, 37, 254, 0, 33)
)
notifSwitchBackupstation.setObjects(
      *(("DB7001-MIB", "alias"),
        ("DB7001-MIB", "snmpaid"))
)
if mibBuilder.loadTexts:
    notifSwitchBackupstation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DB7001-MIB",
    **{"Fr8p8": Fr8p8,
       "Fr1p15": Fr1p15,
       "Ix10": Ix10,
       "Ix1000": Ix1000,
       "devabroadcast": devabroadcast,
       "db7001": db7001,
       "product": product,
       "fwrev": fwrev,
       "sernum": sernum,
       "settings": settings,
       "tuner": tuner,
       "mainStation": mainStation,
       "freq": freq,
       "att": att,
       "piproten": piproten,
       "piprot": piprot,
       "backupStation": backupStation,
       "altsfreq": altsfreq,
       "altsatt": altsatt,
       "altspiproten": altspiproten,
       "altspiprot": altspiprot,
       "freqstep": freqstep,
       "deemph": deemph,
       "rdsmode": rdsmode,
       "ifbw": ifbw,
       "stblend": stblend,
       "hicut": hicut,
       "hiblend": hiblend,
       "smute": smute,
       "audiocut": audiocut,
       "averageAndPeak": averageAndPeak,
       "avratck": avratck,
       "avrrel": avrrel,
       "peakhold": peakhold,
       "mpxGenerator": mpxGenerator,
       "mpxsrc": mpxsrc,
       "stmode": stmode,
       "preemph": preemph,
       "injaudio": injaudio,
       "injpilot": injpilot,
       "injrds": injrds,
       "phpilot": phpilot,
       "mpxlimen": mpxlimen,
       "mpxlimth": mpxlimth,
       "rdsEncoder": rdsEncoder,
       "rdssrc": rdssrc,
       "rdspi": rdspi,
       "rdsps": rdsps,
       "rdsrt": rdsrt,
       "rdspty": rdspty,
       "rdsms": rdsms,
       "rdstp": rdstp,
       "rdsta": rdsta,
       "diFlags": diFlags,
       "rdsdi0": rdsdi0,
       "rdsdi1": rdsdi1,
       "rdsdi2": rdsdi2,
       "rdsdi3": rdsdi3,
       "afList": afList,
       "rdsafcount": rdsafcount,
       "rdsaf1": rdsaf1,
       "rdsaf2": rdsaf2,
       "rdsaf3": rdsaf3,
       "rdsaf4": rdsaf4,
       "rdsaf5": rdsaf5,
       "rdsaf6": rdsaf6,
       "rdsaf7": rdsaf7,
       "rdsaf8": rdsaf8,
       "rdsaf9": rdsaf9,
       "rdsaf10": rdsaf10,
       "rdsaf11": rdsaf11,
       "rdsaf12": rdsaf12,
       "rdsaf13": rdsaf13,
       "rdsaf14": rdsaf14,
       "rdsaf15": rdsaf15,
       "rdsaf16": rdsaf16,
       "rdsaf17": rdsaf17,
       "rdsaf18": rdsaf18,
       "rdsaf19": rdsaf19,
       "rdsaf20": rdsaf20,
       "rdsaf21": rdsaf21,
       "rdsaf22": rdsaf22,
       "rdsaf23": rdsaf23,
       "rdsaf24": rdsaf24,
       "rdsaf25": rdsaf25,
       "rdsreplpi": rdsreplpi,
       "rdsreplps": rdsreplps,
       "rdsreplrt": rdsreplrt,
       "rdsreplpty": rdsreplpty,
       "rdsreplms": rdsreplms,
       "rdsrepltp": rdsrepltp,
       "rdsreplta": rdsreplta,
       "rdsrepldi": rdsrepldi,
       "rdsreplaf": rdsreplaf,
       "communication": communication,
       "generalSetup": generalSetup,
       "ethen": ethen,
       "snmpen": snmpen,
       "appen": appen,
       "httpen": httpen,
       "ftpen": ftpen,
       "emailen": emailen,
       "sntpen": sntpen,
       "streamen": streamen,
       "syslogen": syslogen,
       "uecpsrven": uecpsrven,
       "uecprelen": uecprelen,
       "usben": usben,
       "upnpen": upnpen,
       "ethernet": ethernet,
       "dhcpen": dhcpen,
       "ip": ip,
       "netmask": netmask,
       "gwip": gwip,
       "dns1ip": dns1ip,
       "dns2ip": dns2ip,
       "snmp": snmp,
       "snmpmip": snmpmip,
       "snmpmport": snmpmport,
       "snmpaport": snmpaport,
       "snmpaid": snmpaid,
       "snmprcomm": snmprcomm,
       "snmpwcomm": snmpwcomm,
       "snmptout": snmptout,
       "application": application,
       "appport": appport,
       "apptout": apptout,
       "http": http,
       "httpport": httpport,
       "httptout": httptout,
       "ftp": ftp,
       "ftpdport": ftpdport,
       "ftpcport": ftpcport,
       "sntp": sntp,
       "sntpsrv": sntpsrv,
       "sntpport": sntpport,
       "email": email,
       "smtpsrv": smtpsrv,
       "smtpport": smtpport,
       "email1": email1,
       "email2": email2,
       "smtpsender": smtpsender,
       "smtpuname": smtpuname,
       "smtpupass": smtpupass,
       "smtphostname": smtphostname,
       "smtpconntype": smtpconntype,
       "streamer": streamer,
       "strmport": strmport,
       "strmbps": strmbps,
       "syslog": syslog,
       "slogsrv": slogsrv,
       "slogport": slogport,
       "uecpTpcServer": uecpTpcServer,
       "uecpsrvport": uecpsrvport,
       "uecpUdpRelay": uecpUdpRelay,
       "uecprelsrv": uecprelsrv,
       "uecprelport": uecprelport,
       "gsmModem": gsmModem,
       "mdmtype": mdmtype,
       "mdmbrate": mdmbrate,
       "mdmnum1": mdmnum1,
       "mdmnum2": mdmnum2,
       "mdmnum3": mdmnum3,
       "mdmnum4": mdmnum4,
       "mdmnum5": mdmnum5,
       "security": security,
       "panel": panel,
       "locken": locken,
       "lockcode": lockcode,
       "locktout": locktout,
       "remoteAccess": remoteAccess,
       "accaname": accaname,
       "accapass": accapass,
       "accuname": accuname,
       "accupass": accupass,
       "alarms": alarms,
       "alarmEvents": alarmEvents,
       "alsmtpen": alsmtpen,
       "alsmsen": alsmsen,
       "alsnmpen": alsnmpen,
       "algpoen": algpoen,
       "alarmRfMin": alarmRfMin,
       "alarmRfMax": alarmRfMax,
       "alarmRfTrigger": alarmRfTrigger,
       "alarmRfRelease": alarmRfRelease,
       "alarmRfEvents": alarmRfEvents,
       "alarmMpxMin": alarmMpxMin,
       "alarmMpxMax": alarmMpxMax,
       "alarmMpxTrigger": alarmMpxTrigger,
       "alarmMpxRelease": alarmMpxRelease,
       "alarmMpxEvents": alarmMpxEvents,
       "alarmPilotMin": alarmPilotMin,
       "alarmPilotMax": alarmPilotMax,
       "alarmPilotTrigger": alarmPilotTrigger,
       "alarmPilotRelease": alarmPilotRelease,
       "alarmPilotEvents": alarmPilotEvents,
       "alarmRdsMin": alarmRdsMin,
       "alarmRdsMax": alarmRdsMax,
       "alarmRdsTrigger": alarmRdsTrigger,
       "alarmRdsRelease": alarmRdsRelease,
       "alarmRdsEvents": alarmRdsEvents,
       "alarmLeftMin": alarmLeftMin,
       "alarmLeftMax": alarmLeftMax,
       "alarmLeftTrigger": alarmLeftTrigger,
       "alarmLeftRelease": alarmLeftRelease,
       "alarmLeftEvents": alarmLeftEvents,
       "alarmRightMin": alarmRightMin,
       "alarmRightMax": alarmRightMax,
       "alarmRightTrigger": alarmRightTrigger,
       "alarmRightRelease": alarmRightRelease,
       "alarmRightEvents": alarmRightEvents,
       "alarmTempMin": alarmTempMin,
       "alarmTempMax": alarmTempMax,
       "alarmTempTrigger": alarmTempTrigger,
       "alarmTempRelease": alarmTempRelease,
       "alarmTempEvents": alarmTempEvents,
       "alarmFanMin": alarmFanMin,
       "alarmFanMax": alarmFanMax,
       "alarmFanTrigger": alarmFanTrigger,
       "alarmFanRelease": alarmFanRelease,
       "alarmFanEvents": alarmFanEvents,
       "activeAlarmAction": activeAlarmAction,
       "rfAlarm": rfAlarm,
       "alrmrfaudmute": alrmrfaudmute,
       "alrmrfmpxmute": alrmrfmpxmute,
       "alrmrfswitch": alrmrfswitch,
       "mpxAlarm": mpxAlarm,
       "alrmmpxaudmute": alrmmpxaudmute,
       "alrmmpxmpxmute": alrmmpxmpxmute,
       "alrmmpxswitch": alrmmpxswitch,
       "audioAlarm": audioAlarm,
       "alrmaudaudmute": alrmaudaudmute,
       "alrmaudmpxmute": alrmaudmpxmute,
       "alrmaudswitch": alrmaudswitch,
       "pilotAlarm": pilotAlarm,
       "alrmpltaudmute": alrmpltaudmute,
       "alrmpltmpxmute": alrmpltmpxmute,
       "alrmpltswitch": alrmpltswitch,
       "piProtection": piProtection,
       "alrmpiaudmute": alrmpiaudmute,
       "alrmpimpxmute": alrmpimpxmute,
       "alrmpiswitch": alrmpiswitch,
       "gpOutputs": gpOutputs,
       "gpofunc1": gpofunc1,
       "gpotype1": gpotype1,
       "gpotout1": gpotout1,
       "gpofunc2": gpofunc2,
       "gpotype2": gpotype2,
       "gpotout2": gpotout2,
       "gpofunc3": gpofunc3,
       "gpotype3": gpotype3,
       "gpotout3": gpotout3,
       "gpofunc4": gpofunc4,
       "gpotype4": gpotype4,
       "gpotout4": gpotout4,
       "gpofunc5": gpofunc5,
       "gpotype5": gpotype5,
       "gpotout5": gpotout5,
       "gpofunc6": gpofunc6,
       "gpotype6": gpotype6,
       "gpotout6": gpotout6,
       "gpofunc7": gpofunc7,
       "gpotype7": gpotype7,
       "gpotout7": gpotout7,
       "audioMpxOutputs": audioMpxOutputs,
       "volph": volph,
       "volaudio": volaudio,
       "volmpx": volmpx,
       "volgsm": volgsm,
       "digout": digout,
       "device": device,
       "alias": alias,
       "region": region,
       "dateTime": dateTime,
       "date": date,
       "time": time,
       "tzone": tzone,
       "dsten": dsten,
       "frontPanel": frontPanel,
       "dispcontr": dispcontr,
       "ledbright": ledbright,
       "scrsaver": scrsaver,
       "paneltout": paneltout,
       "loss": loss,
       "audiolossth": audiolossth,
       "audiolosstout": audiolosstout,
       "mpathth": mpathth,
       "mpathtout": mpathtout,
       "rdstout": rdstout,
       "homescreen": homescreen,
       "fanctrl": fanctrl,
       "slogmage": slogmage,
       "monitoring": monitoring,
       "mntrFreq": mntrFreq,
       "mntrRflvlValue": mntrRflvlValue,
       "mntrRflvlValueAvr": mntrRflvlValueAvr,
       "mntrRflvlPeakMax": mntrRflvlPeakMax,
       "mntrMpathValue": mntrMpathValue,
       "mntrMpathValueAvr": mntrMpathValueAvr,
       "mntrMpathPeakMax": mntrMpathPeakMax,
       "mntrMpxtValue": mntrMpxtValue,
       "mntrMpxtValueAvr": mntrMpxtValueAvr,
       "mntrMpxtPeakMax": mntrMpxtPeakMax,
       "mntrPilotValue": mntrPilotValue,
       "mntrPilotValueAvr": mntrPilotValueAvr,
       "mntrPilotPeakMax": mntrPilotPeakMax,
       "mntrRdsValue": mntrRdsValue,
       "mntrRdsValueAvr": mntrRdsValueAvr,
       "mntrRdsPeakMax": mntrRdsPeakMax,
       "mntrLeftValue": mntrLeftValue,
       "mntrLeftValueAvr": mntrLeftValueAvr,
       "mntrLeftPeakMax": mntrLeftPeakMax,
       "mntrRightValue": mntrRightValue,
       "mntrRightValueAvr": mntrRightValueAvr,
       "mntrRightPeakMax": mntrRightPeakMax,
       "mntrRdsgroupValue": mntrRdsgroupValue,
       "mntrRdsLock": mntrRdsLock,
       "mntrRdsPi": mntrRdsPi,
       "mntrRdsPs": mntrRdsPs,
       "mntrRdsRt": mntrRdsRt,
       "mntrRdsTa": mntrRdsTa,
       "mntrRdsTp": mntrRdsTp,
       "mntrRdsMusicspeech": mntrRdsMusicspeech,
       "mntrRdsPty": mntrRdsPty,
       "mntrRdsBer": mntrRdsBer,
       "mntrRdsTotalBits": mntrRdsTotalBits,
       "mntrRdsErrorBits": mntrRdsErrorBits,
       "mntrAudioStereo": mntrAudioStereo,
       "mntrTempcValue": mntrTempcValue,
       "mntrTempcValueAvr": mntrTempcValueAvr,
       "mntrTempcPeakMax": mntrTempcPeakMax,
       "mntrFanrpmValue": mntrFanrpmValue,
       "mntrFanrpmValueAvr": mntrFanrpmValueAvr,
       "mntrFanrpmPeakMax": mntrFanrpmPeakMax,
       "traps": traps,
       "notification": notification,
       "notifTest": notifTest,
       "notifRflvlOk": notifRflvlOk,
       "notifRflvlLow": notifRflvlLow,
       "notifRflvlHigh": notifRflvlHigh,
       "notifMpxtOk": notifMpxtOk,
       "notifMpxtLow": notifMpxtLow,
       "notifMpxtHigh": notifMpxtHigh,
       "notifPilotOk": notifPilotOk,
       "notifPilotLow": notifPilotLow,
       "notifPilotHigh": notifPilotHigh,
       "notifRdsOk": notifRdsOk,
       "notifRdsLow": notifRdsLow,
       "notifRdsHigh": notifRdsHigh,
       "notifLeftOk": notifLeftOk,
       "notifLeftLow": notifLeftLow,
       "notifLeftHigh": notifLeftHigh,
       "notifRightOk": notifRightOk,
       "notifRightLow": notifRightLow,
       "notifRightHigh": notifRightHigh,
       "notifTempcOk": notifTempcOk,
       "notifTempcLow": notifTempcLow,
       "notifTempcHigh": notifTempcHigh,
       "notifFanrpmOk": notifFanrpmOk,
       "notifFanrpmLow": notifFanrpmLow,
       "notifFanrpmHigh": notifFanrpmHigh,
       "notifAudiomuteActive": notifAudiomuteActive,
       "notifAudiomuteInactive": notifAudiomuteInactive,
       "notifMpxmuteActive": notifMpxmuteActive,
       "notifMpxmuteInactive": notifMpxmuteInactive,
       "notifPiprotectionActive": notifPiprotectionActive,
       "notifPiprotectionInactive": notifPiprotectionInactive,
       "notifSwitchMainstation": notifSwitchMainstation,
       "notifSwitchBackupstation": notifSwitchBackupstation}
)
